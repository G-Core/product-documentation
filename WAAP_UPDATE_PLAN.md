# WAAP Documentation Urgent Update Plan

**Created**: 2026-02-12  
**Status**: In Progress  
**Priority**: HIGH (Orange customer escalation)  
**Branch**: `waap-urgent-updates` (from `main`)

---

## Overview

Orange reports that the current WAAP documentation does not match the new customer portal UI.
This plan covers systematic review and update of all 45 WAAP articles.

**Estimated effort**: 23-47 hours  
**Total articles**: 45  
**Total screenshots**: 151  

---

## Workflow

### Git Branching Strategy

```
main
  |
  +-- waap-urgent-updates (main working branch)
        |
        +-- waap/overview
        +-- waap/getting-started/configure-waap-for-a-domain
        +-- waap/analytics
        +-- ... (one branch per article)
```

### Per-Article Process

1. **Create branch** from `waap-urgent-updates`: `waap/<article-path>`
2. **Follow article as instruction** in the portal using Playwright MCP
3. **Compare UI** with documentation screenshots and text
4. **Apply proofreading checklist** (typos, numbering, broken links)
5. **Update screenshots** where UI has changed
6. **Note new/deprecated features** not covered in docs
7. **Write change summary** in commit message
8. **Push branch** and create PR to `waap-urgent-updates`

---

## Proofreading Checklist (per article)

- [ ] Typos and grammar errors
- [ ] Step numbering is correct and sequential
- [ ] All internal links work (no 404s)
- [ ] All external links work
- [ ] Image alt text is present and accurate
- [ ] UI element names match current portal
- [ ] Button/menu labels are exact matches
- [ ] Screenshots reflect current UI
- [ ] Code snippets are valid and tested
- [ ] Metadata (title, description) is accurate

---

## Tools and Resources

### Portal Access

- **URL**: https://auth.gcore.com/login/signin
- **Account**: mycompanytest
- **Credentials**: See `C:\Projects\product-documentation-test2\_private\portal-acces.txt`

### Automation

- **Playwright MCP**: Browser automation for portal verification and screenshot capture
- **Browser viewport**: 1920x1080 (required for proper screenshots)

### Documentation Guidelines

| Guide | Path | Purpose |
|-------|------|---------|
| Unified Style Guide | `_private/guides/unified-style-guide.md` | Writing standards, voice, formatting |
| Screenshot Guidelines | `_private/guides/screenshot-guidelines.md` | Capturing and placing screenshots |
| Proofreading Checklist | `_private/guides/proofreading-checklist.md` | Final review before PR |

---

## Scope of Changes

**MINIMAL CHANGES ONLY:**

- UI element names (buttons, labels, menu items) must match current portal
- Screenshots replaced where UI has changed
- Typos, numbering errors, broken links fixed
- New functionality documented if discovered
- Deprecated functionality marked or removed

**DO NOT:**

- Rewrite entire articles
- Change article structure unless necessary
- Add new sections unless UI has new features

---

## Per-Article Review Checklist

Before marking an article complete, verify:

### UI Comparison
- [ ] All button names match current portal
- [ ] All menu/tab names match current portal
- [ ] All field labels match current portal
- [ ] Navigation paths are accurate
- [ ] Page/dialog titles are accurate

### Screenshots
- [ ] Each screenshot reflects current UI
- [ ] No sensitive data visible (balance, API keys, emails)
- [ ] Context is visible (not just isolated elements)
- [ ] Screenshots placed after instructions, not before
- [ ] Alt text is descriptive

### Proofreading (from checklist)
- [ ] Em dashes used correctly (not -- or ---)
- [ ] Comma before "but" in compound sentences
- [ ] Oxford comma in lists of 3+ items
- [ ] Articles before noun phrases (a, an, the)
- [ ] No "current" without "the"
- [ ] Warnings for deletions/irreversible actions
- [ ] Info blocks for limitations/conditions
- [ ] No consecutive lists without text between
- [ ] Step numbering is sequential
- [ ] All internal links work

### New/Deprecated Features
- [ ] New UI elements documented
- [ ] Removed features noted or content deleted
- [ ] Changed workflows updated

---

## Article List

### Getting Started (4 articles)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 1 | `waap/overview.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed - general overview |
| 2 | `waap/getting-started/configure-waap-for-a-domain.mdx` | 16 | [x] DONE | waap-urgent-updates | Full revision |
| 3 | `waap/billing.mdx` | 0 | [x] DONE | waap-urgent-updates | Fixed broken link, replaced "Common automated services" with "Known Bots" |
| 4 | `waap/getting-started/waap-modes.mdx` | 3 | [x] DONE | waap-urgent-updates | Fixed alt text Analytics->Events |
| 5 | `waap/getting-started/manage-domains.mdx` | 3 | [x] DONE | waap-urgent-updates | Fixed spacing before colons, grammar error |

