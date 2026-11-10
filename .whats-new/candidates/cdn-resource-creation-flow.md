---
product: CDN
status: Include
release_date: 2026-11-10
published_page: null
---

# CDN resource creation form

Customer change: Creating a CDN resource is one form. The form takes a Gcore domain or a custom domain, then an origin (URL or IP, S3 storage, FastEdge, or an existing origin group). A Gcore domain needs no DNS record. A custom domain shows a CNAME or ALIAS record after creation, and the target is the account CNAME. The resource goes live 15 minutes after creation.
Affected users: Customers who create a CDN resource in the Customer Portal. On the existing account used for the check, the Gcore domain suffix was gcdn.co. A new Gcore account is stated to receive gcorecdn.com. That suffix was not shown on this account.
Release evidence: Production Customer Portal on 2026-11-10, https://portal.gcore.com/cdn/resources/create/new. A custom-domain resource and a Gcore-domain resource were created, the confirmation screens were read, and both resources and their origin groups were deleted.
Open verification: The gcorecdn.com suffix for a new Gcore account was not opened on this account.
Source tickets/PRs: DOC-2899
Documentation links: /cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource, /cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn, /cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-video-streaming, /cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-aws-s3, /cdn/video-cdn/hls
Duplicate check: not found. CDN has no What's new page.
Published entry: none
