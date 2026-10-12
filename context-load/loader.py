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

A successful load returns the ordered instruction text for that host. The
host table is the boundary note. It is not the payload.
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

# Verbatim v5 requirement. The Brain example question is not this sentence.
# Provenance: PR #2 operating-system/v5-4Cs-Source-Reference-2026-09-24.md
# at 3dee9cb52e1d5cf291f192fd91d5bf06a15752ae, source member
# v5-4Cs-CoreFramework-2026-09-24.md, section 3. Clarity.
# No owner-utterance message id for this sentence is in this repo.
FOUR_CS_INSTRUCTION = "Ask it as a question, not a conclusion."
FOUR_CS_PROVENANCE_NEEDLES = (
    "operating-system/v5-4Cs-Source-Reference-2026-09-24.md",
    "3dee9cb52e1d5cf291f192fd91d5bf06a15752ae",
    "v5-4Cs-CoreFramework-2026-09-24.md",
)

# Rejected attributions. Matchers only. Not instructions.
# PR #6 owns removal in the Brain files. The decision file
# decisions/2026-10-11-false-quotes-removed.md is not in this tree.
# Owner-utterance message id: unresolved. Do not invent one.
REJECTED_ATTRIBUTION_MARKERS = (
    "automate everything but the love",
    "own what you build",
    "speed over polish",
    "speed matters more than polish",
    "clients own what we build",
)
REJECTED_POINTER = "decisions/2026-10-11-false-quotes-removed.md"
SNAPSHOT_PREFIX = "context-load/releases/snapshots/"

# Every wake. Omitting any of these from a release fails closed.
MANDATORY_WAKE_PATHS = (
    "brain/01-identity/01-who-i-am.md",
    "brain/01-identity/02-family.md",
    "brain/01-identity/03-origin-story.md",
    "brain/01-identity/04-why.md",
    "brain/01-identity/05-beliefs-and-faith.md",
    "brain/01-identity/06-point-of-view.md",
    "brain/09-rules-of-engagement/01-writing.md",
    "brain/09-rules-of-engagement/02-public-copy.md",
    "brain/09-rules-of-engagement/03-message-format.md",
    "brain/09-rules-of-engagement/04-how-ai-works-for-me.md",
    "brain/09-rules-of-engagement/05-approvals.md",
    "brain/09-rules-of-engagement/06-never.md",
)

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
    """Every field except content_revision. Those fields drive behavior."""
    body = {key: value for key, value in release.items() if key != "content_revision"}
    required = body.get("required")
    if isinstance(required, list):
        body["required"] = sorted(required, key=lambda item: item.get("path", ""))
    checks = body.get("precedence_checks")
    if isinstance(checks, list):
        body["precedence_checks"] = sorted(checks, key=lambda item: item.get("id", ""))
    return body


def content_revision(release: dict) -> str:
    payload = json.dumps(_revision_body(release), sort_keys=True, separators=(",", ":"))
    return sha256_bytes(payload.encode("utf-8"))


def _safe_rel(rel: object) -> bool:
    if not isinstance(rel, str) or rel.strip() == "":
        return False
    if rel.startswith(("/", "\\")) or "\\" in rel or "\0" in rel:
        return False
    if Path(rel).is_absolute():
        return False
    parts = Path(rel).parts
    if not parts or any(part in ("..", "") for part in parts):
        return False
    return True


def _resolve_under_root(root: Path, rel: str) -> Path | None:
    if not _safe_rel(rel):
        return None
    root_resolved = root.resolve()
    candidate = (root_resolved / rel).resolve()
    try:
        candidate.relative_to(root_resolved)
    except ValueError:
        return None
    return candidate


def _valid_snapshot_root(snap: object) -> bool:
    if not isinstance(snap, str) or not snap.startswith(SNAPSHOT_PREFIX):
        return False
    rest = snap[len(SNAPSHOT_PREFIX) :]
    if not rest or "/" in rest or "\\" in rest or rest in (".", ".."):
        return False
    return _safe_rel(snap)


