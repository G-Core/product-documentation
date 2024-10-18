---
title: about-cdn-resources-interface-how-it-is-arranged
displayName: CDN resources overview
published: true
order: 40
toc:
   --1--What is it: "what-is-the-cdn-resources-tab"
   --1--Create: "create-a-cdn-resource"
   --1--Manage: "manage-cdn-resources"
   --2--Filter and search: "filter-and-search"
   --2--Manage options: "manage-options"
   --2--Delete: "delete-a-resource"
pageTitle: CDN Resources Tab Overview | Gcore
pageDescription: Explanation of how the CDN resources tab is arranged. 
---
# About CDN resources interface: how it is arranged

## What is the CDN resources tab?

<a href="https://cdn.gcore.com/resources/list" target="_blank">CDN resources</a> is a page in the Gcore Customer Portal where you can create a CDN resource and manage the already created resources.

Also, this tab displays the following:

1\. Current tariff plan. If you want to change it, press **Upgrade** (if you use Free plan) or **Change plan** on the left.

2\. Balance. If you need, press **Recharge** on the right.  

<img src="https://assets.gcore.pro/docs/cdn/about-cdn-resources-interface-how-it-is-arranged/10276342871697.png" alt="CDN resources tab">

## Create a CDN resource

Click the **Create CDN Resource** button.

<img src="https://assets.gcore.pro/docs/cdn/about-cdn-resources-interface-how-it-is-arranged/10272561190417.png" alt="Create a CDN resource">

Refer to the following guide for detailed instructions on creating a CDN resource: <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">Create and integrate CDN resource for static assets only</a>. 

## Manage CDN resources

### Filter and search

There are four statuses for resources:

1\. "Active" is for resources that are ready to use. Content is available to users.

2\. "Suspended" is for resources that are not available. Content is also not available for users.

3\. "In processing" is for resources that were recently created and are now handling. It takes about 15 minutes to propagate the resource settings to all servers.

4\. "Deleted" is for resources that have been deleted. Content is not distributed. You can only view statistics on a resource.

By default, the CDN Resource tab displays only resources with the "Active" and "In processing" statuses.  

For custom search use:

- Search bar. Enter the main or additional CNAME of the needful resource or its ID.
- Status section. Select the needful status or the "Select all" option.  

<img src="https://assets.gcore.pro/docs/cdn/about-cdn-resources-interface-how-it-is-arranged/resources-page-overview.png" alt="Search bar and resource statuses" width="80%">

### Manage options

You can manage a specific CDN resource directly from the list of CDN resources.

To do this, click on the three dots sign next to the required resource.

A list of possible options opens:

<img src="https://assets.gcore.pro/docs/cdn/about-cdn-resources-interface-how-it-is-arranged/cdn-resource-settings-button.png" alt="Manage options" width="80%">

- "Settings" opens the resource settings. You can also go to the resource settings by clicking on the CNAME of the resource.
- "Prefetch" opens the <a href="https://gcore.com/docs/cdn/load-the-content-to-cdn-before-users-request-it" target="_blank">Prefetch</a> section to upload the content to CDN before users request it.
- "Purge" opens the <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">Purge</a> section to purge the resource cache.
- "Statistics" opens the <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">reports</a> of a resource.
- "Turn on LIVE STREAMING preset" adds a set of settings <a href="https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs" target="_blank">to configure HLS file caching through RAM instead of through hard drives</a>.
- "Delete resource" deletes a resource. 

### Delete a resource

<alert-element type="info" title="Info">
 
To delete a resource, you need to have the Administrator or Engineer <a href="https://gcore.com/docs/account-settings/users/about-users#about-users" target="_blank">user role</a>. 
 
</alert-element>

Active resources cannot be deleted. To remove an active CDN resource, you need to suspend it first. 

To delete a resource:  

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **CDN**. 

2\. Find the resource you want to remove and click the three-dot icon next to it. 

3\. Select **Delete resource**.

<img src="https://assets.gcore.pro/docs/cdn/about-cdn-resources-interface-how-it-is-arranged/delete-resource-menu.png" alt="CDN resource settings with delete button highlighted" width="80%">

4\. If the resource is active, you’ll need to suspend it first. Click **Yes, suspend**. 

After the resource is <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/suspend-a-cdn-resource-automatically-or-manually" target="_blank">suspended</a>, it won't deliver any traffic to users. We retain all settings for suspended resources and you can activate a resource back within 90 days after suspension. After this period, the resource is deleted.

<img src="https://assets.gcore.pro/docs/cdn/about-cdn-resources-interface-how-it-is-arranged/confirm-suspension.png" alt="CDN resource deletion confirmation dialog" width="80%">

5\. Proceed with the resource deletion by clicking **Yes, delete**. 

<alert-element type="info" title="Info">
 
CDN resources used for the <a href="https://gcore.com/docs/streaming-platform" target="_blank">Streaming service</a> cannot be deleted.
 
</alert-element>

By default, deleted resources are not displayed in the list of resources. Use [the filter](https://gcore.com/docs/cdn/about-cdn-resources-interface-how-it-is-arranged#filter-and-search) to display them. Deleted resources are shown in the list of all CDN resources for three months. Statistics for deleted resources are also available in the <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">Reports</a> section during this time.

After resource deletion, the CNAME of this resource is no more connected with a resource. So you can use it for the new CDN resource.
