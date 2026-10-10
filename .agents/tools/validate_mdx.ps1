# validate_mdx.ps1 - Compile an MDX article with @mdx-js/mdx and print OK or the exact error.
# Usage (from the repository root): .\.agents\tools\validate_mdx.ps1 path\to\article.mdx
#
# The compiler is installed once into $env:TEMP\mdx-check, outside the repository.
# It does NOT catch a missing .jsx extension in the MethodSwitch import.

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$Path
)

$ErrorActionPreference = "Stop"

$article = (Resolve-Path $Path).Path
$checkDir = Join-Path $env:TEMP "mdx-check"
$installed = Join-Path $checkDir "node_modules\@mdx-js\mdx"

if (-not (Test-Path $installed)) {
    Write-Host "Installing @mdx-js/mdx into $checkDir (one time)..."
    New-Item -ItemType Directory -Force $checkDir | Out-Null
    Push-Location $checkDir
    try {
        if (-not (Test-Path "package.json")) { npm init -y --silent | Out-Null }
        npm install --silent --no-audit --no-fund "@mdx-js/mdx"
        if ($LASTEXITCODE -ne 0) { throw "npm install failed" }
    } finally {
        Pop-Location
    }
}

Copy-Item (Join-Path $PSScriptRoot "validate_mdx.mjs") (Join-Path $checkDir "validate_mdx.mjs") -Force
node (Join-Path $checkDir "validate_mdx.mjs") $article
exit $LASTEXITCODE
