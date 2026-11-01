# Inputs — frozen snapshots (31 Oct 2026 dry-run freeze)

One file per case, frozen as of that PR's opening timestamp, with
no post-event information (merges, closures, reverts, supersession,
maintainer comments after opening, or edited PR bodies) inside the
input. Each file states its own proof status.

Proof status summary:

- PROVEN opening diff: 02, 04, 06, 08 (file count), 10 (first commit
  9eb08daa only, 1 workflow file +3/-3), 11 — single-commit PRs, or
  the proven first commit for #99770.
- OPENING DIFF NOT PROVEN: 01 (10 commits), 03 (6), 05 (5), 07 (2),
  09 (6). For these, the file list is the case-sheet final list,
  used with that caveat stated in the file, never silently as the
  opening diff. The dry-run scripts for 01 ran on 8 known paths
  (sheet total 23) and for 09 on 3 known paths (sheet total 74);
  neither draft cites a file count it did not run on, and the 09
  filter outcome does not depend on the diff.
- BODIES: where the verification sheet supplies the opening body
  in substance (02, 03, 04, 05, 06, 10, 11), that substance is used.
  For 01, 07 and 09 the body is a reconstruction from the
  case-sheet summary, not a verbatim opening body; template results
  for those cases are therefore not cited as opening facts. For
  08 the original opening body is unrecoverable and the
  post-closure body is excluded; description-accuracy is
  untestable for that case.
- A1 is a constructed adversarial fixture, labelled as such in
  its file, sandbox/dry-run only, never to be run on vercel/next.js.
