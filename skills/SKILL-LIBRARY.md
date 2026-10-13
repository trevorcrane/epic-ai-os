# Epic OS Skill Library

Owner: Trevor Crane. Updated 2026-09-28. 20 skills: 9 Live, 6 Draft, 5 Parked.

## How to use this

1. Skim the cards below. Each one says what the skill does, which bot uses it, and whether it is ready.
2. To hand a skill to a bot, say "give skill [name] to bot [name]" (example: "give Score to Content Engine").
3. To approve a draft, say "install [skill name]". Drafts are written but not turned on yet.
4. Mark favorites to share with clients later: say "favorite [skill name]" and it gets a star here and in skills.json.
5. Share column: Yes means ours and safe to give clients, Maybe means needs trimming first, No means Tom-derived, third-party, or client-private.

Status key: Live = installed and in use. Draft = written, not installed. Parked = saved for later or reference only.

That key is the 2026-09-28 index wording, kept. In this repo, Live does not mean the skill body is here. The nine Live folders are index cards. The bodies were not in the compile archive. Do not treat a card, a Live row, or this file as proof of installation. "Epic OS (First Mate)" in the bot column is the 2026-09-28 label. The current First Mate decision is `decisions/2026-10-11-first-mate.md`: whichever AI Trevor is talking to.

## Strategy & planning

| # | Skill | What it does | Bot(s) | Status | Share with clients? | File |
|---|---|---|---|---|---|---|
| 1 | **Master Plan** | Turns a rough project or idea into a short, clear plan card with what done looks like, a grade, and a ship-or-improve decision. | Planner, Advisor, Navigator, Epic OS (First Mate) | Live | Yes | `/home/box/agent-data/workflows/master-plan/SKILL.md` |
| 2 | **Pressure Test Before Go** | Scores a big new tool, system, or workflow on 7 checks before anyone says go, and only allows a small pilot if the key scores are under 80. | Advisor, Navigator, Epic OS (First Mate), Reviewer | Live | Yes | `/home/box/agent-data/workflows/pressure-test-before-go/SKILL.md` |
| 3 | **90-Day Growth Plan** | Builds a 90-day plan to get a live offer in front of the right people and turn them into conversations and customers, with every task given to a named bot. | Campaign Ops, Content Engine, GTM Prospecting, GTM Loop Closer, Call Follow-Ups, Sales Call Coach, Scorekeeper | Draft | No | `/workspace/assets/teaching-frameworks/tom-bilyeu-ai-team-pack/handoffs/marketer-campaign-ops.md` |
| 4 | **Demand Test Design** | Picks the one smallest test (free download, booked call, or pre-sale) that proves people want an offer before it gets built, with a win number and a quit number set up front. | Advisor | Draft | No | `/workspace/assets/teaching-frameworks/tom-bilyeu-ai-team-pack/handoffs/strategist-demand-test.md` |

1. Master Plan: Our own method. Uses the Score skill for the grade. How to start it: Say "master plan re: ...".
2. Pressure Test Before Go: Our own method. How to start it: Runs automatically before any go, install, or build decision.
3. 90-Day Growth Plan: Not installed. Tom-derived. Campaign Ops owns it and hands pieces to the others. How to start it: "How do I get leads?" once a page is live.
4. Demand Test Design: Not installed. Shaped after the Tom Bilyeu pack (personal use only), so not for clients as is. How to start it: "How do I test this?" or after Idea Validation says GO.

## Research

| # | Skill | What it does | Bot(s) | Status | Share with clients? | File |
|---|---|---|---|---|---|---|
| 5 | **Idea Validation** | Proves or kills a business idea using real customer words and proof that people already pay for this, ending in GO, SHARPEN, or KILL. | Researcher | Draft | No | `/workspace/assets/teaching-frameworks/tom-bilyeu-ai-team-pack/handoffs/researcher-idea-validation.md` |

5. Idea Validation: Not installed. Tom-derived. First step of the launch chain. How to start it: "Is this idea any good?" or "validate this".

## Copy & content

| # | Skill | What it does | Bot(s) | Status | Share with clients? | File |
|---|---|---|---|---|---|---|
| 6 | **Landing Page Build** | Turns approved launch copy into one live web page with one button and a working signup form, then hands a checklist to the Reviewer before it goes public. | Builder, Bot Studio, Reviewer | Draft | No | `/workspace/assets/teaching-frameworks/tom-bilyeu-ai-team-pack/handoffs/builder-landing-page.md` |
| 7 | **Launch Copy** | Writes every word a launch needs (hook, page, free download, follow-up emails, posts, DMs) in the client's own voice using only real proof. | Cat (Book: Dr. Leigh), Content Engine, Writing Bot | Draft | No | `/workspace/assets/teaching-frameworks/tom-bilyeu-ai-team-pack/handoffs/copywriter-cat.md` |

