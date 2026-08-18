# STEP 0 ACCESS STATUS v1

Updated: 2026-08-17
Owner: Jay / Hermes
State: WORKS NOW NOT PERMANENT

## Done and proven

- Robyn GHL access is working through scoped key.
  - MCP server: `ghl-robyn`
  - Location: Robyn Crane CFP
  - Location ID: `lVrhjOEgaQSUZoNbuDVm`
  - Proof: Hermes pulled live contact data and location data from this sub-account.

- Epic GHL access is working through scoped key.
  - MCP server: `ghl-epic`
  - Location: Epic Author Publishing
  - Location ID: `iunBLWtvwXGJqcUoci06`
  - Proof: Hermes pulled live contact data and location data from this sub-account.

- The two GHL connections resolve to different sub-accounts, not the same account twice.

- GitHub access for Hermes works.
  - Repo: `trevorcrane/epic-ai-os`
  - Proof: Hermes created the private repo and pushed to `main`.

## Blocked

- Tailscale is installed on the iMac but not authenticated.
- Blocker: local macOS admin password is required to finish Tailscale setup.
- Required owner: whoever normally logs into the iMac, or someone physically at the iMac with admin access.
- Next action: provide the local admin password to Jay through a secure channel or have the local admin run the final Tailscale command directly. Then Trevor approves login as `trevor@epic.media`.

## Follow-up risk

- Epic's GHL sub-account already had a pre-existing Hermes Agent key with broad scope, including payment collection and contract sending.
- Jay left it untouched and created a separate scoped key for tonight's work.
- Not urgent tonight. Audit later before money-touching or contract-sending automations are activated.
