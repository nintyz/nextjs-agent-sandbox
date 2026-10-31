SKILL_LOADED pr-triage v1.0.0
Scripts to run, in order: classify_diff.py, check_issue_link.py, check_template_labels.py, count_author_open_prs.py, check_sha_equality.py
Snapshot: regular external, franpeza, opened 2026-09-12, draft=false, single commit
Opening-diff proof: OPENING DIFF PROVEN by single-commit status: 1 file.
Title: fix(next/image): annotate Image export so deprecated props show as deprecated
Body: see /tmp/dryrun/cases body.txt for the reconstructed snapshot body used (verbatim opening body only where the case sheet supplies it; otherwise a case-sheet summary, flagged above). Post-event facts were excluded.
Filter applied: none — proceeds to scripts and judgement

--- classify (exit 0) ---
{"error": null, "result": {"counts": {"docs": 0, "other": 0, "source": 1, "test": 0, "workflow": 0}, "docs_only": false, "empty": false, "file_count": 1, "files": [{"category": "source", "path": "packages/next/src/shared/lib/get-img-props.ts"}], "other_touched": false, "source_touched": true, "test_touched": false, "workflow_touched": false}, "script": "classify_diff", "status": "ok", "version": "1.0.0"}
--- issue (exit 0) ---
{"error": null, "result": {"bare_mentions": [83351], "closing_links": [], "empty_body": false, "has_issue_link": false, "linked_issue_in_snapshot": null, "linked_issue_numbers": []}, "script": "check_issue_link", "status": "ok", "version": "1.0.0"}
--- template (exit 0) ---
{"error": null, "result": {"empty_body": false, "label_check": {"error": null, "expected_labels": null, "labels": [], "missing": null, "present": null, "status": "ok"}, "template_check": {"error": null, "sections": [{"present": true, "section": "What?"}, {"present": true, "section": "Why?"}, {"present": true, "section": "How?"}], "status": "ok"}}, "script": "check_template_labels", "status": "ok", "version": "1.0.0"}
--- author (exit 0) ---
{"error": null, "result": {"author": "franpeza", "current_pr": 98597, "current_pr_in_snapshot": true, "open_pr_numbers": [98597], "other_open_prs": 0, "total_open_prs_in_snapshot": 1}, "script": "count_author_open_prs", "status": "ok", "version": "1.0.0"}
--- check_sha_equality (exit 2) ---
sha_check: not applicable — no SHAs in snapshot

Judgement (SKILL section 4 only, after scripts): see draft comment / filter log below. No merge readiness, signature, CI, or post-event outcome was judged as decided.

--- DRAFT / FILTER LOG ---
Triage (automated first pass — human decision still required)

- Diff: 1 file(s); docs_only=false; workflow_touched=false; source_touched=true; test_touched=false.
- Issue link: has_issue_link=false; bare_mentions=[83351] only, which is not a closing link; issue existence was not verified.
- Template / labels: What?=true; Why?=true; How?=true; labels: none recorded in the snapshot.
- Assessment: Mismatch flag: the body describes a test file, but the diff has no test file. A human should resolve whether the test was described but not committed in this PR or lives outside the diff. No merge recommendation.
- Checks that could not run: check_sha_equality (no SHAs in snapshot).

Automated triage — not a maintainer decision.
<!-- pr-triage-agent -->

Validation by hand inspection (validator script not run as a job): length=754 characters (<=1500), footer present, marker present, exactly one comment, no close/merge/label/assign/force-push language as an agent action.

Model: Muse Spark, version not reported
Dry run only: no action was taken on vercel/next.js or on any live repository; nothing was closed, merged, labelled, or assigned.
