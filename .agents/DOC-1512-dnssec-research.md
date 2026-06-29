# DOC-1512: Client-facing documentation for DNSSEC

## Meta

- **Ticket**: DOC-1512
- **Reporter**: Rizal Gowandy (developer, DNS team)
- **Assignee**: Sergey Kostichev
- **Status**: In Progress
- **Related epic**: DNS-2966 — DNSSEC ready for General Availability (In Progress)
- **Related task**: DNS-3080 — DNSSEC state machine driven by parent-DS scan (Resolved)
- **Article to edit**: `dns/getting-started-with-dnssec.mdx`
- **Live URL**: https://gcore.com/docs/dns/getting-started-with-dnssec
- **Review required**: Anton Pates before publishing

---

## Problem

DNSSEC now implements a **four-state lifecycle** driven by parent-DS observation (DNS-3080).
The existing docs still reflect the old two-state model (enabled/disabled).
Customers see `status: "pending"` or `"pending-disabled"` in the API response with no explanation.

---

## Acceptance Criteria

1. Document all four DNSSEC lifecycle states: `pending`, `active`, `pending-disabled`, `disabled`
2. Explain what drives transitions (parent-DS scan at the registrar)
3. Document the `modified_on` timestamp field (`dnssec_status_modified_on`) returned with DNSSEC status
4. Include expected timelines (DS propagation delay: minutes to hours depending on registrar)
5. Publish on Gcore help center
6. Link to the new docs from the API spec (swagger annotations in gcdn-dns-api) — dev task
7. Review with Anton Pates before publishing

---

## Developer's Draft (from Jira comment, Rizal Gowandy)

### Four states and their meaning

| Status | Meaning | What to do |
|---|---|---|
| `pending` | DNSSEC enabled, signing keys generated, but DS record not yet detected at registrar. Chain of trust not active. | Add the DS record Gcore provides to your domain registrar. |
| `active` | Valid DS record detected at registrar. Chain of trust established. Zone is fully protected. | Nothing — DNSSEC is working. |
| `pending-disabled` | Disable requested, but DS record still published at registrar. | Remove the DS record at the registrar to finish disabling. |
| `disabled` | DNSSEC is off and no DS record is present. | Nothing. |

### How transitions happen

Driven by the registrar scan:
- `pending` → `active`: once valid DS record is detected. Can take minutes to hours depending on registrar propagation and DS record TTL.
- `pending-disabled` → `disabled`: once DS record is removed at the registrar.
- `active` stays `active`. If DS is removed externally at the registrar, status does NOT automatically change — must call the disable endpoint to turn DNSSEC off.

### API fields on the zone (GET /v2/zones/{name})

- `dnssec_status` — lifecycle status: `pending`, `active`, `pending-disabled`, `disabled`
- `dnssec_status_modified_on` — RFC 3339 timestamp of last status change

Both fields are **omitted entirely** for a zone that has never had DNSSEC enabled. A missing field is not an error.

Note: `dnssec_status` is distinct from the top-level `status` field (zone delegation state). They are independent.

### JSON examples

**pending:**
```json
{
  "name": "example.com",
  "enabled": true,
  "status": "active",
  "dnssec_enabled": true,
  "dnssec_status": "pending",
  "dnssec_status_modified_on": "2026-06-25T09:14:02Z"
}
```

**active:**
```json
{
  "name": "example.com",
  "enabled": true,
  "status": "active",
  "dnssec_enabled": true,
  "dnssec_status": "active",
  "dnssec_status_modified_on": "2026-06-25T11:48:37Z"
}
```

**pending-disabled:**
```json
{
  "name": "example.com",
  "enabled": true,
  "status": "active",
  "dnssec_enabled": false,
  "dnssec_status": "pending-disabled",
  "dnssec_status_modified_on": "2026-06-26T08:02:15Z"
}
```

**disabled:**
```json
{
  "name": "example.com",
  "enabled": true,
  "status": "active",
  "dnssec_enabled": false,
  "dnssec_status": "disabled",
  "dnssec_status_modified_on": "2026-06-27T10:30:00Z"
}
```

### Disabling DNSSEC

- Calling disable endpoint while DS record still published at registrar → `409 Conflict`
- To proceed anyway: pass `force_disable=true`
- Zone then moves to `pending-disabled` → `disabled` once DS removed at registrar

### Checking DS record at registrar

`GET /v2/zones/{name}/dnssec/parent-ds` — reports whether a valid DS record is currently detected:

```json
{
  "has_valid_parent_ds": true,
  "parent_zone": "com.",
  "scanned_at": "2026-06-25T11:48:30Z"
}
```

---

---

## SDK Coverage

### Python SDK (gcore package)

Available methods via `client.dns.zones.dnssec`:
- `update(zone_name, enabled=True)` — enable DNSSEC (PATCH /dns/v2/zones/{name}/dnssec)
- `update(zone_name, enabled=False)` — disable DNSSEC
- `get(zone_name)` — get DS record (GET /dns/v2/zones/{name}/dnssec)

Example (enable):
```python
import os
import gcore

client = gcore.Gcore(api_key=os.environ["GCORE_API_KEY"])

result = client.dns.zones.dnssec.update("example.com", enabled=True)
print(result.ds)
```

Example (get DS record):
```python
ds_info = client.dns.zones.dnssec.get("example.com")
print(ds_info.ds)
```

### Go SDK (github.com/G-Core/gcore-go v0.49.1)

Available methods via `client.DNS.Zones.Dnssec`:
- `Update(ctx, zoneName, dns.ZoneDnssecUpdateParams{Enabled: gcore.Bool(true)})` — enable/disable DNSSEC
- `Get(ctx, zoneName)` — get DS record

Example:
```go
import (
    "github.com/G-Core/gcore-go"
    "github.com/G-Core/gcore-go/dns"
    "github.com/G-Core/gcore-go/option"
)

client := gcore.NewClient(option.WithAPIKey(os.Getenv("GCORE_API_KEY")))

result, _ := client.DNS.Zones.Dnssec.Update(ctx, "example.com",
    dns.ZoneDnssecUpdateParams{Enabled: gcore.Bool(true)})
fmt.Println(result.Ds)
```

### What the SDK does NOT cover (use curl only)

- `dnssec_status` / `dnssec_status_modified_on` fields in zone response — new fields, SDK not yet updated
- `force_disable=true` parameter for disable endpoint
- `GET /v2/zones/{name}/dnssec/parent-ds` endpoint

---

## Article restructuring plan

The existing article uses `<Tabs>` with "DNS API" and "Customer Portal" tabs inside flat MDX.
Must be restructured to use `MethodSwitch` (like other products).

Structure:
- `<MethodSection id="portal" label="Customer Portal">` — Portal steps
- `<MethodSection id="api" label="REST API">` — API content with `<Tabs>` (Python SDK, Go SDK, curl)

---

## What we need to do

1. Read the existing `dns/getting-started-with-dnssec.mdx` article
2. Add a "DNSSEC status lifecycle" section covering:
   - The four states table
   - How transitions happen (registrar scan drives them, not just API calls)
   - Timing expectations (minutes to hours)
   - The `dnssec_status` and `dnssec_status_modified_on` API fields
   - JSON examples for all four states
   - Disabling DNSSEC: 409 behavior and `force_disable=true`
   - The `GET /v2/zones/{name}/dnssec/parent-ds` endpoint
3. Ensure content is accurate per the draft — field names to be verified against public OpenAPI spec
