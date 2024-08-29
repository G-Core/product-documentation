---
title: cdn-service-management
displayName: CDN management
published: true
order: 30
toc:
    --1--General CDN settings: "general-cdn-settings"
    --1--Manage: "manage-general-settings"
    --2--Activate CDN: "activate-cdn"
    --2--Transition to deleted status: "transition-to-deleted-status"
    --1--Free and paid features: "free-and-paid-features"
    --1--Balancer: "balancer"
    --2--Set: "set-traffic-balancer"
---
# CDN service management

## General CDN settings

To open the general CDN settings of a particular customer, go to the account settings:

1\. Go to <a href="https://admin.gcore.top/clients" target="_blank">Accounts</a> and open the list of customers.

2\. Click on the ID of the customer. Or, click the three dots and then click **Edit**.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-10.png" alt="Clients">

A new page will open. 

## Manage general settings

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-20.png" alt="Services" width="80%">

### Activate CDN

1\. Go to the "Products" page.

2\. Click **Show more** to open settings. 

3\. Enable the **Activate product** checkbox. Once the "Activate product" checkbox is enabled, the customer can create and manage CDN resources. You can deactivate the product by unchecking the checkbox. In this case, the customer will see a product activation request form on the CDN tab instead of the CDN resources list.

**Note**: Deactivating the "Activate product" checkbox may suspend the work of active resources.

### Transition to deleted status

The CDN product status switches from "TrialEnd"/"Paused" to "Deleted" after a specified number of days. The "Deleted" status means the customer's resources are deleted. You cannot change the number of days yourself. To change the number of days before deletion for a specific customer, email us at [support@gcore.com](mailto:support@gcore.com).

Don’t forget to click **Save changes** to apply them.

## Free and paid features

To see the list of available features, click **CDN settings**.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-30.png" alt="Services" width="80%">

You can also access customer settings via the CDN application.

1\. Open the list of customers, in the "СDN" section.

2\. Click on the ID of the desired customer. Or, click the three dots and then click **Edit**.

3\. Navigate to the **Features** tab.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-40-v2.png" alt="Edit customer" width="80%">

All available features will appear as a list with toggle buttons. Some features are free, while others are paid.

Free features can be identified by the "Show Origin, Shield, and CDN Traffic Separately" option. Enabling this option allows you to view the traffic data in your Customer Portal in a more detailed way. By default, this feature is turned off, which means all traffic data from the origin, shield, and Content Delivery Network (CDN) is displayed together as a combined report. However, if you enable this feature, you can see the traffic from the origin, shield, and CDN separately. Each of these categories will have its own individual report, allowing you to analyze and understand the traffic from each source more clearly.

Paid features include <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">advanced directory, user agents, geo statistics</a>, <a href="https://gcore.com/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage" target="_blank">raw logs</a>, <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">origin shielding</a> (to set the locations, contact technical support or your manager), and <a href="https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs" target="_blank">Video Streaming</a>.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-50.png" alt="Paid features" width="80%">

After activation, don’t forget to save changes.

Certain features, such as resources with shared cache zone, wildcard purge, and Image Stack, can only be enabled by contacting the Gcore support team at [support@gcore.com](mailto:support@gcore.com). You can learn more about these features by hovering your cursor over the question mark by their name.

## Balancer

CDN servers are grouped into regions in <a href="https://gcore.com/docs/cdn/cdn-resource-options/determine-in-which-regions-the-content-will-be-delivered-with-geo-balancer-for-paid-tariffs" target="_blank">Geobalancer</a>: *North America*, *CIS*, *Australia*, *Middle East*, *Africa*, *Europe*, *Asia*, *Latin America*, and *World*. The *World* option means anycast addressing is used, so the content could be served from any region in the global network, depending on which server can deliver the content most efficiently at that particular moment.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/balancer.png" alt="Balancer tab" width="80%">

### Set traffic balancer

By default, this feature is disabled. If you want to manage routing, e.g., exclude some regions from delivery if there are no end users in this region, enable the feature as follows:

1\. Click **Enable traffic balancer**. 

2\. Ensure that “Enable IPv6 delivery” checkbox is checked if you want to include IPv6 addresses in responses (AAAA record). If you need only IPv4 addresses (A record)—uncheck it. 

3\. Uncheck the checkboxes of the regions you want to exclude.

<alert-element type="caution" title="Caution">

To disable regions for your customers, you must also disable the “World” region. Otherwise, the balancer won't work correctly.

</alert-element>

4\. Save changes.  

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/balancer-set.png" alt="Balancer settings" width="80%">