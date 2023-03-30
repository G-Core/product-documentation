---
title: about-cdn-resources-interface-how-it-is-arranged
displayName: CDN resources overview
published: true
order: 40
toc:
   --1--What is it: "what-is-the-cdn-resources-tab"
   --1--Manage: "manage-cdn-resources"
   --2--Filter and search: "filter-and-search"
   --2--Manage options: "manage-options"
   --2--Delete: "delete-a-resource"
---
   
[Create](#what-is-the-cdn-resources-tab)  
  
        •  
        •  
        •

What is the CDN resources tab?
------------------------------

[CDN resources](https://cdn.gcore.com/resources/list) is a tab where you can create a CDN resource and manage the already created resources.

Also, this tab displays the following:

1\. Current tariff plan. If you want to change it, press **Upgrade** (if you use Free plan) or **Change plan** on the left.   
2\. Balance. If you need, press **Recharge** on the right.  

<img src="https://support.gcore.com/hc/article_attachments/10276342871697" alt="mceclip0.png">

Create a CDN resource
---------------------

Click the **Create CDN Resource** button.

<img src="https://support.gcore.com/hc/article_attachments/10272561190417" alt="mceclip1.png">

See the "[Create and integrate CDN resource for only static files](https://gcore.com/support/articles/213969429/)" guide for detailed instructions on creating a CDN resource. 

Manage CDN resources
--------------------

### Filter and search

There are four statuses for resources:

1\. "Active" is for resources that are ready to use. Content is available to users.

2\. "Suspended" is for resources that are not available. Content is also not available for users.

3\. "In processing" is for resources that were recently created and are now handling. It takes about 15 minutes to propagate the resource settings to all servers.

4\. "Deleted" is for resources that have been deleted. Content is not distributed. You can only view statistics on a resource.

By default, the CDN Resource tab displays only resources with the "Active" and "In processing" statuses.  

For custom search use:

*   Search bar. Enter the main or additional CNAME of the needful resource or its ID.
*   Status section. Select the needful status or the "Select all" option.  

<img src="https://support.gcore.com/hc/article_attachments/10274072513937" alt="mceclip2.png">

### Manage options

You can manage a specific CDN resource directly from the list of CDN resources.

To do this, click on the three dots sign next to the required resource.

A list of possible options opens:

<img src="https://support.gcore.com/hc/article_attachments/10274251831185" alt="mceclip3.png">

*   "Settings" opens the resource settings. You can also go to the resource settings by clicking on the CNAME of the resource.
*   "Prefetch" opens the [Prefetch](https://gcore.com/support/articles/214035089/) section to upload the content to CDN before users request it.
*   "Purge" opens the [Purge](https://gcore.com/support/articles/214532065/) section to purge the resource cache.
*   "Statistics" opens the [reports](https://gcore.com/support/articles/115004917425/) of a resource.
*   "Turn on LIVE STREAMING preset" adds a set of settings [to configure HLS file caching through RAM instead of through hard drives.](https://support.gcore.com/hc/en-us/articles/115002080125)
*   "Delete resource" deletes a resource. 

### Delete a resource

Users with the Administrator's or Engineer's rights can delete resources.

To delete a resource, click on the three dots sign on the left, select **Delete resource**, and confirm the action.

**Note!** The resources used for the Streaming service cannot be deleted.

By default, deleted resources are not displayed in the list of resources. Use [the filter](#filter-and-search) to display them. Deleted resources are shown in the list of all CDN resources for three months. Statistics for deleted resources are also available in the [Reports](https://gcore.com/support/articles/115004917425/) section during this time.

After resource deletion, the CNAME of this resource is no more connected with a resource. So you can use it for the new CDN resource.