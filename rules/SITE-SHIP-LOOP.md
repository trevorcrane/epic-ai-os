# Site ship loop (Epic team SOP)

Locked 2026-10-04. Owner: Elon. Builder follows this on the next site.

## Why
The Clone Your Client page at https://cyc-script.netlify.app/ shipped with every outbound link opening twice. The page set target="_blank" and also called window.open. Builder: Sites fixed and republished it the same day. It should not have been called done before a reviewer clicked the links.

## Who does what
The writer does not publish. On Trevor's pages that is Cat: Trevor. On client pages it is Cat: Dr. Leigh or Cat: Robyn CYC. The handoff names which one.

Builder: Sites builds the page and ships it. Builder does not call it done.

Reviewer scores the live page and returns one verdict: pass, changes required, or blocked. The bar is 95. Do not round up. Reviewer does not accept the work. Trevor does.

Elon makes sure this loop happens. Elon does not send Trevor a second report when the builder is already reporting to him.

## Definition of done
A site is done only when Reviewer has checked all of these:

- One click, one new tab. Reviewer clicks each outbound control once and counts tabs. Pass is exactly one new tab. Landing on the right page is not enough, because a second tab is what the Clone Your Client page hid. Use target="_blank" and rel="noopener". Do not also call window.open.
- Same-page anchors and controls that are not outbound stay as they are.
- No broken links.
- Design and layout are checked.
- Phone menu. On a phone-width screen, open the top nav, including any dropdown or submenu. Tap a link. The menu must close. It must not stay open over the page. Also open it, then tap away, scroll, or tap another nav item. No stuck overlay. Reading the page underneath must still be possible.
- Nothing else on the page is broken.

Ship functional work. A page that has not been clicked through by Reviewer is not ready for Trevor to accept.

A republish is a new ship. This file does not store job status.

A new session says which instruction version it loaded. A published website does not update agents by itself.


## Hosting (locked 2026-10-05)
New builder deploys and previews go to **Cloudflare Pages Direct Upload**. Do not use Netlify for new ships. Netlify credits are nearly exhausted (~192 production deploys). SoT: rules/CLOUDFLARE-PAGES-STANDARD.md

## Launch QC
On every launch, Reviewer also uses rules/LAUNCH-QC-CHECKLIST.md. That list covers phone-width nav close, new-tab links, clicking every link on desktop and mobile, no invented or unlabeled placeholders, bonus names, exact credentials, dates and Zoom when claimed, sample and mock labels, SNAP and RAD before GHL go-live, and approved emails before send.

## Source
Link rule: rules/CTA-NEW-TAB.md
This file: rules/SITE-SHIP-LOOP.md
