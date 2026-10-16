# Grok Bot OS (saved)

Updated: 2026-09-30 (laws appended; full OS refresh still owed). Fleet law list and 2026-10-11 decisions updated 2026-10-11; the stack below is as saved.

## Stack
<!-- context-bundle: preserved-superseded -->
The six lines in this section are the saved 2026-09-30 stack, kept verbatim. They are not current instructions.

1. Compound Engineering — execution engine
2. Linear Fleet DoD — Mission Control / SSOT / dashboard
3. First Mate — Chief of Staff + Grok Operator (combined for now)
4. DoD → LIVE → RAD — closure standard (aligned with Hermes)
5. Pressure Test Before Go — gate before go/install
6. Fleet heartbeat — weekdays 8:30am ET
<!-- /context-bundle -->

Marked superseded, text kept above:
- Line 2 is superseded by `decisions/2026-10-11-task-home.md`. Tango is the project home for now. Linear is a source, not the system of record.
- Line 3 is superseded by `decisions/2026-10-11-first-mate.md`. First Mate is whichever AI Trevor is talking to.
- Line 4 is superseded as the definition of done by `decisions/2026-10-11-definition-of-done.md`. LIVE and RAD below may still describe state. They do not define done.
- Lines 1, 5, and 6 were not replaced by an October 11 decision. They stay inside the saved stack. They are not current-bundle instructions. The refresh note at the bottom still says the full OS refresh is owed.

## LIVE
- L Live — exists where it should
- I Interaction — real user flow works
- V Verification — independent QC passed
- E Evidence — proof artifacts

## RAD
- Reviewed · Approved (if needed) · Delivered

## Skills
- first-mate-os (index card only in this repo; the skill body is absent and is not installed)
- pressure-test-before-go (index card only in this repo; the skill body is absent and is not installed)

## Pilot
5 jobs; revise if >1 fake-done or silent stall.

## Fleet Laws (SoT under `rules/` in this repo)
Updated: 2026-10-16 (all locked rules; `decisions/2026-10-11-grokbot-os-rules.md`)
Each file in `rules/` is the source of truth for its rule. This list is the index.
- Plan → Build → Use: `rules/PLAN-BUILD-USE.md` (ask before build; no magic passwords)
- Verify before you claim: `rules/VERIFY-BEFORE-YOU-CLAIM.md`
- Editable Google Docs: `rules/EDITABLE-GOOGLE-DOCS.md` (anyone-with-link = Editor; no view-only; no files unless asked; no login walls)
- Tango handoff no-drop: `rules/TANGO-HANDOFF-NO-DROP.md`
- Follow published docs first: `rules/FOLLOW-PUBLISHED-DOCS.md` (fetch and follow a tool's official docs before building or improvising)
- CTA new tab: `rules/CTA-NEW-TAB.md` (locked 2026-10-02)
- Epic funnel SOP: `rules/EPIC-FUNNEL-SOP.md` (locked 2026-10-04)
- Cloudflare Pages standard: `rules/CLOUDFLARE-PAGES-STANDARD.md` (locked 2026-10-05)
- Launch QC checklist: `rules/LAUNCH-QC-CHECKLIST.md` (locked 2026-10-04)
- Look before you ask: `rules/LOOK-BEFORE-YOU-ASK.md` (locked 2026-10-04)
- Site ship loop: `rules/SITE-SHIP-LOOP.md` (locked 2026-10-04)
- Cursor Bob dispatch: `rules/CURSOR-BOB-DISPATCH.md` (locked 2026-10-06)
- No unapproved framework edits: `rules/NO-UNAPPROVED-FRAMEWORK-EDITS.md` (locked 2026-10-07)
- Act and finish, hot potato: `rules/ACT-AND-FINISH-HOT-POTATO.md` (locked 2026-10-08)
- Team comms standard: `rules/TEAM-COMMS-STANDARD.md` (locked 2026-10-13)
- Trust relayed approvals: `rules/TRUST-RELAYED-APPROVALS.md` (locked 2026-10-13)
- Shared team inbox: `rules/SHARED-TEAM-INBOX.md` (locked 2026-10-13)
- Team comms never wait on Trevor's permission: `rules/TEAM-COMMS-NO-PERMISSION.md` (locked 2026-10-10)
- Build approved via any bot: `rules/BUILD-APPROVED-VIA-ANY-BOT.md` (locked 2026-10-13)
- Conflicting answers, ask first: `rules/CONFLICTING-ANSWERS-ASK-FIRST.md` (locked 2026-10-13)
- One update per job: `rules/ONE-UPDATE-PER-JOB.md` (locked 2026-10-15)
- Key handoff: `rules/KEY-HANDOFF.md` (locked 2026-10-15)
- Tool rollout: `rules/TOOL-ROLLOUT.md` (locked 2026-10-15)

Order matches `rules/README.md` and `AGENTS.md`. Twenty-three laws on main.

## Decided 2026-10-11
- First Mate is whichever AI Trevor is talking to (`decisions/2026-10-11-first-mate.md`).
- Tango is the project home for now. Linear is a source, not the system of record (`decisions/2026-10-11-task-home.md`).
- Done is Trevor's 5-part Definition of Done plus proof, and the human says done (`decisions/2026-10-11-definition-of-done.md`). That decision file is the five-part source on main. This file does not add `DEFINITION-OF-DONE.md`.

## OS refresh note
This OS file was last stacked 2026-09-15. Full Epic OS refresh (Tango bus, connector reconnect, Robyn OS, meatbag-last, Len she/her, Abi-first reconnect) is **still owed** — Planning until Trevor says build the OS update.
