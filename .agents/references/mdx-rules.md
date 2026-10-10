# MDX Rules — Gcore Product Documentation

Technical rules for MDX files in this repository.
All rules are Mintlify-specific and have been verified against real articles.
Load this file when a skill tells you to. Do not load it proactively.

---

## MethodSwitch component

`MethodSwitch` is a custom component that renders tabbed content (Customer Portal,
REST API, Terraform, CLI) in a single MDX file. It is the only approved way to cover
multiple methods in one article — never create separate files.

### Import line

Always import with the full `.jsx` extension:

```mdx
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";
```

**Missing `.jsx` renders the entire article as a blank page with no error.**
The MDX compiler (`@mdx-js/mdx`) does NOT catch this — the blank page appears
only in the Mintlify runtime. Always verify the import when an article renders empty.

### Structure

`<MethodSwitch>` wraps both sections. `label` belongs on `<MethodSection>`, not on `<MethodSwitch>`.

**Correct:**
```jsx
<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">
  ...
  </MethodSection>
  <MethodSection id="api" label="REST API">
  ...
  </MethodSection>
</MethodSwitch>
```

**Wrong — first MethodSection at column 0 (no indent):**
```jsx
<MethodSwitch>
<MethodSection id="portal" label="Customer Portal">
...
</MethodSection>
```

**Why this breaks:** Mintlify's cloud renderer requires the first child of `<MethodSwitch>` to
be indented 2 spaces. When it is at column 0, the renderer does not recognize it as a child
element, `MethodSwitch` receives no children, and the entire article body renders empty —
only the page title is visible. The MDX compiler (`@mdx-js/mdx`) and local `mintlify dev`
do NOT catch this; it only fails in the deployed Mintlify build.

**Wrong — blank line between `<MethodSwitch>` and first `<MethodSection>`:**
```jsx
<MethodSwitch>

<MethodSection id="portal" label="Customer Portal">
```

Same result: empty page on deploy.

**Wrong — self-closing MethodSwitch with MethodSection outside:**
```jsx
<MethodSwitch methods={[...]} />

<MethodSection id="portal">
...
</MethodSection>
```

### Tab IDs and labels

| `id` | `label` | Status |
|------|---------|--------|
| `portal` | `Customer Portal` | Active |
| `api` | `REST API` | Active |
| `terraform` | `Terraform` | Active |
| `cli` | `CLI` | Planned |

- `portal` always comes first — it is the default tab
- Do not add `terraform` or `cli` tabs until the content exists

**Never use `tab` prop instead of `id` + `label` — tabs silently disappear:**

```mdx
Wrong:   <MethodSection tab="Windows">
Correct: <MethodSection id="windows" label="Windows">
```

`method-switch.jsx` filters tabs by `c.props.id`. With only a `tab` prop, every
`<MethodSection>` maps to null, `tabs` becomes an empty array, and `<MethodSwitch>`
renders nothing. Symptom: the heading before `<MethodSwitch>` displays; everything
inside the component does not. No error is thrown — the compiler reports OK.

For non-standard tabs (platforms, environments, etc.) use a descriptive lowercase slug as `id`
and the display name as `label`. Examples: `id="windows" label="Windows"`,
`id="linux" label="Linux"`, `id="ios" label="iOS and iPadOS"`.

### How Mintlify compiles MethodSwitch internally

Mintlify wraps each custom component in an internal `_MdxComponentBoundary` element
at compile time. The `snippets/method-switch.jsx` component accounts for this: when
iterating over children it first checks for a direct `props.id` (for future-proofing),
then checks `c.props.children.props.id` to unwrap the boundary.

Do not change the filter logic in `method-switch.jsx` without understanding this.
Removing the unwrap step will break all MethodSwitch pages silently (blank page, no JS error).

### No content before `<MethodSwitch>`

All article content — including intro paragraphs — must be INSIDE a `<MethodSection>`.
Nothing goes between the import line and `<MethodSwitch>`.

### Content rules inside `<MethodSection>`

`<MethodSection>` is a passthrough component. When nested inside `<MethodSwitch>`,
MDX compiles its children in **expression mode**, not flow mode. Plain markdown
paragraphs become text strings — blank lines are stripped and content runs together.