def _content_path(root: Path, release: dict, rel: str) -> Path | None:
    """Live tree for a candidate. Sealed snapshot for an accepted release."""
    if not _safe_rel(rel):
        return None
    snap = release.get("snapshot_root")
    if not snap:
        return _resolve_under_root(root, rel)
    if not _valid_snapshot_root(snap):
        return None
    combined = snap.rstrip("/") + "/" + rel
    if not _safe_rel(combined):
        return None
    resolved = _resolve_under_root(root, combined)
    snap_resolved = _resolve_under_root(root, snap)
    if resolved is None or snap_resolved is None:
        return None
    try:
        resolved.relative_to(snap_resolved)
    except ValueError:
        return None
    return resolved


def seal_release(release: dict, root: Path) -> dict:
    """Fill file hashes and content_revision. Does not set accepted_release.

    An accepted release is hashed from snapshot_root, not from the live paths.
    """
    sealed = json.loads(json.dumps(release))
    sealed["schema"] = SCHEMA
    for item in sealed.get("required") or []:
        rel = item.get("path")
        path = _content_path(root, sealed, rel) if isinstance(rel, str) else None
        if path is not None and path.is_file():
            item["sha256"] = sha256_file(path)
            item.pop("missing_at_seal", None)
        else:
            item["sha256"] = None
            item["missing_at_seal"] = True
    sealed["required"] = sorted(sealed["required"], key=lambda item: item.get("path", ""))
    sealed["precedence_checks"] = sorted(
        sealed.get("precedence_checks") or [], key=lambda item: item.get("id", "")
    )
    sealed["content_revision"] = content_revision(sealed)
    return sealed


def _empty_context() -> dict:
    return {
        "host": "",
        "host_note": "",
        "installation_claimed": False,
        "instructions": [],
        "instruction_text": "",
        "instruction_sha256": None,
    }


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
        "instruction_paths": [],
        "current_instructions": [],
        "context": _empty_context(),
        "excluded_stale": [],
        "proposals": [],
        "review_artifacts": [],
        "missing_files": [],
        "withheld_rejections": [],
        "stale": False,
        "fallback_used": False,
        "fallback_limitations": "",
        "gaps": [],
        "decision_precedence": [],
        "four_cs_question_required": True,
        "four_cs_question_present": False,
        "four_cs_instruction": None,
        "four_cs_provenance": None,
        "definition_of_done": None,
        "parallel_dependencies": [],
        "snapshot_root": None,
        "on_demand_resolved": [],
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
    receipt["instruction_paths"] = []
    receipt["context"] = _empty_context()
    receipt["withheld_rejections"] = []
    receipt["four_cs_question_present"] = False
    receipt["decision_precedence"] = []
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


def _withhold_rejected(path: str, text: str, withheld: list[dict]) -> str:
    kept: list[str] = []
    for line in text.splitlines(keepends=True):
        lowered = line.lower()
        if any(marker in lowered for marker in REJECTED_ATTRIBUTION_MARKERS):
            withheld.append(
                {
                    "path": path,
                    "rejected": True,
                    "pointer": REJECTED_POINTER,
                    "parallel_pr": 6,
                    "owner_utterance": "unresolved",
                }
            )
            continue
        kept.append(line)
    return "".join(kept)


def _emit_text(sections: list[dict]) -> str:
    chunks: list[str] = []
    for section in sections:
        body = section["text"].rstrip("\n")
        chunks.append(
            f"----- {section['path']} | {section['scope']} | {section['bundle']} -----\n{body}\n"
        )
    if not chunks:
        return ""
    return "\n".join(chunks) + "\n"


def _check_record_consistency(release: dict, requested_role: str) -> str | None:
    if release.get("schema") != SCHEMA:
        return "schema_mismatch"
    role = release.get("role")
    status = release.get("status")
    flag = release.get("accepted_release")
    if requested_role == "candidate":
        if role != "candidate" or status != "candidate" or flag is not False:
            return "candidate_record_inconsistent"
        if release.get("snapshot_root"):
            return "candidate_snapshot_rejected"
        return None
    if requested_role != "accepted":
        return "unknown_role"
    if role != "accepted":
        return "accepted_role_mismatch"
    if status != "accepted":
        return "accepted_status_mismatch"
    if flag is not True:
        return "accepted_flag_missing"
    acceptance = release.get("acceptance")
    if not isinstance(acceptance, dict):
        return "acceptance_evidence_missing"
    for key in ("accepted_by", "accepted_at", "evidence"):
        value = acceptance.get(key)
        if not isinstance(value, str) or not value.strip():
            return "acceptance_evidence_missing"
    if not _valid_snapshot_root(release.get("snapshot_root")):
        return "accepted_snapshot_missing"
    return None


