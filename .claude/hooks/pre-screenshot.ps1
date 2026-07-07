# Runs before any Playwright screenshot tool call.
# Must return valid JSON for Cursor hooks.

[Console]::In.ReadToEnd() | Out-Null
Write-Output '{"permission": "allow"}'
exit 0
