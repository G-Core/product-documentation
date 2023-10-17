---
title: be-aware-of-the-service-status-scheduled-and-emergency-maintenance
displayName: Status Page
published: true
order: 100
toc:
   --1--Subscription methods: "subscription-methods"
   --2--Email: "email"
   --2--Slack: "slack"
   --3--How to unsubscribe from the old version of Status Page: "how-to-unsubscribe-from-the-old-version-of-status-page"
   --3--Subscribe via Slack: "subscribe-via-slack"
   --2--Webhook: "webhook"
   --1--Subscription management: "subscription-management"
   --2--Email management: "email-management"
   --2--Slack management: "slack-management"
   --2--Webhook management: "webhook-management"
   --2--How to unsubscribe from the subscription: "how-to-unsubscribe-from-the-updates"
   --1--Components: "components"
   --2--Components statuses: "components-statuses"
   --2--Notification types: "notification-types"
pageTitle: Guide to Gcore Status Page Subscriptions | Gcore
pageDescription: A guide on subscribing to and managing notifications about service status, outages, and planned maintenance.
---

# Be aware of the service status, scheduled and emergency maintenance

Status Page is a communication tool that displays information about service status, outages, and planned maintenance. 

## Subscription methods 

To receive notifications about scheduled works and incidents, subscribe to the Status Page: go to <a href="https://status.gcore.com" target="_blank">Status Page of Gcore</a> and click on the **Subscribe to updates** button in the upper-right corner. 

<img src="https://assets.gcore.pro/docs/account-settings/status-page/subscribe-sp-10.png" alt="Subscription methods" width="80%">

Then select the appropriate subscription method (email, slack, webhook). 

### Email 

1\. Enter your email address in the Email Address field and click Subscribe via email.

2\. You will be redirected to the subscription management page. 

3\. Select the components which status information you would like to receive and click the Save button.

<img src="https://assets.gcore.pro/docs/account-settings/status-page/email-sp-20.png" alt="Status Page of Gcore">

4\. Confirm your subscription to get notifications about the status of incidents and scheduled works. To do this, click Confirm subscription in the email sent to the specified email address.  


### Slack

#### How to unsubscribe from the old version of Status Page  

To correctly configure notifications from the new <a href="https://status.gcore.com" target="_blank">Status Page of Gcore</a>, disable the notifications from the old Status Page: 

1\. Open your workspace in Slack. 

2\. On the left side of the workspace, click More, select Apps

<img src="https://assets.gcore.pro/docs/account-settings/status-page/slack-30.png" alt="Click more in Slack">

3\. Enter **Incoming WebHooks** in the search bar.  
  
4\. Click the app to open its settings.

<img src="https://assets.gcore.pro/docs/account-settings/status-page/open-old-app-40.png" alt="Incoming WebHooks">

5\. Go to the Configuration section.  
  
<img src="https://assets.gcore.pro/docs/account-settings/status-page/configuration-50.png" alt="Configuration section." width="80%">

6\. Find the channel for which the notifications are configured. 

7\. Click on the pencil sign to go to the integration settings.

8\. In the upper-right corner, click **Disable** to switch off the integration and Remove to delete the integration.  
  
<img src="https://assets.gcore.pro/docs/account-settings/status-page/remove-integration-60.png" alt="Disable and Remove"  width="80%">

9\. Confirm the action.

10\. Use the next paragraph to integrate this channel with the new Status Page. 

#### Subscribe via Slack

<img src="https://assets.gcore.pro/docs/account-settings/status-page/slack-70.png" alt="Subscribe via Slack">

1\. Click **Subscribe via Slack**.

2\. Enter your Slack workspace URL.

3\. Click Continue.

<img src="https://assets.gcore.pro/docs/account-settings/status-page/slack-continue-80.png" alt="Slack sign in" width="80%">

4\. Log in using your email address and password for the selected workspace in Slack.


5\. Read the channel information that will be provided for Status page. 

**Important**: If you want to use a private channel to send notifications, first add the Status Page app to the channel. To do this, open the channel details and click More > Add Apps.

<img src="https://assets.gcore.pro/docs/account-settings/status-page/private-slack-90.png" alt="Sign in" width="50%">

6\. Enter **Status page** and click on the **Add** button next to the Status page app.  
  
<img src="https://assets.gcore.pro/docs/account-settings/status-page/add-private-100.png" alt="Add apps"  width="50%">

7\. On the page of integration, in the section Where should Status page post specify the channel that will be used to publish notifications. Click Allow.                    

<img src="https://assets.gcore.pro/docs/account-settings/status-page/allow-110.png" alt="Enter Status page"  width="80%">

Next, you will receive a notification from Slack that notifications have been successfully configured, and you will also be automatically redirected to the subscription management page.

Select the components which status information you would like to receive and click the Save button.  

### Webhook 

<img src="https://assets.gcore.pro/docs/account-settings/status-page/webhook-120.png" alt="Permission to access" width="80%">

1\. In the first field, enter the URL for sending notifications. 

2\. In the second field, specify the email address for sending notifications if the above URL is unavailable. 

3\. Click Subscribe. 

4\. You will see a message that webhook notifications have been successfully configured.  

5\. You will also receive a notification email about the configuration to the specified email.  

6\. You can open documentation about how webhooks work by clicking **View documentation**. 

7\. You can manage the subscription by clicking Manage your subscription. Select the components which status information you would like to receive and click the Save button.  

## Subscription management 

### Email management 

You can change the subscription from any notification sent by the system to your email address. 

1\. Open such a notification.

2\. At the bottom of the notification, find and click Manage your subscription.

<img src="https://assets.gcore.pro/docs/account-settings/status-page/manage-130.png" alt="Email management " width="80%">

3\. Edit the component subscription and click **Save**.

### Slack management  

You can change your subscription from any notification sent by the system to Slack. 

1\. Find such notification in Slack.

2\. At the bottom of the notification, find and click Manage your subscription.

3\. Edit the component subscription and click **Save**.

### Webhook management  

You can change your subscription from any notification sent by the system to the URL specified during configuration. 

1\. Open such a notification.

2\. At the bottom of the notification, find and click Manage your subscription.

3\. Edit the component subscription and click **Save**.

### How to unsubscribe from the updates 

1\. To unsubscribe from the notifications, open the management subscription page and click Unsubscribe from the updates. 

2\. Confirm the action. 

## Components 

Components are grouped by services (the Cloud service is grouped by the option+location). 

Each service (or service+location) can also be divided by a geographical or functional basis. 

We use the Updates component (in Releases) to inform you about our releases biweekly. The Website component shows the company website status, and the Knowledge Base informs you about the knowledge base operating. 

### Components statuses  

<img src="https://assets.gcore.pro/docs/account-settings/status-page/components-140.png" alt="Components statuses ">

**Operational**: the component is operating normally. 

**Partial Outage:** the component is partially unavailable. 

**Major Outage:** the component is completely unavailable.  

**Under Maintenance:** the component is in the process of maintenance.  

### Notification types

**Incident | Investigating:** a notification about the component partial or complete outage, the incident is under investigation. 

**Incident | Identified:** the details of the incident have been detected; we are taking steps to resolve it. 

**Incident | Monitoring:** the incident has been resolved, and the component is under monitoring. 

**Incident | Resolved:** the incident has been completely resolved.  

**Incident | Retrospective:** notification of the incident that has already occurred. 

**Maintenance | Scheduled:** notification of upcoming scheduled works. 

**Maintenance | In progress:** scheduled works have been started. 

**Maintenance |Completed:** scheduled works have been completed.
