# WAAP API Tabs — Verification Status

<!-- TEMPORARY FILE. Delete this file before the final push and merge when all articles are verified. -->

## Testing legend

| Symbol | Meaning |
|--------|---------|
| OK | Tested live, works |
| FAIL | Tested live, fails |
| N/A | Not applicable |
| TODO | Not yet tested |

---

## Article status

| # | Article | curl | Python SDK | Go SDK | Comments |
|---|---------|------|------------|--------|----------|
| 1 | waf-and-owasp-top-threats.mdx | OK | OK | OK | View: 18 rules. Toggle: Open redirect flip+revert. All pass. |
| 2 | behavioral-waf.mdx | OK | OK | OK | View: 4 rules. Toggle: Repeated violations flip+revert. All pass. |
| 3 | known-bots.mdx | OK | OK | OK | View: 136 rules (fixed count 118->136). Toggle: Google Bot flip+revert. All pass. |
| 4 | ip-reputation.mdx | OK | OK | OK | Toggle was previously 401; now unblocked. View+Toggle all pass. |
| 5 | cms-protection.mdx | OK | OK | OK | View: 8 rules. Toggle+Allowlist all pass. Fixed: missing waap import in Toggle Go SDK. |
| 6 | anti-automation-and-bot-protection.mdx | OK | OK | OK | View+Toggle all pass. Fixed: unused waap import in View Go SDK (compile error). |
| 7 | advanced-api-protection.mdx | OK | OK | OK | View+Toggle all pass. Fixed: unused waap import in View Go SDK (compile error). |
| 8 | protocol-validation.mdx | OK | OK | OK | View+Toggle all pass. Fixed: unused waap import in View Go SDK; "A permanent" -> "An". |
