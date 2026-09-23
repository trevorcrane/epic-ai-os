# Epic AI progress-check procedure
Version: 1 | Prepared 2026-09-23 | Configuration draft, not an active schedule

Accountable owner: job PM. Scheduler setup and scheduler failure escalation: First Mate. Default check interval: ten minutes, to configure in the chosen always-available runtime. Each job has its own checkpoint; the interval is not a universal deadline.

On each tick:
1. Read active jobs and their checkpoints from the authoritative tracker. If access fails, record the failure and notify First Mate; do not guess statuses.
2. Skip Accepted jobs and internal steps already Verified/Delivered unless a dependency or failed check reopens them. For a delivered parent awaiting acceptance, retain its record but do not repeatedly ask Trevor on every tick.
3. Detect unowned Queued work, overdue checkpoints, unacknowledged handoffs, failed runs, missing review, and explicit blockers.
4. Read actual worker progress and artifacts before retrying. Record an observation, not just an alive signal. Respect launch holds and permission scope.
5. For safe, repeatable reads or recoverable dispatches, verify whether the original action occurred. Retry at most twice per logical dispatch, preserving its ID and recording attempts. Never blindly retry sends, payments, or uncertain external mutations.
6. PM repairs or reassigns within scope. If retries fail, mark Blocked and escalate to First Mate with evidence, next owner, and next checkpoint. Ask Trevor only for a decision or owner-only dependency.
7. Update the tracker and notify only on a meaningful change, delivery, failure, or necessary decision. Stay quiet on unchanged checks. Keep related reports in their originating thread.

Activation evidence required: runtime identity, installed schedule, tracker access, one intentionally overdue test job detected, one duplicate-dispatch test, and one recovery/escalation result. An external uptime check must cover a stopped execution host; a scheduler cannot report its own outage while offline.

No scheduler has been activated by writing this file. First Mate must verify the destination runtime before claiming unattended follow-through.
