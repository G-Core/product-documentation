---
name: api-retest
description: >-
  Checks whether API documentation is still accurate after a backend change
  described in a Jira ticket (migration, refactoring, version bump, handler
  changes). Use when the user gives such a ticket and asks whether the docs need
  updates, or asks to re-test API articles after a backend change. Finds the
  affected articles, runs the curl, Python, and Go examples live on preprod,
  and only then edits the articles to match that run. Not for adding or
  auditing an API tab (use api-use-case or api-audit).
---

# API Retest

Validate that existing documentation articles remain accurate after a backend API change. The goal is a binary outcome: **no changes needed** or **specific fixes required**.

## Hard rule — live test before any write

A live test is a mandatory precondition. Run the call first. Write the article only after that run succeeds.

Do not add or change a sentence, a field name, a JSON example, or an SDK line from a ticket, an OpenAPI file, or SDK source code. Those sources say what might be true. Only the live run says what the article may state.

Each example the article will show is tested in the language the customer copies:

- A curl block is tested by running that curl.
- A Python block is tested by running that Python.
- A Go block is tested by running that Go.

A successful REST call does not count as a test of the Python or Go example. Finding the field in the SDK repository does not count as a test. If that snippet has not been executed against the live API in this session, do not write it.

If the credential, the SDK, or the toolchain is missing, stop. Do not draft the example and test it later.

## Hard rule — preprod is the same product

Preprod and production are the same product. Preprod is where a change can be checked before it is rolled out.

Document the preprod result. If production still returns the previous value, the change has not been rolled out there yet. Do not write that previous value into the article. Do not treat it as a difference between the environments. Do not ask the user to confirm it with engineers.

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

## Phase 3 — Branch

One task uses one branch. If this task already has a branch, stay on it. Do not create another ticket or branch for another article in the same task.

Create a branch only when the task does not have one yet. If the current branch is not `main` and it has uncommitted changes, commit them on that branch first. Never `git stash` to switch. The helper exits with an error when that branch is dirty.

```powershell
.\.agents\tools\create_branch.ps1 {TICKET_ID}
```

Even if no changes turn out to be needed, work on the branch. Delete it at the end if empty.

---

## Phase 4 — Write and run the test script

### Test script location

`$env:TEMP\test_{resource_name}.py` (outside the repository, never committed)

### Environment

Run the test on preprod. That result is the product behavior.

Use production only when the change is not on preprod at all. A production response that still has the old value does not replace a successful preprod run.

| Environment | API base | Portal |
|---|---|---|
| Preprod | `https://api.preprod.world` | `https://portal.preprod.world` |
| Production | `https://api.gcore.com` | `https://portal.gcore.com` |

### Region rules

**Production:**

| Resource type | Region | region_id |
|---|---|---|
| Networking, VMs, reserved IPs, Kubernetes, bare metal | Luxembourg-3 | 148 |
| Container Registry and CaaS only | Luxembourg-2 | 76 |
| Managed PostgreSQL only | Frankfurt-2 | 180 |

**Preprod:**

| Region | region_id |
|---|---|
| Luxembourg Preprod | 4 |
| INF-1 Preprod | 20 |
| ED-10 Preprod | 10 |

Use Luxembourg Preprod (region_id=4) for general networking and VM tests.

### Credentials

Tokens come from the environment or from `.env` via dotenv: `GCORE_API_KEY` for prod and `GCORE_PREPROD_API_KEY` for preprod. Never print a token, and never hardcode one in committed files. If both the environment and `.env` lack the variable, stop and ask the user.

### If the feature is not yet on preprod

If tests show the old behavior on preprod (dev ticket is Done but change is invisible), stop and inform the user. Do not document a behavior you cannot verify. Ask the developer which environment the change is deployed to and retest there.

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
python "$env:TEMP\test_{resource_name}.py"
```

The HTTP script proves the endpoint. It does not replace the examples the article will show. Before any article edit, run each of those examples against the same live API and keep the output:

1. The curl block, when the article has a curl tab.
2. The Python SDK block, when the article has a Python tab.
3. The Go SDK block, when the article has a Go tab.

Use only the field names and values that this run printed. If one language cannot be executed, stop. Leave that language unchanged.

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

- Edit the articles so they match the snippets that already ran in this session. Every new or changed line comes from that run.
- Show the diff to the user and stop. Commit, push, and open a PR only when the user asks, as described in `.agents/references/ticket-and-branch.md`

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
