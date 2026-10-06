# PROPOSED STRUCTURE: epic-ai-os

Status: DRAFT for Trevor. 2026-09-28.
Goal: many small files, one job each. One GitHub repo is the single source of truth. The same tree works as a template for any client.

## The rules behind the shape
1. **One file, one job.** If a file needs two headings that could each stand alone, split it.
2. **A rule lives in one file.** Everything else links to it (copies drift, then lie).
3. **Numbered folders and files.** They load and read in order, and a client copy looks the same.
4. **Brain = who the person is. Team = how the AI works. Machine = what makes money.** Nothing personal goes in team/. No team rules go in brain/.
5. **Template on `main`, one private copy per person.** `epic-ai-os` holds the empty template (every Brain file is a prompt with blanks). `epic-ai-os-trevor`, `epic-ai-os-robyn`, `epic-ai-os-<client>` are the filled copies. Trevor's copy is the first proof.
6. **Small files load cheap.** An AI loads `AGENTS.md`, the 01-identity folder, and 09-rules on every wake. Everything else loads only when the job needs it.

## The tree

```
epic-ai-os/
├── AGENTS.md                         Every AI reads this first. Wake order, done, claims, memory.
├── CLAUDE.md                         One line: import AGENTS.md (Claude Code).
├── README.md                         What this repo is. How to clone it for a client.
├── START-HERE.md                     The human's page. Review, say go, give a job.
│
├── brain/                            WHO THE PERSON IS
│   ├── 00-README.md                  How to read the Brain: tags, source priority, status line.
│   ├── 00-intake.md                  Smart Start: the Smart 10 questions and four ways to answer.
│   │
│   ├── 01-identity/                  Loaded every wake.
│   │   ├── 01-who-i-am.md            Name, role, one-line bio, home base.
│   │   ├── 02-family.md              Spouse, kids, what family means to the work, privacy lines.
│   │   ├── 03-origin-story.md        The fall and the comeback, in their words.
│   │   ├── 04-why.md                 The story behind the mission (for Trevor: Steven).
│   │   ├── 05-beliefs-and-faith.md   What they believe, values, the life they want.
│   │   └── 06-point-of-view.md       Their signature stance (for Trevor: the AI Caveman).
│   │
│   ├── 02-mission/
│   │   ├── 01-mission-and-promise.md The mission, the promise, the one-liner.
│   │   └── 02-customer-journey.md    How a stranger becomes a client, stage by stage.
│   │
│   ├── 03-brands/
│   │   ├── 01-brand-architecture.md  Master brand, sub-brands, who does what.
│   │   ├── 02-<brand>.md             One file per brand (Trevor: Epic Author, Epic Media, Epic OS).
│   │   ├── 05-personal-brand.md      The person as a brand.
│   │   └── 06-other-properties.md    Shows, channels, domains, side brands.
│   │
│   ├── 04-voice/
│   │   ├── 01-core-voice.md          How they sound, the master rule.
│   │   ├── 02-voice-modes.md         By format: copy, post, hook, email, book, DM.
│   │   ├── 03-signature-phrases.md   Their words, verbatim.
│   │   ├── 04-no-ai-slop.md          What never to write.
│   │   ├── 05-samples.md             Real samples they wrote.
│   │   ├── 06-quality-check.md       The questions to run before shipping copy.
│   │   └── by-audience/              One file per audience they talk to.
│   │       ├── 01-public-content.md
│   │       ├── 02-prospects-and-clients.md
│   │       ├── 03-team.md
│   │       ├── 04-spouse.md          (Trevor: Robyn)
│   │       ├── 05-family-content.md
│   │       └── 06-ai-talking-to-me.md  Pointer to team/06-talk/01-captain-mode.md.
│   │
│   ├── 05-messaging/                 One file per framework, deep enough to write from.
│   │   ├── 01-big-idea.md
│   │   ├── 02..09-<framework>.md     (Trevor: Book × Broadcast × Bond, Interview Economy, Profit
│   │   │                              Before Product, Love Business, 4 C's, Authority Ecosystem,
│   │   │                              Brain > Team > Revenue Machine, SLAPS)
│   │   ├── 10-problem-and-transformation.md
│   │   ├── 11-objections.md
│   │   └── 12-hooks-and-one-minute.md
│   │
│   ├── 06-audience/
│   │   ├── 01-targets.md             The 1 to 3 live targets being tested.
│   │   ├── 02-what-they-want.md      Wants, fears, 3 a.m. thoughts, in their words.
│   │   ├── 03-avatars.md             Real people who fit.
│   │   └── 04-not-a-fit.md           Who to turn away.
│   │
│   ├── 07-offers/                    INTERNAL. Prices live here and nowhere public.
│   │   ├── 01-offer-map.md           The ladder, free to top.
│   │   ├── 02..04-<offer>.md         One file per paid offer.
│   │   └── 05-books.md               Books as offers.
│   │
│   ├── 08-likes-dislikes/
│   │   ├── 01-likes.md               What they love, what energizes them.
│   │   └── 02-dislikes.md            What they hate, pet peeves, what drains them.
│   │
│   ├── 09-rules-of-engagement/       Loaded every wake.
│   │   ├── 01-writing.md             Word-level rules (no em dashes, etc.).
│   │   ├── 02-public-copy.md         What public copy may never say.
│   │   ├── 03-message-format.md      How messages to them are shaped.
│   │   ├── 04-how-ai-works-for-me.md Decide vs ask, sources, results over activity.
│   │   ├── 05-approvals.md           What needs their OK (their additions to LAWS 8).
│   │   └── 06-never.md               The hard never list.
│   │
│   ├── 10-goals/01-goals.md          10-year, 12-month, now. Goals, not results.
│   ├── 11-proof/
│   │   ├── 01-claims.md              The one approved wording of each claim.
│   │   ├── 02-cases.md               Case studies with source and status.
│   │   └── 03-do-not-claim.md        Retired numbers, no-wins-yet list.
│   ├── 12-mentors/01-mentors.md      Councils, what they take from each.
│   └── 13-design/01-design.md        Palette, fonts, look. Or NOT DECIDED.
│
├── team/                             HOW THE AI WORKS (ships with Epic OS, rarely edited)
│   ├── 00-README.md                  Map of the team folder.
│   ├── 01-laws.md                    The 10 laws. The only file that holds laws.
│   ├── 02-people/
│   │   ├── 01-captain.md             The human in charge, their handles, their inbox.
│   │   └── 02-humans.md              Other humans, their roles, who approves what.
│   ├── 03-bots/                      One identity card per AI "house".
│   │   ├── 01-<bot>.md               (Trevor: Max on Hermes, Elon on Grok Bot, Claude, ChatGPT unnamed)
│   │   ├── 05-any-other-ai.md        How a new AI becomes First Mate.
│   │   └── 06-names-not-in-use.md    Parked names. Not retired.
│   ├── 04-seats/                     Roles. Any bot can sit in any seat.
│   │   ├── 01-first-mate.md
│   │   ├── 02-lead.md
│   │   ├── 03-researcher.md
│   │   ├── 04-builder.md
│   │   ├── 05-reviewer.md
│   │   └── 06-scorekeeper.md
│   ├── 05-handoffs/
│   │   ├── 01-how-a-job-moves.md     The loop: target, observe, gap, act, learn.
│   │   ├── 02-task-template.md       The fields every task carries.
│   │   ├── 03-handoff-rules.md       Five-line handoff note, who owns what.
│   │   ├── 04-events.md              Which event triggers which seat (event-driven, no polling chatter).
│   │   ├── 05-blocked-1-3-1.md       How to get unstuck, once.
│   │   └── 06-standing-loops.md      Jobs that never close.
│   ├── 06-talk/
│   │   ├── 01-captain-mode.md        How AI talks to the Captain (theirs, verbatim).
│   │   ├── 02-team-and-clients.md    The 4 C's.
│   │   └── 03-slack.md               Channel and thread rules.
│   └── 07-skills/
│       ├── 00-README.md              What a skill is, the camcorder method.
│       └── <skill-name>/SKILL.md     Earned after three reps. None at start.
│
├── machine/                          WHAT MAKES MONEY
│   ├── 01-systems.md                 Where everything lives (tools, channels, approvers).
│   ├── 02-scorecard.md               Net value = saved + earned - cost.
│   └── scorecard.csv                 The rows.
│
├── memory/                           WHAT THE TEAM LEARNED (append only)
│   ├── DECISIONS.md                  Dated decisions. Newest wins.
│   ├── CORRECTIONS.md                Every correction, same turn.
│   └── INPUTS.md                     Real inputs. 100 lines = Epic tier.
│
├── install/
│   ├── INSTALL.md                    Load it into each AI. The test.
│   ├── start-new-chat.md             The paste-to-start prompt (Epic Squad).
│   └── paste/                        GENERATED from the repo by a script. Never hand-edited.
│
├── library/                          Reference only. Never loaded as instructions.
│   ├── bios-swipe-file.md
│   ├── ai-you-book-outline.md
│   └── tom-bilyeu-ai-elite-team/     Third-party. Pattern reference.
│
└── archive/                          Superseded drafts, dated. Nothing is deleted.
```

