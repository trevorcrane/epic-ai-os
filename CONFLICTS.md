# CONFLICTS

Status: closed list. No items are open as of 2026-10-11.

<!-- context-bundle: preserved-superseded -->

This file was an open list in the 2026-10-06 compile. That compile did not choose a winner, and each source kept its own wording. Trevor answered the list on 2026-10-11 at 10:32 PM ET. He closed items 22 and 24 in a follow-up at 10:37 PM ET. Every item below is CLOSED and links to its decision file in [decisions/](decisions/). The paragraphs under each heading are the 2026-10-06 record, kept as written. They are not open conflicts. They are not current instructions. A scoped decision does not approve Brain or Team as a release.

Closing this list did not leave a later item open. Do not describe the file as an open list.

Q numbers point at [QUESTIONS.md](QUESTIONS.md).

## 1. Two org charts

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-org-chart.md](decisions/2026-10-11-org-chart.md).

Aug 17 seed, [EPIC-ORG.md](archive/2026-08-17-seed-org/EPIC-ORG.md) and [ROLE-CARDS.md](archive/2026-08-17-seed-org/ROLE-CARDS.md):

- Trevor talks to Fizz. Fizz is Mission Director and owns outcomes.
- Honey is Communications Director. Bumble is Intelligence and Evidence Auditor. Hermes is Builder and Approver and holds credentials.
- Len is the one human review gate before anything goes live.
- The bench (Claude, ChatGPT, Grok, and others) is summoned per task and then leaves.

Sep 28 Team, [team/](team/):

- Trevor is the Captain. The AI he is talking to can be First Mate.
- Houses with cards: Max on Hermes, Elon on Grok Bot, Claude, and ChatGPT with no Lead name yet.
- Seats any bot can sit: First Mate, Lead, Researcher, Builder, Reviewer, Scorekeeper.
- [team/03-bots/06-names-not-in-use.md](team/03-bots/06-names-not-in-use.md) parks Fizz, Alfred, Director, and the RAIN layer (Researcher, Advisor, Implementer, Navigator as an old stack).

Humans also differ in wording. The seed lists Jomar as read-only reference on Robyn's legacy workflows. [team/02-people/02-humans.md](team/02-people/02-humans.md) does not list Jomar. The seed calls Abi support for orchestration. The Team file calls Abi execution across both companies. The seed calls Jay the credentials and infrastructure human. The Team file calls Jay dev.

## 2. Two sets of laws

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-laws.md](decisions/2026-10-11-laws.md).

[team/01-laws.md](team/01-laws.md) says it is the only file that holds the laws. Ten Epic Laws, plus an always-on list, plus the 2026-09-28 line that nothing leaves the team without the Captain's OK.

[rules/](rules/) is a second set. Twelve fleet files, including [rules/CURSOR-BOB-DISPATCH.md](rules/CURSOR-BOB-DISPATCH.md). Each file is the source of truth for that one rule. [AGENTS.md](AGENTS.md) indexes them.

Both sets stay. Some overlap (evidence before done, nobody grades their own work, no credentials in files) and some do not (Cloudflare hosting, funnel fields, Google Docs, published-docs-first).

## 3. Grok Bot OS lists five fleet laws

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-grokbot-os-rules.md](decisions/2026-10-11-grokbot-os-rules.md).

[fleet-os/GROKBOT_OS.md](fleet-os/GROKBOT_OS.md) is dated 2026-09-30 and lists Plan-Build-Use, Verify before you claim, Editable Google Docs, Tango handoff no-drop, and Follow published docs. It says a full OS refresh is still owed.

[rules/](rules/) also contains CTA-NEW-TAB, EPIC-FUNNEL-SOP, CLOUDFLARE-PAGES-STANDARD, LAUNCH-QC-CHECKLIST, LOOK-BEFORE-YOU-ASK, and SITE-SHIP-LOOP, locked Oct 2 through Oct 5, 2026, plus Follow published docs and Cursor Bob dispatch, both locked 2026-10-06. The OS header date is earlier than those lock dates. The OS still lists five laws.

