---
title: cdn-service-management
displayName: CDN management
published: true
order: 30
toc:
    --1--General CDN settings: "general-cdn-settings"
    --1--Manage: "manage-general-settings"
    --2--Activate Service: "activate-service"
    --2--Transition to deleted status: "transition-to-deleted-status"
    --1--Features: "free-and-paid-features"
    --1--Traffic: "traffic"
---
# CDN service management

## General CDN settings

To open the general CDN settings of the particular client, go to the client settings:

1\. Go to the <a href="https://admin.gcore.top/clients" target="_blank">Accounts</a> section and open the list of clients.

2\. Click on the ID of the desired client, or click three dots and the **Edit** button.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-10.png" alt="Clients">

The new page will open. 

## Manage general settings

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-20.png" alt="Services" width="80%">

### Activate Service

1\. Go to the "Services" page.

2\. Click **Show more** to open settings. 

3\. Enable the **Activate service** checkbox. If the "Activate Service" checkbox is enabled, a client can use the service: create CDN resources and manage them. You can deactivate the service by unchecking the checkbox. In this case, the client will see a service activation request form on the CDN tab instead of the CDN resources list.

**Note**: Deactivating the "Activate service" checkbox may suspend the work of active resources.

### Transition to deleted status

After the specified number of days, the CDN service status switches from "TrialEnd"/"Paused" to "Deleted". During the switch, the client's resources get deleted. You cannot change the number of days yourself. To change the number of days for a specific client, email us at [support@gcore.com](mailto:support@gcore.com).

Don’t forget to click **Save changes** to apply them.

## Free and paid features

To see the list of available features, click **CDN setting**.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-30.png" alt="Services" width="80%">

You can also go to the client settings through the CDN application

1\. Open the list of clients, in the "СDN" section

2\. Click on the ID of the desired client, or click three dots and **Edit**.

3\. Go to the **Features** tab.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-40-v2.png" alt="Edit client" width="80%">

A free feature includes the "Show Origin, Shield, and CDN Traffic Separately" option. It affects the traffic report in the Control Panel. If disabled (the default setting), it shows the origin, shield, and CDN traffic combined. If enabled, it shows the traffic separately.

Paid features includes <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">Advanced directory, user agents, geo statistics</a>, <a href="https://gcore.com/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage" target="_blank">Raw logs</a>, <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin shielding</a> (to set the locations, contact technical support or your manager), and <a href="https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs" target="_blank">Streaming</a>.

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/cdn-settings-50.png" alt="Paid features" width="80%">

After activation, don’t forget to save changes.

Certain features, such as Resources with Shared Cache Zone, Wildcard Purge, and Image Stack, can only be enabled by contacting the support team at [support@gcore.com](mailto:support@gcore.com). You can learn more about these features by placing your cursor on the question mark.

## Traffic

<img src="https://assets.gcore.pro/docs/reseller-support/cdn-service-management/balancer-tab.png" alt="Balancer tab" width="80%">

CDN servers are grouped into several regions in <a href="https://gcore.com/docs/cdn/cdn-resource-options/determine-in-which-regions-the-content-will-be-delivered-with-geo-balancer-for-paid-tariffs" target="_blank">Geobalancer</a>: North America, Asia, the Middle East, Europe, Australia, the World (with the World anycast address behind this region), the CIS, Latin America, and Africa.

**Note**: To disable one of the regions for the client, you should also disable the "World" region. Otherwise, the balance won't work correctly.