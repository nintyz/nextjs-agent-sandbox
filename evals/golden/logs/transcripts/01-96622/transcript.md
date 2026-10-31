SKILL_LOADED pr-triage v1.0.0
Scripts to run, in order: classify_diff.py, check_issue_link.py, check_template_labels.py, count_author_open_prs.py, check_sha_equality.py
Snapshot: first-time external, JannikZed, opened 2026-08-04, draft=false
Opening-diff proof: OPENING DIFF NOT PROVEN: 10 commits; GitHub get_commits attempt could not be parsed into commit dates. File list used is the case-sheet final list (23 files per sheet); script ran on 8 known paths only, so script file_count=8 does NOT equal sheet total 23. Draft cites script count only. Body reconstructed from case-sheet summary, not verbatim opening body; template result therefore not reliable for this case and not cited as an opening fact.
Title: Add cache-handler-redis-turbo example (Next.js 16 Cache Components + Redis)
Body: see /tmp/dryrun/cases body.txt for the reconstructed snapshot body used (verbatim opening body only where the case sheet supplies it; otherwise a case-sheet summary, flagged above). Post-event facts were excluded.
Filter applied: none — proceeds to scripts and judgement

--- classify (exit 0) ---
{"error": null, "result": {"counts": {"docs": 4, "other": 2, "source": 2, "test": 0, "workflow": 0}, "docs_only": false, "empty": false, "file_count": 8, "files": [{"category": "docs", "path": "examples/cache-handler-redis-turbo/README.md"}, {"category": "other", "path": "examples/cache-handler-redis-turbo/package.json"}, {"category": "other", "path": "examples/cache-handler-redis-turbo/compose.yaml"}, {"category": "source", "path": "examples/cache-handler-redis-turbo/app/page.tsx"}, {"category": "source", "path": "examples/cache-handler-redis-turbo/handlers/cache-handler.ts"}, {"category": "docs", "path": "docs/01-app/02-guides/self-hosting.mdx"}, {"category": "docs", "path": "docs/01-app/02-guides/cache-handlers.mdx"}, {"category": "docs", "path": "examples/cache-handler-redis/README.md"}], "other_touched": true, "source_touched": true, "test_touched": false, "workflow_touched": false}, "script": "classify_diff", "status": "ok", "version": "1.0.0"}
--- issue (exit 0) ---
{"error": null, "result": {"bare_mentions": [], "closing_links": [], "empty_body": false, "has_issue_link": false, "linked_issue_in_snapshot": null, "linked_issue_numbers": []}, "script": "check_issue_link", "status": "ok", "version": "1.0.0"}
--- template (exit 0) ---
{"error": null, "result": {"empty_body": false, "label_check": {"error": null, "expected_labels": null, "labels": [], "missing": null, "present": null, "status": "ok"}, "template_check": {"error": null, "sections": [{"present": false, "section": "What?"}, {"present": false, "section": "Why?"}, {"present": false, "section": "How?"}], "status": "ok"}}, "script": "check_template_labels", "status": "ok", "version": "1.0.0"}
--- author (exit 0) ---
{"error": null, "result": {"author": "JannikZed", "current_pr": 96622, "current_pr_in_snapshot": true, "open_pr_numbers": [96622], "other_open_prs": 0, "total_open_prs_in_snapshot": 1}, "script": "count_author_open_prs", "status": "ok", "version": "1.0.0"}
--- check_sha_equality (exit 2) ---
sha_check: not applicable — no SHAs in snapshot

Judgement (SKILL section 4 only, after scripts): see draft comment / filter log below. No merge readiness, signature, CI, or post-event outcome was judged as decided.

--- DRAFT / FILTER LOG ---
Triage (automated first pass — human decision still required)

- Diff: 8 file(s) in the script file list; docs_only=false; workflow_touched=false; source_touched=true; test_touched=false.
- Issue link: has_issue_link=false; no closing link in the PR body; issue existence was not verified.
- Template / labels: not verified by this run (body reconstructed from the case-sheet summary; labels at opening not recorded in the snapshot).
- Assessment: Substantive new example plus docs edits, described in the body as covering Cache Components with Redis where the existing example did not. Human review is needed of the new example's dependencies and handler code. No merge recommendation.
- Checks that could not run: check_sha_equality (no SHAs in snapshot).

Automated triage — not a maintainer decision.
<!-- pr-triage-agent -->

Validation by hand inspection (validator script not run as a job): length=829 characters (<=1500), footer present, marker present, exactly one comment, no close/merge/label/assign/force-push language as an agent action.

Model: Muse Spark, version not reported
Dry run only: no action was taken on vercel/next.js or on any live repository; nothing was closed, merged, labelled, or assigned.
