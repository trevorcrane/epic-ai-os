# Source to target

Concepts reused. Identity, schedule, and host-install rows from the old packages were not migrated. `team/` was not replaced.

| Source | Target in this branch | Left behind |
|---|---|---|
| PR #2 `operating-system/agents/cat/LOAD.md`: exact commit, required file list, receipt fields, missing access named, known local version only with limitations disclosed, host adaptation | `context-load/loader.py` required list, `content_revision`, receipt, fail-closed missing revision or file, stale fallback only when an accepted record verifies | Cat identity, Alfred as job owner, squad workflow, scheduled wakeup, Ojoy, brand package |
| PR #2 `operating-system/adapters/ADOPTION.md`: per-host scope, remaining boundary, no claim that a URL is installation | Host table in the loader. `installation_claimed` is false. Write and send stay false | The Cat host rows and the install baseline SHA on that file |
| 2026-10-06 team receipt in `team/05-handoffs/01-how-a-job-moves.md`: summary, evidence artifacts, open questions | Receipt fields `summary`, `evidence` (path plus sha256), `open_questions` | No Tango `complete_task` call. No live handoff |
| PR #2 4C source: Clarity is asked as a question | Loader requires the question marker in `brain/05-messaging/06-four-cs.md` plus the names in `decisions/2026-10-11-four-cs.md` | The rest of the v5 kit was not copied |
| `decisions/2026-10-11-definition-of-done.md` | `definition_of_done` on the candidate release | A new `DEFINITION-OF-DONE.md` was not created |
| Saved Grok stack, first-mate card, sync plan | Same files, superseded lines marked, excluded from `current_instructions` | Those lines were not deleted |
| Archived contradictory sentences | `context-load/fixtures/` | They are not current instructions |

No Dot team overlay was in the baseline. None was added.
