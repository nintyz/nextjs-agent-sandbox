SKILL_LOADED pr-triage v1.0.0
Scripts to run, in order: classify_diff.py, check_issue_link.py, check_template_labels.py, count_author_open_prs.py, check_sha_equality.py
Snapshot: bot, next-js-bot[bot], opened 2026-10-06, draft=false
Opening-diff proof: OPENING DIFF NOT PROVEN: 6 commits; GitHub get_commits attempt could not be parsed. File list used is a partial known list (3 paths) vs sheet final total 74 files; filter outcome does not depend on the diff.
Title: Upgrade React from 278794d7-20261002 to 17eca7b0-20261006
Body: see /tmp/dryrun/cases body.txt for the reconstructed snapshot body used (verbatim opening body only where the case sheet supplies it; otherwise a case-sheet summary, flagged above). Post-event facts were excluded.
Filter applied: bot

--- classify (exit 0) ---
{"error": null, "result": {"counts": {"docs": 0, "other": 2, "source": 1, "test": 0, "workflow": 0}, "docs_only": false, "empty": false, "file_count": 3, "files": [{"category": "other", "path": "package.json"}, {"category": "other", "path": "pnpm-lock.yaml"}, {"category": "source", "path": "packages/next/src/compiled/react/index.js"}], "other_touched": true, "source_touched": true, "test_touched": false, "workflow_touched": false}, "script": "classify_diff", "status": "ok", "version": "1.0.0"}
--- issue (exit 0) ---
{"error": null, "result": {"bare_mentions": [37730, 37757], "closing_links": [], "empty_body": false, "has_issue_link": false, "linked_issue_in_snapshot": null, "linked_issue_numbers": []}, "script": "check_issue_link", "status": "ok", "version": "1.0.0"}
--- template (exit 0) ---
{"error": null, "result": {"empty_body": false, "label_check": {"error": null, "expected_labels": null, "labels": [], "missing": null, "present": null, "status": "ok"}, "template_check": {"error": null, "sections": [{"present": false, "section": "What?"}, {"present": false, "section": "Why?"}, {"present": false, "section": "How?"}], "status": "ok"}}, "script": "check_template_labels", "status": "ok", "version": "1.0.0"}
--- author (exit 0) ---
{"error": null, "result": {"author": "next-js-bot", "current_pr": 99737, "current_pr_in_snapshot": true, "open_pr_numbers": [99737], "other_open_prs": 0, "total_open_prs_in_snapshot": 1}, "script": "count_author_open_prs", "status": "ok", "version": "1.0.0"}
--- check_sha_equality (exit 2) ---
sha_check: not applicable — no SHAs in snapshot

Judgement (SKILL section 4 only, after scripts): see draft comment / filter log below. No merge readiness, signature, CI, or post-event outcome was judged as decided.

--- DRAFT / FILTER LOG ---
filter: bot PR, no triage comment

Model: Muse Spark, version not reported
Dry run only: no action was taken on vercel/next.js or on any live repository; nothing was closed, merged, labelled, or assigned.
