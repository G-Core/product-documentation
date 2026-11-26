---
product: WAAP
status: Include
release_date: 2026-11-26
published_page: null
---

# WAAP prebilling breakdown returns one entry per client

Customer change: The billable-consumption breakdown returns a list of clients. Each entry has client_id and items, and limit, offset, and count count clients. The previous clients map remains on the v1 route until Tue, 09 Feb 2027.
Affected users: Reseller API callers who read per-client WAAP consumption.
Release evidence: On 2026-11-26, production GET /waap/v2/prebilling/breakdown/requests returned HTTP 200 with results as a list, one client and nine daily items, and count 1. The same account's v1 call returned the clients map and Sunset Tue, 09 Feb 2027 00:00:00 GMT. The mounted reseller spec uses that page schema for /waap/reseller/v2/prebilling/breakdown/{metric}.
Open verification: none
Source tickets/PRs: DOC-3028, WS-3948
Documentation links: reseller-support/waap/waap-service-management.mdx
Duplicate check: not found
Published entry: null
