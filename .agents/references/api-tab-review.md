# API tab review checklist

Used by the `api-use-case` and `api-audit` skills before showing the result.

## Standalone tab test (run this first)

Each tab must work as a complete standalone article. The user reads only one tab — never both.

**Mentally delete the Portal tab. Can the API tab reader:**

1. Understand what this feature/resource is and why they would manage it?
2. Find the right resource, ID, or identifier without switching tabs?
3. Understand the consequence of each action (what enabling/disabling/creating/deleting does)?
4. Complete the full task end-to-end?

If any answer is **no** — the API tab is incomplete. Fix before proceeding.

**Common failures:**
- Feature description exists only in the Portal tab intro → add a one-sentence context to the API tab opener
- Reference table (IDs, names, states) exists only in the Portal tab → add a compact version to the API tab (accordion is fine)
- Policy/resource descriptions exist only in the Portal tab → add a Purpose column to the API reference table
- Portal tab explains "what each option does", API tab only shows the call → API tab user can't make an informed decision

**The goal is not two complementary tabs — it is two independent implementations of the same task.**

---

## Checks

**Structure:**
Search the article with the Grep tool for each pattern (regex, line anchors):
```
^## (What|How|Why|When) 
^## (Next steps|Prerequisites|Requirements|See also)
^(This guide covers|This article|In this |The steps below)
```
Scan every `##` and `###` — verify a prose sentence follows before any code block or table.

**Formatting:**
- Bold only for UI elements — not for emphasis
- Em-dashes spaced: ` — ` not `—`
- Response JSON and "The API returns" live inside the matching method tab — never after `</Tabs>`
- Quickstart scripts have no combined step labels (`# Step 3+4`)
- Flavor and image IDs not hardcoded — selected dynamically

**API style checker (mandatory — run after the article is written, before showing the result):**

```powershell
python .agents/tools/api_check_style.py {relative/path/to/article.mdx}
python .agents/tools/api_check_style.py --all
```

Exit code 0 required. Fix every violation, then re-run. `--all` scans the repo and ignores OS tabs and language-variant curl groups. When a new repeatable API-tab mistake shows up, add a check function to `.agents/tools/api_check_style.py` and a unit test in `.agents/tools/test_api_check_style.py` — do not rely on memory.

**Links:**
- Link text 1–2 words maximum
- Each URL linked only once — subsequent mentions plain text
- No standalone "For more details, see..." sentences

**Voice:**
- No "you" or "your" in prose
- No forbidden words: just, simply, obviously, ensure, platform
- Never describe what is absent: do not write that SDK support is "pending", "not yet available", or "not supported". Document only what exists. If only curl is available, show only curl — no explanation needed.

**MDX:**
- Import has `.jsx` extension
- `<MethodSwitch>` wraps both sections
- Closing `</MethodSection>` tags at column 0 after lists
- No `{identifier}` in inline backtick spans
