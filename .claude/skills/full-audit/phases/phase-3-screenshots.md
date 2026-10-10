# Phase 3 — Screenshot audit

For each screenshot in the article, navigate to the corresponding screen in the portal and **compare the current UI with the existing screenshot**. Retake only if the UI has visibly changed — layout, labels, buttons, or missing/added elements. If the screenshot still accurately represents the current portal state, mark it as `ok` and move on.

**Do not retake screenshots unconditionally.** Retake only when the comparison reveals a real discrepancy. If the user has explicitly told you the screenshots are current, mark all as `ok` without opening the browser.

## Checklist

Before starting, list every `<Frame>` in the article with the following table:

| # | Filename | Screen to reach | Status |
|---|----------|-----------------|--------|
| 1 | `filename.png` | Navigation path or step | pending |

For each row, set status to:
- `ok` — screenshot matches current portal UI, no retake needed
- `retaken` — screenshot was outdated and has been replaced
- `skip` — screenshot cannot be verified (GUI app, gated feature, user confirmed current)

Do not mark Phase 3 as completed until every row has a final status.

## How to take each screenshot

For each screenshot in the article:

1. Navigate to the correct screen in the portal using the existing article
   text as a guide — it describes what each screenshot should show.

2. **Take the screenshot with the `article-screenshot` skill.** Give it the step text next to the `<Frame>` and the target path, for example `$dest = "images\docs\{product}\{slug}\{slug}-imageN.png"`. The skill hides personal data, chooses the area by context, crops from a full-viewport capture, and checks the result. Page-level steps stay full viewport. Never skip the personal-data step: the logged-in email is always visible in the portal header.

3. Verify the file exists before moving on:
   ```powershell
   Get-ChildItem "images\docs\{product}\{slug}" | Select-Object Name
   ```

4. Update the `<Frame>` in the article using the correct format:
   ```mdx
   <Frame>![Alt text](/images/docs/{product}/{slug}/filename.png)</Frame>
   ```
   Always write the `<Frame>` on a single line with the markdown `![alt](src)` shorthand inside. Do not add `width` attributes or `<img>` tags.
5. Update the alt text if the UI shown has changed.
6. Delete the old file:
   ```powershell
   git rm images/docs/{product}/{article-slug}/{old-filename}.png
   ```

## What NOT to do with screenshots

- **Never crop** by passing `element` or `target` to `browser_take_screenshot`: the original is lost.
  The `article-screenshot` skill crops afterwards and keeps the full screenshot if a crop cannot be verified.
- **Never use `savePath`** — it is not a valid parameter. Use `filename` instead.
- **Never change the viewport, window size, or zoom.** Do not call `browser_resize`
  and do not set `document.body.style.zoom`. Capture the page exactly as the
  browser shows it.
- **Never take a screenshot immediately after scrolling** — give the page
  50–100 ms to finish rendering. Use a brief `browser_wait_for(time=100)` or
  take a `browser_snapshot` first (which forces a render cycle) before capturing.

Resources visible in screenshots follow the naming rule from Phase 2 (`my-*-1`, never `test-*`, `docs-*`, `regression-*`, Jira IDs, or article slugs).

## Check the images folder

After all screenshots are saved, run the checker and fix every line it reports:

```powershell
python .agents/tools/check_article_images.py {relative/path/to/article.mdx}
```

- `DUPLICATE` — two files have identical content, so one source screenshot was reused. Decide which filename has the correct meaning (matches alt text and article context) and retake the other. If two places in the article show the same UI state, reference the same file twice instead of copying it.
- `UNREFERENCED` — remove the file with `git rm`.
- `WRONG_FOLDER`, `MISSING`, `NO_EXTENSION` — fix the reference or the file location.

## Transient screenshots (already captured in Phase 2)

If a screenshot was captured during Phase 2 (mid-wizard dialog, resource-dependent
state), skip retaking it here. Verify it is already saved with the correct filename
and that the `<Frame>` reference and alt text are updated.
