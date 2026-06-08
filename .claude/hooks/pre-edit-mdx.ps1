# Injected before editing any .mdx file.
# Forces procedures and MDX rules into context — agent cannot skip them.

$input = [Console]::In.ReadToEnd() | ConvertFrom-Json
$filePath = $input.tool_input.file_path

# Only trigger for .mdx files
if ($filePath -notmatch '\.mdx$') { exit 0 }

$refDir = Join-Path $env:CLAUDE_PROJECT_DIR ".agents" "references"

$procedures = Join-Path $refDir "procedures.md"
$mdxRules   = Join-Path $refDir "mdx-rules.md"

Write-Output "=== RULES LOADED FOR MDX EDIT: $filePath ==="
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

Write-Output "=== Follow these rules exactly when editing the file above. ==="

exit 0