def _check_mandatory_wake(release: dict) -> str | None:
    members = {
        item.get("path"): item
        for item in release.get("required") or []
        if isinstance(item.get("path"), str)
    }
    for rel in MANDATORY_WAKE_PATHS:
        item = members.get(rel)
        if item is None or item.get("scope") != "wake" or item.get("bundle") != "current":
            return "mandatory_wake_missing"
    return None


def _check_consumed_references(release: dict) -> str | None:
    """Every path the loader reads must be a safe hashed manifest member."""
    members = _member_paths(release)
    dod = release.get("definition_of_done")
    if not _safe_rel(dod):
        return "unsafe_path"
    if dod not in members:
        return "definition_of_done_unhashed"
    if release.get("four_cs_question_required") is True:
        source = release.get("four_cs_question_source")
        if not _safe_rel(source):
            return "unsafe_path"
        if source not in members:
            return "four_cs_source_unhashed"
    for check in release.get("precedence_checks") or []:
        for key in ("decision", "fixture"):
            rel = check.get(key)
            if not _safe_rel(rel):
                return "unsafe_path"
            if rel not in members:
                return "precedence_path_unhashed"
    for dep in release.get("parallel_dependencies") or []:
        if not isinstance(dep, dict) or dep.get("merge_authorized") is not False:
            return "parallel_merge_not_authorized"
    return None


def _member_paths(release: dict) -> set[str]:
    paths: set[str] = set()
    for item in release.get("required") or []:
        rel = item.get("path")
        if isinstance(rel, str):
            paths.add(rel)
    return paths


def _check_four_cs(release: dict, texts: dict[str, str], sections: list[dict]) -> str | None:
    if release.get("four_cs_question_required") is not True:
        return "four_cs_requirement_dropped"
    marker = release.get("four_cs_question_marker")
    source = release.get("four_cs_question_source")
    provenance = release.get("four_cs_provenance")
    if marker != FOUR_CS_INSTRUCTION:
        return "four_cs_instruction_replaced"
    if not _safe_rel(source):
        return "unsafe_path"
    members = {
        item.get("path"): item
        for item in release.get("required") or []
        if isinstance(item.get("path"), str)
    }
    item = members.get(source)
    if item is None:
        return "four_cs_source_unhashed"
    if item.get("bundle") not in ("current", "mixed") or item.get("scope") != "wake":
        return "four_cs_source_not_emitted"
    text = texts.get(source, "")
    if FOUR_CS_INSTRUCTION not in text:
        return "four_cs_instruction_missing"
    if not isinstance(provenance, str) or not provenance.strip():
        return "four_cs_provenance_missing"
    for needle in FOUR_CS_PROVENANCE_NEEDLES:
        if needle not in provenance:
            return "four_cs_provenance_missing"
    emitted = "\n".join(section["text"] for section in sections)
    if FOUR_CS_INSTRUCTION not in emitted:
        return "four_cs_instruction_missing"
    return None


