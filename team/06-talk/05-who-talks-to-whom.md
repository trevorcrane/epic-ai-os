# Who talks to whom

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: Wake plan, rules/TANGO-HANDOFF-NO-DROP.md, rules/CURSOR-BOB-DISPATCH.md, rules/SITE-SHIP-LOOP.md, Email map, profiles 780d10a7 and 9d733f0b, Elon brief.

| From | To | Channel | How | Notes |
|---|---|---|---|---|
| Trevor | Elon | Grok Bot chat or voice call | Talks or types | Elon is First Mate when Trevor talks to him. |
| Trevor | Claude, ChatGPT, Hermes | Their own apps, or Tango | Direct | Their chats are scratch until the work lands in Tango. |
| Elon | Claude, ChatGPT, Hermes | Tango | Message to the @handle, or an assigned task | Work goes on a task. A question can go as a message. |
| Claude, ChatGPT, Hermes | Elon | Tango | Message or task to @trevor_grokbot | Elon picks it up on his 5-minute timer. |
| Claude, ChatGPT, Hermes | each other | Tango | Message or task | Same rules: no ACK chatter. |
| Elon | Grok Bot agents (Builder: Sites, Builder: Robyn, Reviewer, Cat: Trevor, and others) | Grok Bot | SendToAgent message, or a group chat | One message per ask. Each reply counts toward usage. |
| Elon or any Grok Bot agent | Bob | Cursor cloud agent | Launch or reply, title "Bob: ..." | Prompt ends "Open a pull request only. Do not merge." |
| Bob | humans | GitHub | A pull request | Bob never merges. A human, or Reviewer per the site ship loop, decides. |
| Writer (Cat: Trevor and other Cats) | Builder | Grok Bot handoff | The handoff names the writer | Writers never publish. |
| Builder | Reviewer | Grok Bot | Hand the live URL or file | Builder never calls it done. |
| Reviewer | Trevor (through Elon) | Grok Bot, then chat or Slack relay | PASS, FAIL, or BLOCKED with a score | Reviewer is the only bot that says a site is done. Trevor or Robyn accepts. |
| Elon | Trevor, Len, Abi, Robyn | Slack via TC's GrokBot | Relay with the label and member IDs | Elon's own Slack is broken. |
| Len, Abi | Elon | Slack, or Tango | Today: through Trevor or a Tango task. Planned: the word "Elon" in one named channel wakes a routine. | The Slack trigger is not live yet (wake plan S1). |
| Any bot | outside people | none without Trevor's OK | Email goes as a draft card | `team/06-talk/channels/08-email.md` |
| Codex | GitHub | git push when tasked | (Sep 30 rule) | needs decide (Trevor): the Oct 6 Bob rule sends repo builds to Bob. See `team/03-bots/04-chatgpt.md`. |

Label on anything Elon posts in Slack, relayed or direct: `[From Elon / Grok Bot — not Trevor typing]`. Whether the relay shows as Trevor's account is untested (`team/03-bots/08-tcs-grokbot.md`).
