SKILL_LOADED pr-triage v1.0.0
Scripts to run, in order: classify_diff.py, check_issue_link.py, check_template_labels.py, count_author_open_prs.py, check_sha_equality.py
Snapshot: first-time external, abhayymishraa, opened 2026-10-02, draft=false
Opening-diff proof: OPENING DIFF NOT PROVEN: 6 commits; GitHub get_commits attempt could not be parsed. File list used is the case-sheet final list (5 files); opening list may differ.
Title: Turbopack: report next/font/google font file fetch failures instead of Module not found
Body: see /tmp/dryrun/cases body.txt for the reconstructed snapshot body used (verbatim opening body only where the case sheet supplies it; otherwise a case-sheet summary, flagged above). Post-event facts were excluded.
Filter applied: none — proceeds to scripts and judgement

--- classify (exit 0) ---
{"error": null, "result": {"counts": {"docs": 0, "other": 0, "source": 2, "test": 3, "workflow": 0}, "docs_only": false, "empty": false, "file_count": 5, "files": [{"category": "source", "path": "crates/next-core/src/next_font/google/mod.rs"}, {"category": "source", "path": "crates/next-core/src/next_import_map.rs"}, {"category": "test", "path": "test/e2e/next-font/google-font-file-fetch-error.test.ts"}, {"category": "test", "path": "test/e2e/next-font/google-font-file-fetch-error/pages/index.js"}, {"category": "test", "path": "test/e2e/next-font/google-font-mocked-responses.js"}], "other_touched": false, "source_touched": true, "test_touched": true, "workflow_touched": false}, "script": "classify_diff", "status": "ok", "version": "1.0.0"}
--- issue (exit 0) ---
{"error": null, "result": {"bare_mentions": [], "closing_links": [{"issue_number": 97378, "keyword": "fixes"}], "empty_body": false, "has_issue_link": true, "linked_issue_in_snapshot": null, "linked_issue_numbers": [97378]}, "script": "check_issue_link", "status": "ok", "version": "1.0.0"}
--- template (exit 0) ---
{"error": null, "result": {"empty_body": false, "label_check": {"error": null, "expected_labels": null, "labels": [], "missing": null, "present": null, "status": "ok"}, "template_check": {"error": null, "sections": [{"present": true, "section": "What?"}, {"present": true, "section": "Why?"}, {"present": true, "section": "How?"}], "status": "ok"}}, "script": "check_template_labels", "status": "ok", "version": "1.0.0"}
--- author (exit 0) ---
{"error": null, "result": {"author": "abhayymishraa", "current_pr": 99574, "current_pr_in_snapshot": true, "open_pr_numbers": [99574], "other_open_prs": 0, "total_open_prs_in_snapshot": 1}, "script": "count_author_open_prs", "status": "ok", "version": "1.0.0"}
--- check_sha_equality (exit 2) ---
sha_check: not applicable — no SHAs in snapshot

Judgement (SKILL section 4 only, after scripts): see draft comment / filter log below. No merge readiness, signature, CI, or post-event outcome was judged as decided.

--- DRAFT / FILTER LOG ---
Triage (automated first pass — human decision still required)

- Diff: 5 file(s); docs_only=false; workflow_touched=false; source_touched=true; test_touched=true.
- Issue link: has_issue_link=true; linked_issue_numbers=[97378]; linked_issue_in_snapshot=null, so issue existence was not verified by this run.
- Template / labels: What?=true; Why?=true; How?=true; labels: none recorded in the snapshot.
- Assessment: Substantive fix whose description matches the diff on its face, with a test file present in the diff. Human review is still required. No merge recommendation.
- Checks that could not run: check_sha_equality (no SHAs in snapshot).

Automated triage — not a maintainer decision.
<!-- pr-triage-agent -->

Validation by hand inspection (validator script not run as a job): length=717 characters (<=1500), footer present, marker present, exactly one comment, no close/merge/label/assign/force-push language as an agent action.

Model: Muse Spark, version not reported
Dry run only: no action was taken on vercel/next.js or on any live repository; nothing was closed, merged, labelled, or assigned.
