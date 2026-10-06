# Channel: the Grok Bot fleet

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: Wake plan S2 (Grok Bot docs), rules/SITE-SHIP-LOOP.md, profiles 9d733f0b, 72ecc9b0, 05524fd8, 26d46717, 780d10a7.

**What it is for.** Trevor's Grok Bot agents working together: Elon, the builders, Reviewer, the Cats, TC's GrokBot, and the rest of the roster (`team/03-bots/00-roster.md`).

**How they talk.**
- **SendToAgent:** one bot sends an asynchronous message to another. The receiver wakes, handles it, and can reply later.
- **Group chats:** several bots in one thread when a job needs more than two.
- Each bot-to-bot reply counts toward usage. One message per ask, no back-and-forth.

**Reviewer gate.** Builders build and ship. Writers write and never publish. Reviewer (agent ID starts 9d733f0b) scores the live thing and returns PASS, FAIL, or BLOCKED. Bar 95. Changes required means FAIL. Reviewer is the only bot that says a site is done. Trevor or Robyn accepts. [rules/SITE-SHIP-LOOP.md; rules/EPIC-FUNNEL-SOP.md]

**How wake works.** A SendToAgent message wakes the receiver right away. Routines wake on their timers or triggers.

**Status.** LIVE.

**Trap.** An approval card raised by work that came from another bot's message expires after about 10 minutes, and the action does not run. Work that needs approval goes to Trevor in chat, not through a bot chain. [Wake plan S2]

**Fallback.** A bot does not answer: Elon checks it, then routes the job to another bot in the same seat, never to a bot that would review its own build.
