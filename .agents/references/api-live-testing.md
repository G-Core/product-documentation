# API live testing and endpoint mapping

Used by the `api-use-case` and `api-audit` skills.

## Contents

- Live API testing
- Finding the API endpoints
- Known gotchas

---

## Live API testing

Always test against the live API. Do not ask the user. Do not use spec-only mode.

- The API token comes from the `GCORE_API_KEY` environment variable, which the user sets before the session. Never read `.env` or `access.md`. If `$env:GCORE_API_KEY` is empty, stop and ask the user to set it.
- Use Luxembourg-3 (`region_id: 148`) — `GCORE_CLOUD_REGION_ID`. Kubernetes uses this region. Do not override it.
- Container Registry and CaaS only: Luxembourg-2 (`region_id: 76`). Those products are not in Luxembourg-3; the articles state this.
- Managed PostgreSQL only: Frankfurt-2 (`region_id: 180`). The service is not in Luxembourg-3; the article sample host is frankfurt-2. No other region overrides.
- Run each API call end-to-end in the terminal using `curl` against `https://api.gcore.com`
- Record real responses — exact fields, structure, error messages
- **Also run every Python SDK and Go SDK code sample** — install the SDK in a venv, execute each snippet against the live API, confirm it runs without errors and returns real data
- Python SDK: `pip install gcore` in a temporary venv (see `sdk-best-practices.md`, "Setting up a test environment"); Go SDK: `go run` in a temp module
- SDK field names (method names, struct fields, response object attributes) must match the actual SDK — never extrapolate or guess them
- Only after the full flow runs end-to-end for BOTH curl AND SDK — move on
- Delete test resources immediately after each test, not at the end
- If the flow needs supporting resources, create the full environment first, then run the article operations, then delete everything
- Never leave `{TODO: verify}` placeholders — live-test until the call is confirmed

---

## Finding the API endpoints

**Run the checker before you write anything:**
```powershell
python .agents/tools/api_check_style.py {relative/path/to/article.mdx}
```
Fix any existing violations in the API tab before adding new content.

Open the OpenAPI YAML for the product:
```
api-reference/services_documented/{product}_api.yaml
```

Specs in the repository: `streaming_api.yaml`, `cloud_api.yaml`, `cdn_api.yaml`, `dns_api.yaml`, `waap_api.yaml`.

For each Portal step, find the equivalent API operation:

```powershell
# Search for an endpoint by path pattern
Select-String -Path "api-reference\services_documented\cloud_api.yaml" `
              -Pattern "/cloud/v\d+/instances"
```

**Mapping rules:**
- Always use the latest non-deprecated API version (`v2` over `v1` when both exist)
- Verify field names from the YAML spec — never write field names from memory
- Note gotchas discovered: wrong methods, missing required fields, non-obvious validation

---

## Known gotchas

Check these before writing, and add new ones as you discover them:

- `GET /cloud/v1/instances/{project_id}/{region_id}/available_flavors` is a POST requiring volume data — use `GET /cloud/v1/flavors/{project_id}/{region_id}` to list flavors
- Instance `name` field is blocked on reseller accounts — standard accounts support it normally; use `name` in article examples
- `addresses` field uses network name as key (e.g. `"pub_net"`), not a fixed string — iterate over all keys
