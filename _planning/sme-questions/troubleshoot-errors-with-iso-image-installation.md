# SME questions — Troubleshoot errors with ISO image installation

**Ticket:** DOC-1763
**Audited:** 2026-07-21

## Questions

| # | Location in article | What the article claims | What we observed | Question for SME |
|---|---------------------|------------------------|-----------------|-----------------|
| 1 | Opening paragraph | Navigation: DCI manager > **Templates** > **ISO-images** | Confluence support doc says "find ISO-images tab" (no mention of Templates parent section) — may reflect old DCImanager 5 UI | Is the current navigation path **Templates** > **ISO-images** correct in DCImanager 6? |
| 2 | Upload failure — bullet 1 | File extension must be lowercase: `.iso`, not `.ISO` | Not mentioned in any Confluence source | Is the lowercase extension requirement still enforced? Is the "letters and numbers only" filename rule accurate? |
| 3 | Upload failure — bullet 4 | ISO images are automatically deleted after 24 hours | Not confirmed in Confluence (Confluence only confirms 9 GB and 4-image limits) | Is the 24-hour auto-deletion still active? Has this policy changed? |
| 4 | Upload failure — last paragraph | DCI manager shows a **Delete the ISO-image** button in the error dialog | Could not verify — no dedicated server provisioned, DCImanager inaccessible | Does the error dialog still show a **Delete the ISO-image** button? Is the button label accurate? |
| 5 | Mounting error | Error message: `Error occurred when mounting ISO-image on the IPMI proxy server. Script output: ''` | Could not verify — no dedicated server provisioned | Is this still the exact error message shown by the current version of DCImanager? |