The OS still points at `/workspace/ops/rules/`. The files in this repo are under `rules/`.

## 4. Who may approve a send

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-approvals.md](decisions/2026-10-11-approvals.md).

[EPIC-AI-WORKING-AGREEMENT.md](EPIC-AI-WORKING-AGREEMENT.md): proceed without human approval except unapproved spend, irreversible data loss, legal or reputational risk in customer-facing output, or a strategic fork. Len gives the one human review before live.

[team/02-people/01-captain.md](team/02-people/01-captain.md) and [team/02-people/02-humans.md](team/02-people/02-humans.md): Len is yellow approver for client-facing delivery. Trevor approves money, brand, naming, and strategy. The approver list is supposed to live in `machine/01-systems.md`, which was not in the archive.

[team/01-laws.md](team/01-laws.md) law 8: yellow means prepare fully, ask the approver once, then go.

Same file, added 2026-09-28: nothing leaves the team without the Captain's OK. It points at Q37.

[brain/09-rules-of-engagement/05-approvals.md](brain/09-rules-of-engagement/05-approvals.md): states the same clash, then says until Trevor says otherwise his rule wins (Len can check, Trevor OKs the send). [QUESTIONS.md](QUESTIONS.md) Q37 is still an open question. This compile does not promote that sentence into a closed decision. [decisions/2026-09-28-chat-rules.md](decisions/2026-09-28-chat-rules.md) records the chat line and replaces nothing.

## 5. What "done" means

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-definition-of-done.md](decisions/2026-10-11-definition-of-done.md).

[EPIC-AI-WORKING-AGREEMENT.md](EPIC-AI-WORKING-AGREEMENT.md): four states (DONE AND PERMANENT, IN PROGRESS, WORKS NOW NOT PERMANENT, BLOCKED). Done needs proof in the same message. Permanent needs a tested restart. Deliveries pass SNAPP-RAD.

[team/01-laws.md](team/01-laws.md) law 5: agents say PASSED REVIEW. The human says done, with one exception for a green task at the check the Lead staffed.

[fleet-os/GROKBOT_OS.md](fleet-os/GROKBOT_OS.md): LIVE (exists, interaction works, verification, evidence) and RAD (reviewed, approved if needed, delivered).

## 6. Where a task lives

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-task-home.md](decisions/2026-10-11-task-home.md).

[team/01-laws.md](team/01-laws.md) law 1: Slack or chat is the front door. The First Mate makes the Tango task.

[rules/TANGO-HANDOFF-NO-DROP.md](rules/TANGO-HANDOFF-NO-DROP.md): Tango is the project home. Chat is scratch.

[sources/GITHUB-TANGO-SYNC-PLAN.md](sources/GITHUB-TANGO-SYNC-PLAN.md): Tango holds tasks. Linear stays the system of record until the pilot decision on Fri Oct 9, 2026. Until then Tango mirrors and Linear wins on conflicts.

[README.md](README.md) and [EPIC-ORG.md](archive/2026-08-17-seed-org/EPIC-ORG.md): Buzz is where agents talk. [EPIC-CONTEXT.md](EPIC-CONTEXT.md): Linear is optional tracking, later. [MISSIONS.md](MISSIONS.md) is the mission board.

## 7. Who the First Mate is

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-first-mate.md](decisions/2026-10-11-first-mate.md).

[team/04-seats/00-overview.md](team/04-seats/00-overview.md): the AI the Captain is talking to. One First Mate at a time, per conversation. Any house.

[fleet-os/GROKBOT_OS.md](fleet-os/GROKBOT_OS.md): First Mate is Chief of Staff plus Grok Operator, combined for now.

[skills/SKILL-LIBRARY.md](skills/SKILL-LIBRARY.md): "Epic OS (First Mate)" is named as a bot next to Planner, Advisor, and Navigator.

[EPIC-ORG.md](archive/2026-08-17-seed-org/EPIC-ORG.md): the standing owner of outcomes is Fizz, and that file does not use the title First Mate.

