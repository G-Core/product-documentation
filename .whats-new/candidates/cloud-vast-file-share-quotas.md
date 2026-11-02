---
product: Cloud
status: Include
release_date: 2026-11-02
published_page: null
---

# VAST file share user and group quotas

Customer change: A VAST file share accepts a user or group quota in share_settings.quota. The quota can be set when the share is created and updated with PATCH on the v3 file share path. hard_limit is in bytes. A Standard file share rejects share_settings.
Affected users: Customers who create VAST file shares through the Cloud API.
Release evidence: On 2026-11-02 the production Cloud API in Sines-3 created a VAST file share with default_user_quota and then applied default_group_quota. The temporary share was deleted. The Customer Portal quota controls are a separate open ticket and were not checked.
Open verification: none for the API fields that were sent. Portal controls, DDN shares, and clearing a quota with null were not tested.
Source tickets/PRs: GCLOUD2-29620, DOC-2863
Documentation links: cloud/file-shares/configure-file-shares.mdx
Duplicate check: no Cloud What's new entry and no earlier candidate for VAST file share quotas
Published entry: null
