# Channel: Cursor / Bob

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: rules/CURSOR-BOB-DISPATCH.md (box only: ops/rules/; not in the repo rules/ yet).

**What it is for.** Build dispatch. Code, repo changes, and app or site source in a GitHub repo go straight to Bob, a Cursor cloud agent. Not through Tango.

**Who is on it.** Bob. Dispatched by Elon, or any Grok Bot agent that hands off build work.

**How it works.**
1. Every job is titled `Bob: <short task name>`, so it is easy to spot at cursor.com/agents.
2. Model `claude-opus-5-5` (Claude Opus 5.5), unless Trevor names another for that job.
3. Bob opens pull requests only. Bob never merges. A human, or Reviewer per the site ship loop, decides the merge.
4. Every Bob prompt includes: "Open a pull request only. Do not merge."
5. Bob cannot see the box. Anything Bob needs travels inside the prompt.

**How wake works.** A launch or a follow-up message starts the cloud run. Replies come back on the job.

**Status.** LIVE as a cloud agent. Bob on a Mac (self-hosted worker named `bob`) is not set up. It waits for Len.

**Out of scope.** Cloudflare Pages deploys, box files, and docs stay with the builder agents.

**Fallback.** Cloud job fails: report it to Elon with the job link. No direct GitHub writes by other bots as a workaround. [ASSUMED]