## 8. Names parked in one file and used in another

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-parked-names.md](decisions/2026-10-11-parked-names.md).

[team/03-bots/06-names-not-in-use.md](team/03-bots/06-names-not-in-use.md): Alfred, Fizz, Director, and the RAIN names are parked. An old file that says Advisor means First Mate. Implementer means Builder. Navigator means Reviewer plus Scorekeeper. Law: no new agent names.

[sources/GITHUB-TANGO-SYNC-PLAN.md](sources/GITHUB-TANGO-SYNC-PLAN.md) section 1 and Phase 1: Alfred (Codex) reads `AGENTS.md`, and Phase 1 says to push the roster with Alfred added. Moving him onto an active card is "one of the first decisions to log." No Captain line bringing the name back was in the archive, so no Alfred card was added.

[EPIC-ORG.md](archive/2026-08-17-seed-org/EPIC-ORG.md): Fizz is the standing Mission Director.

[skills/fleet-shrink-list-2026-09-28.md](skills/fleet-shrink-list-2026-09-28.md), room review the same day: keep Researcher, Advisor, Implementer, and Navigator as the Epic Brain demo team. Keep separate mentor bots.

The skill index still assigns Live skills to Advisor, Navigator, Planner, and Implementer.

The v0.5 rollout branch (not compiled here) treats Alfred as an active Codex lead. That branch was not used as the base. See gaps.

## 9. Mission lines

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-mission-lines.md](decisions/2026-10-11-mission-lines.md).

[EPIC-CONTEXT.md](EPIC-CONTEXT.md): Epic Media's mission is "no one dies with their message inside them."

[brain/02-mission/01-mission-and-promise.md](brain/02-mission/01-mission-and-promise.md): "Build the team that builds your dream" is the company mission. "No one dies with their message inside them" is the why. "Build an Extraordinary Life" is the EPIC master line. The file says that ranking is a read, and Q2 asks Trevor to confirm it.

[brain/05-messaging/01-big-idea.md](brain/05-messaging/01-big-idea.md): he stands for one line, "No one dies with their message still inside them."

Wording differs inside those lines: "inside them" and "still inside them." [decisions/2026-09-28-mission-line.md](decisions/2026-09-28-mission-line.md) records the company-mission sentence and replaces nothing.

## 10. The 4 C's

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-four-cs.md](decisions/2026-10-11-four-cs.md).

[brain/05-messaging/06-four-cs.md](brain/05-messaging/06-four-cs.md) and [team/06-talk/02-team-and-clients.md](team/06-talk/02-team-and-clients.md): Connect, Care, Clarity, Call to Action.

The same Brain file, and Q5: the third word is Clarity in the 4 C's PDF, and Clarify in the 2026 messaging doc and Pro memory. Trevor has not picked.

[ROLE-CARDS.md](archive/2026-08-17-seed-org/ROLE-CARDS.md), Honey's card: the reader feels Seen, Heard, Understood, Confident. A confused mind says no.

## 11. Proof counts

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-proof-count.md](decisions/2026-10-11-proof-count.md).

[EPIC-CONTEXT.md](EPIC-CONTEXT.md): "20-time bestselling author, 1,000+ authors published."

[brain/11-proof/01-claims.md](brain/11-proof/01-claims.md): "For the last 10+ years, I have 20 bestsellers and helped 1,000+ authors." Tagged believed, not verified. Bios wording in that file: "I've helped 1K+ authors become bestsellers & grow their brands & biz." Historical wordings in that file are marked do-not-use ("6 time #1", "14 bestsellers", "200 people").

## 12. Where prices are written

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-prices-internal.md](decisions/2026-10-11-prices-internal.md).

[brain/07-offers/01-offer-map.md](brain/07-offers/01-offer-map.md): prices live in the offers folder and nowhere public.

[EPIC-CONTEXT.md](EPIC-CONTEXT.md): states Robyn's ladder in dollars (PYFP, RAP, and a 1:1 program). Those figures are not in `brain/07-offers/`. The seed file is internal org context. The public-copy rule still applies to anything a person outside the team can see.

