# Buttons and outbound CTAs open in a new tab (Epic Team FLEET LAW)

Locked 2026-10-02 from Trevor. Context: Depleted Brain thank-you page bonus button and Amazon buttons.

## Rule
Buttons and outbound calls to action open in a new window or tab by default.

Use `target="_blank"` and `rel="noopener"` on those links.

Same-page anchors and in-app controls that are not outbound stay as they are.

This stands unless Trevor says otherwise for a specific link.

## SoT
`/workspace/ops/rules/CTA-NEW-TAB.md`

## Open once
Do not also call window.open on a link that already has target="_blank". One or the other. Outbound links use the attribute, not both. A page that opens links twice is not done.
