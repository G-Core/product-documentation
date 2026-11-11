---
product: Object Storage
status: Include
release_date: 2026-11-11
published_page: null
---

# S3 Standard file manager opens without credentials

Customer change: On S3 Standard, the bucket file manager opens from the bucket name or the File manager action. It does not ask for an access key or a secret key. Opening it adds https://portal.gcore.com to that bucket's CORS policy and keeps origins that were already set. S3 Fast still asks for an access key and a secret key.
Affected users: Customers who open the web file manager for an S3 Standard bucket.
Release evidence: Production Customer Portal on 2026-11-11, https://portal.gcore.com/storage. The Standard list says the web file manager opens without credentials. Opening my-bucket-1 on storage 13799 went straight to the file manager and created an access key (POST /storage/v4/object_storages/13799/access_keys, 201). With CORS cleared, opening the file manager set allowed origins to https://portal.gcore.com. With only https://example.com set, opening it kept that origin and added https://portal.gcore.com. The type comparison dialog says S3 Fast asks for access keys. No S3 Fast storage exists on this account, so that form was not opened. CORS was restored to https://portal.gcore.com.
Open verification: The S3 Fast access-key form was not opened.
Source tickets/PRs: DOC-2928, STO-538
Documentation links: /storage/manage-object-storage/manage-buckets-via-the-control-panel
Duplicate check: not found. Object Storage has no What's new page.
Published entry: none
