#!/usr/bin/env python3
"""Preparation-only context loader for epic-ai-os.

Selective reuse, not a migration:
- PR #2 operating-system/agents/cat/LOAD.md: exact revision, required files,
  receipt fields, missing access disclosed, host adaptation.
- PR #2 operating-system/adapters/ADOPTION.md: per-host scope and an explicit
  boundary. A URL or a role note is not installation.
- Team handoff receipt on the 2026-10-06 v0.2 draft
  (team/05-handoffs/01-how-a-job-moves.md): summary, evidence, open questions.

Not reused: Cat or Alfred identity, schedules, host install rows, or any
replacement of team/. This module does not install a loader, merge a pull
request, or designate an accepted release.
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

SCHEMA = "epic-os-context-release/1"
RECEIPT_SCHEMA = "epic-os-context-receipt/1"
CANDIDATE_REL = "context-load/releases/candidate.json"
ACCEPTED_REL = "context-load/releases/accepted.json"
PRESERVED_TOKEN = "context-bundle: preserved-superseded"
PROPOSAL_HEADER = "PROPOSED, not approved"

# Read is not granted until a load succeeds. Write and send stay denied.
HOSTS = {
    "cursor": "Cursor. This adapter does not install a loader into the agent.",
    "tango": "Tango. This adapter does not attach a wake hook or write a task.",
    "grok": "Grok Bot. This adapter does not edit a live profile.",
    "chatgpt": "ChatGPT. Sharing a URL is not installation.",
    "hermes": "Hermes. This adapter does not write a profile.",
    "claude": "Claude Code. CLAUDE.md still only points at AGENTS.md.",
}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def _revision_body(release: dict) -> dict:
    required = sorted(release.get("required") or [], key=lambda item: item["path"])
    checks = sorted(release.get("precedence_checks") or [], key=lambda item: item["id"])
    return {
        "accepted_release": release.get("accepted_release"),
        "definition_of_done": release.get("definition_of_done"),
        "four_cs_question_required": release.get("four_cs_question_required", True),
        "precedence_checks": checks,
        "required": required,
        "role": release.get("role"),
        "schema": release.get("schema"),
        "status": release.get("status"),
    }


def content_revision(release: dict) -> str:
    payload = json.dumps(_revision_body(release), sort_keys=True, separators=(",", ":"))
    return sha256_bytes(payload.encode("utf-8"))


def seal_release(release: dict, root: Path) -> dict:
    """Fill file hashes and content_revision. Does not set accepted_release."""
    sealed = json.loads(json.dumps(release))
    sealed["schema"] = SCHEMA
    for item in sealed.get("required") or []:
        path = root / item["path"]
        if path.is_file():
            item["sha256"] = sha256_file(path)
            item.pop("missing_at_seal", None)
        else:
            item["sha256"] = None
            item["missing_at_seal"] = True
    sealed["required"] = sorted(sealed["required"], key=lambda item: item["path"])
    sealed["precedence_checks"] = sorted(
        sealed.get("precedence_checks") or [], key=lambda item: item["id"]
    )
    sealed["content_revision"] = content_revision(sealed)
    return sealed


def _blank_receipt(request: dict) -> dict:
    now = request.get("now") or datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {
        "schema": RECEIPT_SCHEMA,
        "job": request.get("job") or "",
        "agent_identity": "epic-os-context-load-preparation",
        "worker_id": request.get("worker_id") or "",
        "host": request.get("host") or "",
        "host_note": "",
        "repository": request.get("repository") or "trevorcrane/epic-ai-os",
        "time": now,
        "requested_revision": request.get("expected_revision") or "",
        "requested_role": request.get("release_role") or "candidate",
        "loaded_revision": None,
        "release_role_loaded": None,
        "accepted_release": False,
        "installation_claimed": False,
        "skill_bodies_installed": False,
        "live_agent_changed": False,
        "tests_are_adoption_proof": False,
        "paths_read": [],
        "path_hashes": {},
        "current_instructions": [],
        "excluded_stale": [],
        "proposals": [],
        "review_artifacts": [],
        "missing_files": [],
        "stale": False,
        "fallback_used": False,
        "fallback_limitations": "",
        "gaps": [],
        "decision_precedence": [],
        "four_cs_question_required": True,
        "four_cs_question_present": False,
        "definition_of_done": None,
        "capabilities": {"read": False, "write": False, "send": False},
        "summary": "",
        "evidence": [],
        "open_questions": [],
        "status": "failed_closed",
        "fail_reason": None,
    }


def _read_json(path: Path) -> dict | None:
    if not path.is_file():
        return None
    return json.loads(path.read_text(encoding="utf-8"))


def _fail(receipt: dict, reason: str, extra_gaps: list | None = None) -> dict:
    receipt["status"] = "failed_closed"
    receipt["fail_reason"] = reason
    receipt["capabilities"] = {"read": False, "write": False, "send": False}
    receipt["current_instructions"] = []
    if extra_gaps:
        receipt["gaps"].extend(extra_gaps)
    if reason not in receipt["gaps"]:
        receipt["gaps"].append(reason)
    receipt["summary"] = (
        f"failed_closed:{reason} read=false write=false send=false "
        "installation_claimed=false"
    )
    receipt["evidence"] = [
        {"path": path, "sha256": digest}
        for path, digest in sorted(receipt["path_hashes"].items())
    ]
    return receipt


def _split_mixed(text: str) -> tuple[str, str]:
    unmarked: list[str] = []
    stale: list[str] = []
    rest = text
    while True:
        start = rest.find("<!-- " + PRESERVED_TOKEN)
        if start < 0:
            unmarked.append(rest)
            break
        unmarked.append(rest[:start])
        end_open = rest.find("-->", start)
        if end_open < 0:
            unmarked.append(rest[start:])
            break
        close = rest.find("<!-- /context-bundle -->", end_open)
        if close < 0:
            stale.append(rest[end_open + 3 :])
            break
        stale.append(rest[end_open + 3 : close])
        rest = rest[close + len("<!-- /context-bundle -->") :]
    return "".join(unmarked), "".join(stale)


def _verify_release(root: Path, release: dict, receipt: dict) -> str | None:
    """Return a fail reason, or None when every required file checks out."""
    if release.get("status") == "none" or not release.get("content_revision"):
        return "missing_revision"
    if release.get("content_revision") != content_revision(release):
        return "hash_mismatch"
    dod = release.get("definition_of_done")
    if dod and not (root / dod).is_file():
        receipt["missing_files"].append(dod)
        return "missing_file"
    if dod:
        dod_text = (root / dod).read_text(encoding="utf-8")
        if "Problem, Result" not in dod_text:
            return "definition_of_done_missing"
        receipt["definition_of_done"] = dod

    for item in release.get("required") or []:
        path = root / item["path"]
        bundle = item.get("bundle")
        if not path.is_file():
            receipt["missing_files"].append(item["path"])
            continue
        digest = sha256_file(path)
        receipt["path_hashes"][item["path"]] = digest
        receipt["paths_read"].append(item["path"])
        if item.get("sha256") != digest:
            return "hash_mismatch"
        text = path.read_text(encoding="utf-8")
        if bundle == "current":
            if PRESERVED_TOKEN in text:
                return "stale_in_current_bundle"
            for marker in item.get("must_contain") or []:
                if marker not in text:
                    return "current_marker_missing"
            receipt["current_instructions"].append(item["path"])
        elif bundle == "preserved-superseded":
            if PRESERVED_TOKEN not in text:
                return "superseded_mark_missing"
            for marker in item.get("must_contain") or []:
                if marker not in text:
                    return "superseded_text_missing"
            receipt["excluded_stale"].append(item["path"])
        elif bundle == "mixed":
            unmarked, stale = _split_mixed(text)
            if PRESERVED_TOKEN not in text or not stale.strip():
                return "superseded_mark_missing"
            for marker in item.get("excluded_markers") or []:
                if marker not in stale:
                    return "superseded_text_missing"
                if marker in unmarked:
                    return "stale_in_current_bundle"
            for marker in item.get("current_markers") or []:
                if marker not in unmarked:
                    return "current_marker_missing"
            receipt["current_instructions"].append(item["path"] + "#unmarked")
            receipt["excluded_stale"].append(item["path"] + "#preserved-superseded")
        elif bundle == "proposal":
            if not text.startswith(PROPOSAL_HEADER):
                return "proposal_header_missing"
            receipt["proposals"].append(item["path"])
        elif bundle == "review":
            receipt["review_artifacts"].append(item["path"])
        else:
            return "unknown_bundle"
    if receipt["missing_files"]:
        return "missing_file"

    if release.get("four_cs_question_required") is not True:
        return "four_cs_requirement_dropped"
    question_path = release.get("four_cs_question_source")
    question_marker = release.get("four_cs_question_marker")
    if not question_path or not question_marker:
        return "four_cs_question_missing"
    qfile = root / question_path
    if not qfile.is_file():
        receipt["missing_files"].append(question_path)
        return "missing_file"
    qtext = qfile.read_text(encoding="utf-8")
    if question_marker not in qtext:
        return "four_cs_question_missing"
    receipt["four_cs_question_required"] = True
    receipt["four_cs_question_present"] = True

    for check in release.get("precedence_checks") or []:
        decision_path = check["decision"]
        fixture_path = check["fixture"]
        decision_text = (root / decision_path).read_text(encoding="utf-8")
        fixture_text = (root / fixture_path).read_text(encoding="utf-8")
        if check["decision_marker"] not in decision_text:
            return "precedence_failed"
        if check["fixture_marker"] not in fixture_text:
            return "precedence_failed"
        if fixture_path in receipt["current_instructions"]:
            return "stale_in_current_bundle"
        if decision_path not in receipt["current_instructions"]:
            return "precedence_failed"
        for item in release["required"]:
            if item.get("bundle") != "current":
                continue
            current_text = (root / item["path"]).read_text(encoding="utf-8")
            if check["fixture_marker"] in current_text:
                return "stale_in_current_bundle"
        receipt["decision_precedence"].append(
            {
                "id": check["id"],
                "winner": decision_path,
                "loser": fixture_path,
                "loser_in_current_instructions": False,
            }
        )
    return None


def _succeed(receipt: dict, release: dict, *, fallback: bool) -> dict:
    receipt["loaded_revision"] = release.get("content_revision")
    receipt["release_role_loaded"] = release.get("role")
    receipt["accepted_release"] = bool(release.get("accepted_release")) and not fallback
    if fallback:
        receipt["accepted_release"] = bool(release.get("accepted_release"))
        receipt["status"] = "fallback"
        receipt["fallback_used"] = True
        receipt["fallback_limitations"] = (
            "Requested revision was stale. Loaded the last-known accepted "
            "release only. The candidate was not used. This is not a new "
            "accepted designation."
        )
    else:
        receipt["status"] = "loaded"
        receipt["accepted_release"] = bool(release.get("accepted_release"))
    receipt["capabilities"] = {"read": True, "write": False, "send": False}
    receipt["gaps"].extend(release.get("gaps") or [])
    receipt["open_questions"].extend(release.get("open_questions") or [])
    receipt["evidence"] = [
        {"path": path, "sha256": digest}
        for path, digest in sorted(receipt["path_hashes"].items())
    ]
    receipt["summary"] = (
        f"{receipt['status']} role={receipt['release_role_loaded']} "
        f"revision={receipt['loaded_revision']} read=true write=false "
        "send=false accepted_release="
        f"{str(receipt['accepted_release']).lower()} installation_claimed=false"
    )
    return receipt


def load_context(root: Path | str, request: dict) -> dict:
    root = Path(root)
    receipt = _blank_receipt(request)
    host = receipt["host"]
    if host not in HOSTS:
        return _fail(receipt, "unknown_host")
    receipt["host_note"] = HOSTS[host]
    if request.get("require_write") or request.get("require_send"):
        return _fail(receipt, "capability_denied")
    expected = request.get("expected_revision")
    if expected is None or str(expected).strip() == "":
        return _fail(receipt, "missing_revision")

    candidate = _read_json(root / CANDIDATE_REL)
    accepted = _read_json(root / ACCEPTED_REL)
    role = request.get("release_role") or "candidate"
    if role == "accepted":
        target = accepted
    elif role == "candidate":
        target = candidate
    else:
        return _fail(receipt, "unknown_role")
    if target is None:
        return _fail(receipt, "missing_release_record")
    if target.get("status") == "none" or not target.get("content_revision"):
        return _fail(receipt, "missing_revision")

    if expected != target.get("content_revision"):
        receipt["stale"] = True
        if (
            role == "candidate"
            and accepted
            and accepted.get("status") == "accepted"
            and accepted.get("content_revision")
            and accepted.get("accepted_release") is True
        ):
            reason = _verify_release(root, accepted, receipt)
            if reason:
                receipt["current_instructions"] = []
                receipt["fallback_limitations"] = (
                    "Last-known accepted release failed verification. "
                    "Candidate was not substituted."
                )
                return _fail(receipt, reason)
            return _succeed(receipt, accepted, fallback=True)
        receipt["fallback_limitations"] = (
            "No last-known accepted release is recorded. Candidate was not "
            "loaded in place of the missing revision."
        )
        return _fail(receipt, "stale")

    reason = _verify_release(root, target, receipt)
    if reason:
        receipt["current_instructions"] = []
        return _fail(receipt, reason)
    return _succeed(receipt, target, fallback=False)


def _main(argv: list[str]) -> int:
    if len(argv) < 2 or argv[1] != "seal":
        print("usage: python3 context-load/loader.py seal", file=sys.stderr)
        return 2
    root = Path(__file__).resolve().parents[1]
    path = root / CANDIDATE_REL
    release = json.loads(path.read_text(encoding="utf-8"))
    sealed = seal_release(release, root)
    path.write_text(json.dumps(sealed, indent=2) + "\n", encoding="utf-8")
    print(sealed["content_revision"])
    return 0


if __name__ == "__main__":
    raise SystemExit(_main(sys.argv))
