# nextjs-agent-sandbox — Assignment 3

Sandbox repository for Assignment 3: Configuring and Governing AI Agents.

This is a representative subset of `vercel/next.js`, built for evaluating
an external pull-request pre-flight and first-pass triage agent. It is
not `vercel/next.js` and must not be presented as a copy of it.
Upstream reference: Assignment 2 data freeze, 15 October 2026,
canary HEAD `10c5a6a`.

## Status: submission freeze candidate

- Engine: GitHub Actions (Aaron's decision, 30 Oct 2026).
  Workflow: `.github/workflows/pr-triage.yml` (two jobs: read-only
  triage, comment-only applier). There is no `.lock.yml`, because a
  lockfile is a GitHub Agentic Workflows artefact and Actions has no
  compilation step; the committed `.yml` itself is the execution file.
- Golden cases: locked 30 Oct 2026 (11 historical + 1 adversarial).
  See `evals/golden/expected_outputs/` for expected outcomes written
  before any agent run, and `evals/golden/REPRODUCE.md`.
- Evaluation: live inference failed (see DESIGN.md §7), so the
  golden cases were run as a dry run on 31 Oct 2026: 12 pass, 0 fail
  after one script fix. Transcripts are in
  `evals/golden/logs/transcripts/`, drafts in
  `evals/golden/actual_outputs/`, report in
  `evals/golden/logs/dry-run-report.md`.
- Input snapshots: frozen in `evals/golden/inputs/` as of each PR's
  opening timestamp, with proof caveats stated in
  `evals/golden/inputs/README.md`. Opening diffs for multi-commit
  PRs could not be proven from commit dates and are flagged there,
  not silently presented as proven.
- Action SHA pins: resolved 30 Oct 2026 and present in the workflow.
- Before submitting: add `ctreude` as a collaborator on the private
  repository, then submit the link to the frozen commit via eLearn.

## What the agent does and does not do

- At most one triage comment per PR, or no comment for filter cases
  (bot author, draft until `ready_for_review`, member author unless
  workflow files are touched, empty diff, or a triage marker already
  present).
- It never closes, merges, deletes, labels, assigns, or force-pushes
  anything. Every merge, adoption, and closure decision stays human.
- It never checks out or executes PR head code. Both workflow jobs
  check out the base branch only.
