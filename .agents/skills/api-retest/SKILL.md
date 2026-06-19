---
name: api-retest
description: Verify whether documented API articles need updates after a backend change ticket (migration, refactoring, version bump). Use when a Jira ticket describes backend changes to API handlers and the user asks to check if documentation is still accurate.
---

# API Retest

Validate that existing documentation articles remain accurate after a backend API change. The goal is a binary outcome: **no changes needed** or **specific fixes required**.

---

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Jira ticket ID | Yes | e.g. DOC-1411, GCLOUD2-XXXXX |
| Branch | No | Create a new branch from `main` if any changes are expected |

---

## Phase 1 — Read the ticket

Use the Jira MCP tool to fetch the ticket and any linked tickets.

Identify:
1. **Which API handlers changed** — file names, class names, endpoint paths
2. **Nature of the change** — migration to a new framework, request/response schema change, field rename, removal of a parameter, new validation rules
3. **Scope** — does this change the external API surface (request fields, response fields, status codes, error format) or is it internal refactoring with no external effect?

If the change is purely internal (framework swap with identical external behavior), retest is still required — the ticket description is not sufficient proof.

---

## Phase 2 — Find affected articles

Search the documentation for articles that call these endpoints:

```powershell
rg -l "v1/reserved_fixed_ips" cloud/ edge-ai/
```

Check:
- Articles that show `curl` examples with the endpoint path
- Articles that show SDK calls corresponding to those endpoints
- The OpenAPI spec (`api-reference/services_documented/cloud_api.yaml`) for the current field definitions

---

## Phase 3 — Create a branch

```powershell
git checkout main
git pull origin main
git checkout -b {TICKET_ID}
```

Even if no changes turn out to be needed, work on the branch. Delete it at the end if empty.

---

## Phase 4 — Write and run the test script

### Test script location

`c:\Projects\docops-agent2\scripts\test_{resource_name}.py`

### Region rules

| Resource type | Region | region_id |
|---|---|---|
| Networking, VMs, reserved IPs, bare metal | Luxembourg-3 | 148 |
| DBaaS, Kubernetes | Frankfurt-2 | 180 |

### Credentials

Credentials are in `C:\Projects\docops-agent2\access.md`. Always use dotenv pattern or inline env vars — never hardcode the token in committed files.

### Script structure

1. **List** — verify the list endpoint returns HTTP 200 and expected top-level keys
2. **Filter parameters** — verify each query parameter the article documents actually works
3. **Create** — create a minimal test resource; poll the task to completion
4. **Get** — retrieve by ID; verify all fields the article shows in the response JSON are present
5. **Update** — if the article documents a PATCH/PUT, run it and verify the response
6. **Sub-resources** — if the article documents nested endpoints (e.g. `connected_devices`), test each method (GET, PUT, PATCH)
7. **Delete** — delete the test resource; poll to completion

### Cleanup rule

Every resource created in the test **must be deleted in the same run**. Use `try/finally` if needed to guarantee cleanup even on failure.

### Run the script

```powershell
.\venv\Scripts\python.exe scripts\test_{resource_name}.py
```

---

## Phase 5 — Compare results with documentation

For each endpoint the article documents, check:

| Item | What to verify |
|---|---|
| HTTP method and path | Still correct? |
| Request body fields | Names unchanged? New required fields? Fields removed? |
| Response fields | All fields the article shows are still present? Any renamed? |
| Query parameters | All filter/sort parameters still accepted? |
| Status codes | Same as documented? |
| Task vs synchronous | Still async (returns `tasks`)? Or changed to sync? |
| Error format | If the article shows a 404 or 400 example, still the same shape? |

---

## Phase 6 — Decide and act

**If nothing changed:**

- Delete the branch
- Close the ticket with a comment: "Tested all endpoints against the live API. No changes to documentation required."

**If changes are needed:**

- Update the affected articles
- Test the updated code examples end-to-end
- Commit and push to the branch
- Open a PR

---

## Output

Report to the user:

```
Ticket: {ID}
Articles checked: N
Endpoints tested: list of paths
Result: no changes / N items updated

Changes made:
- {article}: {what changed}
```
