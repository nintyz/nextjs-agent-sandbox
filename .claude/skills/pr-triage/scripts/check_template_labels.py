#!/usr/bin/env python3
"""Deterministic template/label checker for pr-triage. No model judgement.

Reports FACTS the agent may cite; it never returns a verdict ("ready",
"valid", "complete") on its own. Whether missing sections matter is a
skill judgement, made after this script runs.

Inputs:
  --body FILE            PR body (required)
  --template FILE        optional. Either:
                           - JSON list of required section names, or
                             {"sections": [...]}, or
                           - Markdown: lines starting with "## " are taken
                             as the required section headings.
                         If omitted, the template sub-check COULD NOT
                         RUN (the evaluator must supply the frozen
                         template; this script will not invent one).
  --labels FILE          optional JSON list of labels on the PR, or
                         {"labels": [...]}. If omitted, the label
                         sub-check could not run.
  --expected-labels "a,b"  optional comma-separated list. If supplied
                         with --labels, present/missing is reported
                         as fact. If supplied without --labels, the
                         label sub-check could not run.

Section presence: a section counts as present when its heading text
(case-insensitive, whitespace/punctuation-normalised) appears in the
body, OR its first distinctive word appears as a body heading. Empty
bodies are a valid run: every section is absent, not an error.

Output: exactly one JSON object on stdout with two sub-checks, each
with its own status, so a partial run is visible. Exit 0 = every
requested sub-check ran. Exit 2 = at least one requested sub-check
could not run (or the body file could not be read). The agent must
treat exit 2 as "do not cite that sub-check", never as a pass.
"""
import json
import re
import sys

VERSION = "1.0.0"


def emit(status, result, error):
    print(json.dumps({"script": "check_template_labels", "version": VERSION,
                      "status": status, "result": result, "error": error},
                     sort_keys=True))
    return 0 if status == "ok" else 2


def normalise(s):
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def main(argv):
    body_path = template_path = labels_path = None
    expected = None
    i = 0
    while i < len(argv):
        if argv[i] == "--body" and i + 1 < len(argv):
            body_path = argv[i + 1]; i += 2
        elif argv[i] == "--template" and i + 1 < len(argv):
            template_path = argv[i + 1]; i += 2
        elif argv[i] == "--labels" and i + 1 < len(argv):
            labels_path = argv[i + 1]; i += 2
        elif argv[i] == "--expected-labels" and i + 1 < len(argv):
            expected = [x.strip() for x in argv[i + 1].split(",") if x.strip()]; i += 2
        elif argv[i] in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"unknown argument: {argv[i]}", file=sys.stderr)
            return emit("could_not_run", None, "unknown or incomplete argument")
    if not body_path:
        return emit("could_not_run", None, "--body FILE is required")
    try:
        with open(body_path, encoding="utf-8", errors="strict") as f:
            body = f.read()
    except (OSError, UnicodeDecodeError) as e:
        return emit("could_not_run", None, f"cannot read body file: {e}")
    errors = []
    # --- template sub-check ---
    if template_path is None:
        template_check = {"status": "could_not_run",
                          "error": "no --template supplied; template not invented",
                          "sections": None}
        errors.append("template sub-check could not run")
    else:
        try:
            with open(template_path, encoding="utf-8") as f:
                raw = f.read()
        except OSError as e:
            return emit("could_not_run", None, f"cannot read template file: {e}")
        sections = None
        stripped = raw.strip()
        if stripped.startswith("[") or stripped.startswith("{"):
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as e:
                return emit("could_not_run", None, f"malformed JSON template: {e}")
            if isinstance(data, dict):
                data = data.get("sections")
            if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
                return emit("could_not_run", None,
                            "JSON template must be a list of strings or {\"sections\": [...]}")
            sections = data
        else:
            sections = [ln[3:].strip() for ln in raw.splitlines()
                        if ln.startswith("## ")]
            if not sections:
                return emit("could_not_run", None,
                            "Markdown template contains no '## ' headings")
        norm_body = normalise(body)
        sections_out = []
        for s in sections:
            ns = normalise(s)
            sections_out.append({"section": s, "present": ns in norm_body if ns else False})
        template_check = {"status": "ok", "error": None, "sections": sections_out}
    # --- label sub-check ---
    if labels_path is None:
        label_check = {"status": "could_not_run",
                       "error": "no --labels supplied; labels not invented",
                       "labels": None, "expected_labels": expected,
                       "present": None, "missing": None}
        errors.append("label sub-check could not run")
    else:
        try:
            with open(labels_path, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            return emit("could_not_run", None, f"cannot read labels file: {e}")
        if isinstance(data, dict):
            data = data.get("labels")
        if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
            return emit("could_not_run", None,
                        "labels file must be a JSON list of strings or {\"labels\": [...]}")
        label_check = {"status": "ok", "error": None, "labels": data,
                       "expected_labels": expected,
                       "present": [x for x in expected if x in data] if expected else None,
                       "missing": [x for x in expected if x not in data] if expected else None}
    result = {"empty_body": body.strip() == "",
              "template_check": template_check, "label_check": label_check}
    if errors:
        return emit("partial", result, "; ".join(errors))
    return emit("ok", result, None)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
