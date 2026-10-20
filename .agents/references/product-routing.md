# Product Routing Map

This file is loaded in Phase 0 of `full-audit`. It maps article paths to the
correct portal and Jira metadata. Use the longest matching prefix.

---

## Section A — Portal routing

Match on the article path prefix (longest match wins).

| Article path prefix | Portal | URL | Login method |
|---------------------|--------|-----|--------------|
| `hosting/virtual-servers/manage/` | VMmanager 6 | https://sqr-v6.vm.gcore.com | Via BillMgr: Products/Services → Virtual private servers → select row → **To panel**. Auto-login. |
| `hosting/dedicated-servers/manage/` | DCImanager | (URL appears after server is provisioned) | Via BillMgr: Products/Services → Dedicated servers → select row → **To panel**. Auto-login. |
| `hosting/` | BillMgr | https://hosting.gcore.com/billmgr | The user logs in manually in the isolated browser session |
| `cloud/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow — see `.agents/references/mcp-tools/playwright.md` |
| `cdn/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `dns/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `storage/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `waap/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `edge-ai/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `fastedge/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `streaming/` | Gcore Customer Portal | https://portal.gcore.com | SSO flow |
| `reseller-support/` | Admin Portal (Reseller) — BLOCKED, see note below | https://admin.gcore.top/ | SSO flow — Work domain `gcore.com` reaches a **Gcore internal staff superadmin console** (all resellers, all accounts, employee RBAC, feature toggles), not a single reseller's own scoped view. Do not use this login for regression-testing reseller-facing articles until a real reseller-scoped account or an impersonation path is confirmed. |
| `reseller/` (future) | Reseller Portal | TBD | TBD |
| `box/` (future) | Box Portal | TBD | TBD |

**No matching prefix:** `account-settings/`, `developer-tools/`, `ddos-protection/`, `gclaw/`, `edge-proxy/`, `colocation/`, and `api-reference/` have no routing yet. If the article path matches no row, stop and ask the user for the portal and Jira values. Do not guess them.

**Longest-match rule:** `hosting/virtual-servers/manage/` takes priority over `hosting/`.
If the article path starts with `hosting/virtual-servers/manage/`, use VMmanager 6 — not BillMgr.

### BillMgr sub-panel notes

- **VMmanager 6** is reached through BillMgr (no separate credentials).
  If `_private/planning/hosting-account-map.md` exists, load it for full navigation details.
- **DCImanager** is only available when a Dedicated Server is active.
  If no dedicated server is provisioned, stop and report the blocker.

---

## Section B — Jira routing

Use the ORG_UNIT as the `--org-unit` argument of `.agents/tools/create_jira_ticket.py` in Phase 4.

| Article path prefix | ORG_UNIT | ORG_UNIT label |
|---------------------|----------|----------------|
| `hosting/` | 16036 | Cloud |
| `cloud/` | 16036 | Cloud |
| `storage/` | 16036 | Cloud |
| `api-reference/` | 16036 | Cloud |
| `cdn/` | 16037 | Edge Network |
| `streaming/` | 16037 | Edge Network |
| `dns/` | 16037 | Edge Network |
| `fastedge/` | 16037 | Edge Network |
| `waap/` | 16035 | Security |
| `ddos-protection/` | 16035 | Security |
| `edge-proxy/` | 16035 | Security |
| `edge-ai/` | 16034 | AI |
| `account-settings/` | 16038 | Platform/Web |
| `developer-tools/` | 16038 | Platform/Web |
| `gclaw/` | 16038 | Platform/Web |
| `colocation/` | 16038 | Platform/Web |
| Repository tooling: `.claude/`, `.agents/`, `.cursor/`, `.github/`, `scripts/`, `AGENTS.md`, `CLAUDE.md`, `README.md`, `CONTRIBUTING.md` | 16038 | Platform/Web |

The five Org Unit options of the Jira field `Org Unit` (`customfield_14411`): 16034 AI, 16035 Security, 16036 Cloud, 16037 Edge Network, 16038 Platform/Web. Issue type `12504` is `Documentation`.

**Assignee:** always `sergey.kostichev@gcore.lu`. It is the script default, so do not pass `--assignee`.

**Epic:** do not set an epic and do not add a "relates to" link. Epics are temporary: each one belongs to a period of work, and an old epic put into a new ticket is wrong. Pass `--epic` or `--link-to` only when the user names an epic or an issue for the current batch.

**Issue type:** `12504` (the script default).

---

## How to apply this in Phase 0

1. Read the article path (e.g. `hosting/account-management/users/configure-user-rights.mdx`).
2. Strip the `.mdx` extension and match against the prefix table above (longest match).
3. Record:
   - `portal_type` — the portal name (BillMgr / VMmanager 6 / DCImanager / Gcore Customer Portal)
   - `portal_url` — the URL to navigate to
   - `login_method` — how to authenticate
   - `jira_org_unit` — the ORG_UNIT value for the ticket script
4. Use `portal_type` and `login_method` in Phase 1 instead of the hardcoded SSO flow.
5. Use `jira_org_unit` in Phase 4 as the `--org-unit` argument of `create_jira_ticket.py`.
