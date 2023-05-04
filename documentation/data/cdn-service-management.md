---
title: cdn-service-management
displayName: CDN service management
published: true
toc:
   --1--Open CDN settings: "open-cdn-settings"
   --1--Settings sections: "settings-sections"
   --2--General: "general-cdn-settings"
   --3--Activation settings: "activate-service"
   --3--Trial settings: "trial-settings"
   --3--Transition to Deleted status: "transition-to-deleted-status"
   --2--Features: "features"
   --3--Paid: "paid-features"
   --3--Free: "free-features"
   --2--Traffic: "traffic"
---

# CDN service management

Open CDN Settings
-----------------

To open the CDN settings of the particular client, go to the "Clients" section in the admin panel and click the wrench icon on the right in the row of the client for whom you want to set up the CDN.

<img src="https://reseller.support.gcore.com/hc/article_attachments/12763930468497" alt="mceclip0.png">

A new page will open. Go to the "CDN" tab.

Settings sections
-----------------

There are three sections in the CDN:

*   **General** — service activation, status, and trial settings.
*   **Features** — additional options activation.
*   **Traffic** — settings for traffic geo balancing.

<img src="https://reseller.support.gcore.com/hc/article_attachments/12763980917905" alt="mceclip1.png">

### General CDN settings

#### **Activate Service**

<img src="https://reseller.support.gcore.com/hc/article_attachments/12763992814993" alt="mceclip2.png">

If the "Activate Service" checkbox is enabled, a client can use the service: to create CDN resources and manage them. You can deactivate the service by unchecking the checkbox. In this case, the client will see a service activation request form on the CDN tab instead of the CDN resources list.

**Note:** Keep in mind that deactivating the service does not automatically stop the CDN resources. If you want to suspend them, use the "TrialEnd" or "Paused" statuses.

#### **Trial Settings**

**<img src="https://reseller.support.gcore.com/hc/article_attachments/12764114983953" alt="mceclip3.png">**

This tab is used to change trial settings. By default, the trial lasts 14 days, but it may end sooner if the client exceeds the traffic limit of 300 GB. You can change the trial settings (traffic volume and days limit) at any time.

The End Day field defines when the "Trial" status will be changed to the "TrialEnd" status. To change the trial end day, enable the switch opposite the **End Day** field. Don’t forget to click **Save trial settings** to apply the changes.

After changing the trial settings, the new amount of days and/or remaining traffic will be displayed in the client's control panel.

When the trial ends, the client's resources will be stopped, and the CDN service status will be switched to "TrialEnd". If your client wants to continue using the service, manually switch it to the "Active" status.

#### **Transition to Deleted status**

**After the specified number of days, the CDN service status switches from "TrialEnd"/"Paused" to "Deleted". During the switch, the client's resources get deleted. You cannot change the number of days yourself. To change the number of days for a specific client, email us at [support@gcore.com](mailto:support@gcore.com).**

### Features

#### **Paid features**

<img src="https://reseller.support.gcore.com/hc/article_attachments/12764215632273" alt="mceclip4.png">

You can activate additional paid services for the client, including an [Advanced directory, user agents, geo statistics](https://www.gcore.com/support/articles/115004917425/), [Raw logs](https://www.gcore.com/support/articles/115000511685/), [Origin shielding](https://www.gcore.com/support/articles/214080309/) (to set the locations, contact technical support or your manager), and [Streaming](https://www.gcore.com/support/articles/115002080125/).

Don’t forget to save changes at the bottom of the page.

Certain features, such as Resources with Shared Cache Zone, Wildcard Purge, and Image Stack, can only be enabled by contacting the Support Team at [support@gcore.com](support@gcore.com). You can learn more about these features by placing your cursor on the question mark.

#### **Free features**

**<img src="https://reseller.support.gcore.com/hc/article_attachments/12764221754513" alt="mceclip5.png">**

Enabling the "gcdn.co zone (CNAME)" option allows clients to create subdomains for CDN delivery in our zone and use our shared SSL certificate. This is a non-public feature, so please contact the support team ([support@gcore.com](support@gcore.com)) to discuss its availability.

The "Show Origin, Shield, and CDN Traffic Separately" option affects the traffic report in the Control Panel. If disabled (the default setting), it shows the origin, shield, and CDN traffic combined. If enabled, it shows the traffic separately.

### Traffic

<img src="https://reseller.support.gcore.com/hc/article_attachments/12764368565777" alt="mceclip6.png">

CDN servers are grouped into several regions in [Balancer:](https://www.gcore.com/support/articles/360000194885/) North America, Asia, the Middle East, Europe, Australia, the World (with the World anycast address behind this region), the CIS, Latin America, and Africa.

**Note**: To disable one of the regions for the client, you should also disable the "World" region. Otherwise, the balance won't work correctly.