## 13. Buzz and EpicLeads.ai

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-epicleads-name.md](decisions/2026-10-11-epicleads-name.md).

[README.md](README.md) and [EPIC-ORG.md](archive/2026-08-17-seed-org/EPIC-ORG.md): Buzz is the room where agents talk.

[brain/03-brands/06-other-properties.md](brain/03-brands/06-other-properties.md) and [brain/09-rules-of-engagement/02-public-copy.md](brain/09-rules-of-engagement/02-public-copy.md): EpicLeads.ai is the public name for the lead tool. Never say buzz.ai outside the team. Tagged believed.

## 14. Family: Phoenix and "all kids"

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-kids-authors.md](decisions/2026-10-11-kids-authors.md).

[decisions/2026-09-28-family.md](decisions/2026-09-28-family.md) records Robyn, Maverick, Sage, and "all kids are published authors."

[brain/01-identity/02-family.md](brain/01-identity/02-family.md) also lists Phoenix. Birthdates are not stored. Q1 asks whether "all kids" includes Phoenix, and what the book titles are.

[sources/INVENTORY.md](sources/INVENTORY.md) section 5 says the Brain lists three kids and the newer facts name Maverick and Sage.

## 15. Crazy Crane spelling

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-family-channel.md](decisions/2026-10-11-family-channel.md).

[brain/03-brands/06-other-properties.md](brain/03-brands/06-other-properties.md) lists three spellings and says the exact spelling is unverified: Crazy Crane, Crazy Cranes, The Crazy Crane Show. The channel is viewers, not clients.

Phase 1 of the sync plan names a decision, "Crazy Cranes kept separate." No separate decision record was in the archive. The channel description above is what the Brain does say. It was not upgraded into a locked decision file.

## 16. Where decisions live

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-decisions-home.md](decisions/2026-10-11-decisions-home.md).

[sources/PROPOSED-STRUCTURE.md](sources/PROPOSED-STRUCTURE.md): one append-only `memory/DECISIONS.md`. Newest wins.

[sources/GITHUB-TANGO-SYNC-PLAN.md](sources/GITHUB-TANGO-SYNC-PLAN.md) section 3: `decisions/`, one file per decision.

[brain/00-README.md](brain/00-README.md) source priority still lists `memory/DECISIONS.md` second, after what Trevor says now.

This compile put the recorded lines in [decisions/](decisions/) because the sync plan is the layout the task required. It did not create `memory/DECISIONS.md`, so the Brain readme's path is still unmet.

## 17. Where skills live

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-skills-home.md](decisions/2026-10-11-skills-home.md).

[sources/PROPOSED-STRUCTURE.md](sources/PROPOSED-STRUCTURE.md): `team/07-skills/<skill>/SKILL.md`.

[sources/GITHUB-TANGO-SYNC-PLAN.md](sources/GITHUB-TANGO-SYNC-PLAN.md) section 3: `skills/` at the repo root.

The Team draft has no `07-skills/` folder. Live skill cards are under [skills/](skills/).

## 18. What this repo is

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-single-repo.md](decisions/2026-10-11-single-repo.md).

[sources/PROPOSED-STRUCTURE.md](sources/PROPOSED-STRUCTURE.md): `epic-ai-os` is the empty template. Trevor's filled copy would be `epic-ai-os-trevor`.

[sources/GITHUB-TANGO-SYNC-PLAN.md](sources/GITHUB-TANGO-SYNC-PLAN.md), [brain/00-README.md](brain/00-README.md), and [decisions/2026-09-28-repo-shape.md](decisions/2026-09-28-repo-shape.md): `epic-ai-os` is the single source of truth.

This compile filled `brain/` and `team/` in `trevorcrane/epic-ai-os` because that is the repo the task named. Q3 is still open. No second repo was created.

## 19. Two names for the launch skills

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-launch-skill-names.md](decisions/2026-10-11-launch-skill-names.md).

