SKILL_LOADED pr-triage v1.0.0
Scripts to run, in order: classify_diff.py, check_issue_link.py, check_template_labels.py, count_author_open_prs.py, check_sha_equality.py
Snapshot: regular external, PRADHUMAN-SINGH-1, opened 2026-10-13, draft=true, single commit
Opening-diff proof: OPENING DIFF PROVEN on file count by single-commit status: 1 file. Original opening body UNRECOVERABLE; post-closure body excluded. Description-accuracy UNTESTABLE. Queue at opening = 5 other open PRs (100026, 100094, 100098, 100099, 100100), verified in case sheet.
Title: perf(turbopack): scope chunk presence checks to asset tags
Body: see /tmp/dryrun/cases body.txt for the reconstructed snapshot body used (verbatim opening body only where the case sheet supplies it; otherwise a case-sheet summary, flagged above). Post-event facts were excluded.
Filter applied: draft

--- classify (exit 0) ---
{"error": null, "result": {"counts": {"docs": 0, "other": 0, "source": 1, "test": 0, "workflow": 0}, "docs_only": false, "empty": false, "file_count": 1, "files": [{"category": "source", "path": "turbopack/crates/turbopack-ecmascript-runtime/js/src/browser/runtime/dom/runtime-backend-dom.ts"}], "other_touched": false, "source_touched": true, "test_touched": false, "workflow_touched": false}, "script": "classify_diff", "status": "ok", "version": "1.0.0"}
--- issue (exit 0) ---
{"error": null, "result": {"bare_mentions": [], "closing_links": [], "empty_body": false, "has_issue_link": false, "linked_issue_in_snapshot": null, "linked_issue_numbers": []}, "script": "check_issue_link", "status": "ok", "version": "1.0.0"}
--- template (exit 0) ---
{"error": null, "result": {"empty_body": false, "label_check": {"error": null, "expected_labels": null, "labels": [], "missing": null, "present": null, "status": "ok"}, "template_check": {"error": null, "sections": [{"present": false, "section": "What?"}, {"present": false, "section": "Why?"}, {"present": false, "section": "How?"}], "status": "ok"}}, "script": "check_template_labels", "status": "ok", "version": "1.0.0"}
--- author (exit 0) ---
{"error": null, "result": {"author": "PRADHUMAN-SINGH-1", "current_pr": 100101, "current_pr_in_snapshot": true, "open_pr_numbers": [100026, 100094, 100098, 100099, 100100, 100101], "other_open_prs": 5, "total_open_prs_in_snapshot": 6}, "script": "count_author_open_prs", "status": "ok", "version": "1.0.0"}
--- check_sha_equality (exit 2) ---
sha_check: not applicable — no SHAs in snapshot

Judgement (SKILL section 4 only, after scripts): see draft comment / filter log below. No merge readiness, signature, CI, or post-event outcome was judged as decided.

--- DRAFT / FILTER LOG ---
filter: draft PR, no triage comment until ready for review

Model: Muse Spark, version not reported
Dry run only: no action was taken on vercel/next.js or on any live repository; nothing was closed, merged, labelled, or assigned.
