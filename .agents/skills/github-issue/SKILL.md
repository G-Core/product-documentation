---
name: github-issue
description: >-
  Triage and work on a GitHub issue from G-Core/product-documentation one at a
  time. Use when the user asks to pick up an issue, work the issue queue, or
  gives an issue number or URL from https://github.com/G-Core/product-documentation/issues.
---

Work on documentation requests filed as GitHub issues in this repository.
Process **one issue at a time**. Do not start a second issue until the first
is merged or explicitly deferred.

Issue tracker: https://github.com/G-Core/product-documentation/issues

## Scope — read exactly these files

1. This SKILL.md (including the backlog and workflow log at the bottom)
2. `.agents/references/mcp-tools/setup.md` — only if `gh` CLI is not authenticated

Do not read article files during Phase 1–3. Triage first, then load the
downstream skill.

---

## Phase 1 — Sync main and pick an issue

**Step 1.** Ensure you are on an up-to-date `main`:

```powershell
cd C:\Projects\product-documentation
git checkout main
git pull origin main
```

**Step 2.** Pick exactly one issue:

| Rule | Detail |
|------|--------|
| Default order | Oldest open issue first (lowest number), unless the user names a specific issue |
| One at a time | Finish or defer the current issue before starting another |
| Skip if done | If the requested change is already on `main`, report it and ask whether to close the issue |

**Step 3.** Fetch the issue. Prefer `gh` when authenticated:

```powershell
gh issue view {number} --repo G-Core/product-documentation --json number,title,body,labels,state,author,createdAt,url
gh issue view {number} --repo G-Core/product-documentation --comments
```

If `gh` is not authenticated, use the public GitHub API (no token needed for
public repo issues):

```powershell
curl.exe -s "https://api.github.com/repos/G-Core/product-documentation/issues/{number}"
curl.exe -s "https://api.github.com/repos/G-Core/product-documentation/issues/{number}/comments"
```

List all open issues:

```powershell
gh issue list --repo G-Core/product-documentation --state open
# or
curl.exe -s "https://api.github.com/repos/G-Core/product-documentation/issues?state=open&per_page=30"
```

Record what you fetched in the **Workflow log** section at the bottom of this file.

---

## Phase 2 — Triage the issue

Read the issue title, body, labels, and all comments. Apply the same
customer-facing test used in `jira-context`:

Does knowing about this change help a customer choose, plan, operate, or
troubleshoot?

| Decision | When |
|----------|------|
| **PROCEED** | Customer-facing doc gap, wrong content, or missing section |
| **ALREADY DONE** | Change is already on `main` — verify with grep or by reading the target article |
| **BLOCKED** | Not enough detail to write accurately — list what is missing and ask the reporter or user |
| **CANCEL** | Internal-only change, backend-only, or not documentable (same rules as `jira-context` Phase 3) |

**Label hints:**

| Label | Typical routing |
|-------|-----------------|
| `documentation` | Usually PROCEED — explicit doc request |
| `Feature` | Often NEW article or new section — may need SME input |
| `Bug` | Check whether it is a **documentation bug** (PROCEED) or product bug (CANCEL) |
| Product label (`FastEdge`, etc.) | Sets the product folder and PR title prefix |

**Hard stop:** If triage result is CANCEL or BLOCKED, stop. Update the backlog
table and workflow log. Do not create a branch.

---

## Phase 3 — Find affected documentation

Search the repo for the target article or topic:

```powershell
grep -r "keyword" --include="*.mdx" -l
```

Determine the action:

| Situation | Action | Downstream skill |
|-----------|--------|------------------|
| Existing article needs a small addition or fix | UPDATE (simple) | `.agents/skills/update-page/SKILL.md` |
| Existing article needs restructuring or screenshots | UPDATE (complex) | `.agents/skills/update-page/SKILL.md` |
| New article or major new section | NEW | `.agents/skills/write-from-scratch/SKILL.md` |
| Issue links a specific page URL | UPDATE | `.agents/skills/update-page/SKILL.md` — map URL path to repo file |
| End-to-end guide spanning products | NEW | `.agents/skills/cookbook/SKILL.md` |
| Needs portal/API verification before editing | AUDIT first | `.agents/skills/regression-test/SKILL.md`, then update-page |

Map public docs URLs to repo paths: strip `https://docs.gcore.com/` and
append `.mdx`. Example: `/cdn/logs/logs-uploader` → `cdn/logs/logs-uploader.mdx`.

Produce a brief before editing:

```
## GitHub issue context: #{number}

### Triage
- Decision: [PROCEED / ALREADY DONE / BLOCKED / CANCEL]
- Labels: [...]

### What is needed
[1 paragraph]

### Affected documentation
- Article: [path or "none — new article"]
- Action: [UPDATE / NEW / AUDIT]

### Downstream skill
[skill path]
```

---

## Phase 4 — Create branch

Only after triage is PROCEED.

```powershell
git checkout main
git pull origin main
git checkout -b issue/{number}-{short-slug}
```

**Branch naming:** `issue/{number}-{short-slug}`

Examples:
- `issue/1845-fastedge-log-field`
- `issue/1846-fastedge-dictionary`
- `issue/1849-wasi-http-rust-guide`
- `issue/1872-edge-storage-byod`

`{short-slug}`: 2–4 words from the issue title, lowercase, hyphens.

Do not reuse an existing branch for a different issue.

---

## Phase 5 — Execute documentation work

Load **exactly one** downstream skill from Phase 3. Follow that skill for all
writing, testing, and style rules.

Additional rules for issue-driven work:

1. Reference the issue in commit messages: `[Product] Short description (fixes #{number})`
2. If the issue body names a specific URL or field, verify each item explicitly
3. If ALREADY DONE was wrong and you still make changes, note what was missing
   beyond the original request