**Rules for all content inside `<MethodSection>`:**

**1. Numbered steps — wrap every step in `<p>` and write the number as plain `1.` (not `1\.`):**
```mdx
<p>1. Navigate to **Networking** > **Security Groups**.</p>

<p>2. Find the required security group and click its name.</p>
```
Without `<p>`, `MethodSwitch` merges all numbered steps into a single paragraph ("1. ... 2. ... 3. ...") and nothing can split them again.
Put a blank line between steps. Sub-items are plain bullets, indented 3 spaces, placed after the `<p>` of their step:
```mdx
<p>1. Open the creation form:</p>

   - In the Cloud menu, click **Create**.
   - On the VM creation page, navigate to **Networking**.
```

**2. Every prose paragraph — wrap in `<p>` tags:**
```mdx
<p>Both options can be combined. If neither is specified, the rule applies to all IP addresses.</p>
```
Wrap ALL standalone prose paragraphs inside `<MethodSection>` — without exception.
Do not try to determine whether a paragraph is adjacent to a specific block element.
Just wrap every prose paragraph. This eliminates all ambiguity about before/after `<Frame>`,
before/after code blocks, before/after `<Tabs>`, and between numbered steps — all covered
by one rule: every paragraph gets `<p>`.

**3. Bullet-only lists — use `-` at column 0:** `<ul>/<li>` is block-level and renders correctly without wrapping.

**4. JSX components (`<Info>`, `<Frame>`, `<Warning>`, `<Note>`):** always block-level, no special treatment needed.

**5. Structural separators — never remove, only replace text:**

Inside `<MethodSection>`, `<Info>`, `<Warning>`, and `<p>` tags that appear between numbered list items act as structural anchors for the MDX parser — not just as content containers. Removing such a tag (even if the text inside is outdated) changes how the parser reads surrounding numbered lists and can cause the entire page to render blank.

**Rule:** When removing outdated information from a structural element, replace the text inside the tag with neutral content. Never delete the tag itself.

```mdx
# Wrong — blank page after this edit
4. Set **Outbound rules** to define the allowed outgoing traffic.
   Click **Add rule** and select a template or custom rule.   <- inline, Info removed

# Correct — keep the tag, update text
4. Set **Outbound rules** to define the allowed outgoing traffic.

<Info>
By default, all outbound traffic is allowed. Add outbound rules only to restrict specific traffic.
</Info>

<p>Click **Add rule** and select a template or custom rule.</p>
```

A structural separator is any JSX block that sits between a numbered step header and its sub-bullets, or between the last content of one step and the next numbered step.

### Closing tag indent after a list

When a markdown list item immediately precedes `</MethodSection>` or `<MethodSection>`,
that tag must have **zero indentation**. Any indentation causes MDX to treat the tag
as list-item continuation content — the tag becomes invisible to the parser.

**Wrong (tag indented after list):**
```markdown
- Last bullet item.

  </MethodSection>
  <MethodSection id="api" label="REST API">
```

**Correct (tag at column 0):**
```markdown
- Last bullet item.

</MethodSection>
<MethodSection id="api" label="REST API">
```

Symptoms when violated: numbered steps appear merged into the preceding paragraph;
JSX structure appears broken in the active section.

### No `####` headings inside `<MethodSection>`

`MethodSwitch` hides TOC entries only for `h2[id]` and `h3[id]`. Any `####` (h4)
heading inside an inactive `<MethodSection>` is **not hidden** and leaks into the
active tab's TOC.

**Wrong:**
```markdown
#### Sharing a pool across multiple listeners
```

**Correct — use bold text instead:**
```markdown
**Sharing a pool across multiple listeners**
```

### Prose before `<Accordion>` loses spacing

When a prose paragraph immediately precedes an `<Accordion>` inside `<MethodSection>`,
Mintlify does not apply `margin-bottom` to the paragraph — the accordion visually
"glues" to the text above it.

**Fix — wrap the paragraph in an explicit `<p>` tag:**

**Wrong:**
```markdown
Each step below explains what the call does.

<Accordion title="Show all steps">
```

