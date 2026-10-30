#!/usr/bin/env python3
"""Deterministic SHA-equality checker for pr-triage. No model judgement.

Compares two SHAs supplied as --source-sha X --target-sha Y, or in a
JSON snapshot file (--snapshot FILE) with keys source_sha/target_sha
(aliases from_sha/to_sha and head_sha/base_sha are also accepted).
SHAs are compared case-insensitively after stripping whitespace.

Validity: a SHA must be 7-40 lowercase/uppercase hex characters (the
7-char lower bound accepts abbreviated SHAs from snapshots; a full
40-char SHA is expected for a no-op claim). If either SHA is missing
or invalid, the check COULD NOT RUN (exit 2) — it does not report
"not equal" as a substitute, because a malformed input is not evidence
either way.

Meaning, stated precisely: sha_equal=true means the two supplied SHAs
are identical strings. It is a candidate no-op signal only; it does not
by itself prove a PR is a no-op (titles, bodies, branches and file
lists can still differ). The agent must cite it as "SHA equality",
never as a proven no-op, unless the frozen snapshot confirms the
rest of the PR is also identical.

Output: exactly one JSON object on stdout. Exit 0 = check ran.
Exit 2 = check could not run.
"""
import json
import re
import sys

VERSION = "1.0.0"
SHA_RE = re.compile(r"^[0-9a-fA-F]{7,40}$")


def emit(status, result, error):
    print(json.dumps({"script": "check_sha_equality", "version": VERSION,
                      "status": status, "result": result, "error": error},
                     sort_keys=True))
    return 0 if status == "ok" else 2


def main(argv):
    source = target = snapshot_path = None
    i = 0
    while i < len(argv):
        if argv[i] == "--source-sha" and i + 1 < len(argv):
            source = argv[i + 1]; i += 2
        elif argv[i] == "--target-sha" and i + 1 < len(argv):
            target = argv[i + 1]; i += 2
        elif argv[i] == "--snapshot" and i + 1 < len(argv):
            snapshot_path = argv[i + 1]; i += 2
        elif argv[i] in ("-h", "--help"):
            print(__doc__); return 0
        else:
            print(f"unknown argument: {argv[i]}", file=sys.stderr)
            return emit("could_not_run", None, "unknown or incomplete argument")
    if snapshot_path:
        try:
            with open(snapshot_path, encoding="utf-8") as f:
                data = json.load(f)
        except (OSError, json.JSONDecodeError) as e:
            return emit("could_not_run", None, f"cannot read snapshot file: {e}")
        if not isinstance(data, dict):
            return emit("could_not_run", None, "snapshot must be a JSON object")
        source = source or data.get("source_sha") or data.get("from_sha") or data.get("head_sha")
        target = target or data.get("target_sha") or data.get("to_sha") or data.get("base_sha")
    if not isinstance(source, str) or not isinstance(target, str):
        return emit("could_not_run", None, "both source and target SHAs are required")
    source, target = source.strip(), target.strip()
    if not SHA_RE.match(source) or not SHA_RE.match(target):
        return emit("could_not_run", None,
                    "SHA must be 7-40 hex characters; got invalid source or target SHA")
    equal = source.lower() == target.lower()
    result = {
        "source_sha": source.lower(),
        "target_sha": target.lower(),
        "full_length": len(source) == 40 and len(target) == 40,
        "sha_equal": equal,
        # Candidate only — see module docstring. Never read this as proof of no-op.
        "is_no_op_candidate": equal,
    }
    return emit("ok", result, None)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
