---
product: Developer Tools
status: Needs verification
release_date: unknown
published_page: null
---

# Gcore MCP Server dynamic mode

Customer change: The MCP server exposes six tools by default and reaches every operation through them. Named toolsets are gone. Destructive calls stop until approved. Read-only mode and an HTTP session on /mcp are available.
Affected users: Customers who connect an AI client to Gcore MCP Server
Release evidence: Observed on a local checkout of gcore-mcp-server branch feat/mcp-v2 at de24f2a, not on a released package. A cloud instance list against the account API succeeded through that server.
Open verification: Confirm the reviewed build is what customers install, and connect Cursor, Claude Code, Codex, and OpenCode to that build.
Source tickets/PRs: DOC-2897
Documentation links: developer-tools/mcp-server/gcore-mcp-server-overview.mdx, developer-tools/mcp-server/filter-tools-with-gcore-tools.mdx, developer-tools/mcp-server/install-and-configure-gcore-mcp-server.mdx
Duplicate check: not found
Published entry: null
