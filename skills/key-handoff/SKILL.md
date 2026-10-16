---
name: key-handoff
description: Get an API key or token from Trevor or Len with one ask and one paste. Use whenever a job needs a key, token, password or login secret.
---
# Key handoff
1. Check first: is the env var already set? (`env | cut -d= -f1`). If yes, use it, ask nobody.
2. If you are not the bot that will use it, do not ask. Tell the owner bot (default Elon).
3. Ask once: key name, where to get it (exact page), and raise the masked secret box (SendToUser secret request, UPPER_SNAKE name). No links to paste sites, no "skip it," no second ask.
4. Holder (Trevor or Len) pastes once. Len: her own app chat with the bot; else she gives it to Trevor privately (never Slack) and he pastes.
5. Test it, then reply one line: "Got NAME, tested, works." Never print, log, file or repeat the value. If a key shows in plain text anywhere, say "rotate it" and redo step 3.
Full rule: rules/KEY-HANDOFF.md
