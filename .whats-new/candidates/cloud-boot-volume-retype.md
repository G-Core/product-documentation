---
product: Cloud
status: Include
release_date: 2026-10-21
published_page: null
---

# Retype boot volumes between Standard and High IOPS SSD

Customer change: On the production Customer Portal, Retype is offered for an attached Standard boot volume and an attached High IOPS SSD boot volume. The dialog lists only the other of those two types. Retype is also offered for an attached High IOPS SSD data volume, without detaching it first.
Affected users: Customers with a Standard or High IOPS SSD volume, including a boot volume that is in use.
Release evidence: Checked on https://portal.gcore.com in Luxembourg-3 on 2026-10-22. The action menu of both attached boot volumes contained Retype. The type list contained only Standard and High IOPS SSD. The retype was not submitted. GCLOUD2-29867 is Done in cloud-frontend 7.72.0, released 2026-10-21. No Cold, Ultra, SSD Low-Latency, or local SSD volume was present, so the hidden-Retype case for those types was not opened.
Open verification: none for the Standard and High IOPS SSD path. The excluded types were not present in this project and region.
Source tickets/PRs: GCLOUD2-29867, DOC-2820
Documentation links: cloud/virtual-instances/volumes/manage-a-volume.mdx
Duplicate check: no Cloud What's new page and no earlier candidate for this change
Published entry: null
