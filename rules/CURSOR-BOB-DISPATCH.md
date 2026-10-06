# Build dispatch: Bob on Cursor (all Epic agents)

Locked 2026-10-06 by Trevor (voice). Owner: Elon. Covers Elon and every Grok Bot agent that hands off build work.

## Rule
1. Build requests (code, repo changes, app or site source in a GitHub repo) go straight to **Bob**, a Cursor cloud agent. Do not route them through Tango.
2. Every Bob job is titled `Bob: <short task name>` so it is easy to spot at https://cursor.com/agents.
3. Every Bob job uses model `claude-opus-5-5` (Claude Opus 5.5) unless Trevor names a different model for that job.
4. Bob only opens pull requests (change requests). Bob never merges. A human, or Reviewer per SITE-SHIP-LOOP.md, decides the merge.
5. Put this line in every Bob prompt: "Open a pull request only. Do not merge."

## How to launch (Grok Bot agents)
CloudAgent launch with: repo = full GitHub URL, model = claude-opus-5-5, title = "Bob: ...", prompt ending with "Open a pull request only. Do not merge."

## Out of scope
- Work outside a GitHub repo (Cloudflare Pages deploys, box files, docs) stays with the builder agents.
- Bob on a Mac (self-hosted worker named `bob`) is NOT set up. It waits for Len. Doc: https://cursor.com/docs/cloud-agent/self-hosted/my-machines

## Source docs
- Cursor Cloud Agents / Self-Hosted Machines: https://cursor.com/docs/cloud-agent/self-hosted
