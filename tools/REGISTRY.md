# Fleet Tool Registry
Check here before building, buying or installing any tool. Rules: /workspace/ops/rules/TOOL-ROLLOUT.md
Status: works (verified run), testing (runs but not fully proven), broken. Last verified 2026-10-15 by dr eggbot.

| Tool | What it does | How to run (exact) | Owner | Status | Added |
|---|---|---|---|---|---|
| transcript.sh | Gets a video transcript. Uses Trevor's Epic Machines transcriber (epicmachines.ai/transcribe) first, YouTube captions as fallback. Fleet default before any paid service. Exit 2 = failed, never guess. | `bash /workspace/merlin/bin/transcript.sh "<url>" -o /tmp/out.txt` | Merlin | works (live YouTube test 2026-10-15, exit 0) | 2026-10-15 |
| book-title-check | Checks book titles against Open Library listings and USPTO trademarks; prints OPEN / TAKEN / CLOSE. | `python3 /workspace/skill-library/book-title-check/check.py "Title One" "Title Two"` | dr eggbot | works (live run 2026-10-15) | 2026-10-15 |
| nightly-backup.sh | Copies key box folders (no secrets, secret scan on) to the Origin repo epic-team/epic-box-backup. | `bash /workspace/ops/backup/nightly-backup.sh` | dr eggbot | testing (builds and commits locally; push blocked, no Origin git login on box) | 2026-10-15 |
| idea.sh / idea.py | Logs and updates ideas in the Epic Idea Machine (add, update, list, show, top5, archive-stale). | `bash /workspace/merlin/bin/idea.sh list` (see `--help`) | Merlin | works (--help 2026-10-15) | 2026-10-15 |
| skill-library build.py | Rebuilds SKILL-LIBRARY.md/.html and skills.json from the skill list. | `cd /workspace/skill-library && python3 build.py` | dr eggbot | works (ran 2026-10-15) | 2026-10-15 |
| vtt2txt.py | Turns a .vtt caption file into clean plain text. | `python3 /workspace/bot-studio/voice-sources/vtt2txt.py <file.vtt>` | Bot Studio | testing (needs a real .vtt; no --help) | 2026-10-15 |
| tango-elon inbox.py | Reads Elon's Tango threads and unread messages. | `python3 /workspace/ops/tango-elon/inbox.py` | Elon | testing (reads; exited 120 at end of output) | 2026-10-15 |
| tango-live-check scripts | Tango polling and heartbeat checks (poll.py, poll_tasks.py, hbpoll.py, hb.py, check.py, recent.py, mcp.sh). | `python3 /workspace/ops/tango-live-check/<script>.py` | Elon | testing (not re-run 2026-10-15, they post/poll live) | 2026-10-15 |
| verify_len_page.py | Checks Len's page against expected blocks. | `python3 /workspace/ops/verify_len_page.py` | dr eggbot | broken (hung past 15s on --help 2026-10-15) | 2026-10-15 |
| shot (cyc.js) | Puppeteer screenshots of a site at set sizes (URL hardcoded, copy and edit). | `node /workspace/tools/shot/cyc.js` | Builder | testing (one-off, hardcoded URL) | 2026-10-15 |
