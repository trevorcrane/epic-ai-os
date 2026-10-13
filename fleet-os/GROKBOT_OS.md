# Grok Bot OS (saved)

Updated: 2026-09-30 (laws appended; full OS refresh still owed). Fleet law list and 2026-10-11 decisions updated 2026-10-11; the stack below is as saved.

## Stack
1. Compound Engineering — execution engine
2. Linear Fleet DoD — Mission Control / SSOT / dashboard
3. First Mate — Chief of Staff + Grok Operator (combined for now)
4. DoD → LIVE → RAD — closure standard (aligned with Hermes)
5. Pressure Test Before Go — gate before go/install
6. Fleet heartbeat — weekdays 8:30am ET

## LIVE
- L Live — exists where it should
- I Interaction — real user flow works
- V Verification — independent QC passed
- E Evidence — proof artifacts

## RAD
- Reviewed · Approved (if needed) · Delivered

## Skills
- first-mate-os
- pressure-test-before-go

## Pilot
5 jobs; revise if >1 fake-done or silent stall.

## Fleet Laws (SoT under `rules/` in this repo)
Updated: 2026-10-11 (all locked rules; `decisions/2026-10-11-grokbot-os-rules.md`)
Each file in `rules/` is the source of truth for its rule. This list is the index.
- Plan → Build → Use: `rules/PLAN-BUILD-USE.md` (ask before build; no magic passwords)
- Verify before you claim: `rules/VERIFY-BEFORE-YOU-CLAIM.md`
- Editable Google Docs: `rules/EDITABLE-GOOGLE-DOCS.md` (anyone-with-link = Editor; no view-only; no files unless asked; no login walls)
- Tango handoff no-drop: `rules/TANGO-HANDOFF-NO-DROP.md`
- Follow published docs first: `rules/FOLLOW-PUBLISHED-DOCS.md` (fetch and follow a tool's official docs before building or improvising)
- CTA new tab: `rules/CTA-NEW-TAB.md` (locked 2026-10-02)
- Epic funnel SOP: `rules/EPIC-FUNNEL-SOP.md` (locked 2026-10-04)
- Launch QC checklist: `rules/LAUNCH-QC-CHECKLIST.md` (locked 2026-10-04)
- Look before you ask: `rules/LOOK-BEFORE-YOU-ASK.md` (locked 2026-10-04)
- Site ship loop: `rules/SITE-SHIP-LOOP.md` (locked 2026-10-04)
- Cloudflare Pages standard: `rules/CLOUDFLARE-PAGES-STANDARD.md` (locked 2026-10-05)
- Cursor Bob dispatch: `rules/CURSOR-BOB-DISPATCH.md` (locked 2026-10-06)

## Decided 2026-10-11
- First Mate is whichever AI Trevor is talking to (`decisions/2026-10-11-first-mate.md`).
- Tango is the project home for now. Linear is a source, not the system of record (`decisions/2026-10-11-task-home.md`).
- Done is Trevor's 5-part Definition of Done plus proof, and the human says done (`decisions/2026-10-11-definition-of-done.md`).

## OS refresh note
This OS file was last stacked 2026-09-15. Full Epic OS refresh (Tango bus, connector reconnect, Robyn OS, meatbag-last, Len she/her, Abi-first reconnect) is **still owed** — Planning until Trevor says build the OS update.
