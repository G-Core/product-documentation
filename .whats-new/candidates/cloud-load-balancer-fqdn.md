---
product: Cloud
status: Include
release_date: unknown
published_page: null
---

# Load balancer FQDN in the Customer Portal

Customer change: An active load balancer has an FQDN. Customers can use that hostname instead of the VIP address, for example as a CNAME target. The name is generated and cannot be changed.
Affected users: Customers who address a Cloud load balancer by hostname rather than by VIP address
Release evidence: Checked on the preprod Customer Portal. An Active load balancer shows the FQDN in Connection details and in the Endpoints column. That is the production behavior.
Open verification: none
Source tickets/PRs: DOC-2658, DOC-2638
Documentation links: cloud/networking/load-balancers/manage-load-balancers.mdx, cloud/networking/create-and-configure-a-load-balancer.mdx
Duplicate check: not found on a Cloud What's new page or in the candidate register
Published entry: null
