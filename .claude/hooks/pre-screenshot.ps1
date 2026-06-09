# Runs before any Playwright screenshot tool call.
# Injects screenshot standards so the agent follows them before capturing.

$inputJson = [Console]::In.ReadToEnd() | ConvertFrom-Json
$toolName  = $inputJson.tool_name

if ($toolName -notmatch 'screenshot') { exit 0 }

$playwrightFile = Join-Path $env:CLAUDE_PROJECT_DIR ".agents" "references" "mcp-tools" "playwright.md"

if (Test-Path $playwrightFile) {
    Write-Output "=== SCREENSHOT STANDARDS ==="
    Write-Output ""
    Get-Content $playwrightFile -Raw
    Write-Output ""
    Write-Output "=== Follow these standards before taking the screenshot. ==="
}

exit 0
