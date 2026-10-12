# Parallel dependency: PR #6

This follow-up does not merge PR #6. It does not authorize that merge. It does not edit PR #6's branch and it does not copy PR #6's files onto this branch.

| | |
|---|---|
| Pull request | https://github.com/trevorcrane/epic-ai-os/pull/6 |
| State | Draft, open, unmerged |
| Head | `17411a97af1001d74b22f600dc0b68f634e956d8` |
| Base | `74d111fa6260c0d9415ff388bdfc76c51f922df7` (same baseline as this branch) |
| Branch | `cursor/remove-false-quotes-41c6` |
| Job | `bc-9ff579ef` |
| Review boundary | PR #6 owns the quote-removal review. This branch leaves that diff on PR #6. |

## Files PR #6 changes

- `brain/01-identity/05-beliefs-and-faith.md`
- `brain/02-mission/01-mission-and-promise.md`
- `brain/03-brands/04-epic-os.md`
- `brain/04-voice/03-signature-phrases.md`
- `brain/05-messaging/01-big-idea.md`
- `brain/05-messaging/05-love-business.md`
- `brain/05-messaging/08-brain-team-revenue-machine.md`
- `brain/08-likes-dislikes/01-likes.md`
- `decisions/2026-10-11-false-quotes-removed.md`

## Overlap with this branch

This branch does not modify those nine paths. The wake manifest reads `brain/01-identity/05-beliefs-and-faith.md` because `AGENTS.md` reads identity every wake. That read does not change the file. The loader withholds the disputed spans from the emitted instruction bundle and keeps neighboring wording and attribution on the same line. The source file is not rewritten. The other seven Brain paths are not in the wake manifest and are not edited here. `decisions/2026-10-11-false-quotes-removed.md` is not added to this tree. A load that asks for an undeclared Brain path fails closed instead of reading it.

## Rejected attributions

These are not accepted Trevor instructions. This file does not freeze them as verified quotes. The owner-utterance message id is unresolved. This note does not invent one. Pointer: `decisions/2026-10-11-false-quotes-removed.md` on the PR #6 head above.

1. REJECTED. "Automate everything but the love."
2. REJECTED. "Own what you build." and the whole-system line "Own what you build. Clients walk away with the whole system."
3. REJECTED. "Speed over polish." and "Speed matters more than polish. Fast is the point."

The derived line "Clients own what we build." is also withheld. It is not treated as a decision. PR #6 opens that ownership question as a gap. This branch does not close it.

PR #6's replacement is marked there as a draft line, not a quote. This branch does not copy that draft line into the Brain files.

## Decisions this note does not touch

The October 11 org, First Mate, Tango, approval, and definition-of-done files stay as recorded. They are not the PR #6 diff.
