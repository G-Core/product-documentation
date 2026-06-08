# Injected before any Playwright screenshot tool call.
# Forces screenshot standards into context.

$input = [Console]::In.ReadToEnd() | ConvertFrom-Json
$toolName = $input.tool_name

# Only trigger for Playwright screenshot
if ($toolName -notmatch 'screenshot|browser_screenshot') { exit 0 }

$playwrightFile = Join-Path $env:CLAUDE_PROJECT_DIR ".agents" "references" "mcp-tools" "playwright.md"

if (Test-Path $playwrightFile) {
    Write-Output "=== SCREENSHOT STANDARDS — follow before capturing ==="
    Write-Output ""
    Get-Content $playwrightFile -Raw
    Write-Output ""
    Write-Output "=== Apply these standards to the screenshot you are about to take. ==="
}

exit 0
