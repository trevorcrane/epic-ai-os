# INVENTORY: Epic OS handoff zip (2026-09-27)

Status: DRAFT for Trevor. Built 2026-09-28.
Source: `EPIC-OS-HANDOFF-2026-09-27.zip`, unzipped to `/workspace/epic-brain/source/EPIC-OS-HANDOFF-2026-09-27/`.
61 files. 0 byte-identical duplicates. Plenty of content duplicates: the same text copied from file to file, getting more refined each time.

Verdicts:
- **KEEP**: best version. Carry it into the new structure.
- **MERGE**: good parts. Pull them into the KEEP file, then archive.
- **REFERENCE**: not Brain or Team content. Keep in `archive/` or `library/`, don't load into an AI.
- **CUT**: fully superseded or generated. Archive; nothing to pull.

Nothing gets deleted. "Cut" means it moves to `archive/`, so the trail survives.

---

## 1. How the versions stack (the family tree)

Oldest to newest. Each step was built from the one before.

1. **Sep 7, ChatGPT**: `Trevor-Crane-Brain-Complete-Original-Drafts.md` (the ten original Claude brand files, reproduced) + `EPIC-Team-Proposal-ChatGPT-Sep7.md` (team proposal).
2. **Sep 15**: `Trevor-Crane-Brain-updated-9_15_26-MASTER.md`. Same ten files plus Trevor's bio variants and edits. Superset of #1.
3. **Sep 15**: `EPIC-AI-Project-Handoff-2026-09-15.md` and `EPIC-AI-AGENT-TEAM-INSTRUCTIONS-v1.md` (team side), `TREVOR-CRANE-EPIC-BRAIN-v1.md` (a short "simple source of truth" summary).
4. **Sep 21**: `Trevor-Crane-EPIC-Brain-v0.2-Sep21-corrections.md`. Trevor's direct corrections: family birthdays, domains, Authority Accelerator pricing, AIYOU title. Beats Sep 15 where they differ.
5. **Sep 13 to 22**: bios docx (Trevor's own edited copy). Beats any AI draft on wording.
6. **Sep 25 to 27, Claude**: `repo/` (the Epic OS build), plus six reports explaining how it was merged and what's still open.

**Bottom line:** `repo/brain/` and `repo/team/` already hold the best merge of everything in steps 1 to 5. The sources only need re-checking for quotes and the parts that got cut for length (listed in the merge report, section 5).

---

## 2. Duplicate groups

| Group | Files | Best | Why |
|---|---|---|---|
| A. Ten Brain drafts | Original-Drafts.md, 9_15 MASTER.md, v1.md, v0.2.md, repo/brain/01 to 10 | **repo/brain/01 to 10** | Merges all four, with source tags. Sep 21 beats Sep 15, and Trevor's own copy beats AI copy (DECISIONS 2026-09-26). |
| B. Original drafts vs 9_15 master | Complete-Original-Drafts.md vs 9_15-MASTER.md | **9_15 MASTER** (as source) | MASTER = originals + bio block + edits (581 lines differ, all additions or edits). Originals add nothing new. |
| C. The Mechanism | reports/MECHANISM-DEEP-2026-09-27.md vs repo/brain/03-messaging.md "THE MECHANISM" | **repo/brain/03-messaging.md** | The report's full framework section (about 23K chars) is pasted into 03 word for word. Report = duplicate. |
| D. Full repo on one page | review/v1-EpicOS-review-2026-09-27.html vs repo/* | **repo/*** | The HTML is every repo file on one page, for reading. Generated. Its sidebar links are broken (brief). |
| E. Install packets | install/paste/claude.md vs elon-grokbot.md (+ max-soul.md) | **generate from repo** | Both are ~1,060-line copies of the whole repo. They differ only in the name card (about 10 lines). Generated, and they go stale on every commit. |
| F. Team design | EPIC-Team-Proposal-ChatGPT-Sep7.md, EPIC-AI-AGENT-TEAM-INSTRUCTIONS-v1.md, EPIC-AI-Project-Handoff-2026-09-15.md, repo/team/* | **repo/team/*** | The team audit folded the useful parts of all three into repo/team (see TEAM-AUDIT-REPORT section B). The old seat names (Director, Agent One, RAIN) are "not in use right now." |
| G. Talk rules | team/CAPTAIN-MODE.md vs team/TALK.md section 1 vs brain/07-rules.md "How AI talks to me" | **CAPTAIN-MODE.md** (verbatim from Trevor) | TALK.md and 07-rules repeat it in short form, and the short copies drift. |
| H. Tom Bilyeu kit | 5 role .md files vs AI-Elite-Team-Complete-Reference.docx | **the 5 .md files** | The docx = webinar summary + the same 5 skill files verbatim + install guide. Third-party. Pattern reference only. |
| I. Landing page copy | review/v3-EpicOS-LandingPage-Copy (Claude, handoff) vs /workspace/epic-os-page/epic-os-page-copy-v3.md (ours, the Railway page) | **neither as-is** | Two different v3s. The handoff one shows prices and "SMAI (GoHighLevel)", which Trevor's rules now ban. Ours uses the new framework but lacks the Brain facts. See EPIC-OS-SITE-NOTES.md. |

---

## 3. Every file

### Top level
| File | What it is | Verdict | Reason |
|---|---|---|---|
| 00-START-NEW-CHAT.md | The prompt Trevor pastes to start a chat, including the Epic Squad run-a-job prompt | **KEEP** (move to `install/`) | The squad prompt (Lead, Researcher, Builder, Reviewer, Scorekeeper) is the clearest statement of how a job runs. |
| 01-BRIEF.md | One-page story: what Epic OS is, status, what went wrong, how to talk to Trevor, open decisions | **KEEP** (as `HANDOFF.md`, dated) | Best single orientation doc. The "what went wrong" list should become rules. |

### repo/ root
| File | What it is | Verdict | Reason |
|---|---|---|---|
| repo/AGENTS.md | The file every AI reads first: wake order, done, claims, memory | **KEEP** | The open standard file agent tools look for. Trim duplicated rules per RESEARCH-CHECK D. |
| repo/CLAUDE.md | Imports AGENTS.md for Claude Code | **KEEP** | 3 lines. Needed. |
| repo/README.md | What the repo is, the three tiers, cloning | **KEEP** | Update the repo name (see Questions). |
| repo/START-HERE.md | Trevor's three steps: review, say go, give a job | **KEEP** | Short. Right idea. |

### repo/brain/ (group A: best versions)
| File | What it is | Verdict | Reason |
|---|---|---|---|
| 00-INTAKE.md | Smart 10 intake questions, four answer modes, prompts | **KEEP** (template) | Research-backed. Goes into the client template as-is. |
| 01-identity.md | Who Trevor is, family, bankruptcy, Steven, beliefs, AI Caveman | **KEEP**, split | Best source. Split into ~6 small files. |
| 02-voice.md | Voice guide, modes, no-AI-slop, phrases, samples | **KEEP**, split | Full text, no cap (per Trevor's 9/27 correction). Split by topic and audience. |
| 03-messaging.md | Big idea, promise, frameworks in depth, objections, hooks | **KEEP**, split | 37K chars, the richest file. One file per framework. |
| 04-audience.md | Targets, avatars, not-a-fit | **KEEP**, split | Includes the "audience is a test" decision. |
| 05-offers.md | Authority Accelerator, Epic OS Install, AI offer family, prices | **KEEP**, split | Prices stay INTERNAL. Never in public copy. |
| 06-goals.md | 10-year, 12-month, now-to-Dec-11, Robyn, content | **KEEP** | Goals, not results. |
| 07-rules.md | Stands for/against, AI rules, approvals, never list | **KEEP**, split | Becomes likes/dislikes + rules of engagement. |
| 08-design.md | NOT DECIDED: two AI-made palettes, neither approved | **KEEP** (as open) | Blocks visual work until Trevor picks. |
| 09-mentors.md | Councils, what he takes from each, frameworks list | **KEEP** | |
| 10-proof.md | Credibility line, cases, what not to claim | **KEEP** | "One result, one wording, one source, one date." |

### repo/team/ (group F: best versions)
| File | What it is | Verdict | Reason |
|---|---|---|---|
| LAWS.md | The 10 laws + always-on list | **KEEP** | The only place laws live. |
| ROLES.md | Captain, First Mate, the five seats, houses, humans, names not in use | **KEEP**, split | Split into seats/ and houses/ files. |
| NAMES.md | Name cards: Captain, Max, Elon, Claude, ChatGPT (unnamed) | **KEEP**, split | One card per bot file. |
| FIRST-MATE.md | First Mate seat: creed, handoffs, report format | **KEEP** | |
| LEAD.md | Lead seat: staffing, standing duties | **KEEP** | The research check wanted it folded in. DECISIONS 9/26 kept one Lead per harness, so it stays. |
| BUILDER.md | Builder base rules: plan over 60 min, smallest change, branch + PR, no mocks in anything a person sees | **KEEP** | |
| REVIEWER.md | Review method, 5-part score, Green-Light Fix, scoring loop | **KEEP** | |
| LOOP.md | How a job moves; task template; 1-3-1; standing loops | **KEEP**, split | Handoff rules come out of here. |
| TALK.md | Three voices: Captain Mode, 4 C's, Slack rules | **MERGE** | Section 1 duplicates CAPTAIN-MODE. Keep sections 2 and 3. |
| CAPTAIN-MODE.md | Trevor's talk-to-me spec, v5, verbatim | **KEEP** | His words. Wins over TALK.md. |
| SKILLS.md | Skill format, camcorder method, first skills, Tom roles | **KEEP** | |

### repo/machine/, memory/, install/
| File | What it is | Verdict | Reason |
|---|---|---|---|
| machine/SCORECARD.md | Net value = saved + earned - cost; the row format | **KEEP** | |
| machine/scorecard.csv | Header only | **KEEP** | Header doesn't match SCORECARD.md (research check D6). Fix. |
| machine/SYSTEMS.md | Where everything lives; Slack channels; approvers; standing duties | **KEEP** | Internal. Names GoHighLevel, which is fine internally, never in public copy. |
| memory/DECISIONS.md | Dated decision log, newest wins | **KEEP** | Decisions from 2026-09-28 need adding (see trevor/brain/00-README.md). |
| memory/CORRECTIONS.md | Correction log (empty) | **KEEP** | |
| memory/INPUTS.md | The "100 inputs = Epic" ledger (empty) | **KEEP** | |
| install/INSTALL.md | How to load each harness, the test | **KEEP** | |
| install/paste/claude.md | Whole repo pasted as one packet (Claude / any harness) | **CUT** (regenerate) | Group E. Generated. Stale on every commit. |
| install/paste/elon-grokbot.md | Same, Elon card | **CUT** (regenerate) | Group E. |
| install/paste/max-soul.md | Max's short SOUL.md | **KEEP** | 20 lines, hand-written, points to AGENTS.md. |

### reports/
| File | What it is | Verdict | Reason |
|---|---|---|---|
| BRAIN-MERGE-REPORT-2026-09-26.md | Which source won, per file; 15 ranked conflicts; what got cut | **REFERENCE** (keep) | The map of the merge. Section 5 lists good material cut for length. |
| BRAIN-CONFLICTS-2026-09-26.md | Conflicts per Brain file | **REFERENCE** | Several now resolved in DECISIONS. The rest are in the Questions below. |
| MECHANISM-DEEP-2026-09-27.md | Framework deep dive | **CUT** | Group C. Already inside 03-messaging. |
| RESEARCH-CHECK-2026-09-26.md | Repo vs Tango, GitHub, agents.md, Hermes; delete and simplify lists | **REFERENCE** | Use its SIMPLIFY list when splitting files (one rule, one home). |
| SMART-START-RESEARCH-2026-09-27.md | Research behind the Smart 10 | **REFERENCE** | Backs 00-INTAKE. |
| TEAM-AUDIT-REPORT.md | New team sources vs repo; ADOPT list; Tom roles vs seats | **REFERENCE** | Most ADOPT items are already in repo/team. |

### review/
| File | What it is | Verdict | Reason |
|---|---|---|---|
| v1-EpicOS-review-2026-09-27.html | Every repo file on one page | **CUT** (regenerate) | Group D. Rebuild from GitHub after the split, with anchors that work. |
| v3-EpicOS-LandingPage-Copy-2026-09-27.md | Claude's landing copy, "passed review 95/95" | **MERGE** (into site notes) | Good sections (Where this actually is, Steven, the laws). But it shows prices, "SMAI (GoHighLevel)", and "Invisible to in demand." Breaks the current rules. |

### sources/brain-drafts/
| File | What it is | Verdict | Reason |
|---|---|---|---|
| Trevor-Crane-Brain-updated-9_15_26-MASTER.md | Sep 15 master: ten brand files + bio variants | **REFERENCE** | Master source for repo/brain. Re-check quotes here. |
| Trevor-Crane-Brain-Complete-Original-Drafts.md | Sep 7 original ten drafts | **CUT** | Group B. Subset of the 9_15 master. |
| Trevor-Crane-EPIC-Brain-v0.2-Sep21-corrections.md | Sep 21 corrections (family, domains, pricing, IP, voice) | **REFERENCE** | Newest direct statements. Already merged. Its family table is the source for 02-family. |
| TREVOR-CRANE-EPIC-BRAIN-v1.md | Short "simple source of truth" (what I love, who I love, what they love) | **MERGE** | Its sections 2 to 4 ("what I love / who I love / what they love") are the best likes and audience-wants lists. Pulled into trevor/brain/07-likes-dislikes and 05-audience. |
| Trevor-Crane-YouTube-Headers-Bios-LinkedIn-Bios-9-22-26.docx | Trevor's own bios, 20+ variants, Epic AI Lab page copy | **REFERENCE** (swipe file) | Trevor-edited, so VERIFIED wording. Chosen lines are in voice samples and messaging. The rest goes to `library/`. |
| AI YOU Book Framework and Proposals.docx | AI YOU book outline: Clone, Command, Create, Convert, Freedom | **REFERENCE** (book project) | Draft, not final. The Brain keeps the five-part name only. |

### sources/team-drafts/
| File | What it is | Verdict | Reason |
|---|---|---|---|
| EPIC-Team-Proposal-ChatGPT-Sep7.md | ChatGPT's team proposal | **CUT** | Group F. Useful parts adopted by the team audit. Source of the invented "five proofs" (brief, what went wrong #1). |
| EPIC-AI-AGENT-TEAM-INSTRUCTIONS-v1.md | Director / specialists / reviewer team, quality gate, authority | **MERGE** (done) | Reviewer rubric and authority rules already adopted. Archive. |
| EPIC-AI-Project-Handoff-2026-09-15.md | Sep 15 project handoff: first-job questions, loops, tiers, website status | **MERGE** (done) | First-job skill and loop wording adopted. Archive. |

### sources/tom-bilyeu-kit/ (group H)
| File | What it is | Verdict | Reason |
|---|---|---|---|
| AI Elite Team-Researcher.md | Tom's Researcher skill | **REFERENCE** | Third-party. Pattern for team skills. Don't load as ours. |
| AI Elite Team-Strategist.md | Tom's Strategist skill | **REFERENCE** | Same. |
| AI Elite Team-Copywriter.md | Tom's Copywriter skill | **REFERENCE** | Same. |
| AI Elite Team-Builder.md | Tom's Builder skill | **REFERENCE** | Same. |
| AI Elite Team-Marketer.md | Tom's Marketer skill | **REFERENCE** | Same. |
| AI-Elite-Team-Complete-Reference.docx | All five + webinar summary + install guide | **CUT** | Duplicates the five .md files. Keep one copy in `library/`. |

---

## 4. Best version of each thing (the picks)

| Thing | Best version | Runner-up / pull from |
|---|---|---|
| Identity | repo/brain/01-identity.md | v0.2 section 2 (family table) |
| Voice | repo/brain/02-voice.md | /workspace/trevor-voice/wife-robyn.md (voice by audience), CAPTAIN-MODE.md (talking to Trevor) |
| Messaging and frameworks | repo/brain/03-messaging.md | 9_15 MESSAGING (full objections, hooks) |
| Audience | repo/brain/04-audience.md | v1.md sections 3 and 4 |
| Offers | repo/brain/05-offers.md | v0.2 section 6 |
| Goals | repo/brain/06-goals.md | |
| Rules, likes, dislikes | repo/brain/07-rules.md | v1.md section 2 (what I love), v0.2 section 3 (values) |
| Design | repo/brain/08-design.md (NOT DECIDED) | |
| Mentors | repo/brain/09-mentors.md | |
| Proof | repo/brain/10-proof.md | |
| Intake (client template) | repo/brain/00-INTAKE.md | SMART-START-RESEARCH |
| Team laws, seats, loop | repo/team/* | TEAM-AUDIT section B |
| Talk to Trevor | repo/team/CAPTAIN-MODE.md | |
| Run-a-job prompt | 00-START-NEW-CHAT.md (the Epic Squad block) | |

## 5. Things in the zip that break Trevor's newest rules (fix on the way in)
1. **Prices in public copy**: review/v3 landing copy section 10 ($15,000, $1,000, $297). The Brain keeps prices INTERNAL only.
2. **HighLevel in public copy**: review/v3 section 10, "SMAI (GoHighLevel)". Fine in machine/SYSTEMS.md (internal), never on a page.
3. **Em dashes**: the source drafts (v1.md, v0.2.md titles, bios docx) use them. repo/ is clean. Everything in trevor/ is clean.
4. **Family**: the Brain lists three kids (Phoenix, Maverick, Sage). Birthdates are not stored. The new facts name Maverick and Sage. See Questions.
