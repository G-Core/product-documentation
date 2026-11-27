---
product: Cloud
status: Include
release_date: 2026-11-25
published_page: null
---

# Cloud instance create in SDK 0.64.0

Customer change: Python gcore 0.64.0 and Go gcore-go v0.64.0 create an instance from an existing boot volume and an existing port. flavor_name, boot_volume_id, interfaces with port_id, and region_id replace inline volumes and an external interface. The public IP is on the interface. name is optional, and an account that forbids a custom name rejects any other value.
Affected users: Customers who create virtual instances with the Python or Go SDK
Release evidence: Python gcore 0.64.0 and Go gcore-go v0.64.0 published 2026-11-25. The same create, get, and delete ran on production in Luxembourg-3 and returned status active, then the instance, volume, and port were deleted. Python and Go each created an instance with user_data, tags, and placement_group_id. Python attached a security group on the port, attached a reserved IP by port_id, and cleared that group list. A bare metal create with dry_run and a port that had no security groups returned an empty task list in Python and in Go. A vxlan port and a second port group were rejected. Terraform and the regional curl body were not part of this change.
Open verification: none
Source tickets/PRs: DOC-3081, GitHub #3400, PR 3407
Documentation links: cloud/virtual-instances/create-an-instance.mdx, cloud/virtual-instances/check-the-operational-status-of-your-instance.mdx, cloud/virtual-instances/customize-initial-setup-for-your-instance.mdx, cloud/virtual-instances/rebuild-a-virtual-instance.mdx, cloud/virtual-instances/placement-groups/configure-a-placement-group.mdx, cloud/networking/add-and-configure-a-firewall.mdx, cloud/networking/ip-address/create-and-configure-a-floating-ip-address.mdx, cloud/networking/ip-address/create-and-configure-a-reserved-ip-address.mdx, cloud/networking/ip-address/create-and-configure-a-virtual-ip-vip-address.mdx, cloud/tags.mdx, cloud/bare-metal-servers/create-a-bare-metal-server.mdx, cloud/bare-metal-servers/manage-a-bare-metal-server.mdx, developer-tools/rest-api/first-api-call.mdx, developer-tools/rest-api/pagination.mdx, developer-tools/rest-api/tools.mdx, developer-tools/sdks/python.mdx, developer-tools/sdks/go.mdx
Duplicate check: not found
Published entry: null
