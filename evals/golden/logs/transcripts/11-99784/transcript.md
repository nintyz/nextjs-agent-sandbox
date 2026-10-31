SKILL_LOADED pr-triage v1.0.0
Scripts to run, in order: classify_diff.py, check_issue_link.py, check_template_labels.py, count_author_open_prs.py, check_sha_equality.py
Snapshot: internal member, eps1lon, opened 2026-10-07, draft=true, single commit
Opening-diff proof: OPENING DIFF PROVEN by single-commit status: 2 test files.
Title: [test] Report deploy queue vs build timings in deploy tests
Body: see /tmp/dryrun/cases body.txt for the reconstructed snapshot body used (verbatim opening body only where the case sheet supplies it; otherwise a case-sheet summary, flagged above). Post-event facts were excluded.
Filter applied: draft (member non-workflow also applies)

--- classify (exit 0) ---
{"error": null, "result": {"counts": {"docs": 0, "other": 0, "source": 0, "test": 2, "workflow": 0}, "docs_only": false, "empty": false, "file_count": 2, "files": [{"category": "test", "path": "test/lib/e2e-utils/index.ts"}, {"category": "test", "path": "test/lib/next-modes/next-deploy.ts"}], "other_touched": false, "source_touched": false, "test_touched": true, "workflow_touched": false}, "script": "classify_diff", "status": "ok", "version": "1.0.0"}
--- issue (exit 0) ---
{"error": null, "result": {"bare_mentions": [99770], "closing_links": [], "empty_body": false, "has_issue_link": false, "linked_issue_in_snapshot": null, "linked_issue_numbers": []}, "script": "check_issue_link", "status": "ok", "version": "1.0.0"}
--- template (exit 0) ---
{"error": null, "result": {"empty_body": false, "label_check": {"error": null, "expected_labels": null, "labels": [], "missing": null, "present": null, "status": "ok"}, "template_check": {"error": null, "sections": [{"present": true, "section": "What?"}, {"present": true, "section": "Why?"}, {"present": true, "section": "How?"}], "status": "ok"}}, "script": "check_template_labels", "status": "ok", "version": "1.0.0"}
--- author (exit 0) ---
{"error": null, "result": {"author": "eps1lon", "current_pr": 99784, "current_pr_in_snapshot": true, "open_pr_numbers": [99784], "other_open_prs": 0, "total_open_prs_in_snapshot": 1}, "script": "count_author_open_prs", "status": "ok", "version": "1.0.0"}
--- check_sha_equality (exit 2) ---
sha_check: not applicable — no SHAs in snapshot

Judgement (SKILL section 4 only, after scripts): see draft comment / filter log below. No merge readiness, signature, CI, or post-event outcome was judged as decided.

--- DRAFT / FILTER LOG ---
filter: draft PR, no triage comment until ready for review

Model: Muse Spark, version not reported
Dry run only: no action was taken on vercel/next.js or on any live repository; nothing was closed, merged, labelled, or assigned.
