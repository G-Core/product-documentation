# Runs at session start. Injects AGENTS.md into context so the agent
# always knows what skills are available before any task.

$agentsFile = Join-Path $env:CLAUDE_PROJECT_DIR "AGENTS.md"

if (Test-Path $agentsFile) {
    Get-Content $agentsFile -Raw
}
