# Troubleshooting — Mintlify / MDX Build Issues

Known issues with symptoms, root causes, and fixes.
Load this file when a page renders incorrectly, is blank, or returns 404 on preview.

---

## Page renders as blank (empty content area)

The page loads, the title appears in the browser tab, but the content area is empty.
On PR previews the page may return 404 instead.

### Symptom in the DOM

```
<div id="content">
  <div>
    <div role="tablist"></div>  <!-- empty, no buttons -->
  </div>
</div>
```

`MethodSwitch` renders its outer shell but `tabs` is empty — no tab buttons,
no content panels.

### Root cause A: `{identifier}` inside a `<code>` HTML element

MDX treats `{...}` as a JSX expression even inside lowercase HTML elements like `<code>`.
When the identifier (`task_id`, `project_id`, etc.) is not defined in scope, MDX fails.

**Two failure modes depending on context:**

- **Inside `<MethodSection>`:** compilation fails silently. The MethodSwitch component
  receives `undefined` children → `tabs = []` → blank page.
- **Outside `<MethodSection>` (top-level or in a plain article):** `mintlify dev` fails
  to start with an explicit parse error pointing to the file and line:
  ```
  parsing error .\cloud\path\article.mdx:91:8 - Expected a closing tag for `<code>`
  (91:207-91:213) before the end of `paragraph`
  ```
  Mintlify reports the error at the `<code>` opening tag position. If the `<code>` tag
  is inside a `<MethodSection>`, the error may be reported at the `<MethodSection>`
  opening line instead of the actual `{identifier}` location — scan the entire section.

**Find:**
```powershell
# Scan one file
rg "<code>[^<]*\{[^}]+\}[^<]*</code>" path/to/article.mdx

# Scan all changed files
git diff --name-only HEAD | ForEach-Object { rg "<code>[^<]*\{[^}]+\}[^<]*</code>" $_ }
```

**Fix — replace `<code>` with backtick inline code:**
```
# Wrong — API path with placeholder
Poll <code>GET&nbsp;/cloud/v1/tasks/{task_id}</code> every 5 seconds.

# Wrong — Windows path with placeholder
The default directory is <code>C:\Users\{username}\.ssh\</code> for Windows.

# Correct — backtick code spans treat {…} as literal text
Poll `GET /cloud/v1/tasks/{task_id}` every 5 seconds.
The default directory is `C:\Users\{username}\.ssh\` for Windows.
```

Note: `&nbsp;` inside `<code>` becomes a regular space in backtick code — this is fine.

