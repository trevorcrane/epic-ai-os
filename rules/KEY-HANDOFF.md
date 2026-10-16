# Key handoff (one path, fewest steps)
Approved by Trevor, Oct 15 2026. Applies to every bot and every AI (Grok Bot, Claude, ChatGPT, others).

1. **One asker.** Only the bot that will use the key asks (default owner: Elon). One message: key name, where to get it, one masked box. No links, no sites, no reversals.
2. **Holder pastes once into the masked secret box** in that bot's chat (Grok Bot: SendToUser secret request, saved as an env var like `SOCIAL_PLANNER_API_KEY`). Trevor or Len, whoever holds it. Len pastes in her own Grok Bot app chat with that bot if she has access; if not, she sends it to Trevor by phone/1Password share, never Slack, and Trevor pastes it.
3. **Bot confirms in one line:** "Got SOCIAL_PLANNER_API_KEY, tested, works." Never echo the value.
4. **Saved once for all bots.** Secret-box keys are stored by the platform, not on disk: they survived the Oct 15 box reset and every bot on the box can use them. Never save keys in files, notes, memory, Slack, email, docs or chat text (files were what the reset wiped).
5. **If a key is pasted anywhere in plain text:** the bot says "rotate it," the holder makes a new key and repeats step 2.

Other AIs (Claude, ChatGPT): use your app's own secrets/env setting the same way: one asker, one paste into a masked field, one-line confirm, never in chat.
