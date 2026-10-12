# Events (what triggers what)

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: Trevor chat 2026-09-28 (event-driven handoffs), repo/team/LOOP.md, LEAD.md, Wake plan section 2 (Elon backlog export)

Handoffs are event-driven. [VERIFIED: Trevor via chat, 2026-09-28] A seat moves when an event fires on the task. No polling chatter, no "any update?" pings.
The events below are named from the loop in `team/05-handoffs/01-how-a-job-moves.md`. The event names are [ASSUMED]; the reactions are from the repo. Real Tango event names seen on Elon's worker (Oct 5 export): `message.received`, `task.assigned`, `task.mentioned`, `task.commented`, `task.handoff_received`, `context_updated`. The Tango docs (llms.txt) list these webhook events: `task.assigned`, `task.commented`, `task.mentioned`, `task.handoff_received`, `task.deadline_soon`. The rest of the names below are still [ASSUMED] (Q40).

| Event (on the Tango task) | Who reacts | What they do |
|---|---|---|
| Captain asks (Slack or chat) | First Mate | Makes the task. Picks the house. |
| task.created / task.assigned | That house's Lead | Claims it. Staffs it. Says the staffing on the task. |
| current state unknown | Researcher | FOUND / PARTIAL / MISSING with links. Gap in one line. |
| gap written | Builder | Smallest change that closes it. Plan first if over 60 minutes. |
| plan.posted | Reviewer | PLAN OK or PLAN FAIL plus one fix. |
| review.requested | Reviewer | Re-runs checks. PASS, FAIL, or BLOCKED with score. |
| review.fail | Builder | Fixes only what failed. Attempt n of 3. |
| review.pass | Scorekeeper, then Lead | Scorecard row. Lead completes (green) or asks for "done" (yellow, red). |
| blocked (ask_human) | Captain (or approver) | Picks 1, 2, or 3. Default fires at the stated time (never on red). |
| handoff to another house | Other Lead | Confirms on the task. No answer twice: First Mate tells the Captain. |
| Captain says "stop" | Every running task | Blocks with "STOP: Captain." |
| scheduled time (standing loop) | Loop owner | One row: time · observed · gap · act · result, or HOLDS. |
[VERIFIED reactions: LOOP.md, FIRST-MATE.md, LEAD.md, REVIEWER.md]
