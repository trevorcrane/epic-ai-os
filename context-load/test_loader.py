#!/usr/bin/env python3
"""Isolated tests for the preparation context loader.

A pass is evidence about this process. It is not proof of an installed skill,
a live fleet load, or an accepted release.
"""

from __future__ import annotations

import json
import os
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from loader import (  # noqa: E402
    ACCEPTED_REL,
    CANDIDATE_REL,
    FOUR_CS_INSTRUCTION,
    MANDATORY_WAKE_PATHS,
    SCHEMA,
    load_context,
    seal_release,
    sha256_bytes,
    sha256_file,
)

ROOT = Path(__file__).resolve().parents[1]

# Rejected attribution matcher. Not an instruction.
REJECTED_LINE = "Automate everything but the love."

FOUR_CS_PROVENANCE = (
    "Verbatim instruction from PR #2 file "
    "operating-system/v5-4Cs-Source-Reference-2026-09-24.md "
    "at commit 3dee9cb52e1d5cf291f192fd91d5bf06a15752ae. "
    "Source member v5-4Cs-CoreFramework-2026-09-24.md section 3. Clarity. "
    "No owner-utterance message id is recorded here. Do not invent one."
)

FLEET_LAWS = [
    "rules/PLAN-BUILD-USE.md",
    "rules/VERIFY-BEFORE-YOU-CLAIM.md",
    "rules/EDITABLE-GOOGLE-DOCS.md",
    "rules/TANGO-HANDOFF-NO-DROP.md",
    "rules/FOLLOW-PUBLISHED-DOCS.md",
    "rules/CTA-NEW-TAB.md",
    "rules/EPIC-FUNNEL-SOP.md",
    "rules/CLOUDFLARE-PAGES-STANDARD.md",
    "rules/LAUNCH-QC-CHECKLIST.md",
    "rules/LOOK-BEFORE-YOU-ASK.md",
    "rules/SITE-SHIP-LOOP.md",
    "rules/CURSOR-BOB-DISPATCH.md",
]


def _write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _annotate(release: dict) -> dict:
    order = 1
    for item in release["required"]:
        if item.get("scope") == "on_demand":
            continue
        if item.get("bundle") in ("current", "mixed"):
            item["scope"] = "wake"
            item["order"] = order
            order += 1
        else:
            item["scope"] = "record"
    return release


def _four_cs_fields() -> dict:
    return {
        "four_cs_question_required": True,
        "four_cs_question_source": "context-load/sources/v5-4c-clarity-instruction.md",
        "four_cs_question_marker": FOUR_CS_INSTRUCTION,
        "four_cs_provenance": FOUR_CS_PROVENANCE,
    }


def _fixture_files() -> dict[str, str]:
    files = {
        "decisions/task.md": (
            "Decision: Tango is the project home for now. "
            "Linear is not the system of record.\n"
            + REJECTED_LINE
            + "\n"
        ),
        "decisions/mate.md": "The First Mate is whichever AI Trevor is talking to.\n",
        "decisions/alfred.md": "Alfred stays parked and there is no Alfred card.\n",
        "decisions/dod.md": "Problem, Result, Who: owner and QC, What, By when, plus proof.\n",
        "decisions/four.md": "The 4 C's are Connect, Care, Clarity, Call to Action.\n",
        "decisions/approvals.md": "Anything to clients waits for Trevor to press Send.\n",
        "brain/four-cs.md": 'Clarity example only: "Do you know why we\'re here?"\n',
        "context-load/sources/v5-4c-clarity-instruction.md": (
            FOUR_CS_INSTRUCTION + "\n\n" + FOUR_CS_PROVENANCE + "\n"
        ),
        "rules/plan.md": "Fixture fleet law. No code words in this isolated file.\n",
        "context-load/fixtures/archived-linear-is-sor.md": (
            "<!-- context-bundle: preserved-superseded -->\n"
            "Linear wins on conflicts.\n"
        ),
        "context-load/fixtures/archived-fixed-first-mate.md": (
            "<!-- context-bundle: preserved-superseded -->\n"
            "Chief of Staff + Grok Operator (combined for now)\n"
        ),
        "context-load/fixtures/archived-alfred-active.md": (
            "<!-- context-bundle: preserved-superseded -->\n"
            "Push the roster with Alfred added.\n"
        ),
        "mixed/os.md": (
            "# OS\n"
            "<!-- context-bundle: preserved-superseded -->\n"
            "Chief of Staff + Grok Operator (combined for now)\n"
            "Linear Fleet DoD\n"
            "<!-- /context-bundle -->\n"
            "## Fleet Laws\n"
            "## Decided 2026-10-11\n"
        ),
        "review/bar.md": "PROPOSED, not approved\n\nOriginal stays. Choice unresolved.\n",
        "review/map.md": "Review artifact. Not a wake instruction.\n",
    }
    for rel in MANDATORY_WAKE_PATHS:
        files[rel] = f"Mandatory wake stub for {rel}.\n"
    return files


