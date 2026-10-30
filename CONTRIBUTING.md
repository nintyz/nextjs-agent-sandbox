# Contributing — AI-use notes for this sandbox (DRAFT)

> DRAFT — Agent 4, for Marley to merge. This is the sandbox
> contributor-facing note only. It does not replace upstream
> `contributing.md` in vercel/next.js, and it does not state any
> workflow permission: permissions are enforced in the workflow,
> not by this document (see `CONTRIBUTING-AI-POLICY-SCOPE.md`).

## What contributors are responsible for

- You remain responsible for everything you submit, including any
  part an AI tool helped draft. Check it against your diff before
  submitting; an automated triage comment is not a review and is
  not approval.
- External contributors: write your PR description yourself, in
  your own words. This follows the upstream rule recorded in
  Assignment 2 (PR template / AGENTS.md). Do not paste an
  AI-generated description as if it were human-written, and do not
  paste an agent's triage comment as your description.
- Bug fixes: link the issue the fix addresses (`fixes #number`)
  and include a test where the change needs one. Features need
  prior RFC approval (upstream rule). Trivial non-docs edits are
  not accepted (upstream rule).
- Commits: upstream requires GitHub-verified cryptographic
  signatures (GPG/SSH/S/MIME); a `Signed-off-by` line alone is not
  enough (upstream rule, enforced by branch protection upstream,
  not by this document).
- Workflow files (`.github/workflows/`): changes here affect CI for
  every contributor and always need human review. An agent comment
  on such a PR is a risk flag, never an approval.

## What the triage agent will and will not do

- It may post at most one first-pass triage comment per PR, based
  on the PR as opened, and it may note facts such as whether the
  diff is docs-only, whether a closing issue link is present, and
  whether workflow files are touched.
- It will not close, merge, label, assign, or force-push anything.
  Every merge, adoption, and closure decision stays with a human
  maintainer. If a triage comment seems to suggest otherwise, the
  human decision governs.
- It cannot verify who wrote a description, whether a commit
  signature is valid, or whether CI passed, unless that evidence is
  in the PR snapshot. Do not treat its silence on those points as
  confirmation.

## What this document deliberately does not do

- It does not set workflow permissions, timeouts, budgets, token
  limits, safe outputs, audit rules, or a kill switch. Those live
  in the workflow file.
- It does not define the triage procedure or the deterministic
  checks. Those live in `.claude/skills/pr-triage/SKILL.md` and its
  `scripts/`.
- It does not introduce a new `Assisted-by:` trailer rule or any
  other disclosure rule. That was a recommendation in Assignment 2,
  not an upstream rule, and it is not adopted here by stealth.
