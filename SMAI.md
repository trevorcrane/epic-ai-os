# SMAI DOMAIN PACK v1

WHAT IT IS
SMAI = Smart Marketing AI, our agency-level white-label of GoHighLevel.
Sub-accounts per business: Epic Media, Robyn Crane, future clients.

BUILD DOCTRINE
1. GREENFIELD on Robyn rebuilds. Old workflows are read-only reference.
   Extract tags, triggers, timing. Build new, clean, versioned.
2. KILL THE FLIP. Recurring events (webinars, PYFP) survive date changes by
   editing variables (dates, links, event IDs). NEVER by duplicating workflows.
   No step may depend on one human remembering something.
3. PAGES: all new funnel/replay/event pages are built with Claude Code,
   pushed to GitHub, deployed on Cloudflare Pages under owned domains.
   GHL keeps CRM, automations, tracking. No new GHL funnel pages.
4. CALENDAR: we are leaving AddEvent. New calendar invite system required
   (Director posts a 1-3-1 before choosing).
5. NATIVE FIRST: use GHL's built-in AI where it is stronger. External agents
   handle orchestration and improvement GHL cannot do alone.

NAMING AND TAGS
- Mission #M002's Director owns the master naming convention and tag taxonomy.
  All missions adopt it. Posted and pinned within 24 hours of launch.
- Workflow names: version first, plain words. Example: v1-robyn-webinar-signup.
- No orphan tags. Every tag documented at creation.

HANDOFF CONTRACTS
Mission handoffs are written contracts posted in the channel BEFORE building:
- Webinar -> PYFP purchase trigger tag (M002 + M003 Directors agree in writing)
- PYFP -> RAP enrollment trigger tag (M003 + M004 Directors agree in writing)
Nurture pause/resume logic is built ONCE (in M002) and reused everywhere.

TESTING STANDARD
Every workflow: test contact in, every action fires, both branches verified
where branches exist, proof (screenshot or log) posted in the channel.
Recurring-event workflows must ALSO survive a simulated date change with
zero duplication before DONE AND PERMANENT.

INFRASTRUCTURE
Hermes + n8n live on the office iMac. Remote access via Tailscale (Jay owns).
Metrics land where Operator (Len) and Trevor can see them.
