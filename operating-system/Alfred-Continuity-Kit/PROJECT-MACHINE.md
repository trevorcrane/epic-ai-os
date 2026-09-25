# Epic Project Machine: small starter recipe
Version 1 | 2026-09-24 | Proposed practical adapter

This is a working setup recipe, not an installed app. The older Epic Project Machine specification remains a source for future product development.

For each project create one private folder with:
1. AGENTS.md (Codex) or pasted project instructions (ChatGPT/Claude), pointing to the shared current startup kit.
2. PROJECT-BRIEF.md copied from PROJECT-BRIEF-TEMPLATE.md, containing outcome, authority, acceptance criteria, current owner and module references.
3. HANDOFF.md with timestamped current state, evidence and next action. The job tracker stays authoritative when connected.
4. ARTIFACTS.md listing deliverables and review evidence. Store large assets separately.

Reference shared rules and Brain modules instead of duplicating them into every project. A platform using uploads requires dated snapshots and explicit replacement when changed. A platform with repository access should retrieve only needed files at the designated revision. Never promise an exact token count without measurement.

Start prompt:
> Alfred, initialize this project from the shared startup kit. Find existing work first. Define the result, load only relevant Brain modules, and assign one PM, a builder and a separate reviewer when supported. Record actual run receipts and the next checkpoint. Report missing tools or source access. Continue within existing authority.

Validation prompt:
> State your role, loaded file revisions, current job and production owner, last verified evidence, acceptance tests, reviewer identity, next action and any unavailable capability. Do not infer live service health from an old note.