def _release() -> dict:
    release = {
        "schema": SCHEMA,
        "role": "candidate",
        "status": "candidate",
        "accepted_release": False,
        "definition_of_done": "decisions/dod.md",
        "gaps": ["no-accepted-release"],
        "open_questions": ["reviewer-bar-unresolved"],
        "required": [
            {"path": "decisions/task.md", "bundle": "current"},
            {"path": "decisions/mate.md", "bundle": "current"},
            {"path": "decisions/alfred.md", "bundle": "current"},
            {"path": "decisions/dod.md", "bundle": "current"},
            {"path": "decisions/four.md", "bundle": "current"},
            {"path": "decisions/approvals.md", "bundle": "current"},
            {"path": "brain/four-cs.md", "bundle": "current", "scope": "on_demand"},
            {
                "path": "context-load/sources/v5-4c-clarity-instruction.md",
                "bundle": "current",
            },
            {"path": "rules/plan.md", "bundle": "current", "scope": "on_demand"},
            {
                "path": "context-load/fixtures/archived-linear-is-sor.md",
                "bundle": "preserved-superseded",
                "must_contain": ["Linear wins on conflicts"],
            },
            {
                "path": "context-load/fixtures/archived-fixed-first-mate.md",
                "bundle": "preserved-superseded",
                "must_contain": ["Chief of Staff + Grok Operator (combined for now)"],
            },
            {
                "path": "context-load/fixtures/archived-alfred-active.md",
                "bundle": "preserved-superseded",
                "must_contain": ["with Alfred added"],
            },
            {
                "path": "mixed/os.md",
                "bundle": "mixed",
                "excluded_markers": [
                    "Chief of Staff + Grok Operator (combined for now)",
                    "Linear Fleet DoD",
                ],
                "current_markers": ["## Fleet Laws", "## Decided 2026-10-11"],
            },
            {"path": "review/bar.md", "bundle": "proposal"},
            {"path": "review/map.md", "bundle": "review"},
            *[{"path": rel, "bundle": "current"} for rel in MANDATORY_WAKE_PATHS],
        ],
        "precedence_checks": [
            {
                "id": "task-home",
                "decision": "decisions/task.md",
                "fixture": "context-load/fixtures/archived-linear-is-sor.md",
                "decision_marker": "not the system of record",
                "fixture_marker": "Linear wins on conflicts",
            },
            {
                "id": "first-mate",
                "decision": "decisions/mate.md",
                "fixture": "context-load/fixtures/archived-fixed-first-mate.md",
                "decision_marker": "whichever AI Trevor is talking to",
                "fixture_marker": "Chief of Staff + Grok Operator (combined for now)",
            },
            {
                "id": "alfred",
                "decision": "decisions/alfred.md",
                "fixture": "context-load/fixtures/archived-alfred-active.md",
                "decision_marker": "no Alfred card",
                "fixture_marker": "with Alfred added",
            },
        ],
    }
    release.update(_four_cs_fields())
    return _annotate(release)


def _accepted_none() -> dict:
    return {
        "schema": SCHEMA,
        "role": "accepted",
        "status": "none",
        "accepted_release": False,
        "content_revision": None,
        "required": [],
        "note": "No accepted release.",
    }


def _acceptance() -> dict:
    return {
        "accepted_by": "isolated-test-fixture",
        "accepted_at": "2026-10-12T00:00:00Z",
        "evidence": "temporary tree only; not a Trevor approval",
    }


