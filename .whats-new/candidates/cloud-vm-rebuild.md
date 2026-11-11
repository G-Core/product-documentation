---
product: Cloud
status: Include
release_date: 2026-11-10
published_page: null
---

# Rebuild a virtual machine

Customer change: A virtual machine can be rebuilt with POST /cloud/v3/instances/{project_id}/{region_id}/{instance_id}/rebuild. An empty body reinstalls the current image. image_id selects another public image in the same region, and ssh_key_name replaces the SSH key. The boot volume is reimaged. The instance status is REBUILD while the task runs and returns to ACTIVE when the new image is in place.
Affected users: Customers who manage virtual machines with the Cloud API.
Release evidence: Production API on 2026-11-12, https://api.gcore.com. In Luxembourg-3, a new g2-standard-1-2 VM was created, rebuilt with an empty body (image stayed Ubuntu 22.04, task rebuild_vm finished), then rebuilt with image_id for Ubuntu 24.04 and another SSH key name. metadata.image_name became ubuntu-24.04-x64 after status returned to ACTIVE. The VM and its boot volume were deleted. cloud-api 14.514.0 was released 2026-11-10. The v1 rebuild path still returns "The URL does not match an endpoint."
Open verification: A successful user_data payload was not applied. Private images and the Customer Portal were not checked.
Source tickets/PRs: DOC-2912, GCLOUD2-26235
Documentation links: /cloud/virtual-instances/rebuild-a-virtual-instance
Duplicate check: not found. Cloud has no What's new page.
Published entry: none