6. Landing Page Build: Not installed. Tom-derived. Bot Studio Builder for client builds. How to start it: "Publish a page" once copy is approved.
7. Launch Copy: Not installed. Tom-derived. Planned for Cat as she moves into Trevor's copywriter seat. How to start it: After a Demand Test is picked, or any ask for a hook, page, or emails.

## Mentors/coaching

| # | Skill | What it does | Bot(s) | Status | Share with clients? | File |
|---|---|---|---|---|---|---|
| 8 | **Ed Lawrence Mentor** | Coaches Trevor on business YouTube: simple style, intros, stories that turn viewers into buyers, and views versus sales in a Ed Lawrence-style voice, using only saved quotes and videos, never pretending to be Ed Lawrence. | Mentor agents | Live | No | `/home/box/agent-data/workflows/ed-lawrence-advisor/SKILL.md` |
| 9 | **Hormozi Mentor** | Coaches Trevor on offers, leads, free value, and growth in a Alex Hormozi-style voice, using only saved quotes and videos, never pretending to be Alex Hormozi. | Mentor agents, YT Mentor: Hormozi | Live | No | `/home/box/agent-data/workflows/hormozi-advisor/SKILL.md` |
| 10 | **Kallaway Mentor** | Coaches Trevor on YouTube, short videos, packaging, bios, and calls to action in a Kallaway-style voice, using only saved quotes and videos, never pretending to be Kallaway. | Mentor agents | Live | No | `/home/box/agent-data/workflows/kallaway-advisor/SKILL.md` |
| 11 | **Dan Martell Mentor (stub)** | Starter rules for a future Dan Martell-style coach; the videos and quotes are gathered but it is not a working skill yet. | Mentor agents | Parked | No | `/workspace/mentor-machine/packs/dan-martell/persona/SYSTEM.md` |
| 12 | **Gary Vee Mentor (stub)** | Starter rules for a future Gary Vee-style coach; the videos and quotes are gathered but it is not a working skill yet. | Mentor agents | Parked | No | `/workspace/mentor-machine/packs/gary-vee/persona/SYSTEM.md` |
| 13 | **MrBeast Mentor (stub)** | Starter rules for a future MrBeast-style coach; the videos and quotes are gathered but it is not a working skill yet. | Mentor agents | Parked | No | `/workspace/mentor-machine/packs/mrbeast/persona/SYSTEM.md` |
| 14 | **MrBeast Perspective (outside download)** | A free skill someone else published online (written in Chinese) that role-plays MrBeast to give YouTube title, thumbnail, and hook advice. | None yet | Parked | No | `/workspace/mentor-machine/refs/mrbeast-github/alchaincyf-mrbeast-skill/SKILL.md` |

8. Ed Lawrence Mentor: Installed, but the pack scored 56% with Reviewer, so it is held from being promoted as a finished coach. Copy also lives at /workspace/mentor-machine/skills/ed-lawrence-advisor/SKILL.md. The two copies differ slightly (need to pick one). How to start it: Ask for "Ed Lawrence" advice.
9. Hormozi Mentor: Installed, but the pack scored 50% with Reviewer, so it is held from being promoted as a finished coach. Copy also lives at /workspace/mentor-machine/skills/hormozi-advisor/SKILL.md. The two copies are identical. How to start it: Ask for "Alex Hormozi" advice.
10. Kallaway Mentor: Installed, but the pack scored 57% with Reviewer, so it is held from being promoted as a finished coach. Copy also lives at /workspace/mentor-machine/skills/kallaway-advisor/SKILL.md. The two copies differ slightly (need to pick one). How to start it: Ask for "Kallaway" advice.
11. Dan Martell Mentor (stub): Reviewer score 48%. No installed skill and no mentor agent assigned yet. How to start it: Not usable yet.
12. Gary Vee Mentor (stub): Reviewer score 48%. No installed skill and no mentor agent assigned yet. How to start it: Not usable yet.
13. MrBeast Mentor (stub): Reviewer score 42%. No installed skill and no mentor agent assigned yet. How to start it: Not usable yet.
14. MrBeast Perspective (outside download): Third-party. Our MrBeast pack treats it as a guess to check, not a source. No owner bot. How to start it: Reference only.

## Ops & quality

| # | Skill | What it does | Bot(s) | Status | Share with clients? | File |
|---|---|---|---|---|---|---|
| 15 | **First Mate Operating System** | The rulebook for how First Mate takes a request, puts it on a Linear card with an owner and a checker, and only calls it done when there is proof. | Epic OS (First Mate), Implementer, Builder, Reviewer | Live | Maybe | `/home/box/agent-data/workflows/first-mate-os/SKILL.md` |
| 16 | **Score** | Grades any piece of work with a letter and a percent, names the 2 to 4 gaps, and asks whether to ship it or improve it. | Reviewer, Epic OS (First Mate), Planner, All bots | Live | Yes | `/home/box/agent-data/workflows/score/SKILL.md` |
| 17 | **Epic Skill Card Template** | The blank pattern every new skill should follow: one job, what it needs first, hard rules, steps with checks, a self-score, and a handoff note. | Bot Studio, Epic Brain | Draft | No | `/workspace/assets/teaching-frameworks/tom-bilyeu-ai-team-pack/handoffs/00-epic-skill-card-template.md` |
| 18 | **Tango Work Loop (outside tool)** | Instructions from the Tango tool for how bots claim a task, show their work, attach proof, and hand off to the next bot or person. | Epic OS (First Mate), Implementer | Parked | Maybe | `/workspace/tango-pilot/src/skill.md` |

