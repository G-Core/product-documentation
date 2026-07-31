# Confluence MCP — Reference

Instructions for using Confluence MCP to find internal product documentation.
Load this file when a skill tells you to. Do not load it proactively.

---

## When to use Confluence

Confluence contains internal Gcore documentation that is not in Jira or in the
public docs repo. Use it when you need:

- Product specs and technical requirements for a feature
- Release notes and changelogs written by engineering
- Architecture decisions and design docs
- Known limitations and edge cases documented by the product team
- API field definitions and expected behavior

**Do not use Confluence content directly in public documentation.** It is internal.
Use it to understand the feature, then write the public doc in your own words following
the style guide.

---

## Key operations

```
confluence_get_page(page_id)           — fetch a specific page by ID
confluence_search(query, space)        — search pages by keyword
confluence_get_page_children(page_id)  — list child pages under a page
confluence_get_space(space_key)        — get info about a Confluence space
```

---

## What to look for

When researching a feature for documentation:

| What to find | What it tells you |
|---|---|
| Feature spec or PRD | What the feature does, who it is for, edge cases |
| Release notes (internal) | Exact changes, affected endpoints, rollout status |
| Architecture doc | How the system works — useful for concept articles |
| Known issues or limitations | What to warn users about |
| API field definitions | Field names, types, allowed values — verify against OpenAPI YAML |

---

## Search strategy

Start broad, then narrow:

1. **Search by feature name:**
   ```
   confluence_search("load balancer L7 policies")
   ```

2. **Search by Jira ticket key** — engineers often link Confluence pages in tickets:
   ```
   confluence_search("DOC-1142")
   ```

3. **Search by product area:**
   ```
   confluence_search("CDN origin groups", space="CLOUD")
   ```

4. **Follow links from Jira** — the linked dev ticket often has a Confluence page
   linked in its description or comments. Fetch that page directly by ID.

---

## Using Confluence content safely

Confluence pages are internal and may contain:
- Information not yet released to customers
- Internal implementation details not suitable for public docs
- Placeholder text or draft content that has not been reviewed

**Rules:**
- Never copy Confluence text verbatim into public documentation
- Verify technical details (field names, values, behavior) against the OpenAPI YAML
  in `/api-reference/services_documented/` — Confluence may be outdated
- If Confluence contradicts the OpenAPI spec, trust the spec
- If Confluence describes a feature as "not yet released" — do not document it without
  confirming with the user

---

## When Confluence is not helpful

Confluence search may return:
- Unrelated pages with the same keywords
- Outdated docs from old product versions
- Internal team wikis not related to the feature

If you cannot find useful content after 2–3 searches, proceed with what you have
from the Jira ticket, the OpenAPI spec, and (for portal features) Playwright testing.
Do not block work on finding a Confluence page.
