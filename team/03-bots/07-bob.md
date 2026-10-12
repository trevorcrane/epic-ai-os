# Bot card: Bob

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: rules/CURSOR-BOB-DISPATCH.md (box only: ops/rules/; not in the repo rules/ yet).

- **Harness:** Cursor cloud agent.
- **Seat:** Builder (code) for anything in a GitHub repo.
- **Dispatched by:** Elon, or any Grok Bot agent handing off build work. Not through Tango.
- **Rules:** every job is titled "Bob: <short task name>". Model `claude-opus-5-5` unless Trevor names another. Opens pull requests only, never merges. Every prompt includes "Open a pull request only. Do not merge."
- **Merge:** a human decides, or Reviewer per the site ship loop.
- **Sees:** the repo only, not the box. Content travels inside the prompt.
- **Not set up:** Bob on a Mac (self-hosted worker named `bob`). Waits for Len.
- Channel details: `team/06-talk/channels/04-cursor-bob.md`.
