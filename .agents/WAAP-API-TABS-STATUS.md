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
| 1 | waap-policies/waf-and-owasp-top-threats.mdx | OK | OK | OK | OK | View: 18 rules. Toggle: Open redirect flip+revert. Portal: LLM Attack confirmed in portal (Disabled). Added to Portal tab table + Info block. Response-blocking note added to API tab. Committed b5eee831. |
| 2 | waap-policies/behavioral-waf.mdx | OK | OK | OK | OK | View: 4 rules (S3008901-S3008904). Toggle: Repeated violations flip+revert. Portal: 4 rules, states match. No changes needed. |
| 3 | waap-policies/known-bots.mdx | OK | OK | OK | OK | 136 bots confirmed. Fixed unused waap import in Go SDK View tab. Portal nav: Bot Management > Known Bots. |
| 4 | firewall/ip-reputation.mdx | OK | OK | OK | OK | 8 policies. All tests pass. Removed unused waap import from Go SDK View tab. Portal: WAAP > Firewall > IP Reputation tab confirmed. Note: waap-policies/ip-reputation.mdx is an unused duplicate — not in docs.json. |
| 5 | waap-policies/cms-protection.mdx | OK | OK | OK | OK | 8 policies. View+Toggle+Allowlist all pass. Portal: WAAP > Default Rules > CMS Protection. Toggle Warning added. Table simplified. Portal Info block aligned with API description. |
| 6 | waap-policies/anti-automation-and-bot-protection.mdx | OK | OK | OK | OK | 8 policies. All pass. Portal: WAAP > Bot Management > Bot Attacks. Toggle Warning added. Table simplified with Action explanation (Block/Captcha/Handshake). |
| 7 | waap-policies/advanced-api-protection.mdx | OK | OK | OK | OK | 7 policies. All pass. Portal: WAAP > API Protection confirmed. Toggle Warning added. Table simplified. FLAG: Portal section describes only 5 of 7 policies (missing Service protocol validation + Prevent malformed request methods). |
| 8 | waap-policies/protocol-validation.mdx | OK | OK | OK | OK | 2 policies (S3008978, S3008980) in advanced-api-protection rule set. S3008978=enabled, S3008980=disabled. Fixed: removed "both enabled by default" claim, corrected Default state for S3008980 to Disabled, added Warning block for Toggle, aligned View response description. Portal: WAAP > Bot Management > Bot Attacks. |
| 9 | getting-started/configure-waap-for-a-domain.mdx | OK | OK | OK | OK | No POST /waap/v1/domains: domain auto-created via CDN API. WAAP API covers: GET /waap/v1/domains (list + domain_id), PATCH /waap/v1/domains/{id} status: active=Protection, monitor=Monitoring. PATCH returns empty body. Portal uses "Protection"/"Monitoring", API uses "active"/"monitor". |
| 10 | getting-started/manage-domains.mdx | OK | OK | OK | OK | GET /waap/v1/domains/{id} (domain status). DELETE /waap/v1/domains/{id} (requires bypass via CDN API). PATCH bypass=422 confirmed. Portal/API status mapping table added. Committed 12d69023. |
| 11 | response-pages/create-custom-response-pages.mdx | OK | OK | OK | OK | POST /waap/v1/custom-page-sets. Page set params table (block/captcha/browser_validation/enable_cookies/enable_javascript/block_csrf). Go SDK uses gcore.String() for optional fields. Jira: DOC-1500. |
| 12 | response-pages/manage-custom-response-pages.mdx | OK | OK | OK | OK | GET /waap/v1/custom-page-sets (list), PATCH /{set_id} (update content + domains), DELETE /{set_id}. PATCH/DELETE return 204. block.text min 20 chars. Jira: DOC-1501. |
| 13 | api-discovery-and-protection/configure-api-base-path.mdx | OK | OK | OK | OK | GET /waap/v1/domains/{id}/settings (api.is_api + api.api_urls). PATCH 204 for add/remove/set-as-api. api_urls replaces full list. is_api=true makes api_urls ignored. gcore.Bool() for Go SDK. Jira: DOC-1503. |
| 14 | analytics/events.mdx | OK | OK | OK | OK | GET /waap/v1/analytics/requests (full filter set). GET /waap/v1/domains/{id}/requests/{id}/details (curl only, no SDK). pattern_matched_tags = Portal Tags. optional_action=challenge = JS Challenge. Jira: DOC-1504. |
| 15 | firewall/ip-allowlist-and-blocklist.mdx | OK | OK | OK | OK | Renamed from access-control. access-control.mdx converted to conceptual overview. CRUD: List/Create/Update/Toggle/Delete. negation=true maps to Equality=Not. Update example: allow->block (compromised IP). toggle action=enable/disable (not toggle). PATCH+DELETE return 204. Jira: DOC-1505. |
| 16 | waap-policies/invalid-user-agent-and-unknown-user-agent.mdx | OK | OK | OK | OK | S3008869 (Invalid user agent, Block, Enabled) + S3008870 (Unknown user agent, Handshake, Enabled). Both in anti-automation-bot-protection ruleset. GET /rule-sets filtered to 2 IDs. PATCH /policies/{id}/toggle returns {"mode": bool}. Cross-ref to anti-automation article in both tabs. Commit: 745060ec. Jira: DOC-1506. |
| 17 | waap-rules/custom-rules.mdx | OK | OK | OK | OK | Full CRUD: List/Create/Update/Toggle/Delete + bulk_delete. Name pattern ^[A-Za-z0-9\s.:'";<>?&|\\]+$ (no hyphens). country_code=array, match_type capitalized ("Exact"/"Contains"/"Regex"). JS Challenge = handshake in API. Toggle: PATCH /{id}/enable|disable, 204 no body. Bulk delete: POST /bulk_delete with rule_ids=[int]. Tag names: letters/numbers/spaces only. PATCH/DELETE → 204 no body. CREATE → 201 + rule object. Python SDK: delete_multiple() not bulk_delete(). Go SDK: New() not Create(). Action/condition reference in Accordion. Structure B. |
| 18 | waap-rules/advanced-rules.mdx | OK | OK | OK | OK | API-only feature (no portal create). No MethodSwitch. Added Python SDK + Go SDK Tabs to all 5 existing curl examples. Added List/Update/Toggle/Delete sections. All ops verified live: CREATE→201, GET/LIST→200 paginated, PATCH/DELETE/toggle→204 no body. rate_limit CEL confirmed working. Toggle: "enable"/"disable" as first arg same as custom-rules. Go SDK: New() not Create(). |
| 19 | waap-rules/advanced-rules/advanced-rate-limiting-rules.mdx | OK | OK | OK | OK | API-only. No MethodSwitch. Added Python SDK + Go SDK Tabs to all 7 curl examples: cookie exclusions, ip_list, additional conditions, complex URL regex, ip_in_range, cluster scope (method_list+status_list+content_type), tag filter. All 7 verified live (201 OK). CRUD ops not duplicated — linked to parent advanced-rules.mdx. |
| 20 | api-discovery-and-protection/api-discovery.mdx | TODO | TODO | TODO | TODO | MISSED. Full CRUD for API paths: GET/POST /waap/v1/domains/{id}/api-discovery/paths, GET/PATCH/DELETE /{path_id}. Upload Swagger: POST /upload, POST /scan. Settings: GET/PATCH /api-discovery/settings. Scan results: GET /scan-results. |
| 21 | threat-intelligence/security-insights/view-insights.mdx | TODO | TODO | TODO | TODO | MISSED. GET /waap/v1/domains/{id}/insights (list with filters). GET /domains/{id}/insights/{id}. GET /waap/v1/security-insights/types. InsightStatus enum: OPEN/ACKED/CLOSED. |
| 22 | threat-intelligence/security-insights/manage-insights.mdx | TODO | TODO | TODO | TODO | MISSED. PUT /waap/v1/domains/{id}/insights/{id} (update status: ACKED=read, CLOSED=close, OPEN=reopen). POST /waap/v1/domains/{id}/insight-silences (create silence with insight_type + labels). |
| 23 | threat-intelligence/security-insights/manage-silence-rules.mdx | TODO | TODO | TODO | TODO | MISSED. GET /waap/v1/domains/{id}/insight-silences (list). PATCH /insight-silences/{id} (update duration/labels). DELETE /insight-silences/{id} (unsilence). |
| 24 | ip-security/ip-spotlight.mdx | TODO | TODO | TODO | TODO | MISSED. Multiple GET /waap/v1/ip-info/* endpoints: /ip-info (comprehensive IP data), /counts, /blocked-requests, /attack-time-series, /top-attacks, /top-urls, /top-user-agents, /top-domains, /top-sessions, /attack-map, /ddos. v2 scoped endpoints also available. |

---

## Confirmed no API tab needed

| Article | Reason |
|---------|--------|
| overview.mdx | Product overview, no actionable API operations |
| waap-policies.mdx | Index/overview page |
| waap-rules.mdx | Index/overview page |
| analytics/waap-analytics.mdx | 3-line index pointing to sub-pages |
| analytics/domains.mdx | Conceptual navigation guide, no API operations |
| api-discovery-and-protection.mdx | Parent overview page |
| api-discovery-and-protection/configure-api-access-with-reserved-tags.mdx | Tutorial for creating custom rules via Portal; API operations are covered by custom-rules article (#17) |
| firewall/access-control.mdx | Converted to conceptual overview, no procedures |
| firewall/check-ip.mdx | Portal-only feature; no dedicated check-IP endpoint in waap_api.yaml |
| getting-started/billing.mdx | Billing/plan information, no API operations |
| ip-security.mdx | Parent overview page |
| ip-security/ip-spotlight-b.mdx | Variant/duplicate of ip-spotlight.mdx |
| response-pages.mdx | Parent overview page |
| threat-intelligence/ip-spotlight-b.mdx | Variant/duplicate of ip-spotlight.mdx |
| threat-intelligence/security-insights/security-insights.mdx | 5-line overview pointing to sub-pages |
| troubleshooting.mdx | Troubleshooting guide, no API operations |
| troubleshooting/enable-troubleshoot-bot-protection.mdx | Troubleshooting guide |
| troubleshooting/troubleshoot-5xx-errors.mdx | Troubleshooting guide |
| troubleshooting/troubleshoot-blocked-users.mdx | Troubleshooting guide |
| frequently-asked-questions.mdx | FAQ index |
| frequently-asked-questions/javascript-injection.mdx | FAQ |
| frequently-asked-questions/storage-variables.mdx | FAQ |
| frequently-asked-questions/waap-cookies.mdx | FAQ |
| waap-rules/advanced-rules/advanced-rule-objects.mdx | Reference table only |
| waap-rules/advanced-rules/source-field-objects.mdx | Reference table only |
| waap-rules/custom-rules/tag-rules.mdx | Conceptual + Portal guide; API operations covered by custom-rules (#17) |
| waap-rules/custom-rules/tag-rules/predefined-tags.mdx | Reference table only |
| waap-rules/custom-rules/tag-rules/reserved-tags.mdx | Reference table only |
|| analytics/dashboard.mdx | Read-only analytics endpoints only. User can find them in API Reference. No SDK examples add value. |
|| ddos-protection.mdx | Read-only endpoints only. Thresholds configurable by support only, not via API. No SDK examples add value. |

NO needed:
| 20 | analytics/dashboard.mdx | TODO | TODO | TODO | TODO | MISSED. GET /waap/v1/analytics/traffic, /analytics/traffic-filtered, /analytics/stats/{dimension}. Domain-level: GET /waap/v1/domains/{id}/requests. Maps to Dashboard widgets (total requests, detected/prevented attacks, timeline). |
| 21 | ddos-protection.mdx | TODO | TODO | TODO | TODO | MISSED. View: GET /waap/v1/domains/{id}/ddos-info, GET /domains/{id}/ddos-attacks. Configure thresholds: PATCH /waap/v1/domains/{id}/settings with ddos key (global_threshold, burst_threshold). DomainDdosSettings schema confirmed in spec. |