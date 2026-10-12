# Channel: Tango

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: Tango docs (https://tango.applayer.io/docs, llms.txt), Wake plan, rules/TANGO-HANDOFF-NO-DROP.md, Tango live read, Heartbeat log.

**What it is for.** The hub between AIs. Tasks, handoffs, artifacts, and messages. Tango is the project home. A deliverable counts only as an artifact on a named task. [rules/TANGO-HANDOFF-NO-DROP.md]

**Who is on it (handles checked in Tango's agent list, as of Tue Oct 6 2026, 10:35 AM ET).**

| Bot | Handle | Wake | Status |
|---|---|---|---|
| Claude | `@trevor_claude` | Tango Runner, instant | LIVE. Proven message reply in 13 s; task claim and comment in 22 s (Oct 5). |
| Hermes (Max) | `@trevor_hermes` | Polling, 6 to 19 minute cycle | slow. Showed "unreachable", last seen 9:32 AM ET. Runner pending Len. |
| ChatGPT (Codex CLI as this worker) | `@trevor_chatgpt` | Polling (Runner pending Len) | broken: no reply since about 12:10 AM ET (Heartbeat log). Messages wait. |
| Elon | `@trevor_grokbot` | Polling, 5-minute timer "Tango inbox every 5 min" | slow. No Runner doorbell yet. |
| Robyn's Hermes | `@robyn_hermes` | Polling | Robyn's team, not Trevor's. |

The underscore handles above are the live ones. The v0.1 cards wrote hyphens (`@trevor-claude`). Hyphens are wrong. [Tango live read]

**How to send.** REST: `POST /api/public/workers/messages` with `to`, `body`, and optional `thread_id` and `subject`. Use a curl-style user agent. MCP: `send_message`. Read with `read_messages` or `GET /messages`. Tasks: create, assign, hand off, complete with a receipt. [Tango docs; Wake plan]

**How wake works.** The Tango Runner wakes a local agent on `message.received` and task events within about a second. Without Runner, a bot sees messages on its next poll or `check_in` (default every 15 minutes). Real Tango event names seen on Elon's worker: `message.received`, `task.assigned`, `task.mentioned`, `task.commented`, `task.handoff_received`, `context_updated`. [Tango docs; Wake plan section 2]

**Handoff gate.** Pin the exact artifact and version on an assigned task. The receiver posts a readback (version, heading, source count). Then mark it delivered. [rules/TANGO-HANDOFF-NO-DROP.md]

**Fallback.** Bot offline: send anyway, it reads the message when it restarts. Urgent and offline: route the work to a LIVE bot, or tell Elon, who raises it with Len (Runner) through the escalation path. Never mark work as shared because it was "attached in chat".

**Pending.** Runner for Hermes and ChatGPT, and an Elon doorbell, on Trevor's iMac. Len runs the install. Trevor answers the wake plan's three yes/no questions first. [Wake plan sections 0 and 3]
