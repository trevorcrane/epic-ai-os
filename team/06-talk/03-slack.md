# Slack rules

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: repo/team/TALK.md, Wake plan section 6, Profile 780d10a7, Trevor chat 2026-09-28.

1. @mention or it did not happen. **Bots mention people by Slack member ID, written `<@U…>`.** A typed "@Name" from an app notifies nobody, and the person must already be in the channel.
2. One topic, one thread. Stay in the thread the job started in.
3. A job reports in the thread it started in. The Captain's inbox (`team/02-people/01-captain.md`) is for what did not start in a thread: decisions, the weekly 1-3-1, the 7am Scorecard line, and a BLOCKED nobody answered in its thread by the default time. One thread per item.
4. The Captain decides. The Captain does not execute. Exception: the two-minute check.
5. Versions, never "final." The Captain owns the word.
6. Memory saves are confirmed in-thread: "Saved: <what>."
7. Agents coordinate through the task, not bot-to-bot chatter. Only the Lead posts job events.
8. Under ten lines. Commands in code blocks. No model names, token counts, or error codes to humans unless asked.
9. Messages in short numbered bites. [Trevor chat 2026-09-28]

## Elon's relay
Elon's own Slack is broken (`account_inactive`). Elon reaches humans in Slack through TC's GrokBot (`team/03-bots/08-tcs-grokbot.md`). Shows as Trevor's account per the fleet brief. That is untested: wake plan check LT4 (Trevor's account or the bot user) has not run. The label applies either way. **Every Elon post, relayed or direct, starts with this exact label:**

`[From Elon / Grok Bot — not Trevor typing]`

A relayed bot answer reads `[From Elon / Grok Bot — not Trevor typing] Claude says: ...`. No other variants. [Wake plan section 6]

## Member IDs (Epic Media workspace, checked read-only 2026-10-05)
| Person | Write it as |
|---|---|
| Trevor Crane | `<@U52DALA3U>` |
| Len (she/her) | `<@U0759A73T50>` |
| Abi | `<@U08NURSTEUA>` |
| Robyn Crane | `<@UEAHASZNJ>` |

To add someone: their Slack profile, then the three dots, then Copy member ID.

Channel status, wake, and fallback: `team/06-talk/channels/02-slack.md`.
