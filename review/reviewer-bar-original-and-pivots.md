PROPOSED, not approved

# Reviewer bar: original, then pivots

The seat card and the bot card are unchanged. This file does not apply a pivot. Trevor or the named owner chooses. A scoped decision already holds mentor packs until a Reviewer score of 80 or more (`decisions/2026-10-11-mentor-packs.md`). That decision is not this conflict, and this file does not reopen it.

Source of the procedure used here: PR #4, `rules/NO-UNAPPROVED-FRAMEWORK-EDITS.md`, which is not merged and is not copied into this branch. The procedure: original verbatim first, then each numbered pivot with what the original does, the concern, the proposed change, and why.

## Original, verbatim

Source: `team/04-seats/05-reviewer.md` (unchanged).

Line 12:

```
2. The done-checklist and the hunt list (step 5) decide PASS or FAIL. The five-part score decides the number, and under 80 is a FAIL on its own.
```

Line 22, inside the verdict format:

```
The bar: 90 for anything internal, 95 for anything a client reads. Under 80 is FAIL. 80 up to the bar is PASS, below standard: say so, it counts in HEALTH.
```

Line 37, scoring loop step 4:

```
4. Builder: apply it, rescore, repeat until 95 or above, then request review with the before, the after, and the score history. Reviewer: post your score. Under the bar (client copy 95, everything else 90) is a FAIL with that rewrite as the Fix line. Never apply it yourself; that is a rebuild (LAWS 3).
```

Source: `team/03-bots/10-reviewer.md` (unchanged).

```
- **Bar:** 95 for anything a client or the public reads, 90 for internal work. Under 80 is FAIL. Never rounds up.
```

## Where they disagree

Under 80 is FAIL in every original above. That part agrees.

From 80 up to the bar, line 22 says PASS, below standard, and it counts in HEALTH. The scoring loop says under the bar (90 internal, 95 client) is a FAIL. The bot card names the same 90 and 95 bars and the under-80 FAIL, and it does not mention a below-standard PASS.

Intent kept from line 22: a score can be below the bar and still be named, so HEALTH can see it, and under 80 is the hard fail.

Intent kept from the scoring loop: work under the bar is not treated as meeting the bar, and the Reviewer does not rebuild it.

## Pivot 1

What the original does: line 22 already has a third state between hard fail and a clean pass.

Concern: calling that state PASS lets a score under 90 or 95 travel as a pass. The scoring loop then calls the same score a FAIL.

Proposed change: keep under 80 as FAIL. Name 80 up to the bar `PASS, below standard`. It counts in HEALTH. It does not authorize a send or a publish. Under the bar is not renamed to FAIL.

Why: it keeps line 22's third state and the scoring loop's bar, and it stops the word PASS from being read as "meets the bar."

## Pivot 2

What the original does: the scoring loop and the bot card treat the bar as the pass line, with under 80 called out as FAIL.

Concern: a below-standard PASS is a second verdict the scoring loop does not have. Builders can stop when the verdict says PASS and the score is still under 90 or 95.

Proposed change: under the bar is FAIL, as the scoring loop says. Line 22's sentence "80 up to the bar is PASS, below standard" is retired. The score still shows in HEALTH. Under 80 remains FAIL.

Why: one verdict word. The bar in the bot card and the scoring loop match.

## Pivot 3

What the original does: both texts want under 80 to fail, and both want the 90 and 95 bars to matter.

Concern: Pivot 1 still uses the word PASS. Pivot 2 deletes the third state line 22 wrote on purpose.

Proposed change: verdicts are PASS, BELOW STANDARD, FAIL, and BLOCKED. Under 80 is FAIL. From 80 up to the bar the verdict is BELOW STANDARD, the work returns to the Builder, and nothing is sent. PASS means the score met the bar (90 internal, 95 when a client or the public reads it) and every other check passed.

Why: it keeps the hard fail, the bar, and a named middle state, and the middle state is not a pass.

## Choice

Unresolved. No pivot is selected. No recommendation. The originals above stay in force together until Trevor or the named owner picks: original as-is, original with a pivot by number, or the full proposed version. This file stays `PROPOSED, not approved` until that choice is in writing.
