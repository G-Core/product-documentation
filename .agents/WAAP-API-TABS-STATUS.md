# WAAP API Tabs — Verification Status

## Testing legend

| Symbol | Meaning |
|--------|---------|
| OK | Tested live, works |
| FAIL | Tested live, fails |
| N/A | Not applicable for this article |
| TODO | Not yet tested |

---

## Article status

| # | Article | curl | Python SDK | Go SDK | Comments |
|---|---------|------|------------|--------|----------|
| 1 | waf-and-owasp-top-threats.mdx | OK | OK | OK | Jira: DOC-1480 |
| 2 | behavioral-waf.mdx | OK | OK | OK | Jira: DOC-1481 |
| 3 | known-bots.mdx | OK | OK | OK | Jira: DOC-1482. Go SDK fix applied (range *ruleSets, DomainPolicyToggleParams) |
| 4 | ip-reputation.mdx | OK (View only) | OK (View only) | OK (View only) | **Toggle BLOCKED** — see below. Go SDK fix applied |
| 5 | cms-protection.mdx | OK | OK | OK | Jira: DOC-1484. Go SDK fix applied |
| 6 | anti-automation-and-bot-protection.mdx | OK | OK | OK | Go SDK fix applied |
| 7 | advanced-api-protection.mdx | TODO | TODO | TODO | Go SDK fix applied |
| 8 | protocol-validation.mdx | TODO | TODO | TODO | Go SDK fix applied |

---

## Go SDK fixes applied (articles 3–8)

Two bugs found in Go code by live compilation test:

**Bug 1:** `ListRuleSets` returns `*[]waap.WaapRuleSet` (pointer to slice).  
Wrong: `for _, rs := range ruleSets`  
Fixed: `for _, rs := range *ruleSets`

**Bug 2:** `Toggle` third argument must be `waap.DomainPolicyToggleParams`, not raw int64.  
Wrong: `client.Waap.Domains.Policies.Toggle(ctx, policyID, domainID)`  
Fixed: `client.Waap.Domains.Policies.Toggle(ctx, policyID, waap.DomainPolicyToggleParams{DomainID: domainID})`  
Also required adding `"github.com/G-Core/gcore-go/waap"` to imports.

Articles 1 and 2 (waf-and-owasp-top-threats, behavioral-waf) already had the correct signatures.

---

## BLOCKED: ip-reputation.mdx — Toggle

**Bug found:** Toggle endpoint returns `401 feature-check` for all IP Reputation policies.

**Root cause:** IP Reputation is a base Pro/Enterprise WAAP plan feature.  
Test domain `cdn-mcp-test.example.com` (id: 16870) does not have IP Reputation enabled.  
Known Bots and CMS Protection work because they are available as add-ons on the current plan.

**Action required:** Ask product head to upgrade domain id 16870 to Pro plan  
(enable IP Reputation for this domain via backend).

**What was verified:**
- View policy states: OK — 8 policies, all IDs confirmed correct
- Toggle: FAIL — 401 on all 8 IP Reputation policies
- Policy reference table: IDs confirmed correct via View policy states

**What needs re-verification after fix:**
- Toggle a policy (e.g. S3008894 TOR network): curl, Python SDK, Go SDK
