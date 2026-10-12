# Permanent reviewer standard
Version 1 | 2026-09-24 | Authority: Trevor's explicit instruction in Book Site task.

## Purpose
Deliver work that is clear, concise, compelling, usable and operationally correct. QC owns finding and verifying defects before Trevor is asked to inspect the work. Apply this standard to every relevant project and deliverable, not only the book funnel. Mark genuinely inapplicable dimensions N/A with reasons; never use N/A for an unfinished requirement.

## Independence and release gate
- Builder and reviewer must be separate agents. Record agent/run identity, instructions loaded, source/deployment version and evidence timestamp.
- Inspect the actual live or deployable version, not only screenshots supplied by the builder or a summary of claimed success.
- Score each applicable dimension below from 0 to 100 with deductions tied to observed defects. Explain criteria and uncertainty. Scores measure review judgment, not a predicted conversion rate or statistical confidence.
- Release as QC-approved only when every applicable dimension is at least 95, overall score is at least 95, and all mandatory tests pass. Critical failures, broken links, inaccessible forms, misleading promises, failed capture/delivery, inappropriate sends or missing required evidence block approval regardless of averages.
- Builder repairs defects; reviewer retests changed behavior and affected dependencies. Continue within authorized scope. If access, recipient, consent, or business decisions are missing, report that specific dependency. Do not lower the bar or fabricate completion.
- QC approval is distinct from Trevor's acceptance, deployment authorization and permission to send broadcasts. Use existing authority; do not add unnecessary approval gates.

## Review dimensions
1. Site and visual experience: every funnel page, desktop and representative mobile widths, light/dark modes, typography, contrast, spacing, alignment, visual hierarchy, book/brand assets, CTAs, forms, validation, keyboard/focus behavior, optional-field reveal, loading/error/success states. Inspect screenshots and interactions at actual destinations.
2. Copy and promise consistency: clear offer, concise friendly brand voice, compelling next action, matching terminology from opt-in through confirmation and delivery. No unsupported claims or unavailable feature promises. Respect approved copy, punctuation and brand preferences.
3. Email presentation and content: inspect actual delivered/rendered emails, not editor text alone. Check subject, preview, sender/reply-to, personalization/fallback, fonts, size, spacing, line breaks, mobile readability, links/buttons, signature, address/footer and unsubscribe. Verify all sequence messages with designated test contacts and distinguish test-send delivery from timed production execution.
4. SMS: review copy, sender identification, length/readability, links, optional-phone behavior, recorded consent, opt-out/DND, reply handling, timing and suppression. Only send to authorized test numbers. Inactive SMS must be explicitly described as inactive, never approved as operational from draft copy.
5. Workflow: entry/form mapping, contact creation/update, tags, wait durations/timezone, sequence order, duplicate/re-entry handling, existing-contact behavior, blank optional data, failures, suppression/exits/replies, sender configuration and interactions with other workflows. Record actual execution and delivery evidence; configuration alone does not prove execution.
6. Pipeline and internal notifications: actual signup reaches correct pipeline/stage, correct status/source/tag, duplicate protection and intended transitions. Verify accountable owner, recipients, channel, actionable alert content and test receipt. Do not invent owners or notification recipients.
7. SNAPP RAD and operations: Site, Notifications, Automations, Pipeline, Protocol, Reviewed, Approved, Delivered. Verify IDs/URLs, roles, operating instructions, recovery steps, review evidence, existing approval scope and live delivery. Document outstanding dependencies explicitly.

## Required reviewer output
A dated/versioned report with scope, tested versions, reviewer identity, device/theme coverage, score table, evidence for tests, severity-ranked defects, fixes and re-test outcomes, unresolved dependencies and final verdict (PASS >=95, NEEDS FIXES, or BLOCKED). Link it to the project and originating task. Preserve earlier reports as history, identify the current one, and include an operator SOP. Do not claim global rollout without receipts from the shared instruction source and remote agent loaders.

## Shared startup and scoring procedure
For every relevant job, load this file through START-HERE.md and give it to the separate reviewer. Record the GitHub commit, version and reviewer run. This is the canonical shared policy; local copies must identify their source version. Apply each brand's own context and permissions.

Use the seven dimensions above consistently. For each dimension list required checks, evidence, coverage, deductions and score. Overall score is the arithmetic mean of applicable dimension scores, shown to one decimal without rounding upward to pass. Both the overall score and every applicable dimension must be >=95. A 95-99 score permits minor nonblocking polish issues only; material unmet requirements score below 95. Hard blockers cannot be averaged away. Scores are judgments supported by evidence, never invented target numbers.

Required but untested checks remain PENDING and prevent QC approval. N/A requires a scope-based reason and reviewer confirmation; exclude it from the mean but retain it visibly. Inactive channels remain INACTIVE/PENDING when activation is required. An explicitly email-only release can exclude SMS with a reason, but cannot claim SMS is operational or approved. No approval-eligible overall score exists while mandatory coverage is pending.

Inspect the entire in-scope site and workflow, with all supported themes and representative desktop/mobile widths. Record pages, viewport, theme, email clients and tested devices. Do not imply untested coverage. Distinguish test-send rendering from actual timed workflow execution. Source HTML alone is insufficient rendering evidence. Owner-supplied evidence must be labeled until independently inspected.

Maintain a versioned defect and score history across the fix/retest loop. If blocked by access, business choices or authority, report the exact gap, next owner and checkpoint. Do not lower criteria to obtain 95. A blocked draft can be presented honestly for a required decision, without calling it QC-approved.

Preserve one production editor and existing test-recipient authority. The policy does not authorize new sends, enable inactive channels, pick recipients, or expand account permissions. Keep QC verdict, deployment/send authority, delivery evidence and Trevor's business acceptance separate. Trevor accepts parent deliverables. No em dashes in authored deliverables.