### Analytics (1 article)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 6 | `waap/analytics.mdx` | 21 | [x] DONE | waap-urgent-updates | Full revision: terminology, navigation, screenshots |

### IP Firewall (3 articles)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 7 | `waap/ip-security.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 8 | `waap/ip-security/allow-and-block-ip-addresses.mdx` | 8 | [x] DONE | waap-urgent-updates | Fixed UI labels, numbering, em dash spacing |
| 9 | `waap/waap-policies/ip-reputation.mdx` | 2 | [x] DONE | waap-urgent-updates | No changes needed (Pro/Enterprise only) |

### DDoS Protection (1 article)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 10 | `waap/ddos-protection.mdx` | 0 | [x] DONE | waap-urgent-updates | Fixed anchor link to L7 DDoS page |

### Default WAF Policies (4 articles)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 11 | `waap/waap-policies.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 12 | `waap/waap-policies/waf-and-owasp-top-threats.mdx` | 2 | [x] DONE | waap-urgent-updates | Added RFI/LFI abbreviations to match UI |
| 13 | `waap/waap-policies/behavioral-waf.mdx` | 2 | [x] DONE | waap-urgent-updates | No changes needed (Pro/Enterprise features) |
| 14 | `waap/waap-policies/cms-protection.mdx` | 4 | [x] DONE | waap-urgent-updates | No changes needed |

### Custom Rules (8 articles)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 15 | `waap/waap-rules.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 16 | `waap/waap-rules/custom-rules.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 17 | `waap/waap-rules/advanced-rules/advanced-rate-limiting-rules.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed (Enterprise) |
| 18 | `waap/waap-rules/advanced-rules.mdx` | 1 | [x] DONE | waap-urgent-updates | No changes needed (Enterprise) |
| 19 | `waap/waap-rules/advanced-rules/advanced-rule-objects.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed (Enterprise) |
| 20 | `waap/waap-rules/advanced-rules/source-field-objects.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed (Enterprise) |
| 21 | `waap/waap-rules/custom-rules/tag-rules.mdx` | 3 | [x] DONE | waap-urgent-updates | No changes needed |
| 22 | `waap/waap-rules/custom-rules/tag-rules/reserved-tags.mdx` | 9 | [x] DONE | waap-urgent-updates | No changes needed |
| 23 | `waap/waap-rules/custom-rules/tag-rules/predefined-tags.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |

### Bot Management (4 articles)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 24 | `waap/troubleshooting/enable-troubleshoot-bot-protection.mdx` | 2 | [x] DONE | waap-urgent-updates | No changes needed |
| 25 | `waap/waap-policies/known-bots.mdx` | 2 | [x] DONE | waap-urgent-updates | No changes needed (Pro/Enterprise) |
| 26 | `waap/waap-policies/anti-automation-and-bot-protection.mdx` | 2 | [x] DONE | waap-urgent-updates | No changes needed |
| 27 | `waap/waap-policies/invalid-user-agent-and-unknown-user-agent.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |

### Threat Intelligence (2 articles)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 28 | `waap/security-insights.mdx` | 22 | [x] DONE | waap-urgent-updates | No changes needed |
| 29 | `waap/ip-security/ip-spotlight.mdx` | 9 | [x] DONE | waap-urgent-updates | No changes needed |

### API Protection (6 articles)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 30 | `waap/api-discovery-and-protection.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 31 | `waap/api-discovery-and-protection/api-discovery.mdx` | 5 | [x] DONE | waap-urgent-updates | No changes needed (Enterprise) |
| 32 | `waap/api-discovery-and-protection/configure-api-access-with-reserved-tags.mdx` | 6 | [x] DONE | waap-urgent-updates | No changes needed |
| 33 | `waap/api-discovery-and-protection/configure-api-base-path.mdx` | 1 | [x] DONE | waap-urgent-updates | No changes needed |
| 34 | `waap/waap-policies/advanced-api-protection.mdx` | 2 | [x] DONE | waap-urgent-updates | No changes needed (Enterprise) |
| 35 | `waap/waap-policies/protocol-validation.mdx` | 2 | [x] DONE | waap-urgent-updates | No changes needed |

### Response Pages (3 articles)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 36 | `waap/response-pages.mdx` | 5 | [x] DONE | waap-urgent-updates | No changes needed |
| 37 | `waap/response-pages/create-custom-response-pages.mdx` | 9 | [x] DONE | waap-urgent-updates | No changes needed |
| 38 | `waap/response-pages/manage-custom-response-pages.mdx` | 5 | [x] DONE | waap-urgent-updates | No changes needed |

### FAQs and Troubleshooting (7 articles)

