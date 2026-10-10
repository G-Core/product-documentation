# Phase 1 — Open the portal

Use `portal_type` and `login_method` recorded in Phase 0 to determine which portal
to open. The steps below differ by portal type.

## Open an isolated browser session first

**Before navigating to any portal**, open a new incognito window to get a clean,
isolated session that does not interfere with any other agent currently using the browser:

```javascript
// browser_evaluate — opens a new incognito window
window.open('about:blank', '_blank');
```

**Why this is required:** Playwright MCP runs a single browser process shared across
all agents running on the same machine. An incognito window is a separate context:
separate cookies, separate tabs, no cross-contamination.

**If you cannot open an isolated context** — stop and tell the user:
> "Playwright MCP is sharing a browser session with another agent. A separate
> incognito window is required to proceed safely. Please confirm the incognito
> window is open before I continue."

## Portal-specific login

**Gcore Customer Portal** (`portal_type = Gcore Customer Portal`)

Load `.agents/references/mcp-tools/playwright.md` now.

Follow the SSO login flow exactly, inside the isolated session:
1. Navigate to `https://auth.gcore.com/login/signin`
2. Click **SSO**
3. Enter `gcore.com` in the Work domain field and press Enter
4. Verify the browser is at `https://portal.gcore.com`

After login, select region **Luxembourg-3** from the region dropdown before starting
any steps. All required quotas are available in Luxembourg-3.

**BillMgr** (`portal_type = BillMgr`)

The agent never handles BillMgr credentials. If `_private/planning/hosting-account-map.md`
exists, load it for BillMgr navigation structure and active services.

1. Navigate to `https://hosting.gcore.com/billmgr` in the isolated session
2. Stop and ask the user to log in themselves in that window, then wait for confirmation
3. Confirm successful login by taking a screenshot of the BillMgr dashboard

**VMmanager 6** (`portal_type = VMmanager 6`)

VMmanager is reached through BillMgr — no separate login.

1. Log in to BillMgr as above
2. Navigate to Products/Services → Virtual private servers
3. Select the active VDS row
4. Click **To panel** in the toolbar
5. BillMgr opens VMmanager at `https://sqr-v6.vm.gcore.com` via token URL (auto-login)
6. Confirm access by taking a screenshot of the VMmanager dashboard

**DCImanager** (`portal_type = DCImanager`)

DCImanager is only available when a Dedicated Server is active.
If no dedicated server is provisioned — stop and report the blocker to the user.
Otherwise, follow the same BillMgr → Products/Services → Dedicated servers → **To panel** flow.

**Future portals** (`portal_type = Reseller Portal` / `Box Portal`)

Routing is TBD. Stop and tell the user the portal is not yet configured in
`.agents/references/product-routing.md`.
