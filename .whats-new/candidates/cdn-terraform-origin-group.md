---
product: CDN
status: Include
release_date: 2026-10-30
published_page: null
---

# CDN resource origin in Terraform

Customer change: On Terraform provider v2, a CDN resource takes origin_group. The resource does not accept an origin attribute. The origin hostname belongs to gcore_cdn_origin_group.
Affected users: Accounts that create Gcore CDN resources with the v2 provider.
Release evidence: Provider 2.0.0-rc.3, published 2026-10-30. Live apply created an origin group and a CDN resource. A configuration that set origin on the CDN resource was rejected at plan. The test resources were destroyed.
Open verification: none
Source tickets/PRs: https://github.com/G-Core/product-documentation/issues/3251, https://github.com/G-Core/terraform-provider-gcore/releases/tag/v2.0.0-rc.3
Documentation links: waap/manage-waap-via-terraform.mdx, developer-tools/terraform/copy-resources-across-environments.mdx
Duplicate check: not found
Published entry: none
