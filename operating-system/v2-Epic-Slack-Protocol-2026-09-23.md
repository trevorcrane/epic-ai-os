# Epic Slack communication protocol

Version: 2 | Date: 2026-09-23 | Status: consolidated draft for review.
Based on [Epic Slack SOP v1, May 30, 2026](https://docs.google.com/document/d/1xYMywMb1fFiB85xusID1uKUej7l8250Y5Mm8bFm6Z78/edit), reconciled with Trevor's current directions.

1. Explicitly @mention the intended recipient, including agent-to-agent messages. Resolve actual Slack user IDs before sending. A typed nickname is not proof of notification or agent activation.
2. One topic per thread. Separate unrelated decisions. Link sibling threads to the same Linear job where appropriate; keep replies in the relevant thread.
3. For messages longer than two lines, use a recipient mention, short bold section titles, short sentences, numbered choices when needed, concise pros/cons, section dividers where useful, and a visible recommendation. Use code blocks for commands and technical strings. Use clickable links for resources and evidence. This revision replaces the historical code-block treatment of links to make handoffs easier to use.
4. Route Trevor's decisions and approval requests to #_red-flag-trevor, one item per thread. The source identifies #_epic_ai for AI operations and #admin for ops updates. Verify current channel IDs and access before sending. Do not claim these channels or their automations were configured in this task.
5. Bring Trevor decisions with a recommendation and prepared work. Execute authorized tasks yourself. If authentication or another action genuinely requires the account owner, explain the exact dependency rather than promising impossible autonomy.
6. Use versions, never agent-declared finality. Report review findings and delivery evidence; Trevor owns acceptance.
7. After actually saving a rule, confirm in the original thread with the rule, exact destination, version, and scope. Example: “Saved to the local rules draft: no em dashes. Hermes loading remains unverified.” Never claim global memory from a local file edit.
8. Cross-agent requests include job ID, requested action, relevant artifact/version, owner, authority, and checkpoint. Require acknowledgment/read-back. Avoid duplicate dispatches and self-triggering bot loops. Use authorized cross-PM coordination without routing every exchange through First Mate.

Historical references to Viktor managing channels are not verified current assignments. Trevor's instance is Max; Robyn's remains Hermes. Neither nickname establishes a connected Slack identity.

Implementation additions in this draft: job-linked handoffs, read-back verification, exact persistence evidence, and tenant boundaries. Source formatting has been restated without em dashes. This document does not send Slack messages or activate agent integrations.

## Brand-specific routing

The v5 4C kit names #_h_support-inbox for inbound client/lead messages, #_h_request-queue for Robyn or Sam requests, and #_h_red-flag for true emergencies. These are source examples requiring account/channel verification. They do not replace Trevor's #_red-flag-trevor decision inbox. An ordinary approval request is not automatically an emergency.

Keep a routing record per brand: workspace ID, conversation type, channel ID, recipient IDs, responding owner, and acknowledgment test. Until verified, return reports in the current task and mark external delivery pending. No invented channel or bot IDs.

One job can have several linked topic threads. Give each decision its own thread when needed, and keep each topic's replies together. The Linear job links them. Do not impose both one-thread-per-job and one-thread-per-topic as conflicting absolutes.

Use one primary CTA for customer messages. Internal decisions may use 1-3-1, with one requested decision at the end. Do not turn every progress update into three options.
