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

| # | Article | curl | Python SDK | Go SDK | Customer Portal | Comments |
|---|---------|------|------------|--------|-----------------|----------|
| 1 | waf-and-owasp-top-threats.mdx | OK | OK | OK | OK | View: 18 rules. Toggle: Open redirect flip+revert. Portal: LLM Attack confirmed in portal (Disabled). Added to Portal tab table + Info block. Response-blocking note added to API tab. Committed b5eee831. |
| 2 | behavioral-waf.mdx | OK | OK | OK | OK | View: 4 rules (S3008901-S3008904). Toggle: Repeated violations flip+revert. Portal: 4 rules, states match. No changes needed. |
| 3 | known-bots.mdx | OK | OK | OK | OK | 136 bots confirmed. Fixed unused waap import in Go SDK View tab. Portal nav: Bot Management > Known Bots. |
| 4 | ip-reputation.mdx | OK | OK | OK | OK | 8 policies. All tests pass. Removed unused waap import from Go SDK View tab. Portal: WAAP > Firewall > IP Reputation tab confirmed. |
| 5 | cms-protection.mdx | OK | OK | OK | OK | 8 policies. View+Toggle+Allowlist all pass. Portal: WAAP > Default Rules > CMS Protection. Toggle Warning added. Table simplified. Portal Info block aligned with API description. |
| 6 | anti-automation-and-bot-protection.mdx | OK | OK | OK | OK | 8 policies. All pass. Portal: WAAP > Bot Management > Bot Attacks. Toggle Warning added. Table simplified with Action explanation (Block/Captcha/Handshake). |
| 7 | advanced-api-protection.mdx | OK | OK | OK | OK | 7 policies. All pass. Portal: WAAP > API Protection confirmed. Toggle Warning added. Table simplified. FLAG: Portal section describes only 5 of 7 policies (missing Service protocol validation + Prevent malformed request methods). |
| 8 | protocol-validation.mdx | OK | OK | OK | OK | 2 policies (S3008978, S3008980) in advanced-api-protection rule set. S3008978=enabled, S3008980=disabled. Fixed: removed "both enabled by default" claim, corrected Default state for S3008980 to Disabled, added Warning block for Toggle, aligned View response description. Portal: WAAP > Bot Management > Bot Attacks. |
| 9 | getting-started/configure-waap-for-a-domain.mdx | TODO | TODO | TODO | TODO | |
| 10 | getting-started/manage-domains.mdx | TODO | TODO | TODO | TODO | |
| 11 | response-pages/create-custom-response-pages.mdx | TODO | TODO | TODO | TODO | |
| 12 | response-pages/manage-custom-response-pages.mdx | TODO | TODO | TODO | TODO | |
| 13 | api-discovery-and-protection/configure-api-base-path.mdx | TODO | TODO | TODO | TODO | |