Files fixed: `cloud/virtual-instances/create-an-instance.mdx`,
`cloud/networking/add-and-configure-a-firewall.mdx` (PR #2208, June 2026),
`cloud/kubernetes/clusters/upgrade.mdx` line 286,
`cloud/virtual-instances/connect/connect-to-your-instance-via-ssh.mdx` line 91
(branch DOC-1544, June 2026).

### Root cause B: `{identifier}` inside `ai-navigation` frontmatter

The CI workflow sanitizes `:` and `#`, but does not remove `{...}`. The YAML parser
crashes, the frontmatter is not read, and Mintlify cannot compile the page.

**Fix:** remove curly braces from `ai-navigation`. Use plain English ("task ID", not `{task_id}`).

See also: `mdx-rules.md` → `ai-navigation` rules.

### Root cause C: Missing `.jsx` extension on MethodSwitch import

```
# Wrong — Mintlify cannot resolve the module
import { MethodSwitch, MethodSection } from "/snippets/method-switch";

# Correct
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";
```

The MDX compiler does not catch this — the blank page appears only at runtime.

### Root cause D: `_MdxComponentBoundary` wrapping strips `props.id` from tabs (component bug, fixed Jun 2026)

**Symptom:** MethodSwitch renders the outer shell and the tablist div, but the tablist is empty — no tab buttons, no content. All pages using MethodSwitch are affected simultaneously.

**Root cause:** Mintlify's MDX compiler wraps every custom component in an internal `_MdxComponentBoundary` element. When MethodSwitch called `React.Children.toArray(children)`, it received `_MdxComponentBoundary` wrappers, not `MethodSection` elements. The old filter `c => c && c.props && c.props.id` looked for `.props.id` directly on the boundary element — but boundaries have `.props.name`, not `.props.id`. All children were filtered out → `tabs = []`.

Confirmed by inspecting the compiled Next.js RSC payload in DevTools:
```javascript
// script tag in the page — Mintlify compiles MethodSection as null on the server:
const MethodSection = () => null;
const MethodSwitch = () => null;
// and wraps each call in _MdxComponentBoundary:
_jsx(_MdxComponentBoundary, {
  name: "MethodSection",
  children: _jsxs(MethodSection, { id: "portal", label: "Customer Portal", children: [...] })
})
```

**Fix (already applied to `snippets/method-switch.jsx`):** unwrap the boundary before filtering:
```javascript
const tabs = React.Children.toArray(children).map((c) => {
  if (!c || !c.props) return null;
  if (c.props.id) return c;                              // direct MethodSection (fallback)
  const inner = c.props.children;
  if (inner && inner.props && inner.props.id) return inner; // unwrap _MdxComponentBoundary
  return null;
}).filter(Boolean);
```

**This was a bug in the component, not in MDX content.** No per-article fix is needed — the updated `snippets/method-switch.jsx` resolves it globally.

### Root cause E: UTF-8 BOM at the start of the file

A BOM (`\xEF\xBB\xBF`) before the `---` frontmatter delimiter breaks the YAML parser.
Mintlify cannot read the frontmatter and may skip or mis-render the page.

**Check:**
```powershell
python -c "d=open('article.mdx','rb').read(); print('BOM' if d.startswith(b'\xef\xbb\xbf') else 'OK')"
```

**Strip:**
```python
data = open('article.mdx', 'rb').read()
if data.startswith(b'\xef\xbb\xbf'):
    open('article.mdx', 'wb').write(data[3:])
```

### Root cause F: Removing structural JSX elements breaks numbered list parsing inside MethodSection

**Symptom:** After editing an article to remove a content block (`<Info>`, `<Warning>`, or a `<p>` tag), the entire page goes blank or renders only the title. The removed element contained only content that seemed safe to delete.

**Root cause:** Inside `<MethodSection>`, Mintlify's MDX parser uses JSX block elements (`<Info>`, `<Warning>`, `<p>`) as structural anchors that separate numbered list items and reset list context. Removing such an element changes how the parser understands surrounding content — especially numbered lists followed by bullet lists, `<Frame>`, or further `<p>` tags. The parser mis-reads the structure and the section fails to compile.

This is not about the text inside the element — **the tag itself is the separator**. Replacing text content is safe; removing the tag is not.

**Rule: When editing content to remove outdated information, ONLY change the text inside existing tags. Never delete a `<Info>`, `<Warning>`, or `<p>` tag that sits between numbered list items inside a MethodSection.**

**Safe approach:**
```mdx
# Wrong — removing the block breaks structure
4. Set **Outbound rules** to define the allowed outgoing traffic.

<p>Click **Add rule** and select a template or custom rule.</p>

# Correct — keep the block, change its text or replace with neutral content
4. Set **Outbound rules** to define the allowed outgoing traffic.

<Info>
By default, all outbound traffic is allowed. Add rules only to restrict specific destinations.
</Info>

<p>Click **Add rule** and select a template or custom rule.</p>
```

**How to identify structural elements:** Any `<Info>`, `<Warning>`, or `<p>` tag that appears between a numbered step header and its sub-bullets, or between the last sub-item of one step and the next numbered step, is a structural separator — treat it as load-bearing.

---

## MethodSection content not rendering (steps merge, headings disappear)

Steps appear as one unbroken block, or sections from another tab bleed into the active tab.

### Root cause: indented `</MethodSection>` after a markdown list

When `</MethodSection>` or `<MethodSection>` follows a markdown list item and is
indented by 2+ spaces, MDX treats the tag as list-item continuation text. The tag
is invisible to the parser — the section is never closed properly.

**Wrong:**
```markdown
- Last bullet item.

  </MethodSection>
  <MethodSection id="api" label="REST API">
```

**Correct — closing/opening tags at column 0 after a list:**
```markdown
- Last bullet item.

</MethodSection>
<MethodSection id="api" label="REST API">
```

See `mdx-rules.md` → "Closing tag indent after a list".

---

## h4 headings leak into the wrong tab's TOC

`####` headings inside an inactive `<MethodSection>` appear in the active tab's
table of contents because `MethodSwitch` only filters `h2` and `h3` entries.

**Fix:** replace `####` headings inside `<MethodSection>` with bold text (`**Title**`).

---

## Prose paragraph glues to the accordion above it

A paragraph immediately before `<Accordion>` inside `<MethodSection>` has no bottom
margin — the components visually merge.

**Fix:** wrap the paragraph in `<p>...</p>`.

---

## Page returns 404 on Mintlify PR preview

The PR preview shows "Page Not Found" for a page that exists in the file tree.

This usually means Mintlify failed to compile the MDX file. Common causes:
1. Any of the blank-page root causes above (the build fails; there is no cached version to fall back to on preview, unlike production)
2. The page path is not in `docs.json` navigation yet

On production, Mintlify may fall back to a previously compiled version,
showing a stale or blank page instead of 404.

---

## How to validate MDX locally

```powershell
# Install once
cd C:\Temp; npm install @mdx-js/mdx

# Validate
node -e "
const {compile}=require('@mdx-js/mdx');
const fs=require('fs');
const c=fs.readFileSync('path/to/article.mdx','utf8');
compile(c).then(()=>console.log('OK')).catch(e=>console.error('ERROR:',e.message));
"
```

The compiler reports exact line and column numbers for JSX/MDX errors.
It does NOT catch missing `.jsx` import extensions or BOM issues.
