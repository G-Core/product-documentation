# SME questions — Troubleshoot errors with ISO image installation

**Ticket:** DOC-1763
**Audited:** 2026-07-21

## Verified in live testing

- Navigation `Templates > ISO-images` — CONFIRMED (breadcrumb: JB1 > ISO-images)
- File format `.iso` — CONFIRMED (UI shows "Only 1 file in .iso format")
- 9 GB size limit — CONFIRMED (Confluence: "[G-Host] Dedicated server" page)
- 4 images per account limit — CONFIRMED (Confluence: "[G-Host] Dedicated server" page)

## Questions for SME

| # | Location in article | What the article claims | What we observed | Question for SME |
|---|---------------------|------------------------|-----------------|-----------------|
| 1 | Upload failure — bullet 1 | "The file extension must be lowercase: `.iso`, not `.ISO`." | UI shows "Only 1 file in .iso format" with no mention of case sensitivity | Is the lowercase extension still enforced server-side? Or is `.ISO` also accepted? |
| 2 | Upload failure — bullet 1 | "Use only letters and numbers in the filename." | Not shown anywhere in the upload UI | Is this still a requirement? What characters are actually allowed in ISO image names? |
| 3 | Upload failure — bullet 4 | "ISO images are automatically deleted after 24 hours." | Not confirmed in UI or Confluence. DCImanager has a "Deleted ISO images" section (possibly for manually deleted images). | Is the 24-hour auto-deletion still active? Does it apply to all accounts or only accounts without active servers? |
| 4 | Upload failure — last paragraph | DCI manager shows a **Delete the ISO-image** button in the error dialog | Could not trigger a failed upload to verify the error dialog UI | Does the error dialog still show a **Delete the ISO-image** button? Is the button label accurate? |
| 5 | Mounting error | Error message: `Error occurred when mounting ISO-image on the IPMI proxy server. Script output: ''` | Could not mount an image to verify the error message | Is this still the exact error message shown by the current DCImanager version? |
