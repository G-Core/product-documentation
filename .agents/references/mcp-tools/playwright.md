# Playwright MCP — Browser Testing Guide

Instructions for using Playwright MCP to test portal UI steps and capture screenshots.
Load this file when a skill tells you to. Do not load it proactively.

---

## Available tools

```
mcp__playwright__browser_navigate   — open a URL
mcp__playwright__browser_click      — click a UI element
mcp__playwright__browser_type       — type into a field
mcp__playwright__browser_snapshot   — get DOM/accessibility tree (read UI labels)
mcp__playwright__browser_screenshot — capture the current page visually
mcp__playwright__browser_evaluate   — run JavaScript (scroll, zoom, collapse sidebar)
mcp__playwright__browser_select     — select from a dropdown
mcp__playwright__browser_hover      — hover over an element
```

**Key distinction:**
- Use `browser_snapshot` to **read** current UI element names, labels, button text
- Use `browser_screenshot` to **capture** a visual for comparison or saving

When verifying that UI matches an article — always `browser_snapshot` first to read
the actual labels, then `browser_screenshot` to capture if a new screenshot is needed.

---

## Portal access

```
URL:   https://portal.gcore.com/
Login: SSO only — use sergey.kostichev@gcore.com
```

Do not use username/password login — it will not work on this account.

---

## SSO login flow

The SSO login requires one manual step from the user. Follow this sequence:

1. Navigate to `https://auth.gcore.com/login/signin`
2. Click **SSO**
3. Enter `gcore.com` in the "Work domain" field and press Enter
4. Microsoft login page appears — enter `sergey.kostichev@gcore.com` and click **Next**
5. **STOP — ask the user to complete Windows Hello authentication** (Face, fingerprint, PIN, or security key). A native OS-level dialog appears on their desktop. Playwright cannot automate this step.
6. After the user confirms, the browser lands on `https://portal.gcore.com/accounts/reports/dashboard`

**Why user input is required:** Playwright runs a fresh browser context with no cached
credentials. Microsoft's FIDO2/passkey flow opens a native OS dialog that cannot be
automated. Do not attempt to bypass it — ask the user to confirm, then continue.

---

## Screenshot capture standards

### Before every screenshot

1. **Collapse the portal sidebar.** The left sidebar occludes the main content area.
   Use `browser_evaluate` to collapse it, or click the collapse icon on the left edge.
   Verify the sidebar is gone before taking the screenshot.

2. **Scroll to the target element:**
   ```javascript
   // browser_evaluate
   document.querySelector('selector').scrollIntoView()
   ```

3. **Set zoom if needed:**
   ```javascript
   // Zoom in — target is small or text is hard to read
   document.body.style.zoom = '1.25'

   // Zoom out — target is wide (tables, multi-column layouts)
   document.body.style.zoom = '0.8'

   // Reset after capturing
   document.body.style.zoom = '1'
   ```

### Capture settings

| Setting | Rule |
|---------|------|
| Browser width | 1280px minimum (1440px for wide layouts) |
| Zoom | 100% unless adjusted per above |
| Theme | Light mode only |
| Language | English (US) |
| Personal data | None visible — no real emails, names, user IDs, tokens |
| Browser chrome | Crop out toolbar, tab bar, address bar, OS taskbar |
| Cursor | Not visible in screenshot |
| Selected text | Not visible in screenshot |

### Framing

Do not submit a full-page screenshot when the subject is a small part of the page.

- **Crop to the dialog or form:** use the `clip` parameter in `browser_screenshot`
- **Zoom in** when controls or labels would otherwise be too small to read
- **Zoom out** when a wide table would cause horizontal scrolling artifacts
- Be dynamic — adjust zoom, scroll position, and clip per screenshot

### File format

- **Format:** PNG for all UI screenshots
- **Extension:** lowercase `.png` — never `.PNG`
- **Size:** under 500 KB — compress with pngquant if over limit

### Naming

- Descriptive lowercase names with hyphens only — no spaces, underscores, camelCase
- Name describes what is shown, not the step number:
  - Good: `create-instance-form.png`
  - Bad: `step-3.png`
- **Always rename when replacing a screenshot** — reusing the same filename causes CDN
  caching where the old image stays visible after publishing
- **Delete the old file** after renaming: `git rm old-name.png`

### Alt text

- Required on every image
- Under 125 characters, sentence case (capitalize first word only)
- Describe what is shown, not what the user should do
- Do not start with "Screenshot of", "Image of", "A picture of"