def _verify_release(
    root: Path,
    release: dict,
    receipt: dict,
    requested_role: str,
    on_demand: list[str],
) -> str | None:
    """Return a fail reason, or None when the instruction bundle is ready."""
    if release.get("content_revision") != content_revision(release):
        return "hash_mismatch"
    reason = _check_record_consistency(release, requested_role)
    if reason:
        return reason
    reason = _check_mandatory_wake(release)
    if reason:
        return reason
    reason = _check_consumed_references(release)
    if reason:
        return reason

    required = release.get("required") or []
    member_paths = _member_paths(release)
    texts: dict[str, str] = {}
    wake_sections: list[dict] = []
    withheld: list[dict] = []

    dod = release.get("definition_of_done")

    for item in required:
        rel = item.get("path")
        if not _safe_rel(rel):
            return "unsafe_path"
        path = _content_path(root, release, rel)
        bundle = item.get("bundle")
        scope = item.get("scope")
        if path is None:
            return "unsafe_path"
        if not path.is_file():
            receipt["missing_files"].append(rel)
            continue
        digest = sha256_file(path)
        receipt["path_hashes"][rel] = digest
        receipt["paths_read"].append(rel)
        if item.get("sha256") != digest:
            return "hash_mismatch"
        text = path.read_text(encoding="utf-8")
        texts[rel] = text
        if scope not in ("wake", "on_demand", "record"):
            return "unknown_scope"
        if bundle in ("current", "mixed") and scope == "wake" and not isinstance(item.get("order"), int):
            return "emit_order_missing"
        if bundle == "current":
            if PRESERVED_TOKEN in text:
                return "stale_in_current_bundle"
            for marker in item.get("must_contain") or []:
                if marker not in text:
                    return "current_marker_missing"
            if scope == "wake":
                emitted = _withhold_rejected(rel, text, withheld)
                wake_sections.append(
                    {"path": rel, "scope": "wake", "bundle": "current", "order": item["order"], "text": emitted}
                )
        elif bundle == "preserved-superseded":
            if PRESERVED_TOKEN not in text:
                return "superseded_mark_missing"
            for marker in item.get("must_contain") or []:
                if marker not in text:
                    return "superseded_text_missing"
            receipt["excluded_stale"].append(rel)
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
            receipt["excluded_stale"].append(rel + "#preserved-superseded")
            if scope == "wake":
                emitted = _withhold_rejected(rel, unmarked, withheld)
                wake_sections.append(
                    {"path": rel, "scope": "wake", "bundle": "mixed", "order": item["order"], "text": emitted}
                )
        elif bundle == "proposal":
            if not text.startswith(PROPOSAL_HEADER):
                return "proposal_header_missing"
            receipt["proposals"].append(rel)
        elif bundle == "review":
            receipt["review_artifacts"].append(rel)
        else:
            return "unknown_bundle"
    if receipt["missing_files"]:
        return "missing_file"

    dod_item = next(item for item in required if item.get("path") == dod)
    if dod_item.get("bundle") != "current" or dod_item.get("scope") != "wake":
        return "definition_of_done_unhashed"
    dod_text = texts[dod]
    if "Problem, Result" not in dod_text:
        return "definition_of_done_missing"
    receipt["definition_of_done"] = dod

    wake_sections.sort(key=lambda section: (section["order"], section["path"]))
    reason = _check_four_cs(release, texts, wake_sections)
    if reason:
        return reason

    section_paths = [section["path"] for section in wake_sections]
    for check in release.get("precedence_checks") or []:
        decision_path = check.get("decision")
        fixture_path = check.get("fixture")
        if not _safe_rel(decision_path) or not _safe_rel(fixture_path):
            return "unsafe_path"
        if decision_path not in member_paths or fixture_path not in member_paths:
            return "precedence_path_unhashed"
        decision_text = texts[decision_path]
        fixture_text = texts[fixture_path]
        if check["decision_marker"] not in decision_text:
            return "precedence_failed"
        if check["fixture_marker"] not in fixture_text:
            return "precedence_failed"
        if fixture_path in section_paths:
            return "stale_in_current_bundle"
        if decision_path not in section_paths:
            return "precedence_failed"
        for item in required:
            if item.get("bundle") != "current":
                continue
            if check["fixture_marker"] in texts[item["path"]]:
                return "stale_in_current_bundle"
        receipt["decision_precedence"].append(
            {
                "id": check["id"],
                "winner": decision_path,
                "loser": fixture_path,
                "loser_in_current_instructions": False,
            }
        )

    resolved: list[str] = []
    extra_sections: list[dict] = []
    for rel in on_demand:
        if not _safe_rel(rel):
            return "unsafe_path"
        if rel in section_paths or rel in resolved:
            continue
        item = next((row for row in required if row.get("path") == rel), None)
        if item is None:
            return "on_demand_not_declared"
        if item.get("scope") != "on_demand" or item.get("bundle") not in ("current", "mixed"):
            return "on_demand_not_instruction"
        if rel not in texts:
            return "on_demand_not_declared"
        if item.get("bundle") == "current":
            emitted = _withhold_rejected(rel, texts[rel], withheld)
        else:
            unmarked, _stale = _split_mixed(texts[rel])
            emitted = _withhold_rejected(rel, unmarked, withheld)
        extra_sections.append(
            {"path": rel, "scope": "on_demand", "bundle": item["bundle"], "text": emitted}
        )
        resolved.append(rel)

    sections = wake_sections + extra_sections
    instruction_text = _emit_text(sections)
    receipt["withheld_rejections"] = withheld
    receipt["instruction_paths"] = [section["path"] for section in sections]
    receipt["current_instructions"] = [section["text"] for section in sections]
    receipt["on_demand_resolved"] = resolved
    receipt["four_cs_question_required"] = True
    receipt["four_cs_question_present"] = True
    receipt["four_cs_instruction"] = FOUR_CS_INSTRUCTION
    receipt["four_cs_provenance"] = release.get("four_cs_provenance")
    receipt["context"] = {
        "host": receipt["host"],
        "host_note": receipt["host_note"],
        "installation_claimed": False,
        "instructions": [
            {
                "path": section["path"],
                "scope": section["scope"],
                "bundle": section["bundle"],
                "text": section["text"],
            }
            for section in sections
        ],
        "instruction_text": instruction_text,
        "instruction_sha256": sha256_bytes(instruction_text.encode("utf-8")),
    }
    for marker in REJECTED_ATTRIBUTION_MARKERS:
        if marker in instruction_text.lower():
            return "rejected_attribution_emitted"
    return None


