---
product: FastEdge
status: Include
release_date: 2026-10-14
published_page: null
---

# FastEdge one-prompt agent setup

Customer change: The FastEdge dashboard has an onboarding card. Copy prompt copies one prompt for every agent. The agent installs the plugin and returns a Customer Portal link for account approval. An API token is not required for that path. If GCORE_API_KEY is set, it takes priority.
Affected users: Customers who set up Claude Code, Codex, Cursor, or another MCP agent for FastEdge
Release evidence: On 2026-10-14 the production FastEdge dashboard showed the onboarding card. Copy prompt on Claude Code, Codex, Cursor, Other agents, and VS Code copied the same prompt, which fetches https://portal.gcore.com/external-statics/fast-edge/agent-connect-prompt.md. That file returned the install and sign-in instructions. The approval page was not opened in this session.
Open verification: none for the prompt. The approval page itself was not clicked.
Source tickets/PRs: DOC-2653
Documentation links: fastedge/local-development/ai-assisted-development.mdx, fastedge/local-development/configure-plugin-and-mcp-server.mdx, fastedge/local-development/ai-skills-reference.mdx
Duplicate check: not found
Published entry: null
