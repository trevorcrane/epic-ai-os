#!/usr/bin/env python3
"""Isolated tests for the preparation context loader.

A pass is evidence about this process. It is not proof of an installed skill,
a live fleet load, or an accepted release.
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from loader import (  # noqa: E402
    ACCEPTED_REL,
    CANDIDATE_REL,
    SCHEMA,
    load_context,
    seal_release,
)

ROOT = Path(__file__).resolve().parents[1]


def _write(root: Path, rel: str, text: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _fixture_files() -> dict[str, str]:
    return {
        "decisions/task.md": (
            "Decision: Tango is the project home for now. "
            "Linear is not the system of record.\n"
        ),
        "decisions/mate.md": "The First Mate is whichever AI Trevor is talking to.\n",
        "decisions/alfred.md": "Alfred stays parked and there is no Alfred card.\n",
        "decisions/dod.md": "Problem, Result, Who: owner and QC, What, By when, plus proof.\n",
        "decisions/four.md": "The 4 C's are Connect, Care, Clarity, Call to Action.\n",
        "brain/four-cs.md": 'Clarity, "Do you know why we are here?"\nDo you know why we\'re here?\n',
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


def _release() -> dict:
    return {
        "schema": SCHEMA,
        "role": "candidate",
        "status": "candidate",
        "accepted_release": False,
        "definition_of_done": "decisions/dod.md",
        "four_cs_question_required": True,
        "four_cs_question_source": "brain/four-cs.md",
        "four_cs_question_marker": "Do you know why we're here?",
        "gaps": ["no-accepted-release"],
        "open_questions": ["reviewer-bar-unresolved"],
        "required": [
            {"path": "decisions/task.md", "bundle": "current"},
            {"path": "decisions/mate.md", "bundle": "current"},
            {"path": "decisions/alfred.md", "bundle": "current"},
            {"path": "decisions/dod.md", "bundle": "current"},
            {"path": "decisions/four.md", "bundle": "current"},
            {"path": "brain/four-cs.md", "bundle": "current"},
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


class LoaderTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.revision = _plant(self.root)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_candidate_load_is_not_an_accepted_release(self) -> None:
        receipt = load_context(self.root, _request(self.revision))
        self.assertEqual(receipt["status"], "loaded")
        self.assertFalse(receipt["accepted_release"])
        self.assertEqual(receipt["capabilities"], {"read": True, "write": False, "send": False})
        self.assertFalse(receipt["installation_claimed"])
        self.assertFalse(receipt["skill_bodies_installed"])
        self.assertFalse(receipt["tests_are_adoption_proof"])
        self.assertTrue(receipt["four_cs_question_present"])
        self.assertEqual(receipt["definition_of_done"], "decisions/dod.md")
        self.assertEqual(receipt["time"], "2026-10-12T03:30:00Z")
        self.assertEqual(
            [row["id"] for row in receipt["decision_precedence"]],
            ["alfred", "first-mate", "task-home"],
        )
        for row in receipt["decision_precedence"]:
            self.assertIn(row["winner"], receipt["current_instructions"])
            self.assertNotIn(row["loser"], receipt["current_instructions"])
            self.assertFalse(row["loser_in_current_instructions"])
        self.assertIn("mixed/os.md#unmarked", receipt["current_instructions"])
        self.assertNotIn("mixed/os.md", receipt["current_instructions"])
        self.assertIn("mixed/os.md#preserved-superseded", receipt["excluded_stale"])
        self.assertIn("review/bar.md", receipt["proposals"])
        self.assertNotIn("review/bar.md", receipt["current_instructions"])
        self.assertTrue(receipt["evidence"])
        self.assertIn("reviewer-bar-unresolved", receipt["open_questions"])

    def test_missing_revision_fails_closed(self) -> None:
        receipt = load_context(self.root, _request("  "))
        self.assertEqual(receipt["status"], "failed_closed")
        self.assertEqual(receipt["fail_reason"], "missing_revision")
        self.assertEqual(receipt["capabilities"]["read"], False)
        self.assertEqual(receipt["current_instructions"], [])
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

    def test_stale_falls_back_to_last_known_accepted_only(self) -> None:
        accepted_files = {
            "accepted/task.md": "Linear is not the system of record.\n",
            "accepted/mate.md": "whichever AI Trevor is talking to\n",
            "accepted/alfred.md": "no Alfred card\n",
            "accepted/dod.md": "Problem, Result remains the source.\n",
            "accepted/four.md": "Connect, Care, Clarity, Call to Action.\n",
            "accepted/question.md": "Do you know why we're here?\n",
            "accepted/linear.md": (
                "<!-- context-bundle: preserved-superseded -->\nLinear wins on conflicts.\n"
            ),
            "accepted/mate-old.md": (
                "<!-- context-bundle: preserved-superseded -->\n"
                "Chief of Staff + Grok Operator (combined for now)\n"
            ),
            "accepted/alfred-old.md": (
                "<!-- context-bundle: preserved-superseded -->\nwith Alfred added\n"
            ),
            "accepted/os.md": _fixture_files()["mixed/os.md"],
            "accepted/bar.md": _fixture_files()["review/bar.md"],
            "accepted/map.md": "accepted-era map\n",
        }
        for rel, text in accepted_files.items():
            _write(self.root, rel, text)
        accepted = {
            "schema": SCHEMA,
            "role": "accepted",
            "status": "accepted",
            "accepted_release": True,
            "definition_of_done": "accepted/dod.md",
            "four_cs_question_required": True,
            "four_cs_question_source": "accepted/question.md",
            "four_cs_question_marker": "Do you know why we're here?",
            "gaps": ["fallback-fixture-only"],
            "open_questions": [],
            "required": [
                {"path": "accepted/task.md", "bundle": "current"},
                {"path": "accepted/mate.md", "bundle": "current"},
                {"path": "accepted/alfred.md", "bundle": "current"},
                {"path": "accepted/dod.md", "bundle": "current"},
                {"path": "accepted/four.md", "bundle": "current"},
                {"path": "accepted/question.md", "bundle": "current"},
                {
                    "path": "accepted/linear.md",
                    "bundle": "preserved-superseded",
                    "must_contain": ["Linear wins on conflicts"],
                },
                {
                    "path": "accepted/mate-old.md",
                    "bundle": "preserved-superseded",
                    "must_contain": ["Chief of Staff + Grok Operator (combined for now)"],
                },
                {
                    "path": "accepted/alfred-old.md",
                    "bundle": "preserved-superseded",
                    "must_contain": ["with Alfred added"],
                },
                {
                    "path": "accepted/os.md",
                    "bundle": "mixed",
                    "excluded_markers": [
                        "Chief of Staff + Grok Operator (combined for now)",
                        "Linear Fleet DoD",
                    ],
                    "current_markers": ["## Fleet Laws", "## Decided 2026-10-11"],
                },
                {"path": "accepted/bar.md", "bundle": "proposal"},
                {"path": "accepted/map.md", "bundle": "review"},
            ],
            "precedence_checks": [
                {
                    "id": "task-home",
                    "decision": "accepted/task.md",
                    "fixture": "accepted/linear.md",
                    "decision_marker": "not the system of record",
                    "fixture_marker": "Linear wins on conflicts",
                },
                {
                    "id": "first-mate",
                    "decision": "accepted/mate.md",
                    "fixture": "accepted/mate-old.md",
                    "decision_marker": "whichever AI Trevor is talking to",
                    "fixture_marker": "Chief of Staff + Grok Operator (combined for now)",
                },
                {
                    "id": "alfred",
                    "decision": "accepted/alfred.md",
                    "fixture": "accepted/alfred-old.md",
                    "decision_marker": "no Alfred card",
                    "fixture_marker": "with Alfred added",
                },
            ],
        }
        accepted = seal_release(accepted, self.root)
        _write(self.root, ACCEPTED_REL, json.dumps(accepted, indent=2) + "\n")
        receipt = load_context(self.root, _request("0" * 64))
        self.assertEqual(receipt["status"], "fallback", receipt.get("fail_reason"))
        self.assertTrue(receipt["fallback_used"])
        self.assertTrue(receipt["stale"])
        self.assertEqual(receipt["loaded_revision"], accepted["content_revision"])
        self.assertNotEqual(receipt["loaded_revision"], self.revision)
        self.assertTrue(receipt["accepted_release"])
        self.assertEqual(receipt["capabilities"], {"read": True, "write": False, "send": False})
        self.assertIn("last-known accepted", receipt["fallback_limitations"])
        self.assertIn("accepted/task.md", receipt["current_instructions"])
        self.assertNotIn("decisions/task.md", receipt["current_instructions"])
        self.assertFalse(receipt["installation_claimed"])

    def test_accepted_role_does_not_substitute_the_candidate(self) -> None:
        receipt = load_context(
            self.root, _request(self.revision, release_role="accepted")
        )
        self.assertEqual(receipt["status"], "failed_closed")
        self.assertEqual(receipt["fail_reason"], "missing_revision")
        self.assertFalse(receipt["accepted_release"])

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

    def test_dropping_the_four_cs_question_fails_closed(self) -> None:
        _write(self.root, "brain/four-cs.md", "Clarity, stated as a conclusion.\n")
        # Reseal so this is a hash match with the question removed, not a hash miss.
        release = _release()
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "four_cs_question_missing")
        self.assertEqual(receipt["current_instructions"], [])

    def test_dropping_the_question_requirement_flag_fails_closed(self) -> None:
        release = _release()
        release["four_cs_question_required"] = False
        sealed = seal_release(release, self.root)
        _write(self.root, CANDIDATE_REL, json.dumps(sealed, indent=2) + "\n")
        receipt = load_context(self.root, _request(sealed["content_revision"]))
        self.assertEqual(receipt["fail_reason"], "four_cs_requirement_dropped")

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
        self.assertEqual(receipt["fail_reason"], "missing_file")
        self.assertIn("DEFINITION-OF-DONE.md", receipt["missing_files"])


class RepoCandidateTest(unittest.TestCase):
    def test_real_tree_candidate_load(self) -> None:
        release = json.loads((ROOT / CANDIDATE_REL).read_text(encoding="utf-8"))
        receipt = load_context(
            ROOT,
            _request(release["content_revision"], job="repo-candidate-check"),
        )
        self.assertEqual(receipt["status"], "loaded", receipt.get("fail_reason"))
        self.assertFalse(receipt["accepted_release"])
        self.assertEqual(receipt["capabilities"]["write"], False)
        self.assertEqual(receipt["capabilities"]["send"], False)
        self.assertTrue(receipt["capabilities"]["read"])
        self.assertTrue(receipt["four_cs_question_present"])
        self.assertEqual(
            receipt["definition_of_done"], "decisions/2026-10-11-definition-of-done.md"
        )
        winners = {row["winner"] for row in receipt["decision_precedence"]}
        self.assertIn("decisions/2026-10-11-task-home.md", winners)
        self.assertIn("decisions/2026-10-11-first-mate.md", winners)
        self.assertIn("decisions/2026-10-11-parked-names.md", winners)
        for row in receipt["decision_precedence"]:
            self.assertNotIn(row["loser"], receipt["current_instructions"])
        self.assertNotIn("fleet-os/GROKBOT_OS.md", receipt["current_instructions"])
        self.assertIn("fleet-os/GROKBOT_OS.md#unmarked", receipt["current_instructions"])
        self.assertIn(
            "fleet-os/GROKBOT_OS.md#preserved-superseded", receipt["excluded_stale"]
        )
        self.assertIn("skills/first-mate-os/SKILL.md", receipt["excluded_stale"])
        self.assertIn("sources/GITHUB-TANGO-SYNC-PLAN.md", receipt["excluded_stale"])
        self.assertFalse(receipt["tests_are_adoption_proof"])
        self.assertIn("owner-utterance-unresolved", receipt["gaps"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