| # | File | Screenshots | Status | Branch | Notes |
|---|------|-------------|--------|--------|-------|
| 39 | `waap/frequently-asked-questions.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 40 | `waap/frequently-asked-questions/javascript-injection.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 41 | `waap/frequently-asked-questions/waap-cookies.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 42 | `waap/frequently-asked-questions/storage-variables.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 43 | `waap/troubleshooting.mdx` | 0 | [x] DONE | waap-urgent-updates | No changes needed |
| 44 | `waap/troubleshooting/troubleshoot-blocked-users.mdx` | 3 | [x] DONE | waap-urgent-updates | No changes needed |
| 45 | `waap/troubleshooting/troubleshoot-5xx-errors.mdx` | 1 | [x] DONE | waap-urgent-updates | No changes needed |

---

## Progress Summary

| Category | Articles | Screenshots | Completed | Remaining |
|----------|----------|-------------|-----------|-----------|
| Getting Started | 5 | 22 | 5 | 0 |
| Analytics | 1 | 21 | 1 | 0 |
| IP Firewall | 3 | 10 | 3 | 0 |
| DDoS Protection | 1 | 0 | 1 | 0 |
| Default WAF Policies | 4 | 8 | 4 | 0 |
| Custom Rules | 9 | 13 | 9 | 0 |
| Bot Management | 4 | 6 | 4 | 0 |
| Threat Intelligence | 2 | 31 | 2 | 0 |
| API Protection | 6 | 16 | 6 | 0 |
| Response Pages | 3 | 19 | 3 | 0 |
| FAQs/Troubleshooting | 7 | 4 | 7 | 0 |
| **TOTAL** | **45** | **151** | **45** | **0** |

---

## Change Log

| Date | Article | Changes | Author |
|------|---------|---------|--------|
| 2026-02-12 | configure-waap-for-a-domain.mdx | Full revision: terminology, navigation, filters, screenshots, proofreading | Agent |
| 2026-02-12 | analytics.mdx | Full revision: title to Events, terminology, table columns, section descriptions, screenshots | Agent |
| 2026-02-12 | overview.mdx | No changes needed - general overview | Agent |
| 2026-02-12 | billing.mdx | Fixed broken link, replaced "Common automated services" with "Known Bots" | Agent |
| 2026-02-12 | waap-modes.mdx | Fixed alt text Analytics->Events | Agent |
| 2026-02-12 | manage-domains.mdx | Fixed spacing before colons, grammar error | Agent |

---

## Playwright MCP Workflow

### Portal Map

During navigation, build a complete map of the WAAP section:

**Output file**: `C:\Projects\docops-agent\v3-papa-children\cache\portal\portal_map.json`

Map structure:
```json
{
  "waap": {
    "url": "/waap",
    "title": "WAAP",
    "sections": {
      "section_name": {
        "url": "/waap/section",
        "title": "Section Title",
        "tabs": ["Tab1", "Tab2"],
        "buttons": ["Button1", "Button2"],
        "subsections": {}
      }
    }
  }
}
```

### Browser Session

**IMPORTANT**: Do NOT close the browser between articles. Keep the session alive to:
- Avoid re-login for each article
- Speed up the review process
- Maintain portal state

### Login Sequence

1. Navigate to https://auth.gcore.com/login/signin
2. Accept cookies if prompted
3. Enter email and password
4. After login, select account "mycompanytest"

### Screenshot Capture

1. Resize browser to 1920x1080 before capturing
2. Navigate to WAAP section in portal
3. For each article:
   - Follow the article as instructions
   - Compare UI with documentation
   - Capture screenshots of changed sections
   - Save to `images/docs/waap/{section}/`

### Screenshot Rules (from guidelines)

- Capture context, not isolated elements
- Include navigation sidebar when describing how to get somewhere
- NEVER include account balance or billing header
- Crop out empty space
- Use descriptive alt text

### File Naming

Format: `{section}-{action}.png` or `step{N}-{description}.png`

Examples:
- `analytics-dashboard.png`
- `step2-configure-domain.png`
- `ip-firewall-allow-list.png`

---

## Notes

- Credentials stored separately in `_private/portal-acces.txt`
- Do NOT commit credentials or sensitive data
- Each article branch should have descriptive commit messages

---

## Commit Message Template

```
docs(waap): update {article-name}

UI changes:
- {list of UI elements that changed}

Screenshots:
- Updated: {list of updated screenshots}
- Added: {list of new screenshots}
- Removed: {list of removed screenshots}

Proofreading:
- {list of text fixes if any}

New features: {description or "none"}
Deprecated: {description or "none"}
```

---

## Priority Order (suggested)

High-traffic/critical articles first:

1. `configure-waap-for-a-domain.mdx` (16 screenshots, main setup guide)
2. `analytics.mdx` (21 screenshots, frequently used)
3. `security-insights.mdx` (22 screenshots, key feature)
4. `overview.mdx` (entry point)
5. `waap-modes.mdx` (core concept)

Then proceed by section systematically.
