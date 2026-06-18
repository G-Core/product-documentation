# MCP Tools — Setup Check

Read this file at the start of any task that requires Jira, Confluence, or Playwright.

Before using an MCP tool, verify it is available by attempting a minimal call.
If a tool is unavailable, stop the task and give the user the exact setup instructions below.
Do not proceed without the required tool — do not work around it or skip portal verification.

---

## Playwright

### How to check
Attempt to call `mcp__playwright__browser_navigate`. If the tool is not found — tell the user:

---

> **Playwright MCP is not configured for this project.**
>
> To fix this, create a file called `.mcp.json` in the root of the
> `product-documentation` folder with this content:
>
> ```json
> {
>   "mcpServers": {
>     "Playwright": {
>       "command": "npx",
>       "args": ["@playwright/mcp@latest"],
>       "env": {}
>     }
>   }
> }
> ```
>
> **Requirements:**
> - Node.js must be installed. Check: open a terminal and run `node --version`.
>   If not installed, download from https://nodejs.org (LTS version).
>
> **After creating the file:** restart Claude Desktop, then try again.

---

## Confluence

### How to check
Attempt to call `mcp__confluence__search` or `mcp__confluence__get_page`.
If the tool is not found — tell the user:

---

> **Confluence MCP is not configured.**
>
> To fix this, you need:
>
> **Step 1 — Get a personal access token:**
> 1. Go to https://wiki.gcore.lu
> 2. Click your profile avatar → **Profile**
> 3. Navigate to **Personal Access Tokens**
> 4. Click **Create token**, give it a name, set expiry
> 5. Copy the token — it is shown only once
>
> **Step 2 — Add to Claude Desktop config:**
>
> Open `%APPDATA%\Claude\claude_desktop_config.json` and add inside `"mcpServers"`:
>
> ```json
> "confluence": {
>   "command": "node",
>   "args": ["C:/Projects/anton-wiki/wiki/dist/server.js"],
>   "env": {
>     "CONFLUENCE_URL": "http://wiki.gcore.lu",
>     "CONFLUENCE_PERSONAL_TOKEN": "<paste your token here>"
>   }
> }
> ```
>
> **Note:** The server file must exist at `C:/Projects/anton-wiki/wiki/dist/server.js`.
> If it is missing, ask your team for the `anton-wiki` project and run `npm install` inside it.
>
> **After editing the file:** restart Claude Desktop, then try again.

---

## Jira

### How to check
Attempt to call `mcp__jira__get_issue` with any ticket ID (e.g. `DOC-1`).
If the tool is not found — tell the user:

---

> **Jira MCP is not configured.**
>
> To fix this, you need:
>
> **Step 1 — Install the Jira MCP server:**
>
> Open a terminal and run:
> ```powershell
> pip install jira-mcp-server
> ```
> If `pip` is not available, install Python first: https://www.python.org/downloads/
>
> **Step 2 — Get a personal access token:**
> 1. Go to https://jira.gcore.lu
> 2. Click your profile avatar (top right) → **Profile**
> 3. Navigate to **Personal Access Tokens**
> 4. Click **Create token**, give it a name
> 5. Copy the token — it is shown only once
>
> **Step 3 — Add to Claude Desktop config:**
>
> Open `%APPDATA%\Claude\claude_desktop_config.json` and add inside `"mcpServers"`:
>
> ```json
> "jira": {
>   "command": "python",
>   "args": ["-c", "from jira_mcp_server.server import main; main()"],
>   "env": {
>     "JIRA_MCP_URL": "https://jira.gcore.lu",
>     "JIRA_MCP_TOKEN": "<paste your token here>",
>     "JIRA_MCP_VERIFY_SSL": "false"
>   }
> }
> ```
>
> **After editing the file:** restart Claude Desktop, then try again.

---

## Where is `claude_desktop_config.json`?

On Windows, the file is at:
```
C:\Users\<your-username>\AppData\Roaming\Claude\claude_desktop_config.json
```

Quick way to open it: press `Win + R`, paste this, press Enter:
```
%APPDATA%\Claude\claude_desktop_config.json
```

The file must be valid JSON. If Claude Desktop fails to start after editing,
check for missing commas or extra brackets using https://jsonlint.com

---

## After any setup change

Always restart Claude Code after editing `claude_desktop_config.json` or `.mcp.json`.
Changes do not take effect until restart.

## Critical: MCP tools must be connected before starting a session

MCP tool schemas are loaded once at the start of a conversation.
If a tool connects mid-session, its tools are **not available** in the current conversation.

**If a tool shows "Failed to connect" at session start:**
1. Exit the session
2. Fix the connection issue (install browsers, check PATH, restart)
3. Verify with `claude mcp list` — all required tools show ✓ Connected
4. Start a new session

**For Playwright specifically:** run `npx playwright install` once to install browsers
before starting any session that requires portal testing.

---

## Mintlify local preview

Not an MCP tool — a CLI for previewing the documentation site locally before pushing.

### Check if installed

```powershell
mintlify --version
```

### Install if missing

Requires Node.js (https://nodejs.org, LTS version):

```powershell
npm i -g mintlify
```

### Run

From the repository root (`C:\Projects\product-documentation`):

```powershell
mintlify dev
```

Port is chosen automatically (default 3000, increments if taken).
Run in a separate terminal window — does not need to be running for other tasks.
The URL appears in that terminal once ready.
