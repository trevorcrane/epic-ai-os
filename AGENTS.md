# AGENTS.md

Every AI reads this file first. Epic OS v1 compile, 2026-10-06.

Brain files and Team files are DRAFT. Trevor has not approved them. Nobody says final.

When two sources disagree, keep both. The open list is [CONFLICTS.md](CONFLICTS.md). Do not pick a winner from this file.

## Wake order

1. This file.
2. [team/01-laws.md](team/01-laws.md). The Epic Laws. Every agent, every wake.
3. [brain/09-rules-of-engagement/](brain/09-rules-of-engagement/). All six files. Every wake.
4. [brain/01-identity/](brain/01-identity/). Who Trevor is. Every wake.
5. The fleet law list below. Know the list every wake. Open the matching file in [rules/](rules/) before work that file covers. The file is the rule. This list is the index.
6. [CONFLICTS.md](CONFLICTS.md) before you treat overlapping sources as one fact.
7. The folder the job is about. Do not load the whole Brain for a narrow job.
8. [brain/04-voice/](brain/04-voice/) before any writing in Trevor's name.
9. The Aug 17 seed docs, listed below, when the job is about that org chart, SMAI, the mission board, or access status. They are not the wake path for Brain or Team work.

Seat cards add their own wake lines (First Mate and Lead). Follow those after this list.

## Where things live

| Path | What it is |
|---|---|
| [AGENTS.md](AGENTS.md) | This file. Wake order, map, fleet law index. |
| [CLAUDE.md](CLAUDE.md) | Points here. Claude Code starts at that file. |
| [brain/](brain/) | Who Trevor is. Identity, brands, voice, messaging, audience, offers, rules, goals, proof. Draft. |
| [team/](team/) | How Trevor's AI works. Laws, people, bot cards, seats, handoffs, talk rules. Draft. |
| [robyn/](robyn/) | Reserved for Robyn Crane. `robyn/brain/` will mirror `brain/`. `robyn/team/` will mirror `team/`. Not filled in the Trevor compile. |
| [rules/](rules/) | Fleet laws. One file is the source of truth for one rule. Text copied unchanged. |
| [decisions/](decisions/) | One file per recorded decision. Six lines. Newest file wins only when it names what it replaces. |
| [skills/](skills/) | Skill index (all 20) plus a folder for each of the 9 Live skills. Draft and Parked skills are index lines only. |
| [workflows/](workflows/) | One file per workflow. The publishing workflow was not in the compile archive. See that folder's readme. |
| [fleet-os/GROKBOT_OS.md](fleet-os/GROKBOT_OS.md) | Grok Bot OS summary from 2026-09-30. It lists five fleet laws and says a full refresh is still owed. |
| [QUESTIONS.md](QUESTIONS.md) | Open questions for Trevor. Q numbers in the Brain point here. |
| [CONFLICTS.md](CONFLICTS.md) | Places sources disagree. No winner chosen. |
| [sources/](sources/) | The layout plan, the proposed tree, and the source inventory. Reference. Not wake instructions. |
| [brand/](brand/) | Aug 17 voice folders for Trevor and Robyn. Stubs. The drafted voice is [brain/04-voice/](brain/04-voice/). |

Prices stay in [brain/07-offers/](brain/07-offers/). That folder is internal. Public copy never shows a price and never names HighLevel, GoHighLevel, or SMAI. See [brain/09-rules-of-engagement/02-public-copy.md](brain/09-rules-of-engagement/02-public-copy.md).

## Fleet laws

Source of truth: the file in [rules/](rules/). Original copies still name `/workspace/ops/rules/` inside the text. In this repo the same text is `rules/<file>`.

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
11. [rules/SITE-SHIP-LOOP.md](rules/SITE-SHIP-LOOP.md). Builder ships. Reviewer scores the live page. Trevor accepts. Builder does not call it done.

[team/01-laws.md](team/01-laws.md) says it is the only file that holds the laws. The files above are also laws. Both sets stay. See CONFLICTS.md.

## Aug 17 seed (kept)

These root files are the Aug 17-18 Epic AI org seed. This compile does not edit them and does not delete them. They describe Buzz, Fizz, Honey, Bumble, Hermes, Len, SMAI, and the mission board. Where they disagree with Brain, Team, or fleet rules, both stand until a decision file says otherwise.

| File | Scope |
|---|---|
| [README.md](README.md) | What the repo is, plus the Aug 17 read order. Wake order for AI is this file, not that list. |
| [EPIC-AI-WORKING-AGREEMENT.md](EPIC-AI-WORKING-AGREEMENT.md) | Aug 17 doctrine: four-state status, proof gate, Len as the one human review, 1-3-1, SNAPP-RAD. |
| [EPIC-ORG.md](EPIC-ORG.md) | Aug 17 humans and AI core: Fizz, Honey, Bumble, Hermes, and the bench. |
| [EPIC-CONTEXT.md](EPIC-CONTEXT.md) | Aug 17 picture of Epic Media and Robyn Crane, including internal prices and the tool stack. |
| [ROLE-CARDS.md](ROLE-CARDS.md) | Aug 17 seat cards for Fizz, Honey, Bumble, and Hermes. |
| [SMAI.md](SMAI.md) | Aug 17 GoHighLevel domain pack. Internal. Not public copy. |
| [MISSIONS.md](MISSIONS.md) | Aug 17 mission board and LEARNED log. |
| [PLAYBOOK_SOURCE.md](PLAYBOOK_SOURCE.md) | Pointer to the Aug 17 launch playbook import. |
| [STEP0-ACCESS-STATUS.md](STEP0-ACCESS-STATUS.md) | Aug 17 access proof and blockers. Dated. Not a live check. |
| [brand/](brand/) | Aug 17 brand folders. Stubs, waiting for uploads. |

## Memory

The job loop tells the First Mate to write a memory line before reporting ([team/05-handoffs/01-how-a-job-moves.md](team/05-handoffs/01-how-a-job-moves.md)). The handoff repo's `memory/` files were not in the compile archive.

A new decision goes in [decisions/](decisions/), one file, six lines, format in [decisions/README.md](decisions/README.md). [brain/00-README.md](brain/00-README.md) still names `memory/DECISIONS.md`. That path was not created here. Both homes are recorded in CONFLICTS.md.

## Compile note

Branched from `main` (the Aug 17-18 seed). The Sep 28 Brain, Team, fleet rules, and skill index were not on `main`. The v0.5 rollout branch is a different package (`operating-system/`, an Aug 28 brain snapshot, an Alfred runtime bundle) and was left on its own pull request. Why is in the Epic OS v1 pull request.
