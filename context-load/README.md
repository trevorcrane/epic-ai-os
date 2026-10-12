# Context load (preparation only)

This folder is a reviewable loader. It is not installed on a live agent. It does not designate an accepted release. A passing test is evidence about this process. It is not proof that a skill is installed or that the fleet has adopted a release.

## Records

| File | Role |
|---|---|
| releases/candidate.json | Candidate manifest for this branch. `accepted_release` is false. |
| releases/accepted.json | Accepted record. Status `none` until a human designates one. Not pointed at the candidate. |
| loader.py | Checks revision, hashes, bundle class, precedence, the 4C question, and capabilities. |
| test_loader.py | Isolated fail-closed tests, plus one load of this tree. |
| fixtures/ | Archived sentences that contradict scoped decisions. Excluded from current instructions. |

## What a load checks

1. Host is one of cursor, tango, grok, chatgpt, hermes, claude. Any other host fails closed.
2. Write and send are denied. A request that requires either one fails closed and does not grant read.
3. A blank revision fails closed.
4. The requested revision must match the sealed `content_revision`. That id is the sha256 of the manifest body (role, status, file hashes, precedence checks, the question flag, the definition-of-done path). It is not this commit's git SHA.
5. Every required file must exist and match its sha256. A missing file or a hash miss fails closed. The candidate is not half-loaded.
6. If the requested candidate revision is stale and `accepted.json` is a verified accepted release, the loader falls back to that release and says so. If no accepted release is recorded, it fails closed and does not load the candidate in its place.
7. Asking for the accepted role while status is `none` fails closed. The candidate is not substituted.
8. Current-bundle files become `current_instructions`. Marked superseded sections and preserved files stay in `excluded_stale`. A stale sentence inside a current file fails closed.
9. Scoped decision files win over the archived fixtures. The fixture path is not a current instruction.
10. The 4C names stay the scoped decision. The question form stays required: the Brain file's "Do you know why we're here?" marker. Dropping the question or the flag fails closed.
11. Definition of done is `decisions/2026-10-11-definition-of-done.md`. A missing `DEFINITION-OF-DONE.md` is not invented.

## Receipt

Job, agent identity (`epic-os-context-load-preparation`), worker id, host, repository, time, requested revision, loaded revision, paths, sha256 evidence, missing files, stale flag, fallback limitations, gaps, open questions, decision precedence, capabilities. `installation_claimed`, `skill_bodies_installed`, `live_agent_changed`, and `tests_are_adoption_proof` stay false.

Summary, evidence, and open questions follow the 2026-10-06 team handoff receipt. Exact revision and the required list follow PR #2 LOAD. Per-host denial of an install claim follows PR #2 ADOPTION. Cat identity, Alfred schedules, and host install rows were not copied.

## Run

```
python3 context-load/loader.py seal
python3 context-load/test_loader.py
```

Seal rewrites `releases/candidate.json` hashes after a manifest edit. It does not set an accepted release.