4. For FastEdge issues: check internal details against
   `.cursor/rules/confluence-content-filtering.mdc` before publishing

When the user confirms the work is ready, load `.agents/skills/pr/SKILL.md`.

---

## Phase 6 — Pull request and issue closure

When creating the PR (via the `pr` skill), add to the PR body:

```markdown
Closes #{number}
```

Or, if the PR only partially addresses the issue:

```markdown
Related to #{number}
```

Use `Closes` only when the issue is fully resolved.

**PR title:** same product prefix as other PRs, e.g. `[CDN] Add FastEdge log field to Logs uploader`.

After the PR merges, update the backlog table below to **Done** and add a
workflow log entry with the PR URL.

---

## Phase 7 — Resume the queue

After merge (or explicit deferral):

1. Update backlog status in this file
2. Tell the user which issue is next (oldest still Open)
3. Wait for user approval before starting the next issue

---

## Issue backlog

Maintained by the agent. Update after each triage or merge.

| # | Title | Labels | Opened | Status | Branch / PR | Notes |
|---|-------|--------|--------|--------|-------------|-------|
| 1845 | Add FastEdge log field to Logs uploader docs | FastEdge | 2026-02-12 | Open | — | Target: `cdn/logs/logs-uploader.mdx`. Field `$fastedge_field1` may already exist on main — verify before editing. |
| 1846 | Dictionary use in FastEdge | FastEdge | 2026-02-12 | Open | — | New section; needs list of supported dictionary values from SME |
| 1849 | Describe WASI-HTTP rust app | documentation, FastEdge | 2026-02-16 | Open | — | New guide; replace SDK process interface; HuggingFace POC as example |
| 1872 | Add BYOD description to Edge Storage | FastEdge | 2026-02-19 | Open | — | Edge Storage BYOD configuration underdocumented |
| 2650 | Terraform Provider updated to v2.0.0-rc.1 | terraform | 2026-09-01 | PR open | `issue/2650-terraform-lb-floating-ip` | Replaced `floating_ip` inline block in `gcore_cloud_load_balancer` with `gcore_cloud_floating_ip` resource. Updated `.terraform-provider-version` to `2.0.0-rc.1`. |
| 2652 | SDK updated to Python v0.56.0, Go v0.56.0 | api-sdk-tracker | 2026-09-01 | In progress | `issue/2652-sdk-waap-breaking-changes` | Breaking: `policies.toggle()` now requires `mode: bool` (Python) and `WaapDomainPolicySettingsParam{Mode}` (Go). Updated 10 WAAP policy articles. Updated prose in advanced-rules.mdx, custom-rules.mdx, ip-allowlist-and-blocklist.mdx. |

Status values: `Open`, `In progress`, `PR open`, `Done`, `Blocked`, `Cancelled`.

---

## Workflow log

Append-only session notes. Add an entry every time this skill runs.

### 2026-09-02 — Issue #2652: SDK v0.56.0 WAAP breaking changes

- Fetched issue body from upload. Breaking changes: `policies.toggle()` now requires `mode: bool` (Python) / `WaapDomainPolicySettingsParam{Mode}` (Go); endpoint changed from `/policies/{id}/toggle` to `/policies/{id}` with `{"mode": bool}` body.
- Confirmed exact signatures from Go SDK source (`domainpolicy.go`) and Python SDK source (`policies.py`).
- Updated 10 WAAP policy articles: `behavioral-waf`, `waf-and-owasp-top-threats`, `protocol-validation`, `cms-protection`, `invalid-user-agent-and-unknown-user-agent`, `advanced-api-protection`, `anti-automation-and-bot-protection`, `waap-policies/ip-reputation`, `firewall/ip-reputation`, `known-bots`.
  - Section renamed from "Toggle a policy" to "Enable or disable a policy" (or "Set bot mode" for known-bots).
  - Python: added `mode=True` parameter.
  - Go: added `WaapDomainPolicySettings: waap.WaapDomainPolicySettingsParam{Mode: true}` to params struct.
  - curl: updated URL (removed `/toggle`), added `Content-Type` header and `{"mode": true}` body.
  - Removed Warning boxes about toggling.
- Updated prose in `advanced-rules.mdx`, `custom-rules.mdx`, `ip-allowlist-and-blocklist.mdx`: changed "returns 204 with no body" to accurate descriptions for Update/Toggle methods that now return typed results.
- Branch: `issue/2652-sdk-waap-breaking-changes` — in progress.

### 2026-09-02 — Issue #2650: Terraform provider v2.0.0-rc.1

- Fetched issue from GitHub. Breaking change: `floating_ip` inline block removed from `gcore_cloud_load_balancer`.
- Only article affected: `cloud/networking/create-and-configure-a-load-balancer.mdx` (Terraform tab, Step 1).
- Replaced `floating_ip = { source = "new" }` block with `gcore_cloud_floating_ip` resource using `port_id` and `fixed_ip_address`.
- Updated `.terraform-provider-version` from `2.0.0-alpha.15` to `2.0.0-rc.1`.
- Validated with `terraform validate` and schema inspection against real provider v2.0.0-rc.1.
- Branch: `issue/2650-terraform-lb-floating-ip` — pushed, ready for PR.

### 2026-06-10 — Skill created, queue inventoried

- Synced `main` (up to date with `origin/main`).
- Fetched 4 open issues via GitHub API; no comments on any issue.
- Created `github-issue` skill and wired into `AGENTS.md` and `skill-routing.mdc`.
- **#1845 triage note:** `$fastedge_field1` already present in `cdn/logs/logs-uploader.mdx` log-fields table on main — likely ALREADY DONE; confirm with user before closing.
- **Next suggested issue:** #1846 or user priority.

---
