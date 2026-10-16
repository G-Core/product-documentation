---
product: Cloud
status: Include
release_date: unknown
published_page: null
---

# Load balancer FQDN

Customer change: An active load balancer in the Customer Portal has an FQDN. Customers can use that hostname instead of the VIP address, for example as a CNAME target. The name is generated and cannot be changed.
Affected users: Customers who address a Cloud load balancer by hostname rather than by VIP address
Release evidence: Checked on the preprod Customer Portal. An Active load balancer shows the FQDN in Connection details and in the Endpoints column.
Open verification: Production API returns vip_fqdn null while the load balancer is ACTIVE. Python SDK 0.59.0 and Go SDK 0.59.0 print that empty value. A/AAAA was not resolved. Terraform provider 2.0.0-rc.2 has no vip_fqdn attribute.
Source tickets/PRs: DOC-2658, DOC-2638
Documentation links: cloud/networking/load-balancers/manage-load-balancers.mdx, cloud/networking/create-and-configure-a-load-balancer.mdx
Duplicate check: not found on a Cloud What's new page or in the candidate register
Published entry: null
