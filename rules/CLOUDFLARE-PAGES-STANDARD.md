# Cloudflare Pages Direct Upload = fleet hosting standard

Locked 2026-10-05 by Trevor. Owner: Elon.

## Rule
All rapid AI / builder site deploys use **Cloudflare Pages Direct Upload**.

Do **not** use Netlify for new production or preview deploys.

## Why
Netlify production deploys burn credits. As of 2026-10-05 Trevor was almost out: about 192 production deploys used ~2,880 of 3,000 credits.

Cloudflare Pages Direct Upload: unlimited static builds for this use, no Netlify credit drain, and Epic already uses Cloudflare.

## Who must follow
Builder: Sites, Builder: Robyn, Builder: Dr. Leigh, and any other agent that ships HTML/static sites or previews.

Reviewer expects preview and live URLs on Cloudflare Pages (or an existing custom domain already on Cloudflare), not new `*.netlify.app` ships.

## Existing Netlify URLs
Leave live Netlify sites alone until a cutover is asked for. New ships and remounts go to Cloudflare Pages Direct Upload. When remounting a temporary or preview site, remount on Cloudflare, not Netlify.

## How (Direct Upload)
1. Build static output locally (or on the box).
2. Deploy with Cloudflare Pages Direct Upload (`wrangler pages deploy` or the Pages Direct Upload API) to a project under Epic's Cloudflare account.
3. Hand Reviewer the Cloudflare preview/production URL.
4. Custom domains stay on Cloudflare DNS when cut over.

Exact account/project naming lives with Len / site folders. If you lack Cloudflare access, stop and escalate to Len — do not fall back to Netlify.

## Related
- Site ship loop: rules/SITE-SHIP-LOOP.md
- This file: rules/CLOUDFLARE-PAGES-STANDARD.md

## Access (blocker until Len completes)
Builders need one of:
1. **Preferred:** box secrets `CLOUDFLARE_API_TOKEN` (Account > Cloudflare Pages > Edit) and `CLOUDFLARE_ACCOUNT_ID`.
2. **Fallback:** Len signs `wrangler` in once on the shared box.

Until one of those is done, do not deploy and do not fall back to Netlify. Escalate to Elon / Len.

Project naming: Len decides; default draft until then is `epic-{client-or-site}-{page}`.

