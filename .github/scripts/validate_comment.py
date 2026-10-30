#!/usr/bin/env python3
"""Validate a triage comment draft before Job 2 posts it.

Workflow-owned base code (NOT skill-owned, NOT PR code). Reads the
draft comment as TEXT only, never executes it. Checks, in order:
  1. exactly one comment file, UTF-8 text, no NUL bytes
  2. length <= 1500 characters (enforced: failure exits non-zero,
     nothing is posted; never truncate, because truncation can
     change meaning)
  3. footer 'Automated triage — not a maintainer decision.' present
  4. marker '<!-- pr-triage-agent -->' present
  5. dedup: no comment with the marker already on the PR (via gh api;
     repo and PR number come from arguments, never from PR text)

Exit codes: 0 = OK (post) or SKIP (dedup, do not post, not a failure);
2 = validation failure (do not post; the workflow job fails).
Stdout prints 'OK', 'SKIP=true', or an error line. The workflow step
greps stdout for '^SKIP=true' to decide whether to skip posting.
"""
import argparse
import subprocess
import sys

MAX_CHARS = 1500
FOOTER = "Automated triage — not a maintainer decision."
MARKER = "<!-- pr-triage-agent -->"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--comment", required=True)
    ap.add_argument("--repo", required=True)
    ap.add_argument("--pr", required=True)
    args = ap.parse_args()

    try:
        text = open(args.comment, encoding="utf-8").read()
    except (OSError, UnicodeDecodeError) as exc:
        print(f"VALIDATION_FAILED: cannot read comment as UTF-8 text: {exc}")
        return 2
    if "\x00" in text:
        print("VALIDATION_FAILED: comment contains NUL bytes")
        return 2
    if len(text) > MAX_CHARS:
        print(f"VALIDATION_FAILED: comment is {len(text)} chars, over {MAX_CHARS}")
        return 2
    if FOOTER not in text:
        print("VALIDATION_FAILED: footer missing")
        return 2
    if MARKER not in text:
        print("VALIDATION_FAILED: marker missing")
        return 2

    # Dedup check: API output only, never PR text execution.
    out = subprocess.run(
        ["gh", "api", f"repos/{args.repo}/issues/{args.pr}/comments", "--paginate"],
        capture_output=True, text=True, check=False)
    if out.returncode != 0:
        # Cannot prove dedup: fail safe, do not post a possible duplicate.
        print("VALIDATION_FAILED: could not list existing comments for dedup check")
        return 2
    if MARKER in out.stdout:
        print("SKIP=true")
        return 0
    print("OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
