#!/usr/bin/env python3
"""Deterministic issue-link checker for pr-triage. No model judgement.

Reads a PR body from --body FILE (plain text / Markdown). No network,
no GitHub API call: this script reports what the text SAYS, not whether
the linked issue exists. If --issues FILE (JSON list of issue numbers,
or {"issues": [...]}) is supplied, it additionally reports whether each
closing-linked number appears in that frozen snapshot list; without it,
that field is null, never guessed.

A closing link is: fixes|fix|fixed|closes|close|closed|resolves|
resolve|resolved, followed by whitespace and #<digits>, case-insensitive
(e.g. "Fixes #123", "closes #45"), or the same keyword followed by a
full-repo form owner/repo#<digits> (e.g. "Fixes vercel/next.js#92919").
A bare "#123" with no such keyword is reported separately as a bare
mention and does NOT count as a link.

Output: exactly one JSON object on stdout. Exit 0 = check ran (an empty
body is a valid run: has_issue_link=false, empty_body=true). Exit 2 =
check could not run: missing/unreadable body file, malformed --issues
file. Never invent a pass.
"""
import json
import re
import sys

VERSION = "1.0.0"
CLOSING_RE = re.compile(
    r"\b(?:fix|fixes|fixed|close|closes|closed|resolve|resolves|resolved)\s+(?:([A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)#|#)(\d+)\b",
    re.IGNORECASE)
BARE_RE = re.compile(r"#(\d+)\b")


def emit(status, result, error):
    print(json.dumps({"script": "check_issue_link", "version": VERSION,
                      "status": status, "result": result, "error": error},
                     sort_keys=True))
    return 0 if status == "ok" else 2


def main(argv):
    body_path = issues_path = None
    i = 0
    while i < len(argv):
        if argv[i] == "--body" and i + 1 < len(argv):
            body_path = argv[i + 1]; i += 2
        elif argv[i] == "--issues" and i + 1 < len(argv):
            issues_path = argv[i + 1]; i += 2
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
    snapshot = None
    if issues_path:
        try:
            with open(issues_path, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            return emit("could_not_run", None, f"cannot read issues file: {e}")
        if isinstance(data, dict):
            data = data.get("issues")
        if not isinstance(data, list) or not all(isinstance(x, int) for x in data):
            return emit("could_not_run", None,
                        "issues file must be a JSON list of ints or {\"issues\": [...]}")
        snapshot = set(data)
    closing = []
    for m in CLOSING_RE.finditer(body):
        closing.append({"keyword": m.group(0).split()[0].lower(),
                        "issue_number": int(m.group(2)),
                        "form": "full-repo" if m.group(1) else "bare",
                        "repo": m.group(1)})
    closing_numbers = sorted({c["issue_number"] for c in closing})
    bare = sorted({int(n) for n in BARE_RE.findall(body)} - set(closing_numbers))
    result = {
        "empty_body": body.strip() == "",
        "has_issue_link": len(closing) > 0,
        "closing_links": closing,
        "linked_issue_numbers": closing_numbers,
        "bare_mentions": bare,
        "linked_issue_in_snapshot": (
            None if snapshot is None else
            {n: (n in snapshot) for n in closing_numbers}),
    }
    return emit("ok", result, None)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