[skills/SKILL-LIBRARY.md](skills/SKILL-LIBRARY.md), "Things to know": the Epic OS plan calls them pain-research, offer-test, launch-copy, one-page-site, and gtm-plan. The drafts in the index are idea-validation, demand-test-design, launch-copy, landing-page-build, and growth-plan. The index says to pick one set before installing. This compile did not.

## 20. Mentor skills: Live, held, and two copies

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-mentor-packs.md](decisions/2026-10-11-mentor-packs.md).

The index marks Ed Lawrence, Hormozi, and Kallaway Live. The same notes say Reviewer scores were 56%, 50%, and 57%, and the packs are held from being promoted as finished coaches.

Hormozi's two copies are described as identical. Kallaway and Ed Lawrence "differ slightly (need to pick one)." Neither copy's body was in the archive, so both bodies are absent and neither was chosen.

## 21. Depleted Brain Ghostwriting status

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-depleted-brain.md](decisions/2026-10-11-depleted-brain.md).

[skills/skills.json](skills/skills.json) status for that skill is Live. The notes say it is a reference file the book agent reads, not an installed skill. The body at the original path was not in the archive.

## 22. Content Machine and the shrink list

**CLOSED 2026-10-11. Dropped by Trevor 2026-10-11:** no action, nothing retired or merged. Decision: [decisions/2026-10-11-shrink-list-dropped.md](decisions/2026-10-11-shrink-list-dropped.md).

[skills/fleet-shrink-list-2026-09-28.md](skills/fleet-shrink-list-2026-09-28.md) has three layers from the same day:

1. First lists: merge Content Engine into Book: Dr. Leigh. Retire 8, merge 18, keep 16.
2. dr eggbot overrides: hold Content Engine until after Oct 7. Hold Stills & Clips. Keep the Bot Builders group.
3. Room review at 10:27 AM ET: retire only three test chats, pending Trevor. All merges wait until after Oct 7. One writer bot per voice, so Content Engine (Trevor) and Book: Dr. Leigh both stay.

[skills/bot-log.md](skills/bot-log.md): Content Engine upgraded to Content Machine, Trevor-approved. [decisions/2026-09-28-content-machine-rename.md](decisions/2026-09-28-content-machine-rename.md) records that upgrade and replaces none of the shrink-list layers.

## 23. Social Planner and "the tool Elon picks"

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-social-planner.md](decisions/2026-10-11-social-planner.md).

[skills/bot-log.md](skills/bot-log.md): the Content Machine spec sends the pack out "via the publishing tool Elon picks." The next line says the persona was updated to the Social Planner workflow: write and stage in review only, Elon confirms live.

[decisions/2026-09-28-social-planner-workflow.md](decisions/2026-09-28-social-planner-workflow.md) records the second sentence. It does not say Social Planner is the only publishing tool.

## 24. Tango handles

**CLOSED 2026-10-11.** Already resolved (Team v0.2 underscores). Decision: [decisions/2026-10-11-tango-handles.md](decisions/2026-10-11-tango-handles.md).

Resolved in Team v0.2. The cards use underscores, the same spelling as [rules/TANGO-HANDOFF-NO-DROP.md](rules/TANGO-HANDOFF-NO-DROP.md): `@trevor_crane`, `@trevor_claude`, `@trevor_chatgpt`, `@trevor_grokbot`, `@trevor_hermes`. [team/06-talk/channels/01-tango.md](team/06-talk/channels/01-tango.md) says the v0.1 hyphens were wrong.

## 25. Smart, Pro, and Epic mean two things

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-offer-tiers.md](decisions/2026-10-11-offer-tiers.md).

[brain/07-offers/04-free-front-door.md](brain/07-offers/04-free-front-door.md) and [QUESTIONS.md](QUESTIONS.md) Q7: one meaning is Brain depth (Smart 10, a data pack, 100 inputs). The other is the site's offer tiers. The question is still open. The offers file also says which AI products are real versus concepts is open, under the same Q7.

## 26. Stale law path inside the Brain

**CLOSED 2026-10-11.** Decision: [decisions/2026-10-11-laws-path.md](decisions/2026-10-11-laws-path.md).

