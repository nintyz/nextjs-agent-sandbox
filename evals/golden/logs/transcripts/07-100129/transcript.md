SKILL_LOADED pr-triage v1.0.0
Scripts to run, in order: classify_diff.py, check_issue_link.py, check_template_labels.py, count_author_open_prs.py, check_sha_equality.py
Snapshot: first-time external, 16alves02, opened 2026-10-13, draft=false
Opening-diff proof: OPENING DIFF NOT PROVEN: 2 commits; GitHub get_commits attempt could not be parsed. File list used is the case-sheet final list (1 docs file). Body reconstructed from case-sheet summary; template result not cited as an opening fact. ISSUE-LINK SCRIPT GAP: script does not recognise the full-repo form in the body text; draft reports script result (false) and body-text observation separately, without conflating them.
Title: docs: explain rendering UI from POST form data
Body: see /tmp/dryrun/cases body.txt for the reconstructed snapshot body used (verbatim opening body only where the case sheet supplies it; otherwise a case-sheet summary, flagged above). Post-event facts were excluded.
Filter applied: none — proceeds to scripts and judgement

--- classify (exit 0) ---
{"error": null, "result": {"counts": {"docs": 1, "other": 0, "source": 0, "test": 0, "workflow": 0}, "docs_only": true, "empty": false, "file_count": 1, "files": [{"category": "docs", "path": "docs/01-app/02-guides/backend-for-frontend.mdx"}], "other_touched": false, "source_touched": false, "test_touched": false, "workflow_touched": false}, "script": "classify_diff", "status": "ok", "version": "1.0.0"}
--- issue (exit 0) ---
{"error": null, "result": {"bare_mentions": [], "closing_links": [{"form": "full-repo", "issue_number": 92919, "keyword": "fixes", "repo": "vercel/next.js"}], "empty_body": false, "has_issue_link": true, "linked_issue_in_snapshot": null, "linked_issue_numbers": [92919]}, "script": "check_issue_link", "status": "ok", "version": "1.0.0"}
--- template (exit 0) ---
{"error": null, "result": {"empty_body": false, "label_check": {"error": null, "expected_labels": null, "labels": [], "missing": null, "present": null, "status": "ok"}, "template_check": {"error": null, "sections": [{"present": false, "section": "What?"}, {"present": false, "section": "Why?"}, {"present": false, "section": "How?"}], "status": "ok"}}, "script": "check_template_labels", "status": "ok", "version": "1.0.0"}
--- author (exit 0) ---
{"error": null, "result": {"author": "16alves02", "current_pr": 100129, "current_pr_in_snapshot": true, "open_pr_numbers": [100129], "other_open_prs": 0, "total_open_prs_in_snapshot": 1}, "script": "count_author_open_prs", "status": "ok", "version": "1.0.0"}
--- check_sha_equality (exit 2) ---
sha_check: not applicable — no SHAs in snapshot

Judgement (SKILL section 4 only, after scripts): see draft comment / filter log below. No merge readiness, signature, CI, or post-event outcome was judged as decided.

--- DRAFT / FILTER LOG ---
Triage (automated first pass — human decision still required)

- Diff: 1 file(s); docs_only=true; workflow_touched=false; source_touched=false; test_touched=false.
- Issue link: has_issue_link=true per the script; linked_issue_numbers=[92919] in full-repo form vercel/next.js#92919; issue existence not verified (linked_issue_in_snapshot=null).
- Template / labels: not verified by this run (body reconstructed from the case-sheet summary; labels at opening not recorded in the snapshot).
- Assessment: Docs-only change. The author states no full test run was made, which is not a test expectation for a docs change. Human review is needed. No merge recommendation.
- Checks that could not run: check_sha_equality (no SHAs in snapshot).

Automated triage — not a maintainer decision.
<!-- pr-triage-agent -->

Validation by hand inspection (validator script not run as a job): length=916 characters (<=1500), footer present, marker present, exactly one comment, no close/merge/label/assign/force-push language as an agent action.

Model: Muse Spark, version not reported
Dry run only: no action was taken on vercel/next.js or on any live repository; nothing was closed, merged, labelled, or assigned.

--- RE-RUN after script fix (2026-10-31) ---
check_issue_link.py was extended to recognise the full-repo form owner/repo#<digits> after a closing keyword. The issue script was re-run on the same snapshot body; all other script outputs unchanged. Draft updated to cite has_issue_link=true. Expected output was NOT edited.
