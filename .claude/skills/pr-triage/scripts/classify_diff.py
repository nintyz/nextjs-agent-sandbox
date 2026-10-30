#!/usr/bin/env python3
"""Deterministic diff classifier for pr-triage. No model judgement.

Reads EITHER a unified diff (--diff FILE) OR a changed-file list
(--files FILE: one path per line, or a JSON list of paths, or a JSON
object with a "files" list). Exactly one input must be given.

Classification rules (fixed, in priority order per file):
  1. workflow: path matches ^.github/workflows/[^/]+\\.(yml|yaml)$
  2. docs:     path is under docs/, OR ends .md/.mdx, EXCEPT paths
               under .github/ or .claude/ (governance/config, not docs)
  3. test:     path contains /test/ or /__tests__/, starts with test/,
               or ends .test.<ext> / .spec.<ext>
  4. source:   code extension .ts/.tsx/.js/.jsx/.mjs/.cjs/.rs/.go/.py
  5. other:    everything else (configs, lockfiles, images, binaries,
               non-workflow YAML, etc.)

Output: exactly one JSON object on stdout (the envelope below).
Exit 0 = check ran (even if the answer is "empty" or "not docs-only").
Exit 2 = check could not run: missing/unreadable input, both/neither
         input given, malformed JSON file list, or a diff that cannot
         be parsed. In that case result fields are null and no pass
         is invented. Never print a second JSON object or prose to
         stdout; diagnostics go to stderr only.
"""
import json
import re
import sys

VERSION = "1.0.0"
WORKFLOW_RE = re.compile(r"^\.github/workflows/[^/]+\.(yml|yaml)$")
TEST_RE = re.compile(r"(^|/)test(/|$)|/__tests__/|\.(test|spec)\.[A-Za-z0-9]+$")
SOURCE_EXTS = {".ts", ".tsx", ".js", ".jsx", ".mjs", ".cjs", ".rs", ".go", ".py"}
DOCS_EXTS = {".md", ".mdx"}


def emit(status, result, error):
    print(json.dumps({"script": "classify_diff", "version": VERSION,
                      "status": status, "result": result, "error": error},
                     sort_keys=True))
    return 0 if status == "ok" else 2


def classify(path):
    if WORKFLOW_RE.match(path):
        return "workflow"
    low = path.lower()
    ext = "." + low.rsplit(".", 1)[-1] if "." in low.rsplit("/", 1)[-1] else ""
    if (low.startswith("docs/") or ext in DOCS_EXTS) \
            and not (low.startswith(".github/") or low.startswith(".claude/")):
        return "docs"
    if TEST_RE.search(low):
        return "test"
    if ext in SOURCE_EXTS:
        return "source"
    return "other"


def files_from_diff(text):
    files = []
    for line in text.splitlines():
        if line.startswith("+++ "):
            p = line[4:].strip()
            if p == "/dev/null":
                continue
            if p.startswith("b/"):
                p = p[2:]
            elif p.startswith("a/"):
                p = p[2:]
            files.append(p)
        elif line.startswith("Binary files ") and " differ" in line:
            # "Binary files a/X and b/Y differ" — record the b-side path.
            m = re.search(r" and b/(\S+) differ", line)
            if m:
                files.append(m.group(1))
    return files


def main(argv):
    diff_path = files_path = None
    i = 0
    while i < len(argv):
        if argv[i] == "--diff" and i + 1 < len(argv):
            diff_path = argv[i + 1]; i += 2
        elif argv[i] == "--files" and i + 1 < len(argv):
            files_path = argv[i + 1]; i += 2
        elif argv[i] in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"unknown argument: {argv[i]}", file=sys.stderr)
            return emit("could_not_run", None, "unknown or incomplete argument")
    if bool(diff_path) == bool(files_path):
        return emit("could_not_run", None,
                    "exactly one of --diff or --files is required")
    try:
        with open(diff_path or files_path, encoding="utf-8", errors="strict") as f:
            raw = f.read()
    except (OSError, UnicodeDecodeError) as e:
        return emit("could_not_run", None, f"cannot read input file: {e}")
    if diff_path:
        if raw.strip() == "":
            files = []
        else:
            files = files_from_diff(raw)
            if not files and "+++" not in raw and "diff --git" not in raw:
                return emit("could_not_run", None,
                            "diff text contains no parseable file headers")
    else:
        stripped = raw.strip()
        if stripped.startswith("[") or stripped.startswith("{"):
            try:
                data = json.loads(raw)
            except json.JSONDecodeError as e:
                return emit("could_not_run", None, f"malformed JSON file list: {e}")
            if isinstance(data, dict):
                data = data.get("files")
            if not isinstance(data, list) or not all(isinstance(x, str) for x in data):
                return emit("could_not_run", None,
                            "JSON file list must be a list of strings or {\"files\": [...]}")
            files = [x for x in data if x.strip()]
        else:
            files = [ln.strip() for ln in raw.splitlines() if ln.strip()]
    cats = [classify(p) for p in files]
    counts = {c: cats.count(c) for c in ("docs", "workflow", "source", "test", "other")}
    result = {
        "empty": len(files) == 0,
        "file_count": len(files),
        "files": [{"path": p, "category": c} for p, c in zip(files, cats)],
        "counts": counts,
        # docs_only is True ONLY when there is at least one file and all are docs.
        "docs_only": len(files) > 0 and all(c == "docs" for c in cats),
        "workflow_touched": "workflow" in cats,
        "source_touched": "source" in cats,
        "test_touched": "test" in cats,
        "other_touched": "other" in cats,
    }
    return emit("ok", result, None)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
