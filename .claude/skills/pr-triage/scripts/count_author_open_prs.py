#!/usr/bin/env python3
"""Deterministic author open-PR counter for pr-triage. No model judgement.

Counts open PRs for one author FROM FROZEN SNAPSHOT DATA ONLY. It never
queries the live GitHub API and never uses live state: a live count
would mix post-event closures into a pre-event snapshot and invalidate
the golden case (see plan §4).

Snapshot format (--snapshot FILE, JSON object, either shape):
  {"author": "login", "current_pr": 100101,
   "prs": [{"number": 100101, "author": "login", "state": "open"}, ...]}
  or {"author": "login", "current_pr": 100101,
      "open_prs": [{"number": ..., "author": "login"}, ...]}
For "prs", only entries with state exactly "open" count. For
"open_prs", every entry counts (the key itself asserts openness).
--author / --current-pr flags override the snapshot's values.

Outputs both totals, because the golden case needs the distinction:
  total_open_prs_in_snapshot — every open PR by this author in snapshot
  other_open_prs — the same total minus the current PR, if the current
    PR is in the snapshot and open; otherwise equal to the total, and
    current_pr_in_snapshot=false flags that the snapshot may be
    incomplete for this question.
  A count of 0 is a valid run, not an error.

Output: exactly one JSON object on stdout. Exit 0 = check ran.
Exit 2 = check could not run: missing/unreadable/malformed snapshot,
missing author, or a PR entry that is not an object with a string
author (for "prs", also a string state).
"""
import json
import sys

VERSION = "1.0.0"


def emit(status, result, error):
    print(json.dumps({"script": "count_author_open_prs", "version": VERSION,
                      "status": status, "result": result, "error": error},
                     sort_keys=True))
    return 0 if status == "ok" else 2


def main(argv):
    snapshot_path = author = current_pr = None
    i = 0
    while i < len(argv):
        if argv[i] == "--snapshot" and i + 1 < len(argv):
            snapshot_path = argv[i + 1]; i += 2
        elif argv[i] == "--author" and i + 1 < len(argv):
            author = argv[i + 1]; i += 2
        elif argv[i] == "--current-pr" and i + 1 < len(argv):
            try:
                current_pr = int(argv[i + 1])
            except ValueError:
                return emit("could_not_run", None, "--current-pr must be an integer")
            i += 2
        elif argv[i] in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"unknown argument: {argv[i]}", file=sys.stderr)
            return emit("could_not_run", None, "unknown or incomplete argument")
    if not snapshot_path:
        return emit("could_not_run", None, "--snapshot FILE is required")
    try:
        with open(snapshot_path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        return emit("could_not_run", None, f"cannot read snapshot file: {e}")
    if not isinstance(data, dict):
        return emit("could_not_run", None, "snapshot must be a JSON object")
    author = author or data.get("author")
    if current_pr is None:
        current_pr = data.get("current_pr")
    if not isinstance(author, str) or not author:
        return emit("could_not_run", None, "snapshot must name an author (string)")
    if "prs" in data:
        entries = data["prs"]
        if not isinstance(entries, list):
            return emit("could_not_run", None, "\"prs\" must be a list")
        open_numbers = []
        for e in entries:
            if not isinstance(e, dict) or not isinstance(e.get("author"), str) \
                    or not isinstance(e.get("state"), str):
                return emit("could_not_run", None,
                            "each \"prs\" entry needs string author and state")
            if e["author"] == author and e["state"] == "open":
                open_numbers.append(e.get("number"))
    elif "open_prs" in data:
        entries = data["open_prs"]
        if not isinstance(entries, list):
            return emit("could_not_run", None, "\"open_prs\" must be a list")
        open_numbers = []
        for e in entries:
            if not isinstance(e, dict) or not isinstance(e.get("author"), str):
                return emit("could_not_run", None,
                            "each \"open_prs\" entry needs a string author")
            if e["author"] == author:
                open_numbers.append(e.get("number"))
    else:
        return emit("could_not_run", None,
                    "snapshot needs a \"prs\" or \"open_prs\" list")
    in_snapshot = current_pr in open_numbers if current_pr is not None else False
    total = len(open_numbers)
    result = {
        "author": author,
        "current_pr": current_pr,
        "current_pr_in_snapshot": in_snapshot,
        "total_open_prs_in_snapshot": total,
        "other_open_prs": total - 1 if in_snapshot else total,
        "open_pr_numbers": sorted(n for n in open_numbers if isinstance(n, int)),
    }
    return emit("ok", result, None)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
