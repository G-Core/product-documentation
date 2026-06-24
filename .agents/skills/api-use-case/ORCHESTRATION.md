# WAAP API Tab — Orchestration Checklist

Execute every phase in order. Read each file only when its phase arrives.

---

## Phase 0 — Load the skill

Read: `.agents/skills/api-use-case/SKILL.md`

---

## Phase 1 — Read the article

Read the target article in full.

Determine: Structure A (sequential) or Structure B (independent)?

---

## Phase 2 — Live API testing

Always test against the live API. Do not ask the user. Do not use spec-only mode.
Run every operation end-to-end via curl/Python SDK/Go SDK before writing the section.

---

## Phase 3 — Find endpoints in the spec

Read: `api-reference/services_documented/waap_api.yaml` (relevant sections only)

---

## Phase 4 — Write the API section

Read before writing:
- `.agents/references/mdx-rules.md`
- `.agents/references/style-guide.md`

Then write the `<MethodSection id="api">` content.

---

## Phase 5 — Validate MDX

```powershell
cd C:\Temp
node -e "const {compile}=require('@mdx-js/mdx');const fs=require('fs');const c=fs.readFileSync('PATH','utf8');compile(c).then(()=>console.log('OK')).catch(e=>console.error('ERROR:',e.message));"
```

Fix any error before proceeding.

---

## Phase 6 — Show result and WAIT for approval

Show the user a summary of what was written:
- Article path
- API structure (A or B)
- Operations covered (list of endpoints)
- Any gotchas discovered during live testing

**CRITICAL: STOP HERE. NEVER commit or push without explicit user command.**
**Do NOT proceed to Phase 7 automatically after MDX validation.**
**Do NOT proceed to Phase 7 even if the article looks perfect.**
**Wait for the user to say exactly: "коммить", "пушь", "commit", "push", or equivalent.**
**Proceeding without this command is a hard violation of workspace rules.**

---

## Phase 7 — Commit and push (only after explicit user command)

```powershell
cd C:\Projects\product-documentation
git add <file>
git commit -m "feat(waap): add API tab to <article> (article N)"
git push origin waap-api-guides
```

If rejected: `git pull --rebase origin waap-api-guides && git push origin waap-api-guides`

---

## Phase 8 — Jira ticket

```powershell
cd C:\Projects\docops-agent2
.\venv\Scripts\python.exe scripts\create_jira_ticket.py `
  --summary "Add API tab: <title>" `
  --description "<operations covered>"
```

---

## Phase 9 — Update status file

Update `.agents/WAAP-API-TABS-STATUS.md`: set all columns to `OK`, add comment with endpoints and commit hash.
