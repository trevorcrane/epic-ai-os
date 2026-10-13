# Index reconciliation with current main

Current main for this note is `74d111fa6260c0d9415ff388bdfc76c51f922df7`. This branch starts there. It does not merge PR #4 or PR #5 and it does not copy their files.

## Twelve laws on main

These three indexes list the same twelve files, in the same order, after this pass:

- `AGENTS.md` fleet law list
- `rules/README.md`
- `fleet-os/GROKBOT_OS.md` fleet law list

Before this pass, the Grok list placed Cloudflare Pages after the site ship loop. `rules/README.md` and `AGENTS.md` already placed it before Launch QC. The Grok list now follows that order. The rule files themselves are unchanged.

## Laws that are not on main

| PR | File on that PR | State here |
|---|---|---|
| #4 | `rules/NO-UNAPPROVED-FRAMEWORK-EDITS.md` | Not added. The reviewer-bar note follows that PR's propose-then-stop procedure and says so. |
| #5 | `rules/ACT-AND-FINISH-HOT-POTATO.md` | Not added. No other file on that PR is taken. |

PR #5 tells the reader to use `DEFINITION-OF-DONE.md` for the five-part handoff. That path is absent on main. The five-part source that is on main is `decisions/2026-10-11-definition-of-done.md`. `AGENTS.md`, `rules/README.md`, and `fleet-os/GROKBOT_OS.md` point there. This branch does not create `DEFINITION-OF-DONE.md`.

## PR #6

**Update 2026-10-13:** PRs #4, #5 and #6 were merged to main with Trevor's approval. `rules/README.md` now lists fourteen laws. The text below is kept as history.

PR #6 is draft, open, and unmerged at `17411a97af1001d74b22f600dc0b68f634e956d8` (job `bc-9ff579ef`). It owns the quote-removal review. This branch does not merge it, does not authorize that merge, and does not edit its nine paths. The wake set still reads `brain/01-identity/05-beliefs-and-faith.md`. The loader withholds the disputed spans from current instructions and keeps neighboring wording on the same line. Detail is in `review/PARALLEL-DEPENDENCY-PR6.md`.

## Team overlay

`team/` on main stays the Team model from `decisions/2026-10-11-org-chart.md`. No overlay was in the baseline. This branch does not replace `team/`.