15. First Mate Operating System: Our own method, but tied to Trevor's Linear setup and Grok Bot; would need trimming for a client. How to start it: "Get this done" to First Mate.
16. Score: Our own method. How to start it: Say "score this" or "grade this".
17. Epic Skill Card Template: Not installed. Structure inspired by the Tom pack, rewritten in our words; Maybe for clients after Tom says OK. How to start it: Used when writing a new skill.
18. Tango Work Loop (outside tool): Written by Tango (a vendor), saved during a pilot. Not installed. No bot formally owns it. How to start it: Only if the Tango pilot goes ahead.

## Client-specific

| # | Skill | What it does | Bot(s) | Status | Share with clients? | File |
|---|---|---|---|---|---|---|
| 19 | **Depleted Brain Ghostwriting Playbook** | The playbook for drafting Dr. Leigh's book The Depleted Brain: table of contents patterns, launch deadlines, and rules against made-up facts. | Cat (Book: Dr. Leigh), Writing Bot | Live | No | `/workspace/leigh-book/research/COPY-SKILLS.md` |
| 20 | **Dr. Leigh Richardson Voice** | Makes anything written in Dr. Leigh's name (book chapters, emails, posts, bios) sound warm, plain, and hopeful like her, with every science fact sourced. | Cat (Book: Dr. Leigh), Writing Bot, Content Engine | Live | No | `/home/box/agent-data/workflows/dr-leigh-richardson-voice/SKILL.md` |

19. Depleted Brain Ghostwriting Playbook: A reference file the Book agent reads, not an installed skill. How to start it: Book drafting sessions. Moved 2026-10-11 to `clients/dr-leigh/depleted-brain/`: Dr. Leigh's material, not Trevor's (decisions/2026-10-11-depleted-brain.md).
20. Dr. Leigh Richardson Voice: Short installed version. Full version: /workspace/leigh-book/LEIGH-VOICE-SKILL.md (Word copy in /workspace/leigh-docx/). Still partial: blogs and LinkedIn not added yet. How to start it: Any writing in Dr. Leigh's voice.

## On the list, not written yet

From the Epic OS plan. Skills get written after a job repeats three times.

1. intake-brain: Fill in a new person's Brain files.
2. first-job: Five questions that turn a new Brain into one finished job.
3. follow-up-draft: Draft follow-ups in the Brain's voice from a list of names.
4. call-to-content: Turn one call recording into a post, clip list, and newsletter section.
5. log-job: Write the Scorekeeper row for a finished job.
6. 1-3-1: Turn a messy ask into a one problem, three options, one pick decision brief.

## Outside reference skills (Parked)

1. 54 files, 30 unique skills. Free Hormozi-style skills other people published online. Saved as reference, blocked from auto-loading into answers. 24 of them exist twice (once in each folder). Status Parked, Share No, no owner bot.
2. Locations: `/workspace/mentor-machine/packs/hormozi/corpus/from-github/` and `/workspace/mentor-machine/refs/hormozi-github/`

## Things to know

1. Two naming schemes for the same launch skills: the Epic OS plan (team/SKILLS.md) calls them pain-research, offer-test, launch-copy, one-page-site, gtm-plan, while the drafts are idea-validation, demand-test-design, launch-copy, landing-page-build, growth-plan. Trevor picked the draft names on 2026-10-11 (decisions/2026-10-11-launch-skill-names.md).
2. Mentor skills live in two places (installed copy and a copy in mentor-machine/skills). Hormozi copies match; Kallaway and Ed Lawrence copies differ slightly.
3. Dr. Leigh voice exists as a short installed skill, a long Markdown version, and a Word copy.
4. No owner bot: MrBeast Perspective (outside download), the 30 outside Hormozi skills, and Tango Work Loop (only a pilot).
5. Mentor skills are installed but held: none has passed Reviewer yet (scores 50% to 57%). Held until a Reviewer score of 80+ (decisions/2026-10-11-mentor-packs.md).
6. All 5 launch drafts are Tom-derived and marked personal use only, so they are No for clients until rewritten or Tom agrees.

## Appendix

1. Cursor/Grok built-in skills (managed-skills, plugin-skills, plugins/compound-engineering): built-in, not ours.
2. Related instruction files that are not skills (bot start-up rules, drafts): /workspace/epic-brain/source/EPIC-OS-HANDOFF-2026-09-27/repo/AGENTS.md and CLAUDE.md, /workspace/epic-brain/trevor/team/ (seat and handoff rules).
