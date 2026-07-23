# Product Routing Map

This file is loaded in Phase 0 of `regression-test`. It maps article paths to the
correct portal and Jira metadata. Use the longest matching prefix.

---

## Section A — Portal routing

Match on the article path prefix (longest match wins).

| Article path prefix | Portal | URL | Login method |
|---------------------|--------|-----|--------------|
| `hosting/virtual-servers/manage/` | VMmanager 6 | https://sqr-v6.vm.gcore.com | Via BillMgr: Products/Services → Virtual private servers → select row → **To panel**. Auto-login. |
| `hosting/dedicated-servers/manage/` | DCImanager | (URL appears after server is provisioned) | Via BillMgr: Products/Services → Dedicated servers → select row → **To panel**. Auto-login. |
| `hosting/` | BillMgr | https://hosting.gcore.com/billmgr | Credentials: `_private/access.md` lines 13–16 |
| `cloud/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow — see `.agents/references/mcp-tools/playwright.md` |
| `cdn/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `dns/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `storage/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `waap/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `edge-ai/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `fastedge/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `reseller/` (future) | Reseller Portal | TBD | TBD |
| `box/` (future) | Box Portal | TBD | TBD |

**Longest-match rule:** `hosting/virtual-servers/manage/` takes priority over `hosting/`.
If the article path starts with `hosting/virtual-servers/manage/`, use VMmanager 6 — not BillMgr.

### BillMgr sub-panel notes

- **VMmanager 6** is reached through BillMgr (no separate credentials).
  Load `_planning/hosting-account-map.md` for full navigation details.
- **DCImanager** is only available when a Dedicated Server is active.
  If no dedicated server is provisioned, stop and report the blocker.

---

## Section B — Jira routing

Use these values when filling `create_edge_cloud_regression_ticket.py` in Phase 4.

| Article path prefix | ORG_UNIT | ORG_UNIT label | EPIC | ISSUETYPE | ASSIGNEE |
|---------------------|----------|----------------|------|-----------|---------|
| `hosting/` | 16036 | Cloud | DOC-1701 | 12504 | sergey.kostichev@gcore.lu |
| `cloud/` | 16036 | Cloud | TBD | 12504 | sergey.kostichev@gcore.lu |
| `cdn/` | 16036 | Cloud | TBD | 12504 | sergey.kostichev@gcore.lu |
| `dns/` | 16036 | Cloud | TBD | 12504 | sergey.kostichev@gcore.lu |
| `storage/` | 16036 | Cloud | TBD | 12504 | sergey.kostichev@gcore.lu |
| `waap/` | 16035 | Security | TBD | 12504 | sergey.kostichev@gcore.lu |
| `edge-ai/` | 16036 | Cloud | TBD | 12504 | sergey.kostichev@gcore.lu |
| `fastedge/` | 16036 | Cloud | TBD | 12504 | sergey.kostichev@gcore.lu |

**TBD epics:** fill in the EPIC value before running the script for non-hosting products.
Check Jira for the current active epic for that product area.

---

## How to apply this in Phase 0

1. Read the article path (e.g. `hosting/account-management/users/configure-user-rights.mdx`).
2. Strip the `.mdx` extension and match against the prefix table above (longest match).
3. Record:
   - `portal_type` — the portal name (BillMgr / VMmanager 6 / DCImanager / Gcore Customer Portal)
   - `portal_url` — the URL to navigate to
   - `login_method` — how to authenticate
   - `jira_org_unit` — the ORG_UNIT value for the ticket script
   - `jira_epic` — the EPIC value (or TBD if not yet defined)
4. Use `portal_type` and `login_method` in Phase 1 instead of the hardcoded SSO flow.
5. Use `jira_org_unit` and `jira_epic` in Phase 4 when setting script constants.
