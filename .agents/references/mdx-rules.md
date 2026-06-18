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
| `terraform` | `Terraform` | Planned |
| `cli` | `CLI` | Planned |

- `portal` always comes first — it is the default tab
- Do not add `terraform` or `cli` tabs until the content exists

### No content before `<MethodSwitch>`

All article content — including intro paragraphs — must be INSIDE a `<MethodSection>`.
Nothing goes between the import line and `<MethodSwitch>`.

### Content rules inside `<MethodSection>`

`<MethodSection>` is a passthrough component. When nested inside `<MethodSwitch>`,
MDX compiles its children in **expression mode**, not flow mode. Plain markdown
paragraphs become text strings — blank lines are stripped and content runs together.

**Rules for all content inside `<MethodSection>`:**

**1. Numbered steps — use `1.` (not `1\.`):**
```
1. Go to **Networking** > **Security Groups**.
2. Find the required security group and click its name.
```
Sub-items indent 3 spaces:
```
1. Open the creation form:
   - In the Cloud menu, click **Create**.
   - On the VM creation page, go to **Networking**.
```

**2. Prose paragraphs between steps — wrap in `<p>` tags:**
```mdx
<p>Both options can be combined. If neither is specified, the rule applies to all IP addresses.</p>
```
Do NOT leave prose paragraphs unwrapped — they merge with adjacent content and render
as one unbroken block.

**3. Bullet-only lists — use `-` at column 0:** `<ul>/<li>` is block-level and renders correctly without wrapping.

**4. JSX components (`<Info>`, `<Frame>`, `<Warning>`, `<Note>`):** always block-level, no special treatment needed.

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

---

## Frontmatter

Every article must have these fields in the frontmatter block:

```yaml
---
title: Create a Virtual Machine
sidebarTitle: Create an instance
ai-navigation: Create Linux or Windows Virtual Machines in Gcore Cloud via Customer Portal or via REST API.
---
```

### Field rules

| Field | Required | Notes |
|-------|----------|-------|
| `title` | Always | Full title shown in browser tab and page heading |
| `sidebarTitle` | Optional | Shorter label for the left sidebar navigation |
| `ai-navigation` | Required for tabbed articles | See rules below |
| `description` | **NEVER USE** | Mintlify renders it as visible text on the page |

### `ai-navigation` rules

This field is read by AI agents scanning the sitemap. It must be a single plain English
sentence describing what the article covers.

**Required:**
- One sentence, ending with a period
- Starts with an action verb: Create, Configure, Manage, Enable, etc.
- Mentions all methods covered: "via Customer Portal or via REST API"
- Max 160 characters
- No "you", "your", "this article", "learn how to"

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
ai-navigation: Create Linux or Windows Virtual Machines in Gcore Cloud via Customer Portal by configuring image, flavor, volumes, network, and firewall, or via REST API using the Instances API.
ai-navigation: Create, use, or delete permanent API tokens with configurable expiration dates and role-based access control.
```

**Bad examples (will break build):**
```yaml
ai-navigation: Poll GET /cloud/v1/tasks/{task_id} until state is FINISHED.
ai-navigation: Configure the Authorization: APIKey header.
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
# Install once (run from any temp dir)
cd C:\Temp; npm install @mdx-js/mdx

# Validate an article
node -e "
const {compile}=require('@mdx-js/mdx');
const fs=require('fs');
const c=fs.readFileSync('path/to/article.mdx','utf8');
compile(c).then(()=>console.log('OK')).catch(e=>console.error('ERROR:',e.message));
"
```

**Note:** the compiler does NOT catch the missing `.jsx` extension in the MethodSwitch
import — that error appears only in the Mintlify runtime.