def _plant(root: Path, release: dict | None = None, accepted: dict | None = None) -> str:
    for rel, text in _fixture_files().items():
        _write(root, rel, text)
    sealed = seal_release(release or _release(), root)
    _write(root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
    _write(root, ACCEPTED_REL, json.dumps(accepted or _accepted_none(), indent=2) + "\n")
    return sealed["content_revision"]


def _request(revision: str, **extra) -> dict:
    base = {
        "job": "prep-test",
        "worker_id": "test-worker",
        "host": "cursor",
        "expected_revision": revision,
        "release_role": "candidate",
        "now": "2026-10-12T03:30:00Z",
    }
    base.update(extra)
    return base


def _bundle(receipt: dict) -> str:
    return receipt["context"]["instruction_text"]


def _paths(receipt: dict) -> list[str]:
    return [row["path"] for row in receipt["context"]["instructions"]]


class LoaderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.revision = _plant(self.root)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_candidate_load_emits_instructions_and_omits_stale_text(self) -> None:
        receipt = load_context(self.root, _request(self.revision))
        self.assertEqual(receipt["status"], "loaded")
        self.assertFalse(receipt["accepted_release"])
        self.assertEqual(receipt["capabilities"], {"read": True, "write": False, "send": False})
        self.assertFalse(receipt["installation_claimed"])
        self.assertFalse(receipt["skill_bodies_installed"])
        self.assertFalse(receipt["tests_are_adoption_proof"])
        self.assertTrue(receipt["four_cs_question_present"])
        self.assertEqual(receipt["four_cs_instruction"], FOUR_CS_INSTRUCTION)
        self.assertEqual(receipt["definition_of_done"], "decisions/dod.md")
        self.assertEqual(receipt["time"], "2026-10-12T03:30:00Z")
        blob = _bundle(receipt)
        self.assertIn("not the system of record", blob)
        self.assertIn("whichever AI Trevor is talking to", blob)
        self.assertIn("no Alfred card", blob)
        self.assertIn("Problem, Result", blob)
        self.assertIn("press Send", blob)
        self.assertIn(FOUR_CS_INSTRUCTION, blob)
        self.assertIn("## Decided 2026-10-11", blob)
        self.assertNotIn("Linear wins on conflicts", blob)
        self.assertNotIn("Chief of Staff + Grok Operator (combined for now)", blob)
        self.assertNotIn("with Alfred added", blob)
        self.assertNotIn("Linear Fleet DoD", blob)
        self.assertNotIn(REJECTED_LINE, blob)
        self.assertNotIn("Do you know why we're here?", blob)
        self.assertTrue(receipt["withheld_rejections"])
        self.assertEqual(
            receipt["withheld_rejections"][0]["pointer"],
            "decisions/2026-10-11-false-quotes-removed.md",
        )
        self.assertEqual(receipt["withheld_rejections"][0]["owner_utterance"], "unresolved")
        digest = sha256_bytes(blob.encode("utf-8"))
        self.assertEqual(receipt["context"]["instruction_sha256"], digest)
        self.assertEqual(receipt["context"]["host"], "cursor")
        self.assertFalse(receipt["context"]["installation_claimed"])
        self.assertIn("not the system of record", receipt["current_instructions"][0])
        paths = _paths(receipt)
        self.assertEqual(
            [row["id"] for row in receipt["decision_precedence"]],
            ["alfred", "first-mate", "task-home"],
        )
        for row in receipt["decision_precedence"]:
            self.assertIn(row["winner"], paths)
            self.assertNotIn(row["loser"], paths)
            self.assertFalse(row["loser_in_current_instructions"])
        self.assertIn("mixed/os.md", paths)
        self.assertIn("mixed/os.md#preserved-superseded", receipt["excluded_stale"])
        self.assertIn("review/bar.md", receipt["proposals"])
        self.assertNotIn("review/bar.md", paths)
        self.assertNotIn("rules/plan.md", paths)
        self.assertNotIn("No code words in this isolated file.", blob)
        self.assertTrue(receipt["evidence"])
        self.assertIn("reviewer-bar-unresolved", receipt["open_questions"])
        self.assertIn("disputed-attributions-withheld", receipt["gaps"])

    def test_on_demand_resolution_uses_declared_hashes_only(self) -> None:
        base = load_context(self.root, _request(self.revision))
        resolved = load_context(
            self.root, _request(self.revision, on_demand=["rules/plan.md"])
        )
        self.assertEqual(resolved["status"], "loaded", resolved.get("fail_reason"))
        self.assertIn("No code words in this isolated file.", _bundle(resolved))
        self.assertEqual(resolved["on_demand_resolved"], ["rules/plan.md"])
        self.assertNotEqual(
            base["context"]["instruction_sha256"],
            resolved["context"]["instruction_sha256"],
        )
        self.assertEqual(
            resolved["context"]["instruction_sha256"],
            sha256_bytes(_bundle(resolved).encode("utf-8")),
        )
        missing = load_context(
            self.root, _request(self.revision, on_demand=["not/declared.md"])
        )
        self.assertEqual(missing["fail_reason"], "on_demand_not_declared")
        self.assertEqual(missing["context"]["instructions"], [])
        self.assertNotIn("not/declared.md", missing["paths_read"])

    def test_missing_revision_fails_closed(self) -> None:
        receipt = load_context(self.root, _request("  "))
        self.assertEqual(receipt["status"], "failed_closed")
        self.assertEqual(receipt["fail_reason"], "missing_revision")
        self.assertEqual(receipt["capabilities"]["read"], False)
        self.assertEqual(receipt["current_instructions"], [])
        self.assertEqual(receipt["context"]["instructions"], [])
        self.assertFalse(receipt["fallback_used"])

    def test_missing_file_fails_closed(self) -> None:
        (self.root / "decisions/dod.md").unlink()
        receipt = load_context(self.root, _request(self.revision))
        self.assertEqual(receipt["status"], "failed_closed")
        self.assertEqual(receipt["fail_reason"], "missing_file")
        self.assertIn("decisions/dod.md", receipt["missing_files"])
        self.assertEqual(receipt["current_instructions"], [])
        self.assertEqual(receipt["capabilities"]["read"], False)
        self.assertFalse(receipt["fallback_used"])

    def test_stale_without_accepted_release_fails_closed(self) -> None:
        receipt = load_context(self.root, _request("0" * 64))
        self.assertEqual(receipt["status"], "failed_closed")
        self.assertEqual(receipt["fail_reason"], "stale")
        self.assertTrue(receipt["stale"])
        self.assertFalse(receipt["fallback_used"])
        self.assertIn("No last-known accepted release", receipt["fallback_limitations"])
        self.assertEqual(receipt["current_instructions"], [])
        self.assertFalse(receipt["accepted_release"])

    def _snapshot_shared_paths(self, snapshot_root: str) -> None:
        release = _release()
        for item in release["required"]:
            src = self.root / item["path"]
            dest = self.root / snapshot_root / item["path"]
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(src.read_bytes())

    def _plant_accepted(self, **overrides) -> dict:
        """Accepted release over the same logical paths as the candidate.

        Bytes are sealed in a snapshot. Later edits to the live paths do not
        change this record.
        """
        snap = "context-load/releases/snapshots/last-known"
        self._snapshot_shared_paths(snap)
        accepted = _release()
        accepted["role"] = "accepted"
        accepted["status"] = "accepted"
        accepted["accepted_release"] = True
        accepted["acceptance"] = _acceptance()
        accepted["snapshot_root"] = snap
        accepted["gaps"] = ["fallback-fixture-only"]
        accepted["open_questions"] = []
        accepted.update(overrides)
        return seal_release(accepted, self.root)

    def test_stale_falls_back_to_snapshot_after_shared_paths_change(self) -> None:
        accepted = self._plant_accepted()
        _write(self.root, ACCEPTED_REL, json.dumps(accepted, indent=2) + "\n")
        live = self.root / "decisions/task.md"
        live.write_text(
            "Linear is not the system of record. LIVE-PATH-MUTATION\n",
            encoding="utf-8",
        )
        self.assertNotEqual(
            sha256_file(live),
            sha256_file(self.root / accepted["snapshot_root"] / "decisions/task.md"),
        )
        receipt = load_context(self.root, _request("0" * 64))
        self.assertEqual(receipt["status"], "fallback", receipt.get("fail_reason"))
        self.assertTrue(receipt["fallback_used"])
        self.assertTrue(receipt["stale"])
        self.assertEqual(receipt["loaded_revision"], accepted["content_revision"])
        self.assertNotEqual(receipt["loaded_revision"], self.revision)
        self.assertTrue(receipt["accepted_release"])
        self.assertEqual(receipt["release_role_loaded"], "accepted")
        self.assertEqual(receipt["snapshot_root"], accepted["snapshot_root"])
        self.assertEqual(receipt["capabilities"], {"read": True, "write": False, "send": False})
        self.assertIn("sealed snapshot", receipt["fallback_limitations"])
        self.assertIn("decisions/task.md", _paths(receipt))
        blob = _bundle(receipt)
        self.assertIn("not the system of record", blob)
        self.assertNotIn("LIVE-PATH-MUTATION", blob)
        self.assertNotIn("Linear wins on conflicts", blob)
        self.assertIn(FOUR_CS_INSTRUCTION, blob)
        self.assertEqual(
            receipt["path_hashes"]["decisions/task.md"],
            sha256_file(self.root / accepted["snapshot_root"] / "decisions/task.md"),
        )
        self.assertFalse(receipt["installation_claimed"])

    def test_accepted_role_does_not_substitute_the_candidate(self) -> None:
        receipt = load_context(self.root, _request(self.revision, release_role="accepted"))
        self.assertEqual(receipt["status"], "failed_closed")
        self.assertEqual(receipt["fail_reason"], "missing_revision")
        self.assertFalse(receipt["accepted_release"])
        self.assertIsNone(receipt["release_role_loaded"])

    def test_candidate_copied_onto_accepted_fails_closed(self) -> None:
        candidate = json.loads((self.root / CANDIDATE_REL).read_text(encoding="utf-8"))
        required_paths = {item["path"] for item in candidate["required"]}
        self.assertNotIn(ACCEPTED_REL, required_paths)
        _write(self.root, ACCEPTED_REL, json.dumps(candidate, indent=2) + "\n")
        receipt = load_context(
            self.root,
            _request(candidate["content_revision"], release_role="accepted"),
        )
        self.assertEqual(receipt["status"], "failed_closed")
        self.assertEqual(receipt["fail_reason"], "accepted_role_mismatch")
        self.assertIsNone(receipt["release_role_loaded"])
        self.assertNotEqual(receipt["release_role_loaded"], "candidate")
        self.assertFalse(receipt["accepted_release"])
        self.assertFalse(receipt["capabilities"]["read"])
        self.assertEqual(receipt["context"]["instructions"], [])
        self.assertNotIn("not the system of record", _bundle(receipt))

    def test_accepted_record_rejects_bad_status_flag_and_missing_evidence(self) -> None:
        cases = [
            ({"role": "candidate"}, "accepted_role_mismatch"),
            ({"status": "candidate"}, "accepted_status_mismatch"),
            ({"accepted_release": False}, "accepted_flag_missing"),
            ({"acceptance": None}, "acceptance_evidence_missing"),
            ({"acceptance": {"accepted_by": "", "accepted_at": "t", "evidence": "e"}}, "acceptance_evidence_missing"),
        ]
        for overrides, reason in cases:
            accepted = self._plant_accepted(**overrides)
            _write(self.root, ACCEPTED_REL, json.dumps(accepted, indent=2) + "\n")
            receipt = load_context(
                self.root,
                _request(accepted["content_revision"], release_role="accepted"),
            )
            self.assertEqual(receipt["fail_reason"], reason, overrides)
            self.assertEqual(receipt["status"], "failed_closed")
            self.assertEqual(receipt["context"]["instructions"], [])
            self.assertFalse(receipt["accepted_release"])

    def test_fallback_without_acceptance_evidence_does_not_load_candidate(self) -> None:
        accepted = self._plant_accepted(acceptance=None)
        _write(self.root, ACCEPTED_REL, json.dumps(accepted, indent=2) + "\n")
        receipt = load_context(self.root, _request("0" * 64))
        self.assertEqual(receipt["fail_reason"], "acceptance_evidence_missing")
        self.assertFalse(receipt["fallback_used"])
        self.assertNotIn("decisions/task.md", _paths(receipt))
        self.assertNotIn("accepted/task.md", _paths(receipt))

    def test_send_and_write_are_denied(self) -> None:
        for flag in ("require_send", "require_write"):
            receipt = load_context(self.root, _request(self.revision, **{flag: True}))
            self.assertEqual(receipt["fail_reason"], "capability_denied", flag)
            self.assertEqual(
                receipt["capabilities"], {"read": False, "write": False, "send": False}
            )

    def test_unknown_host_fails_closed(self) -> None:
        receipt = load_context(self.root, _request(self.revision, host="alfred-runtime"))
        self.assertEqual(receipt["fail_reason"], "unknown_host")

    def test_removing_only_the_example_sentence_keeps_the_original_instruction(self) -> None:
        _write(self.root, "brain/four-cs.md", "Clarity, stated as a conclusion.\n")
        sealed = seal_release(_release(), self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["status"], "loaded", receipt.get("fail_reason"))
        self.assertIn(FOUR_CS_INSTRUCTION, _bundle(receipt))
        self.assertNotIn("Do you know why we're here?", _bundle(receipt))

    def test_altering_the_original_instruction_fails_closed(self) -> None:
        _write(
            self.root,
            "context-load/sources/v5-4c-clarity-instruction.md",
            "Ask it as a conclusion, not a question.\n\n" + FOUR_CS_PROVENANCE + "\n",
        )
        sealed = seal_release(_release(), self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "four_cs_instruction_missing")
        self.assertEqual(receipt["context"]["instructions"], [])

    def test_replacing_the_marker_with_the_example_fails_even_after_reseal(self) -> None:
        release = _release()
        release["four_cs_question_marker"] = "Do you know why we're here?"
        release["four_cs_question_source"] = "brain/four-cs.md"
        for item in release["required"]:
            if item["path"] == "brain/four-cs.md":
                item["scope"] = "wake"
                item["order"] = 50
        sealed = seal_release(release, self.root)
        self.assertNotEqual(sealed["content_revision"], self.revision)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        stale = load_context(self.root, _request(self.revision))
        self.assertEqual(stale["fail_reason"], "stale")
        replaced = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(replaced["fail_reason"], "four_cs_instruction_replaced")
        self.assertEqual(replaced["context"]["instructions"], [])

    def test_dropping_the_question_requirement_flag_fails_closed(self) -> None:
        release = _release()
        release["four_cs_question_required"] = False
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "four_cs_requirement_dropped")

    def test_unsealed_source_or_marker_change_invalidates_the_revision(self) -> None:
        stored = json.loads((self.root / CANDIDATE_REL).read_text(encoding="utf-8"))
        stored["four_cs_question_source"] = "decisions/four.md"
        stored["four_cs_question_marker"] = "Connect, Care, Clarity, Call to Action."
        _write(self.root, CANDIDATE_REL, json.dumps(stored, indent=2) + "\n")
        receipt = load_context(self.root, _request(self.revision))
        self.assertEqual(receipt["fail_reason"], "hash_mismatch")
        self.assertEqual(receipt["context"]["instructions"], [])
        self.assertNotIn("decisions/four.md", receipt["paths_read"])

    def test_source_outside_the_manifest_fails_closed_without_reading_it(self) -> None:
        secret = "unhashed-source-secret-token"
        _write(self.root, "loose.md", FOUR_CS_INSTRUCTION + "\n" + secret + "\n")
        release = _release()
        release["four_cs_question_source"] = "loose.md"
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "four_cs_source_unhashed")
        self.assertNotIn("loose.md", receipt["paths_read"])
        self.assertNotIn(secret, _bundle(receipt))
        self.assertEqual(receipt["context"]["instructions"], [])

    def test_unsafe_source_path_fails_closed(self) -> None:
        release = _release()
        release["four_cs_question_source"] = "../secret.md"
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "unsafe_path")
        self.assertEqual(receipt["context"]["instructions"], [])

    def test_precedence_path_outside_the_manifest_is_not_read(self) -> None:
        secret = "unhashed-precedence-secret-token"
        _write(self.root, "outside-decision.md", "not the system of record\n" + secret + "\n")
        release = _release()
        release["precedence_checks"][0]["decision"] = "outside-decision.md"
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "precedence_path_unhashed")
        self.assertNotIn("outside-decision.md", receipt["paths_read"])
        self.assertNotIn(secret, _bundle(receipt))

    def test_hash_mismatch_fails_closed(self) -> None:
        _write(self.root, "decisions/task.md", "rewritten without a reseal\n")
        receipt = load_context(self.root, _request(self.revision))
        self.assertEqual(receipt["fail_reason"], "hash_mismatch")
        self.assertEqual(receipt["capabilities"]["read"], False)

    def test_absent_definition_file_is_not_invented(self) -> None:
        release = _release()
        release["definition_of_done"] = "DEFINITION-OF-DONE.md"
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "definition_of_done_unhashed")
        self.assertEqual(receipt["context"]["instructions"], [])
        self.assertFalse((self.root / "DEFINITION-OF-DONE.md").exists())

    def test_omitting_twelve_mandatory_wake_files_fails_after_reseal(self) -> None:
        release = _release()
        blocked = set(MANDATORY_WAKE_PATHS)
        self.assertEqual(len(blocked), 12)
        release["required"] = [item for item in release["required"] if item["path"] not in blocked]
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "mandatory_wake_missing")
        self.assertEqual(receipt["status"], "failed_closed")
        self.assertFalse(receipt["capabilities"]["read"])
        self.assertEqual(receipt["context"]["instructions"], [])

    def test_deleting_one_mandatory_wake_file_fails_closed(self) -> None:
        target = MANDATORY_WAKE_PATHS[0]
        (self.root / target).unlink()
        receipt = load_context(self.root, _request(self.revision))
        self.assertEqual(receipt["fail_reason"], "missing_file")
        self.assertIn(target, receipt["missing_files"])
        self.assertFalse(receipt["capabilities"]["read"])

    def test_unhashed_definition_of_done_stays_closed_after_edits(self) -> None:
        loose = "loose-dod.md"
        release = _release()
        release["definition_of_done"] = loose
        _write(self.root, loose, "Problem, Result. unhashed-dod-secret\n")
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "definition_of_done_unhashed")
        self.assertNotIn("loose-dod.md", receipt["paths_read"])
        self.assertNotIn("unhashed-dod-secret", _bundle(receipt))
        self.assertFalse(receipt["capabilities"]["read"])
        _write(self.root, loose, "Problem, Result. unhashed-dod-secret-edited\n")
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        edited = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(edited["fail_reason"], "definition_of_done_unhashed")
        self.assertNotIn("unhashed-dod-secret-edited", _bundle(edited))
        self.assertNotIn(loose, edited["paths_read"])

    def test_editing_hashed_definition_of_done_fails_closed(self) -> None:
        _write(self.root, "decisions/dod.md", "Problem, Result edited-dod-token\n")
        receipt = load_context(self.root, _request(self.revision))
        self.assertEqual(receipt["fail_reason"], "hash_mismatch")
        self.assertNotIn("edited-dod-token", _bundle(receipt))
        self.assertFalse(receipt["capabilities"]["read"])

    def test_unhashed_precedence_fixture_stays_closed_after_edits(self) -> None:
        loose = "loose-fixture.md"
        release = _release()
        release["precedence_checks"][0]["fixture"] = loose
        _write(
            self.root,
            loose,
            "<!-- context-bundle: preserved-superseded -->\n"
            "Linear wins on conflicts.\nunhashed-fixture-secret\n",
        )
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "precedence_path_unhashed")
        self.assertNotIn(loose, receipt["paths_read"])
        self.assertNotIn("unhashed-fixture-secret", _bundle(receipt))
        _write(
            self.root,
            loose,
            "<!-- context-bundle: preserved-superseded -->\n"
            "Linear wins on conflicts.\nunhashed-fixture-secret-edited\n",
        )
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        edited = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(edited["fail_reason"], "precedence_path_unhashed")
        self.assertNotIn("unhashed-fixture-secret-edited", _bundle(edited))
        self.assertNotIn(loose, edited["paths_read"])

    def test_editing_hashed_precedence_fixture_fails_closed(self) -> None:
        path = self.root / "context-load/fixtures/archived-linear-is-sor.md"
        path.write_text(path.read_text(encoding="utf-8") + "fixture-edit-token\n", encoding="utf-8")
        receipt = load_context(self.root, _request(self.revision))
        self.assertEqual(receipt["fail_reason"], "hash_mismatch")
        self.assertNotIn("fixture-edit-token", _bundle(receipt))

    def test_accepted_release_without_snapshot_fails_closed(self) -> None:
        accepted = self._plant_accepted(snapshot_root=None)
        _write(self.root, ACCEPTED_REL, json.dumps(accepted, indent=2) + "\n")
        receipt = load_context(
            self.root, _request(accepted["content_revision"], release_role="accepted")
        )
        self.assertEqual(receipt["fail_reason"], "accepted_snapshot_missing")
        self.assertFalse(receipt["capabilities"]["read"])
        self.assertEqual(receipt["context"]["instructions"], [])

    def test_mixed_line_keeps_neighbor_quote_and_attribution(self) -> None:
        rel = "brain/01-identity/05-beliefs-and-faith.md"
        text = (
            '"Love first. Learn. Lead. Live your legacy." [VERIFIED: v0.2]\n'
            '"Automate everything but the love." [VERIFIED: v1]\n'
            '"The secret to success is love." [VERIFIED: 07-rules]\n'
            '"Own what you build. Clients walk away with the whole system." '
            '"Tell the truth about the tools." [VERIFIED: v1]\n'
            '"Speed matters more than polish. Fast is the point." '
            "[BELIEVED 75%: 9_15]\n"
            'He stands for one line: "No one dies with their message still inside them." '
            '[07, VERIFIED] Under it sit the rest: "The secret to success is love." '
            '"Automate everything but the love." '
            '"Own what you build. Clients walk away with the whole system." '
            '"Tell the truth about the tools." [07, VERIFIED: v1] And '
            '"Speed matters more than polish. Fast is the point." '
            '[07, BELIEVED 75%: 9_15] He stands against "Fluff. Corporate language."\n'
            "Clients own what we build. Speed over polish.\n"
        )
        _write(self.root, rel, text)
        release = json.loads((self.root / CANDIDATE_REL).read_text(encoding="utf-8"))
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["status"], "loaded", receipt.get("fail_reason"))
        emitted = next(
            row["text"]
            for row in receipt["context"]["instructions"]
            if row["path"] == rel
        )
        self.assertIn('"Tell the truth about the tools."', emitted)
        self.assertIn("[VERIFIED: v1]", emitted)
        self.assertIn("[07, VERIFIED: v1]", emitted)
        self.assertIn("[BELIEVED 75%: 9_15]", emitted)
        self.assertIn("[07, BELIEVED 75%: 9_15]", emitted)
        self.assertIn("The secret to success is love.", emitted)
        self.assertIn("No one dies with their message still inside them.", emitted)
        self.assertIn("Love first. Learn. Lead. Live your legacy.", emitted)
        self.assertIn('He stands against "Fluff. Corporate language."', emitted)
        for phrase in (
            "Automate everything but the love.",
            "Own what you build",
            "Clients walk away with the whole system.",
            "Speed matters more than polish",
            "Fast is the point.",
            "Speed over polish",
            "Clients own what we build",
        ):
            self.assertNotIn(phrase, emitted, phrase)
        source = (self.root / rel).read_text(encoding="utf-8")
        self.assertIn("Own what you build. Clients walk away with the whole system.", source)
        self.assertIn('"Tell the truth about the tools."', source)
        self.assertTrue(receipt["withheld_rejections"])
        self.assertEqual(
            receipt["withheld_rejections"][0]["pointer"],
            "decisions/2026-10-11-false-quotes-removed.md",
        )
        self.assertEqual(receipt["withheld_rejections"][0]["owner_utterance"], "unresolved")

    def _replace_snapshot_root_with_live_alias(self, accepted: dict) -> None:
        snap = self.root / accepted["snapshot_root"]
        shutil.rmtree(snap)
        snap.symlink_to(Path("../../.."), target_is_directory=True)

    def test_symlinked_snapshot_root_rejected_after_shared_path_edit(self) -> None:
        accepted = self._plant_accepted()
        self._replace_snapshot_root_with_live_alias(accepted)
        snap = self.root / accepted["snapshot_root"]
        self.assertTrue(snap.is_symlink())
        self.assertEqual(snap.resolve(), self.root.resolve())
        _write(self.root, ACCEPTED_REL, json.dumps(accepted, indent=2) + "\n")
        before = load_context(self.root, _request("0" * 64))
        self.assertEqual(before["status"], "failed_closed")
        self.assertEqual(before["fail_reason"], "accepted_snapshot_aliased")
        self.assertFalse(before["fallback_used"])
        self.assertEqual(before["context"]["instructions"], [])
        self.assertFalse(before["capabilities"]["read"])
        live = self.root / "decisions/task.md"
        live.write_text(live.read_text(encoding="utf-8") + "LIVE-PATH-MUTATION\n", encoding="utf-8")
        after = load_context(self.root, _request("0" * 64))
        self.assertEqual(after["fail_reason"], "accepted_snapshot_aliased")
        self.assertNotEqual(after["status"], "fallback")
        self.assertNotIn("LIVE-PATH-MUTATION", _bundle(after))
        self.assertFalse(after["fallback_used"])
        self.assertFalse(after["accepted_release"])
        direct = load_context(
            self.root,
            _request(accepted["content_revision"], release_role="accepted"),
        )
        self.assertEqual(direct["fail_reason"], "accepted_snapshot_aliased")
        self.assertEqual(direct["context"]["instructions"], [])

    def test_symlinked_snapshot_file_rejected_after_shared_path_edit(self) -> None:
        accepted = self._plant_accepted()
        live = self.root / "decisions/task.md"
        snap_file = self.root / accepted["snapshot_root"] / "decisions/task.md"
        snap_file.unlink()
        snap_file.symlink_to(live)
        _write(self.root, ACCEPTED_REL, json.dumps(accepted, indent=2) + "\n")
        before = load_context(self.root, _request("0" * 64))
        self.assertEqual(before["fail_reason"], "accepted_snapshot_aliased")
        self.assertNotEqual(before["status"], "fallback")
        live.write_text(live.read_text(encoding="utf-8") + "LIVE-PATH-MUTATION\n", encoding="utf-8")
        after = load_context(self.root, _request("0" * 64))
        self.assertEqual(after["fail_reason"], "accepted_snapshot_aliased")
        self.assertNotIn("LIVE-PATH-MUTATION", _bundle(after))
        self.assertFalse(after["capabilities"]["read"])
        self.assertFalse(after["fallback_used"])

    def test_hardlinked_snapshot_file_rejected_after_shared_path_edit(self) -> None:
        accepted = self._plant_accepted()
        live = self.root / "decisions/task.md"
        snap_file = self.root / accepted["snapshot_root"] / "decisions/task.md"
        snap_file.unlink()
        os.link(live, snap_file)
        self.assertTrue(snap_file.samefile(live))
        _write(self.root, ACCEPTED_REL, json.dumps(accepted, indent=2) + "\n")
        before = load_context(self.root, _request("0" * 64))
        self.assertEqual(before["fail_reason"], "accepted_snapshot_aliased")
        self.assertNotEqual(before["status"], "fallback")
        live.write_text(live.read_text(encoding="utf-8") + "LIVE-PATH-MUTATION\n", encoding="utf-8")
        after = load_context(self.root, _request("0" * 64))
        self.assertEqual(after["fail_reason"], "accepted_snapshot_aliased")
        self.assertNotIn("LIVE-PATH-MUTATION", _bundle(after))
        self.assertFalse(after["fallback_used"])
        self.assertEqual(after["context"]["instructions"], [])

    def test_candidate_load_unused_malformed_accepted_returns_closed_receipt(self) -> None:
        _write(self.root, ACCEPTED_REL, "{")
        receipt = load_context(self.root, _request(self.revision))
        self.assertEqual(receipt["status"], "failed_closed")
        self.assertEqual(receipt["fail_reason"], "malformed_release_record")
        self.assertEqual(receipt["schema"], "epic-os-context-receipt/1")
        self.assertFalse(receipt["fallback_used"])
        self.assertFalse(receipt["stale"])
        self.assertEqual(
            receipt["capabilities"], {"read": False, "write": False, "send": False}
        )
        self.assertEqual(receipt["context"]["instructions"], [])
        self.assertEqual(receipt["current_instructions"], [])
        self.assertFalse(receipt["accepted_release"])
        self.assertNotIn("not the system of record", _bundle(receipt))

    def test_malformed_accepted_on_fallback_and_accepted_role_returns_closed_receipt(
        self,
    ) -> None:
        _write(self.root, ACCEPTED_REL, "{")
        fallback = load_context(self.root, _request("0" * 64))
        self.assertEqual(fallback["status"], "failed_closed")
        self.assertEqual(fallback["fail_reason"], "malformed_release_record")
        self.assertTrue(fallback["stale"])
        self.assertFalse(fallback["fallback_used"])
        self.assertEqual(fallback["context"]["instructions"], [])
        self.assertIn("not substituted", fallback["fallback_limitations"])
        self.assertNotIn("not the system of record", _bundle(fallback))
        accepted_role = load_context(
            self.root, _request(self.revision, release_role="accepted")
        )
        self.assertEqual(accepted_role["status"], "failed_closed")
        self.assertEqual(accepted_role["fail_reason"], "malformed_release_record")
        self.assertEqual(accepted_role["context"]["instructions"], [])
        self.assertFalse(accepted_role["capabilities"]["read"])
        _write(self.root, CANDIDATE_REL, "{")
        _write(self.root, ACCEPTED_REL, json.dumps(_accepted_none(), indent=2) + "\n")
        candidate = load_context(self.root, _request(self.revision))
        self.assertEqual(candidate["fail_reason"], "malformed_release_record")
        self.assertEqual(candidate["context"]["instructions"], [])


