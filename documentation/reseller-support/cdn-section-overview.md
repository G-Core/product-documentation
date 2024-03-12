---
title: cdn-section-overview
displayName: CDN section overview
published: true
order: 25
toc:
    --1--Clients: "clients"
    --1--CDN resources: "cdn-resources"
    --1--Activity logs: "activity-logs"
    --1--Origin groups: "origin-groups"
pageTitle: Understanding Client, Resource, and Activity Information | Gcore
pageDescription: Explore our guide on CDN client details, resource data, activity logs, and origin groups for efficient CDN management.
---
# CDN section overview

The CDN section collects information about your customers who use CDN and the resources they utilize. It includes the following subsections:

## Clients

This subsection provides details about customers who have created CDN resources. Each entry includes:

- The customer’s account ID
- The CDN resource custom domain
- The email associated with the account
- The company name
- The date the CDN resource was created
- The CDN resource ID, along with custom domains and traffic data
- The amount of incoming traffic
A list of paid features activated for the CDN resources
- The CDN resource status (e.g., “New,” “Trial,” “Trial End,” “Active,” “Paused,” “Activating,” “Deleted”) 

You can apply filters to manage specific entries. By default, only CDN resources with an “Active” status are displayed. 

Click the three dots on the right to edit customer settings. For further details, refer to the dedicated guide: <a href="https://gcore.com/docs/reseller-support/manuals/manage-clients#edit-an-account" target="_blank">Manage сlients</a>. Click the arrow to log in to the Customer Portal as a customer.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-section-overview/clients-tab-10.png" alt="Clients tab in the CDN section" width="80%">

## CDN resources

This subsection lists all CDN resources created by customers. Each entry includes:

- The CDN resource ID
- The CDN resource <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">custom domain (CNAME)</a>
- The client's ID
- The ID of the main resource (not the reserve, if an <a href="https://gcore.com/docs/cdn/add-an-origin-group" target="_blank">origin group</a> contains multiple origins)
- The SSL ID (if applicable)
- The shielding status (if enabled)
Any CDN resource rules (if created)
- The origin group ID
- The CDN resource status (e.g., “New,” “Trial,” “Trial End,” “Active,” “Paused,” “Activating,” “Deleted”)
- The resource type (default or technical)
A toggle indicating whether automatic suspension is enabled for the CDN resource
- The date the CDN resource was created

You can log in as a customer to configure specific CDN resource settings without having to navigate to the Customer Portal. 

You can also filter resources scheduled for automatic suspension. This feature can assist you in contacting customers to discuss their plans for using CDN resources or to refine suspension and data deletion procedures.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-section-overview/cdn-resources-tab-20.png" alt="CDN resources tab in the CDN section" width="80%">

## Activity logs

This subsection contains activity logs that document CDN resource changes, rule configurations, purge, and prefetch requests. Each entry includes:

- The client ID
- The user ID (customers can create multiple users per account)
- The date and time of the request (in UTC)
- The HTTP request method (GET, POST, PUT, DELETE, or PATCH)
- The requested path
Request data (if available)
- The request status code (e.g., 200, 404, 503)
- The customer's remote IP address
- The requested host
- The API token ID and the ID of the user who issued it

You can add filters to display logs based on specific parameters.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-section-overview/activity-logs-tab-30.png" alt="Activity logs tab in the CDN section" width="80%">

## Origin groups

This subsection provides information about <a href="https://gcore.com/docs/cdn/add-an-origin-group" target="_blank">origin groups</a>. Each entry includes:

- The origin group ID
- The origin group name
- A list of origins included in the group
- The CDN resource’s custom domain and ID (if a CDN resource has been specified for the origin group)

You can edit or delete an origin group by clicking the three dots and selecting the appropriate action.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-section-overview/origin-groups-tab-40.png" alt="Origin groups tab in the CDN section" width="80%">