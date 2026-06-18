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
When the identifier (`task_id`, `project_id`, etc.) is not defined in scope, compilation
fails silently. The MethodSwitch component receives `undefined` children → `tabs = []`.

**Find:**
```
rg "<code>[^<]*\{[^}]+\}[^<]*</code>" path/to/article.mdx
```

**Fix — replace `<code>` with backtick inline code:**
```
# Wrong
Poll <code>GET&nbsp;/cloud/v1/tasks/{task_id}</code> every 5 seconds.

# Correct
Poll `GET /cloud/v1/tasks/{task_id}` every 5 seconds.
```

Files fixed: `cloud/virtual-instances/create-an-instance.mdx`,
`cloud/networking/add-and-configure-a-firewall.mdx` (PR #2208, June 2026).

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
