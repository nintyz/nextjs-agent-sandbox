# AGENTS.md — Sandbox repository (representative subset of vercel/next.js)

> DRAFT — Agent 4 (Skill and Scripts Designer), for Marley to merge.
> Status: design draft only. Not deployed to vercel/next.js. Engine
> choice (see plan §3) is still pending; nothing in this file depends
> on that choice.
>
> Scope rule for this whole file: repository facts only. No procedure
> is defined here, and no judgement rule is defined here. Procedure
> lives in `.claude/skills/pr-triage/SKILL.md`; hard restrictions live
> in the workflow permissions and safe outputs. If this file and the
> skill disagree, the skill governs procedure and the workflow
> governs what is permitted — this file does not override either.

## 1. What this repository is

- Sandbox copy / representative subset of `vercel/next.js`, built for
  Assignment 3 (Configuring and Governing AI Agents). It is not
  vercel/next.js and must not be presented as a copy of it.
- Upstream reference, from Assignment 2 (data freeze 15 October 2026,
  canary HEAD `10c5a6a`): a TypeScript / Rust monorepo, package
  manager pnpm, ~143k stars, 2,571 open PRs against 1,100 open issues
  at freeze. The sandbox reproduces only the paths the triage checks
  need to see; it does not reproduce the full monorepo.
- What the sandbox omits, deliberately: the Rust/SWC build, the
  1,281-line upstream test matrix (`build_and_test.yml`), the full
  `packages/next` source tree, preview tarballs, deploy tests, and
  any secret-bearing CI. That omission does not change a triage
  decision, because triage here judges only the PR text, the changed
  file list, and frozen snapshot data — it never builds PR code.
- Every stub in this sandbox is labelled as a stub in its own header.
  No stub is a copy of upstream source.

## 2. Sandbox layout

```text
.github/workflows/
  pr-triage.yml             # GitHub Actions workflow (two-job split)
.claude/skills/pr-triage/
  SKILL.md                  # triage procedure (see §5, and the skill file itself)
  scripts/                  # deterministic checks — see SKILL.md §3
AGENTS.md                   # this file: repository facts only
CONTRIBUTING.md             # contributor-facing AI policy (scope in §6 below)
DESIGN.md                   # design justification, max 150 lines (separate workstream)
evals/golden/
  cases/ inputs/ expected_outputs/ actual_outputs/ logs/ REPRODUCE.md
docs/                       # representative docs tree (stub docs, labelled as stubs)
packages/example-package/   # representative source path (stub, labelled as a stub)
.github/workflows/          # representative workflow stub (labelled as a stub)
```

Upstream layout, for reference only (not all present in the sandbox):

```text
packages/next/              # framework source (TypeScript, plus Rust via SWC/Turbopack)
packages/create-next-app/   # scaffolding tool
docs/                       # documentation (MDX)
test/                       # integration / unit test suites
.github/workflows/          # 29 workflows at Assignment 2 freeze, incl. build_and_test.yml
.github/pull_request_template.md
contributing/               # triaging.md, linting.md, pull-request-descriptions.md, …
.husky/                     # git hooks (see forbidden paths, §4)
```

## 3. Build and test commands

### 3a. Commands that run in the sandbox (verified, no network)

These are the only commands the sandbox guarantees. They check the
triage scripts themselves, not upstream code:

```sh
python3 --version            # scripts require Python 3, standard library only
python3 .claude/skills/pr-triage/scripts/classify_diff.py --help
python3 .claude/skills/pr-triage/scripts/check_issue_link.py --help
python3 .claude/skills/pr-triage/scripts/check_sha_equality.py --help
python3 .claude/skills/pr-triage/scripts/count_author_open_prs.py --help
python3 .claude/skills/pr-triage/scripts/check_template_labels.py --help
```

Each script prints exactly one JSON object to stdout and uses exit
code `0` when the check ran and `2` when it could not run (see
SKILL.md §3 and the script headers). No script calls the network
and no script calls the GitHub API.

### 3b. Upstream commands (facts about vercel/next.js, NOT run in the sandbox)

Recorded in Assignment 2 / upstream contributing material. The
triage agent does not run these, and the sandbox does not provide
the dependencies to run them:

