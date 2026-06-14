# Terraform Provider v2 — Known Issues

Provider version tested: `2.0.0-alpha.8`
Test environment: Luxembourg-3, region_id=148, project_id=1186668

---

## BUG-1: `gcore_cloud_load_balancer_pool_member` — cannot create

**Resource:** `gcore_cloud_load_balancer_pool_member`

**Symptom:**
- With `project_id` + `region_id`: `Error: failed to make http request — requestconfig: base url is not set`
- Without `project_id` + `region_id`: `Error: failed to make http request — missing required project_id parameter`

Catch-22: the resource requires `project_id` to build the API URL, but providing it triggers a different error.

**Workaround in docs:** Pool members are documented using the inline `members` attribute inside `gcore_cloud_load_balancer_pool`, which works correctly.

**Article affected:** `cloud/networking/create-and-configure-a-load-balancer.mdx`

---

## BUG-2: `data.gcore_cloud_instances` (plural) — RFC3339 validation error on plan

**Resource:** `data "gcore_cloud_instances"`

**Symptom:** `terraform plan` fails with an RFC3339 date validation error even when no date fields are specified in the data source config. Error appears on the `updated_at`/`created_at` computed fields during schema validation.

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

**Symptom:** Resource does not exist in provider v2 schema at all. Cannot manage volume snapshots via Terraform.

**Article affected:** Volume snapshots article — Terraform tab skipped entirely.

---

## BUG-4: `gcore_cloud_load_balancer_listener.secret_id` — validation rejects valid UUID

**Resource:** `gcore_cloud_load_balancer_listener`

**Symptom:** Setting `secret_id` to an actual secret UUID fails at plan time with:
`Error: Invalid Attribute Value Match — Attribute secret_id value must be one of: [""], got: "<uuid>"`

The schema description for `secret_id` lists `Available values: ""` — the provider's validation only accepts an empty string, making it impossible to attach a TLS certificate to a listener via Terraform.

`sni_secret_id` (list of SNI cert IDs) is likely affected by the same issue and was not tested further.

**Impact:** Cannot configure `TERMINATED_HTTPS` listeners with TLS certificates via Terraform. The `gcore_cloud_secret` resource itself works correctly; only the listener attachment is broken.

**Articles affected:**
- `cloud/networking/load-balancers/add-certificates-to-load-balancer.mdx` — Terraform tab skipped (no working path to document)
- `cloud/networking/create-and-configure-a-load-balancer.mdx` — HTTPS listener example removed from Terraform tab
- `cloud/secrets-manager/upload-a-pkcs12-file.mdx` — "Use in an HTTPS listener" Terraform snippet removed
