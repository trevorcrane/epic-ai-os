# Source to target

Concepts reused. Identity, schedule, and host-install rows from the old packages were not migrated. `team/` was not replaced.

| Source | Target in this branch | Left behind |
|---|---|---|
| PR #2 `operating-system/agents/cat/LOAD.md`: exact commit, required file list, receipt fields, missing access named, known local version only with limitations disclosed, host adaptation | `context-load/loader.py` required list, `content_revision`, receipt, fail-closed missing revision or file, stale fallback only when an accepted record verifies | Cat identity, Alfred as job owner, squad workflow, scheduled wakeup, Ojoy, brand package |
| PR #2 `operating-system/adapters/ADOPTION.md`: per-host scope, remaining boundary, no claim that a URL is installation | Host table in the loader. `installation_claimed` is false. Write and send stay false | The Cat host rows and the install baseline SHA on that file |
| 2026-10-06 team receipt in `team/05-handoffs/01-how-a-job-moves.md`: summary, evidence artifacts, open questions | Receipt fields `summary`, `evidence` (path plus sha256), `open_questions` | No Tango `complete_task` call. No live handoff |
| PR #2 v5 core framework, section 3 Clarity: the imperative "Ask it as a question, not a conclusion." Provenance is the PR #2 file `operating-system/v5-4Cs-Source-Reference-2026-09-24.md` at `3dee9cb52e1d5cf291f192fd91d5bf06a15752ae`, source member `v5-4Cs-CoreFramework-2026-09-24.md` | `context-load/sources/v5-4c-clarity-instruction.md`. The loader requires that sentence, seals the source and the marker, and emits the sentence. The Brain example question is not the safeguard | The rest of the v5 kit was not copied. No owner-utterance message id was invented |
| Last-known accepted release | A sealed snapshot under `context-load/releases/snapshots/<id>/`. Fallback reads the snapshot when live paths later change | This tree has no accepted release and no snapshot |
| `decisions/2026-10-11-definition-of-done.md` | `definition_of_done` on the candidate release | A new `DEFINITION-OF-DONE.md` was not created |
| Saved Grok stack, first-mate card, sync plan | Same files, superseded lines marked, excluded from `current_instructions` | Those lines were not deleted |
| Archived contradictory sentences | `context-load/fixtures/` | They are not current instructions |

No Dot team overlay was in the baseline. None was added.
