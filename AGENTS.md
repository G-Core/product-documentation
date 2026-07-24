# AGENTS.md — Gcore Product Documentation

This file is loaded automatically. Read it fully, then stop and wait for a task.
Do not explore the repository until you have a task and have loaded the matching skill.

## ABSOLUTE RULES — NO EXCEPTIONS

- **ONE article per session.** Stop after completing one article. Wait for explicit approval before starting the next.
- **NEVER commit** unless the user explicitly says to commit.
- **NEVER push** unless the user explicitly says to push.
- **NEVER create a PR** unless the user explicitly says to create a PR.
- **NEVER do any git write operation** without explicit instruction.

## How to handle any task

The user may write in any language. Follow these steps every time:

1. **Translate** the user's request to English internally (no external call needed — you speak all languages).
2. **Match** the translated request against the Task → Skill table below.
3. **Use the Read tool** to open the matching skill file. This is your first tool call — before writing any response, before asking any question.
4. **Follow the skill file exactly.** It overrides everything else.

## What this repo is

Mintlify documentation site for Gcore cloud products. Content is MDX files in
product folders. Articles that cover multiple tools (Customer Portal, REST API,
Terraform, CLI) live as a single MDX file using the `MethodSwitch` component —
not as separate files. OpenAPI specs for all products are in the repo and used
as the source of truth for API documentation.

## Folder structure

```
/{product}/{section}/article.mdx       Main content (cloud, cdn, dns, waap, …)
/{product}.mdx                         Product landing/navigation page
/api-reference/services_documented/    OpenAPI YAML specs, one per product
/snippets/                             Shared JSX and MDX components
/.agents/skills/                       Skills — load on demand, one per task
/.agents/references/                   Reference files — load only when a skill says to
```

## Three rules that apply to every task

**1. Never create separate files for Portal / API / Terraform.**
All methods for the same feature live in one `.mdx` file using `MethodSwitch`.
If you are adding API coverage to an existing Portal article, add a tab — do
not create a new file.

**2. Never use `description` in frontmatter.**
Mintlify renders `description` as visible page text. Use `ai-navigation` instead.
`ai-navigation` is one sentence, max 160 characters, starts with an action verb,
mentions all methods covered.

`ai-navigation` is not just a label — it is read by a GitHub Action that generates
`llms.txt` files for every product. These files are how AI agents (including Claude)
discover what documentation exists. A missing or broken `ai-navigation` means the
article is invisible to AI-powered search and navigation tools.

Forbidden characters in `ai-navigation`: `:` (colon) and `#` (hash). The CI
workflow auto-replaces them with ` -`, but the result may look wrong. Avoid them.

**3. Internal links are always root-relative.**
Use `/cloud/virtual-instances/create-an-instance`, never a full
`https://docs.gcore.com/…` URL and never a relative `../` path.

## Available MCP tools

These are configured in this environment. Skills that need them will say so.

| MCP | Purpose |
|-----|---------|
| Jira | Fetch tickets, acceptance criteria, linked issues |
| Confluence | Internal product specs, release notes |
| Playwright | Browser testing at https://portal.gcore.com |

**Before using any MCP tool:** verify it is available. If not — read
`.agents/references/mcp-tools/setup.md` and give the user the exact setup
instructions from that file. Do not attempt to work around a missing tool.

## Task → Skill

Identify the task from the user's request. Load exactly one skill file.
Read nothing else until the skill tells you to.

| Task | Load this skill |
|------|----------------|
| Product or UI changed — find affected articles and update them | `.agents/skills/update-page/SKILL.md` |
| Write a new article from scratch | `.agents/skills/write-from-scratch/SKILL.md` |
| Analyze a Jira ticket — what needs documenting | `.agents/skills/jira-context/SKILL.md` |
| Add REST API tab to an existing Portal article | `.agents/skills/api-use-case/SKILL.md` |
| Test an article step by step and fix it | `.agents/skills/regression-test/SKILL.md` |
| Product team: new feature → draft PR | `.agents/skills/feature-draft/SKILL.md` |
| Compile a multi-topic end-to-end guide | `.agents/skills/cookbook/SKILL.md` |
| Create a PR after work is done | `.agents/skills/pr/SKILL.md` |

## Common mistakes

These errors are specific to this repository. They cause silent failures or broken
builds that are hard to debug. Know them before touching any file.

