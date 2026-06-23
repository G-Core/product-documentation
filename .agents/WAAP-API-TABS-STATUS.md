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
| 1 | waf-and-owasp-top-threats.mdx | | | | |
| 2 | behavioral-waf.mdx | | | | |
| 3 | known-bots.mdx | | | | |
| 4 | ip-reputation.mdx | | | | Toggle BLOCKED — see below |
| 5 | cms-protection.mdx | | | | |
| 6 | anti-automation-and-bot-protection.mdx | | | | |
| 7 | advanced-api-protection.mdx | | | | |
| 8 | protocol-validation.mdx | | | | |

---

## BLOCKED: ip-reputation.mdx — Toggle

**Bug found:** Toggle endpoint returns `401 feature-check` for all IP Reputation policies.

**Root cause:** IP Reputation is a base Pro/Enterprise WAAP plan feature.
Test domain `cdn-mcp-test.example.com` (id: 16870) does not have IP Reputation enabled.
Known Bots and CMS Protection work because they are available as add-ons on the current plan.

**Action required:** Ask product head to upgrade domain id 16870 to Pro plan
(enable IP Reputation for this domain via backend).

**What needs re-verification after fix:**
- Toggle a policy (e.g. S3008894 TOR network): curl, Python SDK, Go SDK
