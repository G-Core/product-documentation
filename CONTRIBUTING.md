# Contributing guide for content writers

This guide covers conventions and rules for working in this repository.
It is especially important for articles that use the multi-method tab layout
(Customer Portal / REST API / Terraform / CLI on a single page).

---

## Windows setup (one time)

Run this once after cloning to avoid git errors with long file paths:

```bash
git config --global core.longpaths true
```

This is required because some image paths in the repository exceed the default
260-character limit on Windows. Without this setting, `git checkout` and `git stash`
will fail with "Filename too long" errors.

---

## Tabbed articles: the MethodSwitch component

### What it is

Some articles describe the same scenario using multiple tools: Customer Portal,
REST API, Terraform, and CLI. Instead of maintaining separate pages for each
method, all methods live in one MDX file using a custom `MethodSwitch` component.

The component renders a tab bar at the top of the article. The user picks a method
and sees only that content. The tab choice is remembered across pages via
`localStorage` — if a user switches to REST API on one article, the next article
they open will also show REST API.

### File structure

```
cloud/virtual-instances/create-an-instance.mdx   <- one file, all methods
cloud/networking/create-and-manage-a-network.mdx  <- same pattern
```

There are no longer separate `/cloud/api/`, `/cloud/terraform/`, or `/cloud/cli/`
sibling files for the articles that already have merged versions.

### How to write a tabbed article

**1. Add the import at the top of the file (after frontmatter):**

```mdx
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";
```

**2. Wrap all content inside `<MethodSwitch>`:**

```mdx
<MethodSwitch>
  <MethodSection id="portal" label="Customer Portal">

  [Customer Portal content here]

  </MethodSection>
  <MethodSection id="api" label="REST API">

  [REST API content here]

  </MethodSection>
</MethodSwitch>
```

**Tab IDs and labels:**

| `id`        | `label`           | Status |
|-------------|-------------------|--------|
| `portal`    | `Customer Portal` | Active |
| `api`       | `REST API`        | Active |
| `terraform` | `Terraform`       | Planned |
| `cli`       | `CLI`             | Planned |

Always put `portal` first. The first tab is the default.

Do not add Terraform or CLI tabs until the content exists.

---

## Headings inside tabbed articles

Both sections use standard markdown headings (`##`, `###`). Do not use HTML
`<h2>` tags or custom components — the ToC filtering logic depends on standard
markdown headings.

```mdx
<MethodSection id="portal" label="Customer Portal">

## Step 1. Select a region
...

## Step 2. Configure the image
...

</MethodSection>

<MethodSection id="api" label="REST API">

## Step 1. Add an SSH key
...

## Step 2. Choose an OS image
...

</MethodSection>
```

The "On this page" sidebar (table of contents) is automatically filtered to show
only the headings from the active tab. You do not need to do anything special for
this to work — it is handled by the component automatically.

---

## Critical MDX parsing rule: lists before `</MethodSection>`

**This is the most common cause of broken pages.**

If a section ends with a markdown list, the closing `</MethodSection>` tag
**must not be indented**. The MDX parser treats indented content after a list
as a continuation of the last list item.

**Wrong (breaks the page):**

```mdx
  <MethodSection id="portal" label="Customer Portal">

  - Limitation A
  - Limitation B

  </MethodSection>          <- 2-space indent after a list = MDX parser error
  <MethodSection id="api" label="REST API">
```

**Correct:**

```mdx
  <MethodSection id="portal" label="Customer Portal">

  - Limitation A
  - Limitation B

</MethodSection>            <- no indent = safe
<MethodSection id="api" label="REST API">
```

The rule applies whenever the **last block of content** in a section is a list.
Paragraphs, code blocks, Info/Warning boxes, and images do not have this problem —
only markdown lists (`-` or `1.` style).

---

## Frontmatter requirements

Every tabbed article must have an `ai-navigation` field that describes **all
methods** covered in the article. Do not use `description` — Mintlify renders
that field as visible page text.

```mdx
---
title: Create a Virtual Machine
sidebarTitle: Create an instance
ai-navigation: Create Linux or Windows Virtual Machines in Gcore Cloud via Customer Portal by configuring image, flavor, volumes, network, and firewall, or via REST API using the Instances API.
---
```

Rules for `ai-navigation`:
- One sentence, max 160 characters.
- Start with an action verb: Create, Configure, Manage, Enable, etc.
- Mention both methods if both are present (e.g., "via Customer Portal ... or via REST API").
- No "you", "your", "this article", "learn how to".

---

## Internal links in tabbed articles

All internal links must point to the merged article path, not to any old
`/cloud/api/` path. The `cloud/api/` directory no longer exists.

**Wrong:**
```mdx
See the [VM guide](/cloud/api/virtual-instances/create-an-instance).
```

**Correct:**
```mdx
See the [VM guide](/cloud/virtual-instances/create-an-instance).
```

When adding a link to a specific section of a tabbed article, use the heading
anchor as usual:
```mdx
[SSH key setup](/cloud/virtual-instances/create-an-instance#step-1-add-an-ssh-key)
```

---

## How the ToC filtering works (background)

The "On this page" sidebar in Mintlify is built from all `##` and `###` headings
in the MDX file at compile time. Without filtering, it would show headings from
all tabs simultaneously.

The `MethodSwitch` component solves this with a `useEffect` hook that runs every
time the active tab changes:

