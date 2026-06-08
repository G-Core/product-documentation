# Blocks any direct push to main or production branch.
# Changes must go through a pull request.

$input = [Console]::In.ReadToEnd() | ConvertFrom-Json
$command = $input.tool_input.command

if ($command -match 'git push.*\bmain\b' -or $command -match 'git push.*\bproduction\b' -or $command -match 'git push origin main' -or $command -match 'git push origin production') {
    Write-Error "BLOCKED: Direct push to main/production is not allowed. Create a branch and open a PR instead." -ErrorAction Continue
    exit 2
}

exit 0