**Correct:**
```markdown
<p>Each step below explains what the call does.</p>

<Accordion title="Show all steps">
```

Applies to every prose paragraph that immediately precedes `<Accordion>` inside any
`<MethodSection>`. Does not affect content outside JSX.

### `<p>` for all prose inside `<MethodSection>`

Inside `<MethodSection>`, every standalone prose paragraph must be wrapped in `<p>`.
This covers all cases: before/after `<Frame>`, before/after code blocks,
before/after `<Tabs>`, and between numbered steps.

**The rule is simple: if it is a prose paragraph inside `<MethodSection>`, it gets `<p>`.**

**When to use `<p>`:**
- Every standalone prose paragraph inside `<MethodSection>`

**Correct:**
```mdx
<p>Upload the compiled binary file:</p>

<Frame>![Upload binary dialog](/images/docs/fastedge/.../upload-binary.png)</Frame>

<p>After uploading, click **Save binary** to confirm.</p>
```

```mdx
<p>Run the following command to compile:</p>

```sh
cargo build --target wasm32-wasi --release
```

<p>The output file is located in `target/wasm32-wasi/release/`.</p>
```

**Never wrap in `<p>`:**
- Bullet list items (`-`, `*`) — block-level, renders correctly without wrapping
- JSX components (`<Info>`, `<Warning>`, `<Frame>`, `<Tabs>`) — already block-level

**Numbered list items — wrap each item individually:**
```mdx
<p>1. Navigate to **Streaming** > **AI**.</p>
<p>2. In the **Origin URL** field, enter the link to your MP4 video.</p>
<p>3. Click **Generate task**.</p>
```
Without `<p>`, numbered items inside `<MethodSection>` merge into a single line, because `MethodSwitch` compiles its children in expression mode.

This applies inside any `<MethodSection>`. Does not apply to content outside `<MethodSection>`.

---

## Frontmatter

Every article must have these fields in the frontmatter block:

```yaml
---
title: Create a Virtual Machine
sidebarTitle: Create an instance
description: Create a Gcore Cloud Virtual Machine with an image, flavor, volume, network, and firewall.
---
```

### Field rules

| Field | Required | Notes |
|-------|----------|-------|
| `title` | Always | Full title shown in browser tab and page heading |
| `sidebarTitle` | Optional | Shorter label for the left sidebar navigation |
| `description` | Required | Search summary, 140 characters maximum. See rules below |

### `description` rules

This field is the search summary. Mintlify copies it into the meta description and also prints it under the title. `custom.css` hides that paragraph. `llms.txt` reads the same sentence.

**Required:**
- One sentence, 140 characters maximum
- Summarize what the article is about. Use the feature name and the words a person would type into search
- Do not write Portal, API, or Terraform. Naming the interface does not help search
- No "you", "your", "this article", "learn how to"

Do not rewrite existing descriptions to this rule unless the task is a description pass.

**Strictly forbidden — these break the YAML parser and crash the Mintlify build:**
- Curly braces: `{task_id}` or `{variable}` — even inside apparent text
- Slashes: `/cloud/v1/tasks` — no URL paths
- Colons: any `:` inside the value — YAML treats it as a key separator
- Hash: `#` — YAML treats it as a comment start
- Backticks, square brackets, pipe characters

The CI `sanitize-ai-navigation` workflow auto-replaces `:` and `#` with ` -`,
but the result may look wrong. Avoid these characters from the start.

**Safe:** commas, periods, hyphens, parentheses, semicolons, capitalized product names,
descriptive terms without symbols ("task ID", "project ID")

**Good examples:**
```yaml
description: Create a Gcore Cloud Virtual Machine with an image, flavor, volume, network, and firewall.
description: Issue a token with an expiration date and a limit on what the token can access.
```

**Bad examples (will break build):**
```yaml
description: Poll GET /cloud/v1/tasks/{task_id} until state is FINISHED.
description: Configure the Authorization: APIKey header.
```

---

## MDX parsing gotchas

### `{identifier}` inside inline code — use backticks, never `<code>`

MDX treats `{...}` as a JSX expression **even inside `<code>` HTML elements**. If the
identifier is a valid JavaScript name (`task_id`, `project_id`, `LB_VIP`), the parser
throws at compile time. The page renders as a blank shell — no error is shown in the browser.