1. Find every `h2[id]` and `h3[id]` element on the page.
2. Check `heading.offsetParent === null` — this is `true` for headings inside a
   `display: none` container (i.e., the inactive tab).
3. For each heading, find the ToC `<a href="#heading-id">` link that is outside
   a heading element (i.e., the ToC sidebar link, not the heading's own anchor).
4. Show or hide the `<li>` wrapping that link.

Writers do not need to interact with this code. It works automatically as long as
standard markdown headings are used.

---

## Adding a new tabbed article from scratch

1. Start from an existing tabbed article as a template.
2. Write the Customer Portal section first (it is the default tab).
3. Write the REST API section second.
4. Use `##` headings throughout both sections.
5. Ensure no section ends with a list followed by an indented `</MethodSection>`.
6. Update `ai-navigation` to mention both methods.
7. Check that all internal links use the correct merged-article path.
8. Preview locally with `mintlify dev` before opening a PR.

---

## Adding a new method tab to an existing article

1. Add `<MethodSection id="terraform" label="Terraform">` (or `cli`) after the
   existing sections, inside `<MethodSwitch>`.
2. Write the new method content using `##` headings.
3. Close with `</MethodSection>`.
4. Update `ai-navigation` to mention the new method.
5. No changes to `docs.json` or any other configuration are needed.

---

## Re-merging after a reverted PR

If a PR containing merged articles was merged to main and then reverted (via
`git revert -m 1 <merge-commit-sha>`), re-merging the feature branch later
requires an extra step. Git sees the original commits as "already applied and
then undone" and may not include them again automatically.

**Process when ready to re-merge:**

1. On `main`, revert the revert commit:
   ```bash
   git revert <revert-commit-sha>
   # this creates a commit that re-applies the original changes
   git push origin main
   ```

2. Then open a new PR from the feature branch as normal. It will now merge
   cleanly on top of the re-applied base.

The revert commit to undo is:
```
c639bb25 Revert "Merge pull request #2116 from G-Core/cloud-api-guides"
```

---

## MDX parsing: additional rules

### Validate with the MDX compiler

Before committing any new or heavily edited article, validate it locally:

```powershell
# Install once in any temp dir
cd C:\Temp; npm install @mdx-js/mdx

# Validate an article
node -e "
const {compile}=require('@mdx-js/mdx');
const fs=require('fs');
const c=fs.readFileSync('path/to/article.mdx','utf8');
compile(c).then(()=>console.log('OK')).catch(e=>console.error('ERROR:',e.message));
"
```

The compiler produces an exact error message with line and column number, which is far more useful than the generic "A parsing error occurred" shown in the browser.

### Blank page: missing `.jsx` in the MethodSwitch import

If an article using `MethodSwitch` renders as a completely blank page with no error in the browser or MDX compiler, check the import line first:

**Wrong — causes a blank page at runtime (MDX compiler still says OK):**
```mdx
import { MethodSwitch, MethodSection } from "/snippets/method-switch";
```

**Correct:**
```mdx
import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx";
```

The `.jsx` extension is required. Mintlify resolves the file differently without it and silently produces an empty render. The `@mdx-js/mdx` validator does not catch this — always check the import line when a tabbed article appears empty.

---

### No `{identifier}` inside backtick inline code spans

MDX parses `{identifier}` inside single-backtick spans as JSX expressions. If the identifier is a valid JavaScript name (`task_id`, `project_id`, `LB_VIP`, etc.), the parser throws an error.

**Wrong:**
```
Poll `GET /cloud/v1/tasks/{task_id}` every 5 seconds until `state` is `FINISHED`.
```

**Correct** — use an HTML `<code>` tag with `&nbsp;` for spaces:
```
Poll <code>GET&nbsp;/cloud/v1/tasks/{task_id}</code> every 5 seconds until `state` is `FINISHED`.
```

Content inside triple-backtick fenced code blocks is always safe — `{...}` there is never parsed as JSX.

### No UTF-8 BOM at the start of a file

Files must not start with a UTF-8 BOM (`\xEF\xBB\xBF`). A BOM before `---` breaks the YAML frontmatter parser and produces a generic "parsing error" with no line number.

Check and strip using Python:

```python
data = open('article.mdx', 'rb').read()
if data.startswith(b'\xef\xbb\xbf'):
    open('article.mdx', 'wb').write(data[3:])
```

### Do not use `####` (h4) headings inside `<MethodSection>`

The `MethodSwitch` component hides inactive-tab headings from the TOC by querying `h2[id]` and `h3[id]` elements only. Any `####` (h4) heading inside an inactive `<MethodSection>` is **not hidden** and will appear as a stray entry in the active tab's TOC.

**Wrong:**
```markdown
#### Sharing a pool across multiple listeners
```

**Correct** — use bold text instead of a heading:
```markdown
**Sharing a pool across multiple listeners**
```

---

## What not to do

- Do not create separate files under `cloud/api/`, `cloud/terraform/`, or
  `cloud/cli/` for scenarios that already have a merged article. Add a new
  `<MethodSection>` tab instead.
- Do not use `description` in frontmatter (Mintlify renders it on the page).
  Use `ai-navigation`.
- Do not use HTML `<h2>` or custom heading components inside `MethodSection`.
  Use standard markdown `##` and `###`.
- Do not leave `ApiH2` or `ApiH3` components in files — these were a temporary
  experiment and have been removed.
