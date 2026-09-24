# create_branch.ps1 — Create a feature branch from a Jira ticket key.
# Usage: .\.agents\tools\create_branch.ps1 DOC-2405
#
# Validates the ticket key format, checks out main, pulls, and creates the branch.
# Branch name = ticket key exactly. No suffixes, no slugs, no descriptions.

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$TicketKey
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Validate format: uppercase DOC-XXXX
if ($TicketKey -notmatch '^DOC-\d+$') {
    Write-Error "Invalid ticket key: '$TicketKey'. Expected format: DOC-XXXX (e.g. DOC-2405)"
    exit 1
}

$RepoRoot = "C:\Gcore_projects\product-documentation"

Set-Location $RepoRoot

Write-Host "Checking out main..."
git checkout main
if ($LASTEXITCODE -ne 0) { Write-Error "git checkout main failed"; exit 1 }

Write-Host "Pulling latest..."
git pull origin main
if ($LASTEXITCODE -ne 0) { Write-Error "git pull failed"; exit 1 }

Write-Host "Creating branch $TicketKey..."
git checkout -b $TicketKey
if ($LASTEXITCODE -ne 0) { Write-Error "git checkout -b failed"; exit 1 }

Write-Host "Branch '$TicketKey' created and checked out."
git branch --show-current
