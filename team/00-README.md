# How the AI works (team folder map)

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: PROPOSED-STRUCTURE.md, Trevor's ask 2026-10-06, Reviewer score of this draft (2026-10-06).

Reviewer fixes 1 to 8 applied and re-scored 2026-10-06 (95, PASS).

Brain = who the Captain is. Team = how the AI works. Machine = what makes money. Nothing personal goes here.

## Paths
Every path in these files is relative to the root of the repo `trevorcrane/epic-ai-os`: `team/01-laws.md`, `brain/04-voice/`, `rules/SITE-SHIP-LOOP.md`. A file that lives only on Elon's box is written "box only: <path>", relative to the box workspace folder. That is a source note, not a link: it cannot be opened from the repo. The repo is the source of truth; a box file is a working copy until it is committed.

## Map
- `team/01-laws.md` The 10 laws.
- `team/02-people/` The Captain and the other humans, with Slack member IDs.
- `team/03-bots/` One card per bot. Start at `team/03-bots/00-roster.md`.
- `team/04-seats/` The roles any bot can sit in: First Mate, Lead, Researcher, Builder, Reviewer, Scorekeeper.
- `team/05-handoffs/` How a job moves from ask to proof. Event-driven. [Trevor chat 2026-09-28]
- `team/06-talk/` How AI talks to the Captain, the team, clients, and in Slack. **Communication protocols start at `team/06-talk/04-protocols.md`**: every channel, its status, who talks to whom, and the escalation path.
- `team/TEAM-INDEX.md` Every file, one line each.
For a client copy, change only `team/02-people/`, `team/03-bots/`, `team/06-talk/01-captain-mode.md`, `team/06-talk/03-slack.md` (member IDs), `team/06-talk/04-protocols.md` to `team/06-talk/06-escalation.md`, and `team/06-talk/channels/`.

## Status and privacy words
- Each file has a status line: WORKING (draft in use, not approved) and a tag: private (team only) or public (safe to show outside). Every file in this folder is private.
- Open items use three labels, the same words as Robyn's team (Trevor set them 2026-10-02). The word CONFLICT is retired.
  - **needs decide**: a choice is still open, or two sources or rules disagree. A human picks. An AI never picks.
  - **confusion**: sources use different names or words for what may be the same thing. Ask before you act on it.
  - **clear up**: a small fix or check. Any AI may make it or propose it on a task.
- Also used: [ASSUMED] (an unconfirmed guess) and Q# (a question in `QUESTIONS.md`).
- Channel status words (LIVE, slow, broken) carry a date. Re-check before relying on one.
- No money figures or hour rates, no kids' birthdates, ages, or genders, no client or testimonial names, no full agent IDs, no private share links, no credentials in team files.

## Sources key (short names on the Sources lines)
| Short name | Where it is |
|---|---|
| repo/team/*.md (NAMES, ROLES, LAWS, LOOP, LEAD, TALK, FIRST-MATE, REVIEWER, CAPTAIN-MODE) and repo/machine/SYSTEMS.md | The Sep 27 2026 handoff repo the v0.1 draft was moved from. A source note only: it is not in epic-ai-os. |
| PROPOSED-STRUCTURE.md | `sources/` in the repo (PR #3) |
| Trevor chat 2026-09-28 | The chat that commissioned the v1 Brain and Team |
| Trevor's ask 2026-10-06 | Elon's brief for this v0.2 update |
| Elon brief | Same brief. Each brief fact used here is either checked against a file named next to it or marked unchecked. |
| Heartbeat log | box only: ops/tango-live-check/poll.log (Elon's Tango probes, Oct 6) |
| Voice call 2026-10-06 | Trevor and Elon, Oct 6, 8:35 to 9:28 AM ET (Grok Bot voice call records, box only) |
| Grok Bot product rule | How the Grok Bot app itself behaves (for example, draft cards). Not a fleet file. |
| AGENTS.md | Repo root. Wake order and the fleet laws list. |
| Wake plan | box only: ops/TANGO-INSTANT-WAKE-PLAN.md (v4, 2026-10-05) |
| Connect Tango done | box only: ops/CONNECT-TANGO-DONE.md |
| Tango live read | Read-only `GET /api/public/workers/agents`, Tue Oct 6 2026, 10:35 AM ET. The output was not saved, so treat statuses from it as unchecked. |
| Tango docs | https://tango.applayer.io/docs and /llms.txt (public) |
| Hermes rules | box only: robyn-brain/hermes-sop-2026-10-02/UNIVERSAL_HERMES_RULES.md |
| Reconnect plan | box only: ops/connector-health/RECONNECT-SYSTEM-PLAN-v1.md |
| Email map | box only: ops/EMAIL-MAP.md |
| Grok Bot OS | `fleet-os/GROKBOT_OS.md` |
| rules/<FILE>.md | `rules/` in the repo, including `rules/CURSOR-BOB-DISPATCH.md` |
| Profile <id> | box only: the Grok Bot agent profile with that ID prefix |
| Grok Bot voice call records | box only: Elon's voice call log |
| Robyn team | box only: robyn-brain/team/ (staged for `robyn/team/`, not in the repo yet) |
| PR #3 | https://github.com/trevorcrane/epic-ai-os/pull/3 |

## Open items for Trevor (v0.2)
1. needs decide: may Elon post in Slack directly, as your account, with the label? (Wake plan question 2.) `team/06-talk/channels/02-slack.md`
2. Decided 2026-10-11: keep both. `team/01-laws.md` holds the core 10 Epic Laws; `rules/` holds the fleet rules, each file its own source of truth (`decisions/2026-10-11-laws.md`).
3. needs decide: Codex git pushes when tasked (Sep 30) vs Bob for every repo build (Oct 6). `team/03-bots/04-chatgpt.md`
4. Decided 2026-10-11: Alfred stays parked. No Alfred card (`decisions/2026-10-11-parked-names.md`). The Grok Bot "Epic OS" profile still calls him "Codex First Mate".
5. needs decide: law 2 wording. Proposed addition: "Code in a GitHub repo goes straight to Bob instead (`team/03-bots/07-bob.md`)." Law 2 stays as written until Trevor says GO. The Bob rule already binds through `rules/CURSOR-BOB-DISPATCH.md`.
6. needs decide: where the Scorecard hour rate lives, now that it is out of team files. No number goes here.
7. needs decide: agent ID prefixes in card bodies. Keep them (they help routing), or move them to the Sources key only.
8. needs decide: Slack member IDs. Keep one table in `team/06-talk/channels/02-slack.md` and point to it from the other five files, or keep them inline.
9. confusion: "COO". Hermes "COO mode" is how a Hermes agent runs its own house. On this team that is the Lead seat of the Hermes house. Elon is the fleet orchestrator. Trevor decides only if he wants one fleet-wide COO title. `team/06-talk/channels/03-hermes.md`
10. clear up: ChatGPT has not replied since about 12:10 AM ET Oct 6 (heartbeat log). Its Runner was never installed.
11. clear up: something posts as Elon's worker and "Max" on the hourly Connection Test task.
12. Still open from v0.1: Q38 (`#_build-log` and the per-house channel names, and a yes on the duty owners in `team/05-handoffs/06-standing-loops.md`), Q39 (ChatGPT Lead name), Q40 (Tango event names, partly answered in `team/05-handoffs/04-events.md`). Q37 closed 2026-10-11 (`decisions/2026-10-11-approvals.md`).
