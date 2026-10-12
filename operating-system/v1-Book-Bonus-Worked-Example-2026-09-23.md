# Worked example: Robyn's book-bonus funnel
Version: 1 | Prepared 2026-09-23 | Illustrative walkthrough, not executed work

## Parent assignment

Outcome: a reader can opt in, see confirmation, access the agreed bonuses, and receive the correct fulfillment messages in Robyn's voice. Parent acceptance owner: Trevor. PM, builders, and separate reviewer must be assigned before dispatch. Source URLs, tenant IDs, and current source version are inputs to retrieve, not invented placeholders for publication.

Existing authority: launch requested. Current hold: wait for Trevor's edited-site ready signal. Preparation and review can advance without deploying the held draft.

## Handoffs

| Step | Owner | Artifact and evidence | State / next action |
|---|---|---|---|
| Retrieve current source, URLs, offers, access rules | Researcher | Source manifest with gaps; distinguish verified facts from older campaigns | Internal step Verified after checks; PM scopes build |
| Draft welcome and access copy | Cat in Robyn context | Versioned copy, source facts, 4C notes, timing, personalization fallbacks | Ready for review; separate reviewer checks |
| Prepare pages and CRM workflow | Builder | Site draft, notification map, tags, pipeline transitions, workflow entry/exits | Ready for review; no live activation while held |
| Test the journey | Reviewer | Form submission, duplicate entry, first-name fallback, links/access, opt-outs, pipeline movement, internal alerts, actual message receipt | PASS leads to Verified; failures become Changes required |
| Deploy the authorized version after ready signal | Builder under PM | Referenced authority, removed hold evidence, reversible change record, observed destination tests | Parent Delivered, acceptance pending |
| Assess the deliverable | Trevor | Explicit response tied to the presented version | PM records Accepted only when supported by Trevor's response |

A copy-review PASS permits the next authorized build step. It does not require Trevor to approve that internal step. A verified workflow does not bypass the site hold. A reviewer may report observed delivery without declaring the project done.

## SNAPP RAD coverage

S: agreed opt-in, confirmation, and bonus URLs. N: internal alerts to the assigned owner. A: fulfillment sequence and suppression. P: lead/client stages and transitions. P: operator and recovery instructions. R: separate reviewer evidence. A: existing scoped launch authorization plus ready signal. D: observed working journey at the intended destination.

## Example report shape

“Book-bonus funnel v2 is ready for your review. Evidence: [verified test report and URLs]. Observed checks: [actual results]. Remaining gap: [actual gap or none observed within the stated checks].”

Bracketed text is a template, not test evidence. No live result is claimed here.
