---
name: api-audit
description: >-
  Audits an existing REST API tab by live-testing every curl, Python SDK, and Go
  SDK code block, running the API style checker, applying the standalone tab
  test, and fixing broken code, missing operations, and checker violations in
  the API tab only. Use when the user asks to audit, verify, live-test, or
  improve an existing API tab or API section, for example "test the code samples
  in this doc" or "check whether the API examples still work". Not for adding an
  API tab that does not exist (use api-use-case), re-checking docs after a
  backend change ticket (use api-retest), or auditing Portal steps (use full-audit).
---

Audit and repair the `<MethodSection id="api">` of an existing article. Edit only the API tab.

**Portal tab rule:** do not touch the Portal tab's content. Fix only its MDX syntax if needed. Read `.agents/references/api-portal-tab-rule.md` before editing.

## Scope — read exactly these files

1. This SKILL.md
2. The article specified by the user
3. `api-reference/services_documented/{product}_api.yaml`
4. `.agents/references/api-live-testing.md`
5. `.agents/references/api-tab-structures.md` — structure rules to check the tab against
6. `.agents/references/api-tab-review.md`
7. `.agents/references/sdk-best-practices.md`
8. `.agents/references/ticket-and-branch.md` and `.agents/references/product-routing.md`
9. `.agents/references/mdx-rules.md`, `style-guide.md` — prose and MethodSwitch rules

## Inputs

| Input | Required | Notes |
|-------|----------|-------|
| Path to the article | Yes | Must already contain `<MethodSection id="api">` |

If the article has no API tab, stop and use the `api-use-case` skill.

---

## Flow

1. Read the existing API tab fully.
2. Read the Portal tab fully to understand what it covers.
3. Run the API checker and record the violations:
   ```powershell
   python .agents/tools/api_check_style.py {relative/path/to/article.mdx}
   ```
4. Live-test every curl, Python SDK, and Go SDK code block as described in `.agents/references/api-live-testing.md`. Record which blocks fail and why.
5. Run the standalone tab test from `.agents/references/api-tab-review.md`: mentally delete the Portal tab and list every topic the Portal tab covers that the API tab does not.
6. **Create the Jira ticket and feature branch now**, following `.agents/references/ticket-and-branch.md`. Do not write on `main`. In the ticket description include the article path, "Audit API tab", the failing blocks, and the missing operations.
7. Add missing operations using the templates in `api-tab-structures.md`. Fix broken code. Fix checker violations in the API tab only.
8. Run the checker again. Exit code must be 0.
9. Update `description` only if the tab content changed significantly. Rules are in `.agents/references/mdx-rules.md`.
10. Show the diff to the user.

## Output

```
Article: [path]
Blocks tested: [N] — failed before fix: [N]
Checker: exit code 0
Missing operations added: [list or none]
Ticket: DOC-XXXX
Branch: DOC-XXXX
```

Commit and push only when the user asks, as described in `.agents/references/ticket-and-branch.md`. Load the `pr` skill if the user also asked for a PR.