## How the template works for a client
1. Copy `epic-ai-os` to `epic-ai-os-<client>`.
2. Run `brain/00-intake.md` (Smart 10). Each answer fills one folder.
3. Empty brand files and by-audience files get deleted, not left blank. A missing file is fine. A fake one is not.
4. Change only: `brain/`, `team/02-people/`, `team/03-bots/`, `team/06-talk/01-captain-mode.md`, `machine/01-systems.md`. Everything else ships as-is.
5. Tiers: Smart = the Smart 10 answered. Pro = a data pack (content, books, calls). Epic = 100 real inputs logged in `memory/INPUTS.md`.

## Mapping from today's repo (what moves where)
| Today (repo/) | Goes to |
|---|---|
| brain/01-identity.md | brain/01-identity/01 to 06 |
| brain/02-voice.md | brain/04-voice/01 to 06 + by-audience/ |
| brain/03-messaging.md | brain/02-mission/, brain/05-messaging/01 to 12 |
| brain/04-audience.md | brain/06-audience/01 to 04 |
| brain/05-offers.md | brain/07-offers/01 to 05 |
| brain/06-goals.md | brain/10-goals/01-goals.md |
| brain/07-rules.md | brain/08-likes-dislikes/ + brain/09-rules-of-engagement/ |
| brain/08, 09, 10 | brain/13-design, 12-mentors, 11-proof |
| new (not in repo) | brain/03-brands/ (Author, Media, OS), brain/02-mission/02-customer-journey.md |
| team/LAWS.md | team/01-laws.md |
| team/ROLES.md + NAMES.md | team/02-people/, 03-bots/, 04-seats/ |
| team/FIRST-MATE, LEAD, BUILDER, REVIEWER | team/04-seats/ |
| team/LOOP.md | team/05-handoffs/01 to 06 |
| team/CAPTAIN-MODE.md + TALK.md | team/06-talk/ |
| team/SKILLS.md | team/07-skills/00-README.md |
| machine/*, memory/*, install/INSTALL.md | same names, numbered |
| install/paste/claude.md, elon-grokbot.md | regenerate by script |
| 00-START-NEW-CHAT.md | install/start-new-chat.md |

## What I drafted now
`/workspace/epic-brain/trevor/` holds v1 of Trevor's filled copy, following this tree:
- `brain/`: every folder above, filled from the best sources.
- `team/`: laws, people, bot cards, seats (plus `04-seats/00-overview.md`), handoffs (including a new `04-events.md` for event-driven handoffs), and talk rules, moved from repo/team with file references updated.
- `QUESTIONS.md`: every gap, as a question for Trevor.
Not drafted yet: machine/, memory/, install/ (they move over from repo/ nearly unchanged).
