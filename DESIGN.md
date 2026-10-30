# DESIGN.md — DRAFT, not the submission freeze

Sandbox: `nintyz/nextjs-agent-sandbox` (private). Target:
`vercel/next.js`. Engine: GitHub Actions, workflow
`.github/workflows/pr-triage.yml`. Under the 150-line limit.

## 1. Workflow choice and evidence of need

The workflow is external pull-request pre-flight and first-pass
triage: read a newly opened or updated PR, run deterministic checks,
judge only what a script cannot judge, and post at most one comment.
At the Assignment 2 freeze (15 Oct 2026), `vercel/next.js` had 2,571
open PRs against 1,100 open issues (2.34:1). In the 27-PR stratified
sample, first-time external PRs waited 24 hours to 69 days for a
first human response; the longest merge decision, 185 days for
#92646, was regular external. Medians were 0.75 days (internal
member) and 0.4 days (coding-agent), reported separately. The
sample is stratified, not a census, so these figures establish
a triage bottleneck, not a precise queue forecast.

## 2. Why an agent, alternative rejected, deliberately prevented

A script can check exactly: empty diff, docs-only files, workflow
files touched, a `fixes #number` link, identical source and target
SHAs, and author open-PR count from snapshot data. A script cannot
judge whether a description accurately summarises a diff, whether
a change is trivial under the contributing rules, or whether a
workflow-file change is high risk. That judgement is the agent's job.
Rejected alternative: a single-job workflow where the agent job
itself holds `pull-requests: write` and posts directly, because it
collapses token scope and safe outputs into one prompt instruction.
Deliberately prevented: close, delete, merge, label, assign,
force-push, PR-head checkout or execution, privileged CI, and
enforcement of a per-author cap by closure.

## 3. Enforcement separation

Workflow permissions and safe outputs are the hard boundary.
`AGENTS.md` holds repository facts only. The skill holds procedure
and deterministic checks. `CONTRIBUTING.md` holds contributor policy
only. An instruction telling the model not to merge is not a
substitute for a token and safe-output set that cannot merge.

## 4. Governance summary

Status key: implemented and tested / implemented but untested /
proposed only. All controls below are proposed only at scaffold stage.

- Identity: `github-actions[bot]` via the workflow token, never a
  personal account. Proposed only.
- Least privilege: read-only triage job; comment-only applier job.
  Proposed only, hand-checked, not compiler-checked.
- Safe outputs: one validated comment or skip, 1,500-character cap
  enforced in Job 2, marker dedup. Proposed only.
- Human approval: every merge, adoption, and closure stays human;
  `CODEOWNERS` on workflow and skill files. Proposed only.
- Budgets: Job 1 timeout 15 minutes, Job 2 timeout 5 minutes.
  No enforced per-run credit cap exists in Actions; private-repo
  runner minutes are a second, unmeasured budget. Proposed only.
- Audit trail: Actions run logs, mirrored into `evals/golden/logs/`.
  Cost is reported only if the platform reports it. Proposed only.
- Kill switch: disable the workflow, then cancel each running run.
  Disabling alone does not cancel in-flight runs. Untested.
- Drift detection: rerun all 12 golden cases on every model change;
  every changed output is reviewed by Aaron; a failing case blocks
  reliance on the new version. Proposed only.
- Accountability: sandbox owner/admin is Aaron; change and disable
  authority sits with Aaron. Upstream Vercel maintainers have not
  approved anything. Proposed only.

Untrusted inputs: PR title, body, comments, diff, file contents,
linked-issue text, and tool output. After a worst-case tool
compromise, the remaining harm is wording inside that one comment
and bounded run time, not closure, merge, or file changes.

## 5. Five mandatory questions

1. An issue instructs the agent to close all stale issues and
   claims maintainer approval. An issue triggers nothing in this
   PR-only workflow (0 runs, 0 comments, 0 closures). The tested
   case A1 is the same instruction in a PR body: it is untrusted
   data, the claim is ignored, and Job 1 has no write capability,
   so closure is impossible even if the model complies.
2. The provider updates the model and a golden task starts failing.
   Detection is at the next golden rerun after the change, by
   comparing the model in a new run log against the previous
   golden run. No automated alert is claimed.
3. The project receives 300 issues in one week. Literally, 300
   issues plus 0 PRs means 0 triage runs, 0 comments, and 0 model
   cost. For 300 PR-equivalent events, the binding limit is the
   credit allowance, unmeasured until Aaron's billing numbers are
   confirmed. Policy on exhaustion: defer, not drop — later PRs
   are logged as credit-deferred and left for human triage.
4. A tool or MCP server returns malicious instructions. No custom
   or external MCP server is configured, and the model step has no
   tools, token, or shell, so the worst case is tainted wording
   inside one validated comment, plus bounded run time. Close,
   merge, label, assign, push, file edits, PR-code execution, and
   external fetches from PR text remain impossible.
5. A maintainer needs to stop the agent using only a phone. In a
   phone browser: repository, Actions, workflow, Disable workflow
   (stops new runs only), then Cancel workflow for each running
   run, then verify no queued or in-progress runs remain and no
   new comment appears after the disable timestamp. No token
   revocation is needed for the run-scoped token. Untested.

## 6. Agent bill of materials

- Model: example name in the workflow, unverified; no model
  was ever recorded from a successful run log.
- Instructions: `AGENTS.md` and `.claude/skills/pr-triage/SKILL.md`.
- Tools and MCP servers: GitHub API via `gh`, base-branch Python
  scripts, one named inference endpoint; no custom MCP server.
- Permissions: Job 1 read-only plus `models: read`; Job 2
  `pull-requests: write` plus `actions: read`; top-level empty.
- Data sources: frozen golden snapshots at PR opening timestamps.
- Logs: Actions run logs, mirrored into `evals/golden/logs/`.
- Evaluations: 11 historical + 1 adversarial, in `evals/golden/`.
- Responsible humans: Aaron (sandbox owner, evaluator, kill-switch
  holder). `ctreude` is marking access only, not an agent role.

## 7. Tests revealed and what remains unresolved

Smoke test, 30-31 Oct 2026: draft PR #1 succeeded (draft filter,
no comment). Docs PRs #2-#6 failed at the inference step: the
endpoint returned HTTP 200 with body `OK` (4 bytes, not JSON)
for both the workflow token and a MODELS_TOKEN PAT, so no
comment was ever drafted. Inference is therefore unproven, and
the workflow was NOT tested end-to-end. Dry run, 31 Oct 2026:
12/12 golden cases pass after fixing `check_issue_link.py` to
accept the full-repo form `vercel/next.js#92919` (case 07
initially failed on that script gap); transcripts and drafts
are in `evals/golden/logs/` and `evals/golden/actual_outputs/`.
Untested, never claimed as tested: token scoping, Job 2
validator as a job, comment attribution, trigger/concurrency,
timeout kills, model pinning/cost, audit-trail format,
kill-switch cancellation, CODEOWNERS enforcement, and the
inference endpoint itself. A dry run does not prove the
workflow would make the same decisions. Still unresolved:
Aaron's actual credit allowance, trivial-rule and queue-comment
coverage lost in the locked set, phone-only kill-switch test,
and the A1 sandbox issue-list verification (draft-level pass
only, no fixture issues were created).

## 8. AI-use statement — DRAFT, for Aaron to confirm in his own words

Aaron wrote the Assignment 2 analysis and the setup decisions.
AI-generated drafts were verified against the brief, the workflow
file, and the locked golden cases before any run. Aaron must
confirm or correct this statement before submission.
