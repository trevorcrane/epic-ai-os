# Epic AI job template
Version: 1 | Prepared 2026-09-23 | Copy for each substantive assignment

```yaml
job_id: REQUIRED
parent_job_id: null
level: deliverable # or internal_step
brand: REQUIRED
department: REQUIRED
outcome: REQUIRED
acceptance_owner: Trevor Crane # explicitly bind for a client deployment
pm: REQUIRED
builder: REQUIRED
reviewer: REQUIRED_SEPARATE_SESSION
researcher: REQUIRED_ROLE_OWNER
scorekeeper: REQUIRED_ROLE_OWNER
status: Queued
review_verdict: null # PASS, CHANGES REQUIRED, BLOCKED
acceptance_state: pending # not_applicable for internal_step; accepted only with owner evidence
authority_record: REQUIRED
holds: []
source_versions: []
artifact_version: null
artifact_url: null
acceptance_criteria: []
evidence: []
due_at: REQUIRED_ISO_TIME_WITH_OFFSET
next_action: REQUIRED
next_owner: REQUIRED
checkpoint_at: REQUIRED_ISO_TIME_WITH_OFFSET
last_progress_at: null
dispatch_id: null
acknowledgment: null
retry_count: 0
blocker: null
acceptance_evidence: null
```

Status vocabulary: Queued, In progress, Ready for review, Changes required, Verified, Delivered, Accepted, Blocked. Never auto-translate Delivered into owner acceptance. Internal steps end active execution at Verified or Delivered; parent acceptance stays pending.

Handoff: recipient + job ID + exact request + artifact version/link + evidence + authority/holds + checkpoint. Recipient acknowledges ownership or explains the blocker. A retry keeps the logical dispatch ID to avoid duplicate work.

Reviewer packet: original requirements, source references, inspected version, test cases and observed results, communication-rule checks, unresolved gaps, verdict. Distinguish independent evidence from the builder's own claims.

Owner report: version/status; what changed; evidence; remaining gap; next action and owner. Ask Trevor only for a decision that is actually needed.
