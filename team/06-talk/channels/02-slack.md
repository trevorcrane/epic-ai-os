# Channel: Slack

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: Wake plan section 6, profile 780d10a7, team/06-talk/03-slack.md, Elon brief.

**What it is for.** Humans and alerts. Trevor, Len, Abi, Robyn, and the team. Bots do not chat with each other in Slack. (CONNECT-TANGO-DONE calls Slack the second place harnesses can talk; today that means bridged through Elon, not new bot identities.) [Robyn team 06-talk/03-slack.md; Wake plan S3; Connect Tango done]

**Who is on it.** Epic Media workspace. Primary Owner: Trevor. Admins include Len and Abi. Bot users: TC's GrokBot and Cursor. [Wake plan section 6]

**Member IDs.** Mentions by member ID only, written `<@U…>`. A typed "@Name" from an app notifies nobody, and the person must already be in the channel.

| Person | Write it as |
|---|---|
| Trevor Crane | `<@U52DALA3U>` |
| Len (she/her) | `<@U0759A73T50>` |
| Abi | `<@U08NURSTEUA>` |
| Robyn Crane | `<@UEAHASZNJ>` |

There is no Slack user named Elon, Max, or Claude. The v0.1 lines "Slack: @Elon" and "Slack: @Max" were wrong.

**Status (as of Tue Oct 6 2026, 10:35 AM ET).**
- Elon direct: broken. Elon's own Slack connection fails with `account_inactive`.
- Relay: Elon sends a Grok Bot message to TC's GrokBot, which posts the text unchanged and returns the permalink. Speed not measured yet.

**The label.** Shows as Trevor's account per the fleet brief. That is untested: wake plan check LT4 (Trevor's account or the bot user) has not run. The label applies either way. Every Elon post, relayed or direct, starts with this exact label:

`[From Elon / Grok Bot — not Trevor typing]`

A relayed bot answer reads `[From Elon / Grok Bot — not Trevor typing] Claude says: ...`. No other variants.

**Relay format.** One message per post: `RELAY TO SLACK | channel: #<channel> | post exactly the text between the markers, do not edit | >>> [label] <text with <@U…> mentions> <<<`. [Wake plan S2]

**How wake works (inbound).** Not live. Planned: a Slack-triggered Elon routine on the word "Elon" in one named channel, after Len or Abi types `/invite @Cursor` there. The routine skips messages that start with `[From `. Never poll Slack. [Wake plan S1]

**Fallback.** If TC's GrokBot raises an approval card, the relay fails silently after about 10 minutes. Then the message goes to Trevor in Elon's chat, and Trevor's wake plan question 2 (direct posting) comes back to him. needs decide (Trevor): may Elon post in Slack directly, as Trevor's account, with the label?
