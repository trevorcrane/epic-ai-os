# GitHub + Tango Sync Plan (Epic Team)

<!-- context-bundle: preserved-superseded -->

This file is the Sep 28 sync plan, kept. It is a source, not a current wake instruction. Sentences below about Alfred as an active reader, a roster with Alfred added, and Linear as the system of record are superseded and marked in place. Current decisions: `decisions/2026-10-11-parked-names.md`, `decisions/2026-10-11-task-home.md`, `decisions/2026-10-11-first-mate.md`. This file does not install a harness.

**TLDR**
1. GitHub repo `trevorcrane/epic-ai-os` is the single source of truth for decisions, bots, skills and workflows, so every AI reads the same thing.
2. Tango holds tasks and projects. Elon owns a weekly sync. Two things are blocked: the Tango worker key and repo access.

Owner: Elon (Grok Bot). Written Mon Sep 28, 2026. Phase 1 runs now through Oct 7. Phase 2 starts after Oct 7.

## 1. Who needs to stay in the loop

1. Codex "Alfred" (on Trevor's Mac): reads `AGENTS.md` at the repo root. Superseded 2026-10-11: Alfred stays parked, no Alfred card (`decisions/2026-10-11-parked-names.md`). The sentence is kept. It is not a current instruction.
2. Hermes "Max" (iMac now, Orgo later): pulls the repo before each job.
3. Claude (Claude Code): reads `CLAUDE.md`, which points to `AGENTS.md`.
4. ChatGPT: reads the repo through its GitHub connector, or a pasted bundle from `install/paste/`.
5. Elon (Grok Bot): writes most updates and runs the weekly sync.
6. Note: "Alfred" is listed in `team/03-bots/06-names-not-in-use.md` today. Moving him to an active bot card is one of the first decisions to log. Superseded 2026-10-11: that decision is logged. Alfred stays parked. No card (`decisions/2026-10-11-parked-names.md`). The sentence is kept. It is not a current instruction.

## 2. What goes where

1. **GitHub (the Epic Brain and rules):** naming, bot roster, skills, workflows, decisions, standing approvals. Anything that should still be true next month.
2. **Tango (the work):** tasks, projects, who is doing what this week, handoffs between bots.
3. **Rule of thumb:** if it is a decision or a "how we do it", it goes to GitHub. If it is a to-do, it goes to Tango.
4. **Never in either:** API keys, tokens, passwords, card numbers.
5. Note: the Tango pilot plan (`/workspace/tango-pilot/PILOT-PLAN.md`) says Linear stays the system of record for tasks until the pilot decision on Fri Oct 9. Until then, Tango mirrors tasks and Linear wins on conflicts. Superseded 2026-10-11: Tango is the project home for now, and Linear is a source, not the system of record (`decisions/2026-10-11-task-home.md`). The sentence is kept. It is not a current instruction.

## 3. Repo layout (small files, one topic each)

1. `AGENTS.md`: every AI reads this first. Wake order and where things live.
2. `CLAUDE.md`: one line pointing to `AGENTS.md`.
3. `brain/`: who Trevor is (identity, brands, voice, offers, rules). Draft files already exist in `/workspace/epic-brain/trevor/brain/`.
4. `decisions/`: one file per decision, named `YYYY-MM-DD-short-name.md`. Example: `2026-09-28-content-machine-rename.md`.
5. `team/`: one bot roster file per bot (`team/03-bots/01-max.md`, `02-elon.md`, `03-claude.md`, `04-chatgpt.md`, plus Alfred). Drafts exist in `/workspace/epic-brain/trevor/team/`. Superseded 2026-10-11 for the Alfred addition: no Alfred card (`decisions/2026-10-11-parked-names.md`). The sentence is kept. It is not a current instruction.
6. `skills/`: one folder per skill with a `SKILL.md`. Source list: `/workspace/skill-library/SKILL-LIBRARY.md` and `skills.json` (20 skills: 9 Live, 6 Draft, 5 Parked).
7. `workflows/`: one file per workflow. First one: the AI publishing workflow from `/workspace/strategy/ai-publishing-workflow.md`.
8. This matches `/workspace/epic-brain/PROPOSED-STRUCTURE.md` with two changes: decisions become a `/decisions` folder (not one `memory/DECISIONS.md` file), and skills and workflows sit at the top level.

## 4. Decision file format (keep it to 6 lines)

1. `Date:` 2026-09-28
2. `Decision:` one sentence.
3. `Why:` one sentence.
4. `Decided by:` Trevor, or "standing approval" with a link.
5. `Affects:` files or bots it changes.
6. `Replaces:` older decision file, if any. Newest wins.

## 5. Weekly sync (Elon owns it)

1. **When:** every Friday, 3 PM ET. Takes about 30 minutes of bot time and zero Trevor time.
2. **Step 1.** Elon collects the week's decisions from Slack, Grok Bot chats, bot logs (like `/workspace/skill-library/bot-log.md`) and Tango comments.
3. **Step 2.** Elon writes one decision file per decision into `decisions/`.
4. **Step 3.** Elon updates the affected files (bot roster, skills, workflows) so they match.
5. **Step 4.** Elon opens ONE pull request titled `Weekly sync YYYY-MM-DD`.
6. **Step 5.** A bot from a different house (Max or Alfred) reviews it. This is the cross-house review rule from the team laws. Superseded 2026-10-11 where it assigns the review to Alfred: Alfred stays parked (`decisions/2026-10-11-parked-names.md`). The sentence is kept. It is not a current instruction.
7. **Step 6.** Merge after review. Trevor does not review unless the PR changes a rule on the Trevor-only list. Then it goes on his sign-off list as one tap.
8. **Step 7.** Elon posts a 3-line "what changed" note in Tango (and Slack once Slack posting is approved).
9. **In between syncs:** urgent decisions (anything that changes live work) get pushed the same day, not held for Friday.

## 6. Phase 1: now through Oct 7 (lightweight)

1. Create the folders: `decisions/`, `team/`, `skills/`, `workflows/`, plus `AGENTS.md`.
2. Push the bot roster cards from `/workspace/epic-brain/trevor/team/03-bots/`, with Alfred added. Superseded 2026-10-11: no Alfred card (`decisions/2026-10-11-parked-names.md`). The sentence is kept. It is not a current instruction.
3. Backfill decisions from the last week only (Content Machine rename, fleet shrink list, Social Planner as primary publishing tool, Robyn's channel written by her media person, Crazy Cranes kept separate).
4. Push the skill library index and the 9 Live skills. Drafts and Parked stay as index lines only.
5. Push the publishing workflow and the Minimum Buttons Rule (`/workspace/ops/MINIMUM-BUTTONS-RULE.md`).
6. Tango: once the key arrives, create one project "Epic OS Sync" with a weekly recurring task assigned to @elon.
7. Do NOT build automation yet. Manual weekly PR is enough before the Oct 7 trip.

## 7. Phase 2: after Oct 7

1. Tango tasks link to the decision file that created them, and each decision file links back to its Tango task.
2. Tango webhook (`task.commented`, `task.handoff_received`) wakes Elon to log decisions as they happen, instead of only on Fridays.
3. Each harness (Alfred, Max, Claude) pulls the repo automatically at the start of every job. Superseded 2026-10-11 where it names Alfred as a harness to pull: Alfred stays parked (`decisions/2026-10-11-parked-names.md`). The sentence is kept. It is not a current instruction. This review pass does not migrate that schedule.
4. Generate the ChatGPT paste bundle from the repo by script (never hand-edited).
5. Move the Brain drafts from DRAFT to approved, one folder per week, via the sign-off list.
6. Use the Tango pilot decision (Fri Oct 9) to decide whether Tango replaces Linear. Log it as a decision. Superseded 2026-10-11: the logged decision is `decisions/2026-10-11-task-home.md`. Tango is the project home for now. Linear stays a source. The sentence is kept. It is not a current instruction.
7. Consider a template copy of the repo for clients once Trevor's copy has run for a month.

## 8. What is blocked

1. **Tango worker key.** The Tango connection is waiting on Trevor's `tng_` worker key for @elon (see `/workspace/tango-pilot/ELON-CONNECT.md`). Trevor-only step: paste it into Grok Bot's secure secret box. One tap on the sign-off list.
2. **Epic OS bot's access to the repo.** The Epic OS bot cannot write to `trevorcrane/epic-ai-os` yet. Checked today: the connected GitHub account cannot see the repo (private, not granted to the app, or not created yet). The box's GitHub CLI login also timed out (`/workspace/gh-login.log`).
3. **Fix for #2 (team does it, Trevor taps once):**
   1. Team confirms the repo exists. If not, the team creates it as private (after one sign-off tap).
   2. Team prepares the GitHub App install screen for the repo. Trevor approves it with one tap (it is his account consent).
   3. Access is scoped to this one repo only, not all of Trevor's repos.
4. Until both are fixed, Elon keeps the sync files in `/workspace/epic-brain/` and pushes the backlog in one PR on the first day access works.

## 9. Local sources used

1. `/workspace/strategy/ai-publishing-workflow.md`
2. `/workspace/epic-brain/` (PROPOSED-STRUCTURE.md, trevor/brain, trevor/team)
3. `/workspace/skill-library/` (SKILL-LIBRARY.md, skills.json, bot-log.md, fleet-shrink-list-2026-09-28.md)
4. `/workspace/tango-pilot/` (PILOT-PLAN.md, RESEARCH.md, ELON-CONNECT.md)
