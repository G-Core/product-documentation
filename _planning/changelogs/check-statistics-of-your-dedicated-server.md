# Changelog: Check statistics of your dedicated server

**Article path:** `hosting/dedicated-servers/check-statistics-of-your-dedicated-server.mdx`
**Branch:** `DOC-1821`
**Jira ticket:** [DOC-1821](https://jira.gcore.lu/browse/DOC-1821)
**Regression date:** 2026-07-20
**Agent:** regression-test skill, phases 0-10

---

## Summary of changes

### Content fixes (from regression findings)

| # | Location | Article said | Portal shows | Fix applied |
|---|----------|-------------|--------------|-------------|
| 1 | Step 1, ai-navigation | "In the DCI Manager panel, go to the 'Statistics' section and click on the 'Traffic' tab." | New DCImanager has no Statistics section (sidebar: Servers, Templates only). Statistics is in Control Panel toolbar. | Updated navigation to Control Panel > Dedicated servers > Statistics toolbar button |
| 2 | Section heading 1, ai-navigation | "incoming and outcoming traffic" | "outcoming" is not standard English | Replaced all instances with "outgoing" |
| 3 | Step 1 | "DCI Manager panel" | Product is styled "DCImanager" (one word) | Fixed to "DCImanager" (removed in final rewrite as navigation changed) |
| 4 | Steps, headings | UI labels in "quotes" ("Statistics", "Traffic", "Common Traffic") | Style guide requires bold for UI element names | Converted all quoted UI names to **bold** |

### Style guide fixes (Phase 6)

- Added numbered steps for the two sequential actions in section 1 (procedures.md violation)
- Rewrote intro paragraph to describe what the feature provides (was missing)
- Intro sentence added to section 2 (was previously heading → prose with redundancy)
- Removed "you want" phrasing from step text

### MDX fixes (Phase 7)

- None required; article has no MethodSwitch, no raw HTML

---

## Screenshots replaced

| Old filename | New filename | Notes |
|-------------|--------------|-------|
| (none replaced) | — | Statistics feature blocked by "Insufficient privileges to perform 'service.stat'" on test account. Both screenshots show 2017-era ISPsystem UI and need retaking. Tracked in DOC-1821. |

## Screenshots removed (orphaned)

- None

---

## Portal verification log

| # | Element tested | Article says | Portal confirmed | Status |
|---|---------------|--------------|-----------------|--------|
| 1 | DCImanager sidebar navigation | Statistics section exists | No Statistics section in new DCImanager (only Servers, Templates) | FINDING 1 |
| 2 | Control Panel Statistics button | N/A (was DCImanager) | Statistics button exists in toolbar | Confirmed button exists |
| 3 | Statistics feature access | Shows traffic chart | "Insufficient privileges to perform 'service.stat'" error | FINDING 2 |
| 4 | Screenshot image1 | Traffic Statistics page (2017 ISPsystem UI) | Cannot verify — feature inaccessible | FINDING 3 |
| 5 | Screenshot image2 | Common Traffic section (2017 ISPsystem UI) | Cannot verify — feature inaccessible | FINDING 4 |

---

## Issues noted but not fixed (out of scope)

- Both screenshots show 2017-era ISPsystem UI and must be retaken once an account with Statistics access is available. The test account (`sergey.kostichev@gcore.com`) returns "Insufficient privileges to perform 'service.stat'" when clicking Statistics.
- The "Traffic" tab name and "Common Traffic" section name could not be verified against the current UI.

---

## Lessons learned (skill improvements made)

- The hosting Control Panel (`hosting.gcore.com/billmgr`) Statistics toolbar button is separate from DCImanager. Old articles may incorrectly point to DCImanager for features that actually live in the Control Panel.
- DCImanager session management: navigating away from the initial page (via `browser_navigate` or `window.location.href`) kills the SPA session. Client-side navigation via React Router or link clicks is needed but can also trigger session loss.
