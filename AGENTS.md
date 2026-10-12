# AGENTS.md

Every AI reads this file first. Epic OS v1 compile, 2026-10-06, plus the recorded 2026-10-11 decision files.

## Release status

Candidate baseline. Not an accepted release for runtime loading. This file does not designate one.

The commit subject on `74d111fa6260c0d9415ff388bdfc76c51f922df7` (PR #3 merge) says Trevor approved 2026-10-11. That subject is not an accepted-release designation. The starting point for review is that commit. A host that loads context uses [context-load/README.md](context-load/README.md). Candidate and accepted stay separate records.

Scoped decisions and the overall release are different. Each file in [decisions/](decisions/) dated 2026-10-11 records Trevor's answer to one named CONFLICTS item. That answer stands for the item it names. It does not approve Brain or Team as a whole. Brain files and Team files stay DRAFT until Trevor approves those files. Nobody says final.

When a scoped decision names what it replaces, that decision beats the draft or archived sentence it names. The old sentence stays in its file. Where this review pass marked it, the mark means it is not a current instruction.

## Wake order

1. This file, including the release status above. Read it before any other source.
2. The scoped decision files in [decisions/](decisions/) that name the job's conflict. Newest wins only when the file names what it replaces. Provenance for the 2026-10-11 set is [decisions/PROVENANCE-2026-10-11.md](decisions/PROVENANCE-2026-10-11.md). A missing owner-utterance reference stays unresolved. Do not invent one.
3. [context-load/README.md](context-load/README.md) when a host is loading a revision. Load the exact revision and the required manifest, or fail closed. Do not treat a candidate load as an accepted release.
4. [team/01-laws.md](team/01-laws.md). The Epic Laws. Every agent, every wake.
5. [brain/09-rules-of-engagement/](brain/09-rules-of-engagement/). All six files. Every wake.
6. [brain/01-identity/](brain/01-identity/). Who Trevor is. Every wake.
7. The fleet law list below. Know the list every wake. Open the matching file in [rules/](rules/) before work that file covers. The file is the rule. This list is the index.
8. [CONFLICTS.md](CONFLICTS.md) as the closed record. No item on that list is open. The paragraphs under each heading are the 2026-10-06 wording, kept as written. They are not open conflicts and they are not current instructions.
9. The folder the job is about. Do not load the whole Brain for a narrow job.
10. [brain/04-voice/](brain/04-voice/) before any writing in Trevor's name.
11. The Aug 17 seed docs, listed below, when the job is about SMAI, the mission board, or access status. The Aug 17 org chart is archived. They are not the wake path for Brain or Team work.

Seat cards add their own wake lines (First Mate and Lead). Follow those after this list. A seat card does not outrank a scoped decision that names what it replaces.

PR #6 is draft, open, and unmerged (head `17411a97af1001d74b22f600dc0b68f634e956d8`, job `bc-9ff579ef`). It owns removal of three attributions in Brain files. This file does not merge it and does not authorize that merge. Identity is still read every wake. A context load withholds those rejected lines and does not treat them as accepted Trevor instructions. The decision file is not in this tree. The owner-utterance id is unresolved. Do not invent one. See [review/PARALLEL-DEPENDENCY-PR6.md](review/PARALLEL-DEPENDENCY-PR6.md).

## Where things live

| Path | What it is |
|---|---|
| [AGENTS.md](AGENTS.md) | This file. Wake order, map, fleet law index. |
| [CLAUDE.md](CLAUDE.md) | Points here. Claude Code starts at that file. |
| [brain/](brain/) | Who Trevor is. Identity, brands, voice, messaging, audience, offers, rules, goals, proof. Draft. |
| [team/](team/) | Trevor Team v0.2. Laws, people, bot cards, seats, handoffs, talk rules. Reviewer A/95 on 2026-10-06. Not approved by Trevor. |
| [robyn/](robyn/) | Reserved for Robyn Crane. `robyn/brain/` will mirror `brain/`. `robyn/team/` will mirror `team/`. Not filled in the Trevor compile. |
| [rules/](rules/) | Fleet laws. One file is the source of truth for one rule. Text copied unchanged. |
| [decisions/](decisions/) | One file per recorded decision. Six lines. Newest file wins only when it names what it replaces. The 2026-10-11 files are scoped answers, not an overall release. |
| [decisions/PROVENANCE-2026-10-11.md](decisions/PROVENANCE-2026-10-11.md) | Blob references for those recorded answers. Owner-utterance links that were not found stay unresolved. |
| [context-load/](context-load/) | Reviewable context loader. Candidate and accepted records, manifest, receipt, isolated tests. Not installed on a live agent. |
| [skills/](skills/) | Skill index (all 20) plus a folder for each of the 9 Live skills. Those folders are index cards. The skill bodies were not in the archive and are not installed by this repo. Draft and Parked skills are index lines only. |
| [workflows/](workflows/) | One file per workflow. The publishing workflow was not in the compile archive. See that folder's readme. |
| [fleet-os/GROKBOT_OS.md](fleet-os/GROKBOT_OS.md) | Grok Bot OS summary from 2026-09-30. The fleet law list points at all twelve files in `rules/` (2026-10-11). The saved stack is marked and is not a current instruction. A full refresh is still owed. |
| [QUESTIONS.md](QUESTIONS.md) | Open questions for Trevor. Q numbers in the Brain point here. |
| [CONFLICTS.md](CONFLICTS.md) | Closed record of places sources disagreed. No item is open. Each item links to its decision file. The 2026-10-06 paragraphs stay in the file and are not current instructions. |
| [sources/](sources/) | The layout plan, the proposed tree, and the source inventory. Reference. Not wake instructions. |
| [brand/](brand/) | Aug 17 voice folders for Trevor and Robyn. Stubs. The drafted voice is [brain/04-voice/](brain/04-voice/). |
| [clients/](clients/) | Client material, not Trevor's. [clients/dr-leigh/](clients/dr-leigh/) is a case study and funnels to model. |
| [archive/](archive/) | Retired files. [archive/2026-08-17-seed-org/](archive/2026-08-17-seed-org/) holds the Aug 17 org chart. |

Prices stay in [brain/07-offers/](brain/07-offers/). That folder is internal. Public copy never shows a price and never names HighLevel, GoHighLevel, or SMAI. See [brain/09-rules-of-engagement/02-public-copy.md](brain/09-rules-of-engagement/02-public-copy.md).

## Fleet laws

Source of truth: the file in [rules/](rules/). Twelve fleet laws.

1. [rules/PLAN-BUILD-USE.md](rules/PLAN-BUILD-USE.md). Plan, then build, then use. Unclear means Planning. No magic-password approval. Build only after Trevor asks or approves that plan.
2. [rules/VERIFY-BEFORE-YOU-CLAIM.md](rules/VERIFY-BEFORE-YOU-CLAIM.md). Same-turn live check before any "no access", "blocked", or done claim.
3. [rules/EDITABLE-GOOGLE-DOCS.md](rules/EDITABLE-GOOGLE-DOCS.md). Deliverables Trevor or Robyn will reuse are Google Docs or Sheets, anyone with the link can edit.
4. [rules/TANGO-HANDOFF-NO-DROP.md](rules/TANGO-HANDOFF-NO-DROP.md). A deliverable counts when it is a Tango artifact on a named task and the recipient posts a readback.
5. [rules/FOLLOW-PUBLISHED-DOCS.md](rules/FOLLOW-PUBLISHED-DOCS.md). Fetch and follow a tool's official docs before building or improvising.
6. [rules/CTA-NEW-TAB.md](rules/CTA-NEW-TAB.md). Outbound buttons and calls to action open in a new tab. Do not also call `window.open`.
7. [rules/EPIC-FUNNEL-SOP.md](rules/EPIC-FUNNEL-SOP.md). Opt-in fields use placeholder text. Default form is the Epic two-step popup.
8. [rules/CLOUDFLARE-PAGES-STANDARD.md](rules/CLOUDFLARE-PAGES-STANDARD.md). New site deploys use Cloudflare Pages Direct Upload.
9. [rules/LAUNCH-QC-CHECKLIST.md](rules/LAUNCH-QC-CHECKLIST.md). Reviewer runs this list before anyone calls a launch ready.
10. [rules/LOOK-BEFORE-YOU-ASK.md](rules/LOOK-BEFORE-YOU-ASK.md). Search the Brain, shared memory, and these rules before asking Trevor for a fact the fleet already has.
11. [rules/SITE-SHIP-LOOP.md](rules/SITE-SHIP-LOOP.md). Builder ships. Reviewer scores the live page. Reviewer is the only bot that says a site is done. Trevor or Robyn accepts. Builder does not call it done.
12. [rules/CURSOR-BOB-DISPATCH.md](rules/CURSOR-BOB-DISPATCH.md). Code and repo changes go straight to Bob, a Cursor cloud agent, not through Tango. Bob opens a pull request only and never merges. A human decides the merge.

[team/01-laws.md](team/01-laws.md) holds the core 10 Epic Laws. The files above are the specific fleet rules, each its own source of truth. Both sets stay ([decisions/2026-10-11-laws.md](decisions/2026-10-11-laws.md)).

Done, when a task needs that word, uses the five-part source that is already on main: [decisions/2026-10-11-definition-of-done.md](decisions/2026-10-11-definition-of-done.md). There is no `DEFINITION-OF-DONE.md` in this tree. This file does not add one.

Two fleet-law pull requests are not in this tree and are not copied here. PR #4 (`rules/NO-UNAPPROVED-FRAMEWORK-EDITS.md`) and PR #5 (`rules/ACT-AND-FINISH-HOT-POTATO.md`) stay on their own branches. PR #5 cites `DEFINITION-OF-DONE.md`. On main, the five-part source is the decision file named above. The index in this file stays at the twelve laws on main. See [review/INDEX-RECONCILIATION.md](review/INDEX-RECONCILIATION.md).

## Aug 17 seed (kept)

These root files are the Aug 17-18 Epic AI org seed. They describe Buzz, Hermes, Len, SMAI, and the mission board. The Aug 17 org chart (Fizz, Honey, Bumble) is retired and archived ([decisions/2026-10-11-org-chart.md](decisions/2026-10-11-org-chart.md)). Where these files disagree with Brain, Team, or fleet rules, both stand until a decision file says otherwise. The 2026-10-11 files in [decisions/](decisions/) say otherwise on several points.

| File | Scope |
|---|---|
| [README.md](README.md) | What the repo is, plus the Aug 17 read order. Wake order for AI is this file, not that list. |
| [EPIC-AI-WORKING-AGREEMENT.md](EPIC-AI-WORKING-AGREEMENT.md) | Aug 17 doctrine: four-state status, proof gate, Len as the one human review, 1-3-1, SNAPP-RAD. |
| [EPIC-CONTEXT.md](EPIC-CONTEXT.md) | Aug 17 picture of Epic Media and Robyn Crane, including internal prices and the tool stack. |
| [SMAI.md](SMAI.md) | Aug 17 GoHighLevel domain pack. Internal. Not public copy. |
| [MISSIONS.md](MISSIONS.md) | Aug 17 mission board and LEARNED log. |
| [PLAYBOOK_SOURCE.md](PLAYBOOK_SOURCE.md) | Pointer to the Aug 17 launch playbook import. |
| [STEP0-ACCESS-STATUS.md](STEP0-ACCESS-STATUS.md) | Aug 17 access proof and blockers. Dated. Not a live check. |
| [brand/](brand/) | Aug 17 brand folders. Stubs, waiting for uploads. |

## Memory

The job loop tells the First Mate to write a memory line before reporting ([team/05-handoffs/01-how-a-job-moves.md](team/05-handoffs/01-how-a-job-moves.md)). The handoff repo's `memory/` files were not in the compile archive.

A new decision goes in [decisions/](decisions/), one file, six lines, format in [decisions/README.md](decisions/README.md). [brain/00-README.md](brain/00-README.md) points there too ([decisions/2026-10-11-decisions-home.md](decisions/2026-10-11-decisions-home.md)).

## Compile note

Branched from `main` (the Aug 17-18 seed). The Sep 28 Brain, Team, fleet rules, and skill index were not on `main`. The v0.5 rollout branch is a different package (`operating-system/`, an Aug 28 brain snapshot, an Alfred runtime bundle) and was left on its own pull request. Why is in the Epic OS v1 pull request.
