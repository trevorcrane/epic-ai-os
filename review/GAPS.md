# Gaps for review

These are open on purpose.

1. Owner-utterance references for all 26 decisions dated 2026-10-11 are unresolved. See `decisions/PROVENANCE-2026-10-11.md`. The decisions stay as recorded.
2. No accepted runtime release is designated. `context-load/releases/accepted.json` has status `none`. Fallback to a last-known accepted release is implemented and tested only in an isolated tree that plants its own accepted fixture. The real tree has nothing to fall back to.
3. Reviewer 80-to-bar PASS versus under-90/95 FAIL is unresolved. Originals and three pivots are in `review/reviewer-bar-original-and-pivots.md`. The seat card was not edited.
4. Skill bodies are absent. Tests do not install them. A Live index row is not installation.
5. The loader is not installed on Cursor, Tango, Grok, ChatGPT, Hermes, or Claude. No live profile, webhook, or wake hook was changed.
6. PR #4 and PR #5 were not merged and were not combined with this branch in a joint test.
7. The candidate manifest is a bounded wake set. It does not hash the whole Brain.
8. Git cannot store this commit's own SHA inside the commit. The exact revision the loader checks is `content_revision` (sha256 of the sealed manifest body). The pull request body pins the git head SHA beside it.
9. Grok OS lines for Compound Engineering, the pressure-test gate, and the weekday heartbeat were not replaced by an October 11 decision. They stay inside the marked stack. The full OS refresh note is still owed.
10. Tests are preparation evidence. They are not proof of fleet adoption.