class RepoCandidateTest(unittest.TestCase):
    def test_real_tree_candidate_load(self) -> None:
        release = json.loads((ROOT / CANDIDATE_REL).read_text(encoding="utf-8"))
        accepted = json.loads((ROOT / ACCEPTED_REL).read_text(encoding="utf-8"))
        self.assertEqual(accepted["status"], "none")
        self.assertFalse(accepted["accepted_release"])
        self.assertIsNone(accepted["content_revision"])
        self.assertNotIn("acceptance", accepted)
        receipt = load_context(
            ROOT,
            _request(release["content_revision"], job="repo-candidate-check"),
        )
        self.assertEqual(receipt["status"], "loaded", receipt.get("fail_reason"))
        self.assertFalse(receipt["accepted_release"])
        self.assertEqual(receipt["release_role_loaded"], "candidate")
        self.assertEqual(receipt["capabilities"]["write"], False)
        self.assertEqual(receipt["capabilities"]["send"], False)
        self.assertTrue(receipt["capabilities"]["read"])
        self.assertFalse(receipt["installation_claimed"])
        self.assertEqual(receipt["four_cs_instruction"], FOUR_CS_INSTRUCTION)
        self.assertEqual(
            receipt["definition_of_done"], "decisions/2026-10-11-definition-of-done.md"
        )
        blob = _bundle(receipt)
        paths = _paths(receipt)
        self.assertEqual(
            receipt["context"]["instruction_sha256"],
            sha256_bytes(blob.encode("utf-8")),
        )
        self.assertIn(FOUR_CS_INSTRUCTION, blob)
        self.assertIn("Len checks client delivery", blob)
        self.assertIn("Problem, Result", blob)
        self.assertIn("No em dashes.", blob)
        self.assertIn("Trevor Crane.", blob)
        self.assertIn("not the system of record", blob)
        manifest_paths = {item["path"] for item in release["required"]}
        self.assertEqual(
            sum(1 for rel in MANDATORY_WAKE_PATHS if rel in manifest_paths),
            12,
        )
        for rel in MANDATORY_WAKE_PATHS:
            self.assertIn(rel, paths, rel)
            item = next(row for row in release["required"] if row["path"] == rel)
            self.assertEqual(item["scope"], "wake")
            self.assertEqual(item["bundle"], "current")
        self.assertIn("rules/README.md", paths)
        for rel in FLEET_LAWS:
            self.assertNotIn(rel, paths, rel)
        self.assertNotIn("unicorn dinosaur", blob)
        # Rejected attributions. Not instructions. The source file still has them.
        beliefs = (ROOT / "brain/01-identity/05-beliefs-and-faith.md").read_text(encoding="utf-8")
        self.assertIn(REJECTED_LINE, beliefs)
        self.assertIn("Own what you build", beliefs)
        self.assertIn("Speed matters more than polish", beliefs)
        for phrase in (
            REJECTED_LINE,
            "Own what you build",
            "Speed over polish",
            "Speed matters more than polish",
            "Clients own what we build",
            "Clients walk away with the whole system.",
            "Fast is the point.",
        ):
            self.assertNotIn(phrase, blob, phrase)
        beliefs_out = next(
            row["text"]
            for row in receipt["context"]["instructions"]
            if row["path"] == "brain/01-identity/05-beliefs-and-faith.md"
        )
        self.assertIn('"Tell the truth about the tools."', beliefs_out)
        self.assertIn("[VERIFIED: v1]", beliefs_out)
        self.assertIn("[BELIEVED 75%: 9_15]", beliefs_out)
        self.assertIn("The secret to success is love.", beliefs_out)
        self.assertIn("Love first. Learn. Lead. Live your legacy.", beliefs_out)
        self.assertNotIn("Chief of Staff + Grok Operator (combined for now)", blob)
        self.assertNotIn("Linear wins on conflicts", blob)
        self.assertNotIn("with Alfred added", blob)
        self.assertNotIn("2. Linear Fleet DoD — Mission Control / SSOT / dashboard", blob)
        self.assertNotIn("puts it on a Linear card with an owner", blob)
        winners = {row["winner"] for row in receipt["decision_precedence"]}
        self.assertIn("decisions/2026-10-11-task-home.md", winners)
        self.assertIn("decisions/2026-10-11-first-mate.md", winners)
        self.assertIn("decisions/2026-10-11-parked-names.md", winners)
        for row in receipt["decision_precedence"]:
            self.assertNotIn(row["loser"], paths)
            self.assertIn(row["winner"], paths)
        self.assertIn("fleet-os/GROKBOT_OS.md", paths)
        self.assertIn("skills/first-mate-os/SKILL.md", receipt["excluded_stale"])
        self.assertIn("sources/GITHUB-TANGO-SYNC-PLAN.md", receipt["excluded_stale"])
        self.assertFalse(receipt["tests_are_adoption_proof"])
        self.assertIn("owner-utterance-unresolved", receipt["gaps"])
        self.assertIn("parallel-pr-6-unmerged", receipt["gaps"])
        self.assertTrue(receipt["withheld_rejections"])
        self.assertEqual(receipt["parallel_dependencies"][0]["pr"], 6)
        self.assertEqual(
            receipt["parallel_dependencies"][0]["head"],
            "17411a97af1001d74b22f600dc0b68f634e956d8",
        )
        self.assertFalse(receipt["parallel_dependencies"][0]["merge_authorized"])
        bar = (ROOT / "review/reviewer-bar-original-and-pivots.md").read_text(encoding="utf-8")
        self.assertTrue(bar.startswith("PROPOSED, not approved"))
        self.assertIn("## Pivot 1", bar)
        self.assertIn("## Pivot 2", bar)
        self.assertIn("## Pivot 3", bar)
        self.assertIn("Unresolved.", bar)

    def test_real_tree_on_demand_fleet_law_and_undeclared_path(self) -> None:
        release = json.loads((ROOT / CANDIDATE_REL).read_text(encoding="utf-8"))
        receipt = load_context(
            ROOT,
            _request(
                release["content_revision"],
                on_demand=["rules/PLAN-BUILD-USE.md"],
            ),
        )
        self.assertEqual(receipt["status"], "loaded", receipt.get("fail_reason"))
        self.assertIn("rules/PLAN-BUILD-USE.md", _paths(receipt))
        self.assertIn("unicorn dinosaur", _bundle(receipt))
        self.assertIn(FOUR_CS_INSTRUCTION, _bundle(receipt))
        blocked = load_context(
            ROOT,
            _request(
                release["content_revision"],
                on_demand=["brain/04-voice/03-signature-phrases.md"],
            ),
        )
        self.assertEqual(blocked["fail_reason"], "on_demand_not_declared")
        self.assertEqual(blocked["context"]["instructions"], [])
        self.assertNotIn(REJECTED_LINE, _bundle(blocked))


if __name__ == "__main__":
    unittest.main(verbosity=2)