**1. MethodSwitch import missing `.jsx` — blank page, no error**
```mdx
Wrong:  import { MethodSwitch, MethodSection } from "/snippets/method-switch"
Correct: import { MethodSwitch, MethodSection } from "/snippets/method-switch.jsx"
```
The MDX compiler reports OK. The blank page appears only in the Mintlify runtime.

**2. `description` in frontmatter — renders as visible page text**
```yaml
Wrong:  description: How to create a VM   ← appears on the page
Correct: ai-navigation: Create a VM ...   ← invisible to users, read by AI
```

**3. `{identifier}` in inline backtick code spans — MDX parse error**
```mdx
Wrong:  Poll `GET /tasks/{task_id}` every 5 seconds.
Correct: Poll <code>GET&nbsp;/tasks/{task_id}</code> every 5 seconds.
```
Safe inside triple-backtick fenced blocks. Only breaks in single-backtick inline spans.

**4. `</MethodSection>` indented after a list — tag becomes invisible to parser**
```mdx
Wrong:
- Last item.

  </MethodSection>   ← indented = MDX treats as list continuation

Correct:
- Last item.

</MethodSection>     ← column 0
```

**5. Prose not wrapped in `<p>` inside `<MethodSection>` — content merges into one block**
```mdx
Wrong:  <MethodSection>Some intro text. Then a step.</MethodSection>
Correct: <MethodSection><p>Some intro text.</p>1. Then a step.</MethodSection>
```
Plain paragraphs inside `<MethodSection>` compile to text strings — blank lines are stripped.

**6. `####` heading inside `<MethodSection>` — appears in the wrong tab's TOC**
```mdx
Wrong:  #### Subsection title   ← leaks into active tab's TOC
Correct: **Subsection title**   ← bold text, no TOC entry
```

**7. `ai-navigation` with `{...}`, `/paths/`, `:` or `#` — breaks build**
```yaml
Wrong:  ai-navigation: Poll GET /tasks/{task_id} until state: FINISHED
Wrong:  ai-navigation: See #overview for details
Correct: ai-navigation: Create and manage virtual machines via the Gcore Cloud API.
```
Allowed: commas, periods, hyphens, parentheses. Forbidden: `{` `}` `/` `:` `#`.

**8. Image file without extension — does not display in browser**
```mdx
Wrong:  ![Alt text](/images/docs/cloud/create-vm/step-3)
Correct: ![Alt text](/images/docs/cloud/create-vm/step-3.png)
```
Always verify the file exists at the path before referencing it.

**9. `git add .` or `git add -A` — stages unrelated files from other sessions**
Always stage files by name: `git add cloud/virtual-instances/create-an-instance.mdx`

**10. Branching from stale local main — silently includes other branches' commits**
```powershell
Always run before branching:
git checkout main
git pull origin main   ← required, not optional
git checkout -b update-{product}-{slug}
```

**11. Writing content without reading the full product section first — creates duplicate content**
Before writing or expanding any article, read ALL sibling articles in the same product
folder and check `docs.json` to understand the nav group structure. Only then can you
determine what belongs in the target article and what is already covered elsewhere.

Skipping this step causes content to be written that duplicates existing articles,
regardless of how correct or accurate that content is.

---

## CI workflows — what runs automatically

Two GitHub Actions run automatically when you push a branch or open a PR.
Know about them to avoid confusion.

**`sanitize-ai-navigation`** — runs on every push to non-main branches:
Scans all `.mdx` files and replaces `:` and `#` in `ai-navigation` values with ` -`.
Auto-commits the fix directly to your branch. If this happens, run `git pull`
before any follow-up commits to avoid conflicts.

**`normalize-images`** — runs on every PR when images or MDX files change:
Renames images to `{article-slug}-imageN.ext` and updates the paths in MDX files.
Also regenerates `llms.txt` files. Auto-commits everything to your branch.
Same rule: run `git pull` before follow-up commits.

**Image naming convention** (the action enforces this, but follow it from the start):
```
images/docs/{product}/{article-slug}/{article-slug}-image1.png
images/docs/{product}/{article-slug}/{article-slug}-image2.png
```

---

**12. "permanent" API token — incorrect product terminology**
```
Wrong: A permanent API token is required.
Wrong: a permanent [API token]
Correct: An [API token](/account-settings/api-tokens) is required.
```
API keys have optional expiration set by the user. "Permanent" is not accurate — never use this word when describing API tokens.

---

## Hard stop

Load one skill per task. Do not read other skill files. Do not read articles to
"understand context." Do not read references unless the skill explicitly says to.
When in doubt about what to do next, ask the user — do not explore.
