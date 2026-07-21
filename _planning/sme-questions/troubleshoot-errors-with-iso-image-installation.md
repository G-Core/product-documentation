# SME questions — Troubleshoot errors with ISO image installation

**Ticket:** DOC-1763
**Audited:** 2026-07-21

## Verified in live testing and cross-article review

- Navigation `Templates > ISO-images` — CONFIRMED (DCImanager breadcrumb: JB1 > ISO-images)
- File format `.iso` — CONFIRMED (DCImanager upload dialog: "Only 1 file in .iso format")
- Lowercase `.iso` extension requirement — CONFIRMED (parallel VPS article `/hosting/virtual-servers/troubleshooting/troubleshoot-errors-with-iso-image-installation.mdx` states same rule)
- "Letters and numbers only" filename rule — CONFIRMED (same parallel VPS article)
- 9 GB size limit — CONFIRMED (Confluence: "[G-Host] Dedicated server")
- 4 images per account limit — CONFIRMED (Confluence: "[G-Host] Dedicated server")

## Questions for SME

| # | Location in article | What the article claims | What we observed | Question for SME |
|---|---------------------|------------------------|-----------------|-----------------|
| 1 | Upload failure — bullet 4 | "ISO images are automatically deleted after 24 hours." | Not confirmed in UI or Confluence. DCImanager has a "Deleted ISO images" subnav section (possibly for manually deleted images only). | Is the 24-hour auto-deletion still active? Does it apply to all ISO images or only images in a failed state? |
| 2 | Upload failure — last paragraph | DCI manager shows a **Delete the ISO-image** button in the error dialog | Could not trigger a failed upload to verify the error dialog UI | Does a failed upload still show a **Delete the ISO-image** button in the error dialog? Is the label exact? |
| 3 | Mounting error | Error message: `Error occurred when mounting ISO-image on the IPMI proxy server. Script output: ''` | Could not mount an image without uploading one first | Is this still the exact error message shown by the current DCImanager version? |
