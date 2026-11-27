---
product: API
status: Include
release_date: 2026-11-27
published_page: null
---

# api.gcore.com and gcore.com accept only TLS 1.2 and TLS 1.3

Customer change: HTTPS connections to api.gcore.com and gcore.com complete only with TLS 1.2 or TLS 1.3. A client that offers only TLS 1.0 or TLS 1.1 fails the handshake.
Affected users: API clients and visitors whose TLS stack stops at TLS 1.1. CDN resources keep their own TLS version setting.
Release evidence: On 2026-11-27 a production handshake to api.gcore.com and gcore.com on port 443 was refused for TLS 1.0 and TLS 1.1 (TLSV1_ALERT_PROTOCOL_VERSION) and succeeded for TLS 1.2 and TLS 1.3. ENOPS-1623 is Closed, and the engineer comment of 2026-09-22 says the same public endpoints already had legacy TLS disabled.
Open verification: none
Source tickets/PRs: DOC-3087, ENOPS-1623
Documentation links: api-reference/overview.mdx
Duplicate check: not found
Published entry: null
