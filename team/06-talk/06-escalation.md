# Escalation path

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: team/01-laws.md (laws 7, 8), team/05-handoffs/03-handoff-rules.md, Reconnect plan, Hermes rules (rule 10), rules/LOOK-BEFORE-YOU-ASK.md, rules/CLOUDFLARE-PAGES-STANDARD.md, Wake plan.

Use the lowest step that can solve it. Say which step you are on, on the task.

1. **Look first.** Search shared memory, the repo, and the rules before asking anyone. Name the paths you opened. [rules/LOOK-BEFORE-YOU-ASK.md]
2. **Retry inside the limit.** Three attempts, max. The third verdict is BLOCKED with a 1-3-1. [Law 7]
3. **AI route before a human.** Check Composio and the other bots (Tango, SendToAgent) for an access path or a workaround. A missing access is a red flag to solve, not a reason to stop quietly. [Hermes rules, rule 10]
4. **Your house Lead, then Elon.** Elon is the orchestrator and owns "is it on the box or in Tango". Twice with no answer from another house: tell Trevor in one line and offer the fastest path. [rules/TANGO-HANDOFF-NO-DROP.md; team/05-handoffs/03-handoff-rules.md]
5. **A human, by kind of problem.**
   - Dead connector or login: Abi first, Len second, Monday to Friday about 9 AM to 6 PM ET. In hours: an urgent Slack to Abi, and copy Len if Abi has not answered in 30 minutes. Out of hours: queue it and Slack both for the morning. [Reconnect plan]
   - Keys, access, Cloudflare, the Tango Runner on Trevor's iMac, the Bob Mac worker: Len. No Cloudflare access means stop and escalate to Len. Never fall back to Netlify. [rules/CLOUDFLARE-PAGES-STANDARD.md; Wake plan]
   - Money, brand, naming, strategy, anything red (money out, deletes, access changes, no rollback): Trevor decides. Bring a recommendation. [Law 8]
6. **Trevor.** A 1-3-1 in the task thread, then one Slack relay line that mentions `<@U52DALA3U>`, or the next voice call. Batch asks. Trevor keeps one sign-off list from Elon, not many pings. [Wake plan section 0]
7. **Still red after 2 business hours** (connector cases): goes to Trevor as an ACTION, batched. [Reconnect plan]

Stop rule: Trevor says "stop" and every running task blocks with "STOP: Captain." [team/05-handoffs/04-events.md]
