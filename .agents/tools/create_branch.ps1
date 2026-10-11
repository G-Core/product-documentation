# create_branch.ps1 - Create a work branch from main.
# Usage: .\.agents\tools\create_branch.ps1 DOC-2405
#        .\.agents\tools\create_branch.ps1 issue/1845-fastedge-log-field
#        .\.agents\tools\create_branch.ps1 feature-draft/DOC-2405
#        Add -DryRun to validate the name without touching git.
#
# Accepted names (exactly one of these formats):
#   DOC-XXXX                    work tied to a Jira ticket: the branch is named exactly as the ticket key
#   issue/{number}-{short-slug} work from a GitHub issue
#   feature-draft/{name}        contributor draft: a ticket key or a short slug
#
# The script checks out main, pulls, and creates the branch.

param(
    [Parameter(Mandatory = $true, Position = 0)]
    [string]$BranchName,

    [switch]$DryRun
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$valid = ($BranchName -cmatch '^DOC-\d+$') `
    -or ($BranchName -cmatch '^issue/\d+-[a-z0-9]+(-[a-z0-9]+)*$') `
    -or ($BranchName -cmatch '^feature-draft/[A-Za-z0-9._-]+$')

if (-not $valid) {
    Write-Error ("Invalid branch name: '$BranchName'. Expected one of: DOC-XXXX (Jira ticket key), " +
        "issue/{number}-{short-slug} (GitHub issue), feature-draft/{name} (contributor draft).")
    exit 1
}

if ($DryRun) {
    Write-Host "OK: '$BranchName' is a valid branch name (dry run, git not touched)."
    exit 0
}

$RepoRoot = Resolve-Path (Join-Path $PSScriptRoot "..\..")

Set-Location $RepoRoot

git show-ref --verify --quiet "refs/heads/$BranchName"
if ($LASTEXITCODE -eq 0) {
    Write-Error "Branch '$BranchName' already exists. Check it out instead of creating it again."
    exit 1
}

Write-Host "Checking out main..."
git checkout main
if ($LASTEXITCODE -ne 0) { Write-Error "git checkout main failed"; exit 1 }

Write-Host "Pulling latest..."
git pull origin main
if ($LASTEXITCODE -ne 0) { Write-Error "git pull failed"; exit 1 }

Write-Host "Creating branch $BranchName..."
git checkout -b $BranchName
if ($LASTEXITCODE -ne 0) { Write-Error "git checkout -b failed"; exit 1 }

Write-Host "Branch '$BranchName' created and checked out."
git branch --show-current
