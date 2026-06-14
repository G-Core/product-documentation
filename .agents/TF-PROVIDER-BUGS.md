# Terraform Provider v2 — Known Issues

Provider version tested: `2.0.0-alpha.8`
Test environment: Luxembourg-3, region_id=148, project_id=1186668

---

## BUG-1: `gcore_cloud_load_balancer_pool_member` — cannot create

**Resource:** `gcore_cloud_load_balancer_pool_member`

**Retested:** 2026-06-14, provider v2.0.0-alpha.8 — **still broken**

**Symptom:**
- With `project_id` + `region_id`: `Error: failed to make http request — requestconfig: base url is not set`
- Without `project_id` + `region_id`: `Error: failed to make http request — missing required project_id parameter`

Catch-22: the resource requires `project_id` to build the API URL, but providing it triggers a different error. The registry documentation shows the resource should accept `project_id` and `region_id` — this is a provider-side URL construction bug.

**Workaround in docs:** Pool members are documented using the inline `members` attribute inside `gcore_cloud_load_balancer_pool`, which works correctly.

**Article affected:** `cloud/networking/create-and-configure-a-load-balancer.mdx`

---

## BUG-2: `data.gcore_cloud_instances` (plural) — RFC3339 validation error on plan

**Resource:** `data "gcore_cloud_instances"`

**Retested:** 2026-06-14, provider v2.0.0-alpha.8 — **still broken**

**Symptom:** `terraform plan` fails with `RFC3339 string value is null` even when no date fields are specified. The error fires on a computed field during schema read.

**Schema change in alpha.8:** The attribute formerly known as `results` was renamed to `items`. The RFC3339 bug persists regardless of attribute name.

**Workaround in docs:** Use `data "gcore_cloud_instance"` (singular) instead.

**Article affected:** `cloud/virtual-instances/check-the-operational-status-of-your-instance.mdx`

---

## BUG-3: `gcore_cloud_reserved_fixed_ip` with `is_vip = true` — delete rejected by API

**Resource:** `gcore_cloud_reserved_fixed_ip`

**Symptom:** `terraform destroy` fails with an API error when `is_vip = true`. The API refuses to delete a port that is still in VIP mode.

**Workaround:** Two-step deletion — first set `is_vip = false` and apply, then remove the resource block and apply again. Documented as a Warning in the article (this is a legitimate operational constraint, not a provider bug — the API enforces it).

**Article affected:** `cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address.mdx`

---

## GAP-1: `gcore_cloud_volume_snapshot` — resource missing in provider v2

**Resource:** `gcore_cloud_volume_snapshot`

**Retested:** 2026-06-14 — confirmed absent in alpha.8 and alpha.7 (latest public). The v2 migration guide does not list a snapshot equivalent resource. The `gcore_cloud_volume` resource accepts `snapshot_id` as a source when creating a volume, but there is no resource to create or manage the snapshots themselves.

**Symptom:** Resource does not exist in provider v2 schema at all. Cannot manage volume snapshots via Terraform.

**Article affected:** Volume snapshots article — Terraform tab skipped entirely.

---

## BUG-4: `gcore_cloud_load_balancer_listener.secret_id` — RESOLVED

**Resource:** `gcore_cloud_load_balancer_listener`

**Original symptom:** Setting `secret_id` to an actual secret UUID fails at plan time with:
`Error: Invalid Attribute Value Match — Attribute secret_id value must be one of: [""], got: "<uuid>"`

**Resolution (tested 2026-06-14, provider v2.0.0-alpha.8):**
`secret_id` is intentionally restricted to `""` in the provider schema. TLS certificates for `TERMINATED_HTTPS` listeners must be attached via `sni_secret_id` (list of secret UUIDs). Tested live in Luxembourg-3:

```hcl
resource "gcore_cloud_load_balancer_listener" "https" {
  protocol      = "TERMINATED_HTTPS"
  protocol_port = 443
  secret_id     = ""
  sni_secret_id = [gcore_cloud_secret.tls.id]
}
```

Apply succeeded — listener created in ACTIVE state with the secret attached.

**Action required:** Update affected articles to add working HTTPS listener examples.

**Articles affected:**
- `cloud/networking/load-balancers/add-certificates-to-load-balancer.mdx` — Terraform tab needs update
- `cloud/networking/create-and-configure-a-load-balancer.mdx` — Terraform HTTPS listener example needs update
- `cloud/secrets-manager/upload-a-pkcs12-file.mdx` — "Use in an HTTPS listener" Terraform snippet needs update
