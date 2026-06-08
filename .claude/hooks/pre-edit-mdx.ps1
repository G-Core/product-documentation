# Runs before every Edit or Write tool call.
# If the file is .mdx, injects procedures.md and mdx-rules.md into context.
# The agent cannot skip these rules — they are physically present before the edit.

$inputJson = [Console]::In.ReadToEnd() | ConvertFrom-Json
$filePath = $inputJson.tool_input.file_path

if ($filePath -notmatch '\.mdx$') { exit 0 }

$refDir = Join-Path $env:CLAUDE_PROJECT_DIR ".agents" "references"
$procedures = Join-Path $refDir "procedures.md"
$mdxRules   = Join-Path $refDir "mdx-rules.md"

Write-Output "=== RULES FOR MDX EDIT: $filePath ==="
Write-Output ""

if (Test-Path $procedures) {
    Write-Output "--- procedures.md ---"
    Get-Content $procedures -Raw
    Write-Output ""
}

if (Test-Path $mdxRules) {
    Write-Output "--- mdx-rules.md ---"
    Get-Content $mdxRules -Raw
    Write-Output ""
}

Write-Output "=== Apply these rules to the edit. ==="

exit 0
