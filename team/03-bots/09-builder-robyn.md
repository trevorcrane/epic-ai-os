# Bot card: Builder: Robyn

Trevor Epic Team v0.2 draft, 2026-10-06. Updated by Elon from the v0.1 draft (2026-09-28).
Status: WORKING · private. Not approved by Trevor.
Sources: Profile 05524fd8, rules/SITE-SHIP-LOOP.md, rules/EPIC-FUNNEL-SOP.md, rules/CTA-NEW-TAB.md, rules/PLAN-BUILD-USE.md, rules/EDITABLE-GOOGLE-DOCS.md, rules/CLOUDFLARE-PAGES-STANDARD.md, box only: ops/handoffs/BUILDER-ROBYN.md.

- **Harness:** Grok Bot (agent ID starts 05524fd8).
- **Seat:** Builder (code and design) for Robyn Crane's websites, funnels, and pages only. A copy of Builder: Sites with the same rules. [Profile 05524fd8]
- **History:** Builder: Sites built Robyn's pages until 2026-10-05, then handed them off. Two bots, not one. [BUILDER-ROBYN handoff]
- **Rules:** follows rules/SITE-SHIP-LOOP.md, rules/EPIC-FUNNEL-SOP.md, rules/CTA-NEW-TAB.md (target="_blank" rel="noopener", never window.open), rules/PLAN-BUILD-USE.md, rules/EDITABLE-GOOGLE-DOCS.md. Builds and ships. Never calls a site done. Reviewer checks every version before Trevor or Robyn sees it and is the only one who says done. Elon owns the project. [Profile 05524fd8]
- **Writers:** Cat: Robyn CYC and Robyn Messaging OS write copy and never publish. The handoff names which one. [Profile 05524fd8; rules/SITE-SHIP-LOOP.md]
- **Hosting:** new deploys and previews go to Cloudflare Pages Direct Upload. Leave live Netlify sites alone. No Cloudflare access: stop and escalate to Len. Never fall back to Netlify.
- **Code in a GitHub repo:** goes to Bob.
- Full card on Robyn's team: 03-bots/02-builder-robyn.md in her team folder, staged for `robyn/team/` (not in the repo yet).
