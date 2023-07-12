---
title: cdn-service-management
displayName: CDN management
published: true
order: 30
toc:
    --1--General CDN settings: "general-cdn-settings"
    --2--Activate Service: "activate-service"
    --2--Service statuses: "service-statuses"
    --2--Trial Settings: "trial-settings"
    --2--Transition to Deleted status: "transition-to-deleted-status"
    --1--Features: "features"
    --2--Paid features: "paid-features"
    --2--Free features: "free-features"
    --1--Traffic: "traffic"
---
# CDN service management

## General CDN settings

To open the general CDN settings of the particular client, go to the client settings:

1\. Open the list of clients, in the "Accounts" section.

2\. Click on the ID of the desired client, or click on the "Edit" button in the "Actions" сolumn.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-page-10.png" alt="">

3\. Click on the "Services" tab.

### Activate Service

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/activate-cdn-20.png" alt="" width="80%">

If the "Activate Service" checkbox is enabled, a client can use the service: to create CDN resources and manage them. You can deactivate the service by unchecking the checkbox. In this case, the client will see a service activation request form on the CDN tab instead of the CDN resources list.

**Note**: Keep in mind that deactivating the "Activate service" checkbox may suspend the work of active resources.

### Service statuses 

You can configure a service status for a client.

### Trial Settings

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/trial-settings-30.png" alt="" width="50%">

This tab is used to change trial settings. By default, the trial lasts 14 days, but it may end sooner if the client exceeds the traffic limit of 300 GB. You can change the trial settings (traffic volume and days limit) at any time.

The End Day field defines when the "Trial" status will be changed to the "TrialEnd" status. To change the trial end day, enable the switch opposite the **End Day** field. Don’t forget to click **Save trial settings** to apply the changes.

After changing the trial settings, the new amount of days and/or remaining traffic will be displayed in the client's control panel.

When the trial ends, the client's resources will be stopped, and the CDN service status will be switched to "TrialEnd". If your client wants to continue using the service, manually switch it to the "Active" status.

### Transition to Deleted status

After the specified number of days, the CDN service status switches from "Trialend"/"Paused" to "Deleted". During the switch, the client's resources get deleted. You cannot change the number of days yourself. To change the number of days for a specific client, email us at [support@gcore.com](mailto:support@gcore.com).

## Features

To see the list of available features, click on the "CDN setting" button on the "Services" tab.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-40.png" alt="" width="50%">

You can also go to the client settings through the CDN application

1\. Open the list of clients, in the "СDN" section

2\. Click on the ID of the desired client, or click on the "Edit" button in the "Actions" сolumn.

### Paid features

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/paid-features-50-v2.png" alt="" width="80%">

You can activate additional paid services for the client, including an <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">Advanced directory, user agents, geo statistics</a>, <a href="https://gcore.com/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage" target="_blank">Raw logs</a>, <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin shielding</a> (to set the locations, contact technical support or your manager), and <a href="https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs" target="_blank">Streaming</a>.

Don’t forget to save changes at the bottom of the page.

Certain features, such as Resources with Shared Cache Zone, Wildcard Purge, and Image Stack, can only be enabled by contacting the support team at [support@gcore.com](mailto:support@gcore.com). You can learn more about these features by placing your cursor on the question mark.

### Free features

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/free-features-60-v2.png" alt="" width="80%">

Enabling the "gcdn.co zone (CNAME)" option allows clients to create subdomains for CDN delivery in our zone and use our shared SSL certificate. This is a non-public feature, so please contact the [support team](mailto:support@gcore.com) to discuss its availability.

The "Show Origin, Shield, and CDN Traffic Separately" option affects the traffic report in the Control Panel. If disabled (the default setting), it shows the origin, shield, and CDN traffic combined. If enabled, it shows the traffic separately.

## Traffic

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/balancer-70-v2.png" alt="" width="80%">

CDN servers are grouped into several regions in <a href="https://gcore.com/docs/cdn/cdn-resource-options/determine-in-which-regions-the-content-will-be-delivered-with-geo-balancer-for-paid-tariffs" target="_blank">Geo Balancer</a>: North America, Asia, the Middle East, Europe, Australia, the World (with the World anycast address behind this region), the CIS, Latin America, and Africa.

Note: To disable one of the regions for the client, you should also disable the "World" region. Otherwise, the balance won't work correctly.