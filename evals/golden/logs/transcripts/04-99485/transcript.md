SKILL_LOADED pr-triage v1.0.0
Scripts to run, in order: classify_diff.py, check_issue_link.py, check_template_labels.py, count_author_open_prs.py, check_sha_equality.py
Snapshot: first-time external, blz-ea, opened 2026-09-30 16:46 UTC, draft=false, single commit
Opening-diff proof: OPENING DIFF PROVEN by single-commit status: 4 files.
Title: fix: Bump vendored @mswjs/interceptors from 0.42.5 to 0.42.6
Body: see /tmp/dryrun/cases body.txt for the reconstructed snapshot body used (verbatim opening body only where the case sheet supplies it; otherwise a case-sheet summary, flagged above). Post-event facts were excluded.
Filter applied: none — proceeds to scripts and judgement

--- classify (exit 0) ---
{"error": null, "result": {"counts": {"docs": 0, "other": 3, "source": 1, "test": 0, "workflow": 0}, "docs_only": false, "empty": false, "file_count": 4, "files": [{"category": "other", "path": "packages/next/package.json"}, {"category": "source", "path": "packages/next/src/compiled/@mswjs/interceptors/ClientRequest/index.js"}, {"category": "other", "path": "pnpm-lock.yaml"}, {"category": "other", "path": "pnpm-workspace.yaml"}], "other_touched": true, "source_touched": true, "test_touched": false, "workflow_touched": false}, "script": "classify_diff", "status": "ok", "version": "1.0.0"}
--- issue (exit 0) ---
{"error": null, "result": {"bare_mentions": [], "closing_links": [], "empty_body": false, "has_issue_link": false, "linked_issue_in_snapshot": null, "linked_issue_numbers": []}, "script": "check_issue_link", "status": "ok", "version": "1.0.0"}
--- template (exit 0) ---
{"error": null, "result": {"empty_body": false, "label_check": {"error": null, "expected_labels": null, "labels": [], "missing": null, "present": null, "status": "ok"}, "template_check": {"error": null, "sections": [{"present": true, "section": "What?"}, {"present": true, "section": "Why?"}, {"present": false, "section": "How?"}], "status": "ok"}}, "script": "check_template_labels", "status": "ok", "version": "1.0.0"}
--- author (exit 0) ---
{"error": null, "result": {"author": "blz-ea", "current_pr": 99485, "current_pr_in_snapshot": true, "open_pr_numbers": [99485], "other_open_prs": 0, "total_open_prs_in_snapshot": 1}, "script": "count_author_open_prs", "status": "ok", "version": "1.0.0"}
--- check_sha_equality (exit 2) ---
sha_check: not applicable — no SHAs in snapshot

Judgement (SKILL section 4 only, after scripts): see draft comment / filter log below. No merge readiness, signature, CI, or post-event outcome was judged as decided.

--- DRAFT / FILTER LOG ---
Triage (automated first pass — human decision still required)

- Diff: 4 file(s); docs_only=false; workflow_touched=false; source_touched=true; test_touched=false.
- Issue link: has_issue_link=false; no vercel/next.js closing link in the PR body; upstream mswjs links in the body are not counted as a closing link; issue existence was not verified.
- Template / labels: What?=true; Why?=true; How?=false; labels: none recorded in the snapshot.
- Assessment: Vendored bump only, with an upstream justification stated in the body. No test file in the diff. Human review of the vendored change is needed. No merge recommendation.
- Checks that could not run: check_sha_equality (no SHAs in snapshot).

Automated triage — not a maintainer decision.
<!-- pr-triage-agent -->

Validation by hand inspection (validator script not run as a job): length=769 characters (<=1500), footer present, marker present, exactly one comment, no close/merge/label/assign/force-push language as an agent action.

Model: Muse Spark, version not reported
Dry run only: no action was taken on vercel/next.js or on any live repository; nothing was closed, merged, labelled, or assigned.