def _succeed(receipt: dict, release: dict, *, fallback: bool) -> dict:
    receipt["loaded_revision"] = release.get("content_revision")
    receipt["release_role_loaded"] = release.get("role")
    receipt["parallel_dependencies"] = list(release.get("parallel_dependencies") or [])
    if fallback:
        receipt["accepted_release"] = True
        receipt["status"] = "fallback"
        receipt["fallback_used"] = True
        receipt["snapshot_root"] = release.get("snapshot_root")
        receipt["fallback_limitations"] = (
            "Requested revision was stale. Loaded the last-known accepted "
            "release from its sealed snapshot. Live files that share those "
            "paths were not used. The candidate was not used. This is not a "
            "new accepted designation."
        )
    else:
        receipt["status"] = "loaded"
        receipt["accepted_release"] = bool(release.get("accepted_release"))
    receipt["capabilities"] = {"read": True, "write": False, "send": False}
    receipt["gaps"].extend(release.get("gaps") or [])
    if receipt["withheld_rejections"] and "disputed-attributions-withheld" not in receipt["gaps"]:
        receipt["gaps"].append("disputed-attributions-withheld")
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


def _on_demand_paths(request: dict) -> list[str] | str:
    raw = request.get("on_demand") or []
    if raw is None:
        return []
    if not isinstance(raw, list) or any(not isinstance(item, str) for item in raw):
        return "on_demand_not_declared"
    return raw


def load_context(root: Path | str, request: dict) -> dict:
    root = Path(root)
    receipt = _blank_receipt(request)
    host = receipt["host"]
    if host not in HOSTS:
        return _fail(receipt, "unknown_host")
    receipt["host_note"] = HOSTS[host]
    receipt["context"]["host"] = host
    receipt["context"]["host_note"] = HOSTS[host]
    if request.get("require_write") or request.get("require_send"):
        return _fail(receipt, "capability_denied")
    expected = request.get("expected_revision")
    if expected is None or str(expected).strip() == "":
        return _fail(receipt, "missing_revision")
    on_demand = _on_demand_paths(request)
    if isinstance(on_demand, str):
        return _fail(receipt, on_demand)

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
        if role == "candidate" and accepted and accepted.get("status") not in (None, "none"):
            reason = _check_record_consistency(accepted, "accepted")
            if reason:
                receipt["fallback_limitations"] = (
                    "Last-known accepted release failed the accepted-record "
                    "check. Candidate was not substituted."
                )
                return _fail(receipt, reason)
            reason = _verify_release(root, accepted, receipt, "accepted", on_demand)
            if reason:
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

    reason = _verify_release(root, target, receipt, role, on_demand)
    if reason:
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