**Wrong — `<code>` does NOT escape curly braces in MDX:**
```
Poll <code>GET&nbsp;/cloud/v1/tasks/{task_id}</code> every 5 seconds.
```

**Correct — backtick code spans escape their content; `{...}` is treated as literal text:**
```
Poll `GET /cloud/v1/tasks/{task_id}` every 5 seconds.
```

`{...}` inside triple-backtick fenced code blocks is also always safe.

**How to find violations:**
```
rg "<code>[^<]*\{[^}]+\}[^<]*</code>" path/to/article.mdx
```

### PowerShell file edits corrupt non-ASCII characters

`Get-Content` + `Set-Content` without explicit encoding uses the system ANSI codepage
(Windows-1252), which cannot represent Unicode characters such as em dashes (`—`, U+2014),
non-breaking spaces, or any other non-ASCII character. They are silently replaced with `?`.

**Never edit MDX files with PowerShell `Set-Content` without specifying UTF-8:**

```powershell
# Wrong — corrupts em dashes and other non-ASCII characters
$c = Get-Content file.mdx -Raw
$c = $c -replace 'foo', 'bar'
Set-Content file.mdx $c

# Correct — preserves UTF-8 encoding
$c = [System.IO.File]::ReadAllText('file.mdx', [System.Text.Encoding]::UTF8)
$c = $c -replace 'foo', 'bar'
[System.IO.File]::WriteAllText('file.mdx', $c, [System.Text.Encoding]::UTF8)
```

**Recovery:** if corruption has already occurred (em dashes show as `?` in the browser),
the affected characters have a space on both sides — use ` — ` as the replacement pattern:

```powershell
$c = [System.IO.File]::ReadAllText('file.mdx', [System.Text.Encoding]::UTF8)
$c = $c -replace ' \? ', ' — '
[System.IO.File]::WriteAllText('file.mdx', $c, [System.Text.Encoding]::UTF8)
```

This is safe because URL query strings use `?` without surrounding spaces.

### CRITICAL: Never simplify method-switch.jsx

`snippets/method-switch.jsx` must NOT be refactored or simplified. The child-resolution
logic in `MethodSwitch` is intentionally defensive:

```javascript
const tabs = React.Children.toArray(children).map((c) => {
  if (!c || !c.props) return null;
  if (c.props.id) return c;
  const inner = c.props.children;
  if (inner && inner.props && inner.props.id) return inner;
  return null;
}).filter(Boolean);
```

**Why it must stay this way:** Mintlify's runtime wraps `<MethodSection>` children in an
intermediate element before passing them to `MethodSwitch`. The simplified `.filter(c => c.props.id)`
does NOT see `id` on the wrapper — it returns `tabs = []` — and the entire article renders
as a blank page (only the title and ToC appear).

**Symptom:** deployed article shows only title + ToC; empty `<div role="tablist">` in DOM.

**Root cause confirmed by DOM inspection:** `document.querySelector('[role=tablist]').parentElement.childElementCount === 1`
(only the tablist div, no content divs — because `tabs.map(...)` produces nothing).

The simplified version works locally (`mintlify dev`) and passes the MDX compiler — the
blank page appears ONLY on Mintlify deploy. Do not "fix" this code.

---

### UTF-8 BOM at the start of a file

Files must not start with a UTF-8 BOM (`\xEF\xBB\xBF`). A BOM before the `---`
frontmatter delimiter breaks the YAML parser and produces a generic "parsing error"
with no line number.

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

## Image display width

All screenshots use a single-line `<Frame>` with a markdown image shorthand inside.
Do not add `width` attributes or `style` props — let Mintlify size the image naturally.

**Correct:**
```mdx
<Frame>![Alt text](/images/docs/...)</Frame>
```

**Wrong — width attribute breaks on Mintlify production:**
```mdx
<Frame>
  <img src="/images/docs/..." alt="Alt text" width="70%"/>
</Frame>
```

**Wrong — style prop is unnecessary and inconsistent with the rest of the repo:**
```mdx
<Frame>
  <img src="/images/docs/..." alt="Alt text" style={{width: "70%"}}/>
</Frame>
```

