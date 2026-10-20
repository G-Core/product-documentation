---
product: WAAP
status: Include
release_date: 2026-10-12
published_page: null
---

# WAAP SDK rule sets and policy updates

Customer change: Python and Go SDK v0.59.0 return domain rule sets as a page without embedded rules. Rules are listed with policies.list filtered by rule_set_id. The list is paginated, with a maximum of 100 rules per page. Enabling or disabling a domain policy uses policies.update with mode, not policies.toggle.
Affected users: Customers who list WAAP policy groups or enable and disable those policies with the Python or Go SDK
Release evidence: Python SDK v0.59.0 published 2026-10-12. Production calls listed rule sets, listed policies for the OWASP and known-bots groups (109 rules across pages, including Google Bot), and sent a no-op policy update that returned the same mode. The same list and no-op update compiled and ran with Go SDK v0.59.0. REST v1 still returns rule sets with embedded rules.
Open verification: none
Source tickets/PRs: https://github.com/G-Core/product-documentation/issues/3165
Documentation links: waap/waap-policies/waf-and-owasp-top-threats.mdx, waap/waap-policies/behavioral-waf.mdx, waap/waap-policies/protocol-validation.mdx, waap/waap-policies/cms-protection.mdx, waap/waap-policies/invalid-user-agent-and-unknown-user-agent.mdx, waap/waap-policies/advanced-api-protection.mdx, waap/waap-policies/anti-automation-and-bot-protection.mdx, waap/waap-policies/known-bots.mdx, waap/firewall/ip-reputation.mdx
Duplicate check: not found
Published entry: null
