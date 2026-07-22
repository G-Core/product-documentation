# Changelog: About Gcore DDoS protection for dedicated servers

**Article path:** `hosting/other-services/ddos-protection/about-gcore-ddos-protection-for-dedicated-servers.mdx`
**Branch:** `DOC-1830`
**Jira ticket:** [DOC-1830](https://jira.gcore.lu/browse/DOC-1830)
**Regression date:** 2026-07-22
**Agent:** regression-test skill, phases 0, C, 4-10

---

## Summary of changes

### Content fixes (from regression findings)

| # | Location | Article said | Fix applied |
|---|----------|-------------|-------------|
| 1 | title frontmatter | "About GCore DDoS protection..." | Fixed brand name: GCore -> Gcore |
| 2 | top of article | No intro paragraph before first ## | Added opening paragraph |
| 3 | "How it works" section | "You can order advanced (paid) Protection." | Removed second-person; rewrote as "Advanced (paid) Protection is available as an upgrade" |
| 4 | "How always-on protection works" | "your traffic passes through the TMS" | Removed "your" |
| 5 | Comparison table | "You are attacked frequently", "You are hardly ever attacked" | Rewrote as third-person: "Frequent attacks", "Rare attacks" |
| 6 | Billing section | "we will be happy to discuss an individual offer for you" | Removed entire marketing sentence |
| 7 | Billing section (x2) | "tariff" | Replaced with "plan" |
| 8 | Redundant sentence | "Advanced protection uses an always-on mode." | Removed (covered by section heading) |
| 9 | Billing section | "The price of DDoS Protection service depends on three things:" | Replaced with "Advanced Protection is a paid service. The price depends on three factors:" |

### Style guide fixes (Phase 6)

- Renamed ## How it works -> ## Protection modes (forbidden "How" heading)
- Renamed ## How always-on protection works -> ## Always-on protection (forbidden "How" heading)
- Rewrote ai-navigation to start with action verb "Configure" and fit within 160 chars
- Added &nbsp; to [technical support] link text (multi-word link requirement)

### MDX fixes (Phase 7)

- None required (no MethodSwitch, no screenshots, UTF-8 clean)

### LLM quality review (Phase 8)

- Auto-review: 9.45/10
- Improved TMS introduction: "Advanced (paid) Protection uses TMS — Threat Mitigation System — to redirect and clean traffic"
- Added short Billing section lead-in for smoother transition from technical content

---

## Screenshots replaced

None.

## Screenshots removed (orphaned)

None.

---

## Portal verification log

No portal testing required. Concept/overview article with no steps and no screenshots.

---

## SME questions pending

| # | Location | What the article claims | What we observed | Question |
|---|----------|------------------------|-----------------|---------|
| 1 | Comparison table, "How soon it recognizes an attack" row | Always-on detection: 5 seconds | Confluence ([DDoS] Advanced protection, Jun 2026) says "under three seconds" | Is the correct maximum detection time 5 seconds or 3 seconds? |

---

## Issues noted but not fixed (out of scope)

- Billing section lists all specific bandwidth options (1 Mbps through 10 Gbps) — LLM flagged as potentially verbose for an overview; left as-is since the list is factually correct and helps customers assess costs.

---

## Lessons learned

- Concept articles need an intro paragraph before the first ## heading per content-types.md rules.
- The `regression-test/SKILL.md` file was corrupted with credentials (local uncommitted change). Restored with `git restore` — file was intact in git history.
