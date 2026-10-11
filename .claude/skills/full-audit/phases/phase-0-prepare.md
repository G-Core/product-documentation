# Phase 0 — Find and read the article

If the article path is given — open the file directly.

If only a topic is given — search the repository:

```powershell
rg "keyword" --glob "*.mdx" -l
```

## Determine portal and Jira routing

Load `.agents/references/product-routing.md` now.

Match the article path against the prefix table (longest match wins). Record:

- `portal_type` — BillMgr / VMmanager 6 / DCImanager / Gcore Customer Portal
- `portal_url` — the URL to navigate to in Phase 1
- `login_method` — how to authenticate
- `jira_org_unit` — the ORG_UNIT value for Phase 4. If the article path matches no row, ask the user.

## Claim the article before doing any work

If the task names a plan file (for example one under `_private/planning/`), open it before reading the article and change this article's row from `pending` to `in_progress`.

If no plan file is named, skip the claim and mark row 0c as n/a.

**Why this matters:** two agents may be running in parallel on separate repository
clones. Both can see the same `pending` rows. Claiming the article first — before
reading it, before opening the portal — ensures no other agent picks up the same
article and produces duplicate work or a merge conflict.

**If the article's status is already `in_progress` or `done`:** stop immediately.
Report to the user: "Article [path] is already claimed or completed in the plan.
Choose a different article." Do not proceed until the user confirms a different target.

After updating the plan, proceed to read the article.

## Verify the screenshot folders

The only correct images folder for an article is its path without `.mdx` under `images/docs/`:

```
Article:  streaming/ai-video-service/content-moderation/soft-nudity-detection.mdx
Images:   images/docs/streaming/ai-video-service/content-moderation/soft-nudity-detection/
```

Run the checker:

```powershell
python .agents/tools/check_article_images.py {relative/path/to/article.mdx}
```

It reports image references that point to another folder (including a sibling article's folder), missing files, duplicate files, and unreferenced files. Record every `WRONG_FOLDER` and `MISSING` line immediately as a FINDING with category `Outdated screenshot path`.

Files that already exist in the correct folder were placed by the user. Use them as-is. Do not retake or overwrite them in Phase 3 unless a comparison reveals a real discrepancy.

Read the entire article before touching the portal.
Build a mental map:
- What is the user expected to achieve by the end?
- What steps does the article prescribe?
- What UI elements, buttons, field names, and navigation paths does it mention?
- How many screenshots are in the article and what do they show?
- Are there prerequisites that require other resources (network, cluster, SSH key, etc.)?

List each prerequisite resource and check whether a documentation article covers
its creation. Note the article path for each — do not open or test those articles now.
They will be tested in their own turn.
