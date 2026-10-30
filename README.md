# nextjs-agent-sandbox — Assignment 3

Sandbox repository for Assignment 3: Configuring and Governing AI Agents.

This is a representative subset of `vercel/next.js`, built for evaluating
an external pull-request pre-flight and first-pass triage agent. It is
not `vercel/next.js` and must not be presented as a copy of it.
Upstream reference: Assignment 2 data freeze, 15 October 2026,
canary HEAD `10c5a6a`.

## Status: initial scaffold, not the submission freeze

- Engine: GitHub Actions (Aaron's decision, 30 Oct 2026).
  Workflow: `.github/workflows/pr-triage.yml` (two jobs: read-only
  triage, comment-only applier). There is no `.lock.yml`, because a
  lockfile is a GitHub Agentic Workflows artefact and Actions has no
  compilation step; the committed `.yml` itself is the execution file.
- Golden cases: locked 30 Oct 2026 (11 historical + 1 adversarial).
  See `evals/golden/expected_outputs/` for expected outcomes written
  before any agent run, and `evals/golden/REPRODUCE.md`.
- Input snapshots for multi-commit PRs are not yet reconstructed in
  this scaffold. They must be reconstructed as of each PR's opening
  timestamp from commits dated at or before opening, and must not
  silently use the current file list. See `evals/golden/inputs/README.md`.
- Freeze blockers, not yet done: SHA pins for every third-party action
  in the workflow (placeholders must be replaced at freeze and the
  smoke test re-run), GitHub Models inference endpoint smoke test,
  Aaron's actual Copilot/Student plan and allowance from his billing
  page, `ctreude` added as a collaborator before submission, and
  Aaron's confirmation of the AI-use statement in `DESIGN.md`.
- Every stub in this scaffold is labelled as a stub in its own header.
  No stub is upstream source code.

## What the agent does and does not do

- At most one triage comment per PR, or no comment for filter cases
  (bot author, draft until `ready_for_review`, member author unless
  workflow files are touched, empty diff, or a triage marker already
  present).
- It never closes, merges, deletes, labels, assigns, or force-pushes
  anything. Every merge, adoption, and closure decision stays human.
- It never checks out or executes PR head code. Both workflow jobs
  check out the base branch only.