| Bad | Good |
|-----|------|
| `Screenshot of the DNS page` | `DNS records list with the Add record button highlighted` |
| `Image showing the create form` | `Instance creation form with flavor and region fields` |

### Annotations

- No red arrows
- Highlight rectangles (subtle stroke) only when the target is not obvious from the text
- Annotations are done in Figma using the Screenshots for product docs library

---

## Image verification before publishing

Before finalising any article that contains images, verify every image actually exists.

### Check each image reference

For each `<Frame>`, `<img>`, or `![]()` in the article:

1. Extract the path from `src="..."` or `![](...)`
2. Check the file exists:
   ```powershell
   Test-Path "C:\Projects\product-documentation{image-path}"
   ```
3. If the file does not exist — flag it. Do not change the path without confirming
   the file exists at the new location.

**Critical rule:** never change an image path without first verifying the file
exists with the new name. Changing a path to a non-existent file breaks the image silently.

### Detect corrupted image files

Some files in the repo are data URIs saved as files instead of actual images.
Check the first bytes before using a file:

```powershell
$bytes = [System.IO.File]::ReadAllBytes("C:\Projects\product-documentation\images\file.png")[0..3]
```

Valid signatures:
- PNG: `137 80 78 71` (bytes: `0x89 0x50 0x4E 0x47`)
- JPEG: `255 216 255` (bytes: `0xFF 0xD8 0xFF`)
- GIF: `71 73 70` (bytes: `0x47 0x49 0x46`)

If the file starts with `100 97 116 97 58` (= "data:") — it is a corrupted data URI:

```powershell
$content = Get-Content "corrupted-file" -Raw
if ($content -match "base64,(.+)") {
    $decoded = [Convert]::FromBase64String($Matches[1])
    [System.IO.File]::WriteAllBytes("fixed-file.png", $decoded)
}
```

### Fix broken images

If an image file is missing or has no extension:
1. Rename/copy to correct name with `.png` extension
2. Update the path in the article to match
3. Both changes go in the same commit
4. Note the change in the changelog file

**Images must have a file extension.** A file without `.png`, `.jpg`, or `.gif`
will not display in browsers.

---

## Screenshot file path limitation

`browser_screenshot` with a `filename` parameter can only save files inside the
**current working directory** of the active project. It cannot write directly to
`C:\Projects\product-documentation`.

**Workaround:** Save to the current project directory first, then copy with PowerShell:

```powershell
Copy-Item ".\screenshot.png" `
          "C:\Projects\product-documentation\images\docs\{product}\{slug}\screenshot.png" -Force
```

Screenshot storage path in the docs repo:
```
C:\Projects\product-documentation\images\docs\{product}\{article-slug}\{filename}.png
```

Referenced in MDX as:
```
/images/docs/{product}/{article-slug}/{filename}.png
```

**Folder rule:** every article has its own subfolder matching the article path.
Article `account-settings/my-profile/overview.mdx` → images at
`images/docs/account-settings/my-profile/overview/`.
Never save images to the product root folder.

---

## Known portal quirks

Update this section when you discover new quirks during testing.

- **Login is SSO only** — no username/password option on the login page
- **Portal URL structure:** `https://portal.gcore.com/{product}/...` — some products
  use different sub-paths; confirm by navigating in the browser
- **If `mcp__playwright__*` tools are unavailable** at session start: restart Claude Desktop.
  Do not attempt portal verification without Playwright — it is mandatory.
- **Playwright availability check:** if ToolSearch returns no matches for playwright,
  stop and tell the user before starting any audit work

---

## Testing protocol (for full-audit skill)

When executing an article step-by-step:

1. Open the portal and navigate to the section the article describes
2. Follow the article's steps in order, as a real user would
3. At each step, use `browser_snapshot` to read actual current UI labels
4. Use `browser_screenshot` to capture screens that have a corresponding screenshot
5. Record every divergence in FINDING format:

```
FINDING: [category]
Location: Step N / screenshot name
Article says: "..."
Portal shows: "..."
Action needed: rename / reorder / add step / update screenshot / remove
```

Categories:
- Wrong UI element names
- Changed navigation path
- Step order changed
- Missing steps (new mandatory step not in article)
- Outdated screenshots
- Missing sections (new feature not documented)
- Wrong field names
- Deprecated options

**Do not fix anything during testing. Collect findings first, apply fixes after.**

If the task cannot be completed (feature gated, account limitation, region unavailable):
note the blocker, describe how far you got, mark specific findings as unverified.