Several Brain files still point at `team/LAWS.md` or say "LAWS.md". The moved file is [team/01-laws.md](team/01-laws.md). Examples: [brain/09-rules-of-engagement/05-approvals.md](brain/09-rules-of-engagement/05-approvals.md) and [brain/09-rules-of-engagement/04-how-ai-works-for-me.md](brain/09-rules-of-engagement/04-how-ai-works-for-me.md). The source text was left as written.

## Gaps (sources that were named and not in the archive)

1. Live skill bodies. Nine cards are under `skills/<id>/SKILL.md`. The original files (under `/home/box/agent-data/workflows/` and the Leigh book paths) were not in the archive.
2. Draft and Parked skill bodies. Index lines only, on purpose. Their original paths are in `skills/skills.json`.
3. AI publishing workflow, cited as `/workspace/strategy/ai-publishing-workflow.md`. See [workflows/README.md](workflows/README.md).
4. Minimum Buttons Rule, cited as `/workspace/ops/MINIMUM-BUTTONS-RULE.md`. Not the same file as `rules/CTA-NEW-TAB.md`.
5. `machine/` (systems map and scorecard). Team law 8, the Captain card, the Lead card, and the Scorekeeper card point at `machine/01-systems.md` and `machine/02-scorecard.md`. [sources/PROPOSED-STRUCTURE.md](sources/PROPOSED-STRUCTURE.md) says those files were not drafted in the Trevor copy.
6. `memory/DECISIONS.md`, `memory/CORRECTIONS.md`, and `memory/INPUTS.md`. Named by the Brain readme and the proposed structure. Not created. Decisions that had source text went to `decisions/`. `memory/DECISIONS.md` is no longer needed: decisions live in `decisions/` (item 16).
7. `install/` (load instructions and generated paste bundles). Not in the archive's Trevor draft. [sources/INVENTORY.md](sources/INVENTORY.md) says the paste bundles should be regenerated, not hand-edited.
8. `team/07-skills/`. In the proposed structure. Absent from the Team draft. Skills sit at `skills/` per the sync plan. No longer a gap: skills live in `skills/` (item 17).
9. "Robyn's channel written by her media person." Named in Phase 1 of the sync plan. No source paragraph in the archive.
10. A locked "Crazy Cranes kept separate" decision. The Brain describes the family channel as its own brand and says viewers, not clients. Spelling is unverified. No decision file was added. Closed: [decisions/2026-10-11-family-channel.md](decisions/2026-10-11-family-channel.md).
11. Alfred's active card. Phase 1 asks for one. The names-not-in-use file parks Alfred. No Captain line was in the archive. No card was added. Closed: no Alfred card ([decisions/2026-10-11-parked-names.md](decisions/2026-10-11-parked-names.md)).
12. Branches left where they are. `epic-team-v05-rollout-20260923` (draft PR #1) holds the v0.5 operating package, an Aug 28 Trevor Brain snapshot under `brain-sources/`, and `runtime/alfred/`. `copycat-shared-learning-20260924` (draft PR #2) is stacked on that. `epic-team-v2-review-20260925` has no PR. Those trees were not merged and were not diffed against this Brain. This compile branched from `main`.
13. [fleet-os/GROKBOT_OS.md](fleet-os/GROKBOT_OS.md) says the full Epic OS refresh (Tango bus, connector reconnect, Robyn OS, and the rest of that note) is still owed.
14. [QUESTIONS.md](QUESTIONS.md) is still the open list, including the top 10. Design has no approved palette (Q36). Standing authority for publish, send, or spend is unwritten (Q32).
15. [rules/LOOK-BEFORE-YOU-ASK.md](rules/LOOK-BEFORE-YOU-ASK.md) says the check is not done until a blind test passes. The file also says a copy on GitHub is not the check.
16. Sync plan blockers that are outside this repo: the Tango worker key, and Epic OS bot write access to `trevorcrane/epic-ai-os`. The plan's section 8 describes both. No key was copied.
