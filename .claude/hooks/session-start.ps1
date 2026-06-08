# Injected at session start — makes skill descriptions available in context.
# Agent sees what skills exist and when to use them.

$agentsFile = Join-Path $env:CLAUDE_PROJECT_DIR "AGENTS.md"

if (Test-Path $agentsFile) {
    Get-Content $agentsFile -Raw
}
