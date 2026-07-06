# DOC-1502 — JA3/JA4 TLS Fingerprinting: Research File

**Jira:** [DOC-1502](https://jira.gcore.lu/browse/DOC-1502)
**Epic:** [WS-3202](https://jira.gcore.lu/browse/WS-3202) JA4 Fingerprinting
**Assignee:** Sergey Kostichev
**Status:** To Do (Backlog)

---

## Dev ticket status (what is live vs. in QA)

| Ticket | Summary | Status |
|--------|---------|--------|
| EPX-99 | [nginx] Implement JA4 TLS and X-JA4 header to WAAP | Closed (Done) |
| EPX-101 | [core-proxy] Implement JA4 TLS and X-JA4 header to WAAP | Closed (Done) |
| WS-3208 | WAAP: add JA4 fingerprint support - Shield, ETL, and Events API | Done |
| WS-3413 | Expose ja4 field in GET /v1/analytics/requests | Done |
| WS-3372 | FE: add JA4 fingerprint field to rule builder | Done |
| WS-3371 | BE: JA4 fingerprint as condition in advanced rules | QA / IN PROGRESS |
| WS-3370 | FE: show JA4 fingerprint in event details and add filter in Events | QA / TODO |
| WS-3298 | [Spike] JA4 fingerprint variant selection and external feed compatibility | In Review |

**Key implication for docs — UPDATED after live testing (2026-06-25):**

Live testing against production API (`domain_id=16870`, prod token):

| Feature | Jira status | Live test result |
|---------|-------------|-----------------|
| JA4 in Events API response (`ja4` field) | Done (WS-3413) | Confirmed (field in RequestSummary spec) |
| JA4 in rule builder UI (FE) | Done (WS-3372) | Confirmed (descriptor v1.11 includes `request.ja4`) |
| JA4 as BE condition in advanced rules | QA (WS-3371) | **LIVE** — POST /waap/v1/domains/{id}/advanced-rules with `request.ja4` expression returned 201 |
| JA4 in Events UI detail panel + filter | QA (WS-3370) | Cannot confirm (no live traffic in test domain, portal session timeout) |
| JA4 filter in events API | Done (WS-3413) | **LIVE** — `?ja4=<value>` returns 200 with valid format |

**Advanced rules descriptor (v1.11) confirms:**
```json
{"name": "ja4", "type": "Var", "hint": "str", "description": "JA4 TLS client fingerprint"}
```
Both `request.ja3` and `request.ja4` are official attributes in the rule engine.

**JA4 format confirmed from API validation errors:**
- Pattern: `^[0-9a-zA-Z]{10}_[0-9a-fA-F]{12}_[0-9a-fA-F]{12}$`
- Example: `t13d1516h2_8daaf6152771_b1ff8ab2d16f`

**JA3 format (from OpenAPI spec):**
- Pattern: `^[0-9a-fA-F]{32}$` (32 lowercase hex chars)
- Example: `e7d705a3286e19ea42f587b344ee6865`

**CONCLUSION: Both JA3 and JA4 are fully live in prod for advanced rules and events API filtering.**
The only unconfirmed item is JA4 display in the Events UI detail panel (WS-3370), but the filter query param works.

---

## What JA3 and JA4 are

**From WS-3202 epic description:**

JA3 is a TLS client fingerprint — a hash computed from ClientHello attributes:
- TLS version
- Cipher suites
- Extensions
- Elliptic curves
- Elliptic curve point formats

JA3 limitations:
- Easily evaded by minor ClientHello modifications (e.g., field reordering)
- Limited reliability with TLS 1.3
- High variability — multiple fingerprints for the same client across sessions
- No extensibility beyond TLS for cross-layer correlation

JA4 benefits (why it was introduced):
- Normalizes handshake data to reduce variability
- Produces more stable fingerprints across sessions
- More resistant to fingerprint randomization and spoofing
- Based on more parameters than JA3
- Improves detection of automated and obfuscated clients
- Enables future multi-layer correlation (JA4 is a family — see below)

**JA4 is a family of fingerprints (from WS-3298 spike):**
- JA4 — TLS ClientHello (what we implement first)
- JA4S — TLS ServerHello
- JA4H — HTTP
- JA4L — Light/latency
- JA4X — X.509 certificates
- JA4T — TCP
- JA4TS — TCP server
- JA4SSH — SSH

Gcore implements JA4 (TLS ClientHello variant). Other variants are future scope.

---

## How it works in Gcore WAAP

From WS-3208 (tech description):

1. CDN proxy layer extracts JA3 and JA4 from TLS handshake (ClientHello) at the edge
2. Adds them as `X-JA3` and `X-JA4` headers
3. Shield (WAAP backend) reads the headers and stores them in ClickHouse logs
4. Events API (`GET /waap/v1/analytics/requests`) returns both `ja3` and `ja4` fields per event
5. Advanced Rules can use JA3 and JA4 as condition fields
6. Rule builder UI exposes JA4 in the field picker

---

## Real incident case (from dev call transcript)

A gaming client was attacked:
- Volume: ~1.5 billion requests
- Botnet: ~2,200 IPs, only 5 User-Agents
- Attack distributed across many countries and subnets
- Bots were mimicking a real browser

Why standard mitigations failed:
- IP-based blocking: too many unique IPs, would cut off real traffic
- User-Agent blocking: only 5 UAs, but bots mimicked real browsers
- Subnet blocking: too many subnets, would affect real clients
- Rate limiting: distribution too broad

Solution: ~99% of attack traffic shared a single JA3 fingerprint. Engineers created one Advanced Rule with a JA3 condition → the entire 1.5B-request botnet was mitigated.

**This is the key worked example for the article.**

---

## API fields (from waap_api.yaml)

### Events API filter (`GET /waap/v1/analytics/requests`)

`ja3` query parameter:
- Type: string
- Pattern: `^[0-9a-fA-F]{32}$` (exactly 32 hex characters, case-insensitive)
- Description: "Filter by JA3 TLS client fingerprint. When present, the value must be exactly 32 hexadecimal characters (mixed case allowed) and is case-folded to lowercase when the backend filter is built."
- Example: `e7d705a3286e19ea42f587b344ee6865`

`ja4` query parameter: present in API (WS-3413 Done), same pattern expected.
{TODO: verify exact ja4 pattern from updated waap_api.yaml — WS-3413 was merged after current spec snapshot}

### Advanced Rules (source field) — CONFIRMED LIVE

Both JA3 and JA4 are confirmed live. CEL expression syntax:
```
request.ja3 == 'e7d705a3286e19ea42f587b344ee6865'
request.ja4 == 't13d1516h2_8daaf6152771_b1ff8ab2d16f'
```

Note: The field is under `request.` (not `source.`) object.
The advanced rules descriptor endpoint (`/waap/v1/advanced-rules/descriptor`) v1.11 lists both.

JA3 is already documented in `source-field-objects.mdx`.
JA4 needs to be added alongside it — confirmed live as of 2026-06-25.

---

## Where to see fingerprints in the portal

From WS-3370 (FE ticket):
- Event details panel: JA4 shown alongside JA3 (in QA, not live yet)
- Events list filter: JA4 as filterable field (in QA, not live yet)
- JA3 is already visible in event details

{TODO: take screenshots of Events page showing JA3 field once portal is verified — playwright screenshot needed}
{TODO: verify JA4 field label in portal once WS-3370 is deployed to production}

---

## Predefined tag: Malicious TLS Fingerprint

From DOC-1502 brief:
- The "Malicious TLS Fingerprint" predefined tag exists in WAAP
- Currently listed in docs without explanation
- File: `waap/waap-rules/custom-rules/tag-rules/predefined-tags.mdx`
- The new article should explain what this tag indicates, and the predefined-tags page should link to the new article

{TODO: verify exact behavior — does this tag fire when ja3/ja4 matches a known malicious fingerprint from Gcore's internal threat intel? Check with dev team.}

---

## Existing docs to update

1. `waap/waap-rules/advanced-rules/source-field-objects.mdx` — JA3 mentioned in table, add JA4 + link to new article
2. `waap/waap-rules/custom-rules/tag-rules/predefined-tags.mdx` — "Malicious TLS Fingerprint" tag, add description + link

---

## Article file path

`waap/threat-intelligence/tls-fingerprinting.mdx`

OR possibly: `waap/waap-rules/advanced-rules/tls-fingerprinting.mdx`

Since the article covers both observability (Events) and rules usage, the threat-intelligence section seems more appropriate. To be decided.

{TODO: confirm placement with team — Events page is under threat-intelligence, rules are under waap-rules}

---

## Attachment (not fetched)

WS-3202 has a PDF attachment: "Supporting JA4 Fingerprint in Production Systems.pdf"
URL: https://jira.gcore.lu/secure/attachment/496338/Supporting+JA4+Fingerprint+in+Production+Systems.pdf
This is a technical research doc — may contain additional implementation details useful for context.

---

## Source material summary for write-from-scratch

- **Transcript key points**: JA4 harder to spoof, based on more parameters, Gcore collects at edge → WAAP; gaming client incident: 1.5B requests, single JA3 fingerprint defeated entire botnet via one Advanced Rule.
- **Epic WS-3202**: JA3 limitations, JA4 benefits, full acceptance criteria.
- **WS-3208**: Technical pipeline — edge X-JA4 header → Shield → ClickHouse → Events API.
- **WS-3413**: ja4 field now returned in GET /v1/analytics/requests.
- **WS-3372**: JA4 in rule builder UI — Done.
- **WS-3371**: JA4 as BE condition in advanced rules — still in QA.
- **WS-3370**: JA4 in Events UI — still in QA.
- **OpenAPI**: ja3 filter = 32-char hex, `e7d705a3286e19ea42f587b344ee6865` example.