```sh
pnpm install                 # pnpm workspace install (upstream package manager)
pnpm build                   # upstream build (includes native SWC/Turbopack work)
pnpm new-test -- --args <appDir> <name> <type>   # generate a new test suite (upstream)
pnpm pr-adopt <pr>           # maintainer adoption of a fork PR into an internal branch
```

Upstream CI checks recorded in Assignment 2: ESLint (flat config),
Prettier, `alex`, browser-variant alias check
(`git diff --exit-code`), precompiled type checks, and
`ast-grep@1.5.0`. The sandbox does not reproduce these checks; a
triage comment must never claim they passed unless a CI result is
in the frozen snapshot.

### 3c. What is never built here

- No Rust/SWC compilation, no `pnpm build` of `packages/next`, no
  deploy test, no preview tarball. If a future sandbox change needs
  a real build, that is a new scope decision for Marley, not
  something this file authorises.

## 4. Conventions (repository facts, not triage procedure)

- Package manager: pnpm, not npm or yarn (upstream workspaces).
- Language: TypeScript for framework code; Rust for SWC/Turbopack
  components (upstream only, not in the sandbox subset).
- Formatting / lint: ESLint flat config, Prettier, `alex` (upstream).
- Commit signatures: upstream requires GitHub-verified cryptographic
  signatures (GPG/SSH/S/MIME). A `Signed-off-by` line alone is not
  enough (Assignment 2, §1). This is a fact about upstream
  enforcement (branch protection), not a check this triage agent
  performs — the scripts do not verify signatures.
- Linked issues: upstream contributing rules require bug fixes to
  link an issue (`fixes #number`) and, for fixes, a test suite via
  `pnpm new-test`. Features require prior RFC approval and
  telemetry. These are upstream facts; whether a given PR satisfies
  them is a skill judgement, not a fact stated here.
- Trivial non-docs edits: upstream contributing rules ban them.
  Whether a given diff is trivial is a skill judgement, not stated
  here.
- External PR descriptions: upstream PR template / AGENTS.md state
  that descriptions from external contributors must be human-written.
  Assignment 2 found no CI check enforcing this (prompt honour
  system). The triage scripts do not detect authorship.
- AI co-author footers: upstream AGENTS.md prohibits
  `Generated with Claude Code` / co-author footers, while Assignment
  2 found merged PRs carrying them. The scripts do not detect
  authorship and this file does not resolve that upstream tension.

## 5. Forbidden paths (facts about this sandbox)

Paths the triage run must not treat as ordinary editable content.
This list is about repository structure, not about what the agent
may decide — permitted actions are set by workflow permissions:

- `.github/workflows/` — workflow definitions; a PR touching this
  path is a workflow-file PR (see skill, workflow-file risk flag).
- `.claude/skills/` — skill and scripts; the triage agent reads
  these, it does not rewrite them during a triage run.
- `AGENTS.md`, `CONTRIBUTING.md`, `DESIGN.md` — governance and
  design documents; not triage targets.
- `evals/golden/expected_outputs/` — expected outcomes are written
  before any agent run and are never overwritten by a run.
- `.husky/` (upstream) — git hooks; never executed by a triage run.
- Any path outside the sandbox repository, and any secret, token,
  or credential file. The triage run has no credential to read and
  no path outside the repository to write to.

## 6. Where the other rules live (enforcement separation)

- Workflow permissions and safe outputs: the hard boundary
  (read-only by default, comment-only output, one comment per PR
  per run, no close / delete / merge / force-push). Owned by the
  workflow/governance workstream.
- Skill (`.claude/skills/pr-triage/SKILL.md` plus `scripts/`):
  the step-by-step procedure and the deterministic checks.
- `CONTRIBUTING.md`: contributor-facing AI policy only — see the
  scope note in `CONTRIBUTING-AI-POLICY-SCOPE.md` in this draft
  folder. Workflow permissions are not duplicated there as policy
  sentences.
- This file deliberately contains no step-by-step procedure, no
  "if X then comment Y" judgement rule, and no permission claim.
  Any such sentence found here during review is a defect to be
  moved to the skill or the workflow, not kept here.
