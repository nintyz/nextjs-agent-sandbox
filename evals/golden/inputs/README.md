# Inputs — not yet frozen in this scaffold

Input snapshots are not included in this initial scaffold. Each case
in `cases/` must be frozen as of its PR opening timestamp, with no
post-event information (merges, closures, reverts, supersession,
maintainer comments after opening, or edited PR bodies) inside the
input.

For multi-commit PRs (#99574, #92646, #99737, #96622), reconstruct
the diff from commits dated at or before opening. Only single-commit
PRs and #99770's first commit have a proven opening diff so far.

Verification sheets (with knowable-at-opening separated from
post-event information) are in the workspace under
`assignment3-agent-output/golden-cases/` and must not be copied
wholesale into snapshots, because the raw outputs there contain
post-event state.