To convert `<img ... width="N%"/>` tags in a file back to markdown shorthand, use the script
`scripts/fix_image_widths.py` from the repository root:

```powershell
python scripts/fix_image_widths.py path/to/article.mdx
```

The script:
- Converts `<img src="src" alt="alt" width="N%"/>` to `![alt](src)`
- Writes UTF-8 with LF line endings and no BOM

---

## Internal links

All internal links must be root-relative:

**Correct:**
```mdx
See the [VM guide](/cloud/virtual-instances/create-an-instance).
```

**Wrong — full URL:**
```mdx
See the [VM guide](https://docs.gcore.com/cloud/virtual-instances/create-an-instance).
```

**Wrong — old path that no longer exists:**
```mdx
See the [VM guide](/cloud/api/virtual-instances/create-an-instance).
```

The `/cloud/api/` directory no longer exists. All merged articles live at
`/cloud/{section}/{article}`.

Anchor links work as usual:
```mdx
[SSH key setup](/cloud/virtual-instances/create-an-instance#step-1-add-an-ssh-key)
```

---

## Validation

Validate MDX locally before committing. The compiler gives exact error line and column numbers,
unlike the generic "parsing error" shown in the browser.

```powershell
.\.agents\tools\validate_mdx.ps1 path\to\article.mdx
```

The script installs the compiler once into `$env:TEMP\mdx-check` (outside the repository) and prints `OK`
or the exact error.

**Note:** the compiler does NOT catch the missing `.jsx` extension in the MethodSwitch
import — that error appears only in the Mintlify runtime.

---

## Steps component

Use `<Steps>` with `<Step>` for procedures with large steps, where each step is a mini-task made of several actions. This renders numbered UI blocks with a title and body. Procedures with short steps use a plain numbered list (see `procedures.md`, "Choosing the format").

### When to use

Use `<Steps>` when each step consists of several actions the reader must perform in order, for example configuring a resource through a form, with a screenshot or callout inside the step.

Do **not** use `<Steps>` for short single-action steps (use a numbered list), conceptual lists, reference tables, or a single action.

### Basic structure

```mdx
<Steps>
  <Step title="Open the settings">
    In the **Cloud** menu, select **Networking** and then **Load Balancers**. Click the name.
  </Step>
  <Step title="Configure the option">
    Toggle **Enable Feature** and select a value from the dropdown.

    <Frame>![Alt text describing the screenshot](/images/docs/.../screenshot.png)</Frame>
  </Step>
  <Step title="Save">
    Click **Save changes**.
  </Step>
</Steps>
```

### Rules

- `<Step title="...">` — the `title` attribute is required; it renders as the bold heading next to the number.
- Keep the title in **sentence case**: `"Open the Load Balancer settings"`, not `"Open The Load Balancer Settings"`.
- Body content inside `<Step>` follows all normal MDX rules: prose, `<Frame>`, code blocks, nested lists.
- A `<Frame>` screenshot goes **inside** the relevant `<Step>`, after the instructions that describe the UI state being shown.
- Do not number the steps manually — the component handles numbering.
- **Three forms of a step** (very small, with a little explanation, large and complex): see `procedures.md`, "Three forms of a `<Step>`".
- **No body that restates the title.** If the body text is identical or near-identical to the title, omit the body entirely — the title alone is sufficient. A step with only a title renders correctly and is less noisy than a title + one-word restatement.

**Wrong — body restates title:**
```mdx
<Step title="Create the cluster">
  Click **Create Cluster**.
</Step>

<Step title="Select a region">
  Select a region where Spot is available.
</Step>
```

**Correct — body omitted when title says it all:**
```mdx
<Step title="Create the cluster">
</Step>

<Step title="Select a region">
  <Frame>![Region selector](/images/docs/.../region-selector.png)</Frame>
</Step>
```

### Converting an existing list

Convert a plain numbered list to `<Steps>` only when its steps are large: each step has several actions, a screenshot, or a callout. Do not convert lists of short steps. A section title such as "Enable X" or "Create X" does not decide the format; the size of the steps does.
