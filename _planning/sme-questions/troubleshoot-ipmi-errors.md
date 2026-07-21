# SME questions — Troubleshoot IPMI errors

**Ticket:** DOC-1826
**Audited:** 2026-07-21

## Verified in live testing

- IPMI access path: BillMgr → Dedicated Servers → To panel → DCImanager → server row → Connections → IPMI v2(lanplus) → Go to — CONFIRMED
- Autocomplete buttons "Login" and "Password" exist in the top-left corner of the IPMI proxy — CONFIRMED
- Server uses iDRAC 9 (Dell PowerEdge R340 Enterprise) — CONFIRMED
- Error 1006 cause: only 1 active IPMI session allowed — CONFIRMED (Confluence)
- Full-screen mode: Options > Full-Screen Mode, exit with F3 — CONFIRMED (Confluence)

## Questions for SME

| # | Location in article | What the article claims | What we observed | Question for SME |
|---|---------------------|------------------------|-----------------|-----------------|
| 1 | Remote console section | "In the IPMI panel, open the **Maintenance** menu and select **IKVM Reset**" | Could not log in to iDRAC 9 without triggering an actual connection failure. Confluence does not mention this step. | Is the Maintenance > IKVM Reset path still correct for iDRAC 9? Does iDRAC 9 have this option? |
| 2 | Remote console section | "In the IPMI panel, open the **Maintenance** menu and select **Unit Reset**" | Could not verify in iDRAC 9 UI | Is Unit Reset still available in iDRAC 9 Maintenance menu, or has the menu structure changed? |
| 3 | Error 1006 screenshot | Screenshot shows old DCImanager proxy header with error 1006 | Current proxy shows iDRAC 9 HTML interface — cannot reproduce error 1006 without two concurrent sessions | Does error 1006 still appear as a banner in the proxy header, or is it shown differently in the current iDRAC 9 proxy? |
| 4 | IPMI URL not available screenshot | Screenshot shows plain text error "IPMI URL (http://192.168.x.x) of the selected server is not available" | Cannot reproduce without a server with IPMI connection failure | Does this error still appear in the same format in DCImanager 6, or has the error display changed? |
