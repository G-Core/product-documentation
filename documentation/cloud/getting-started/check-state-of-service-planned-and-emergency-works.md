---
title: check-state-of-service-planned-and-emergency-works
displayName: Check the health service, planned and emergency works
published: true
order: 50
toc:
   --1--Subscription methods: "subscription-methods"
   --2--Email: "email"
   --2--Slack: "slack"
   --1--How to unsubscribe from the old version of Status Page: "how-to-unsubscribe-from-the-old-version-of-status-page"
   --1--Subscribe via Slack: "subscribe-via-slack"
   --2--Webhook: "webhook"
   --1--Subscription management: "subscription-management"
   --2--Email management: "email-management"
   --2--Slack management: "slack-management"
   --2--Webhook management: "webhook-management"
   --1--How to unsubscribe from the subscription: "how-to-unsubscribe-from-the-updates"
   --1--Components: "components"
   --2--Components statuses: "components-statuses"
   --1--Notification types: "notification-types"
---
_**Note!** Information on the status of services in the period up to 15th February 2021_  _is published on the [https://historystatus.gcore.com/](https://historystatus.gcorelabs.com/)_

**_Status Page_** is a communication tool that displays information about service status, outages, and planned maintenance. 

  
  
  
•  
•  
  
  
  
  
  
  
  
  

### **Subscription methods** 

To receive notifications about scheduled works and incidents, subscribe to the Status Page: go to [https://statuspage.gcore.com](https://statuspage.gcorelabs.com) and click on the Subscribe to updates button in the upper-right corner. 

<img src="https://support.gcore.com/hc/article_attachments/360015963318/subscribe_to.png" alt="subscribe_to.png">Then select the appropriate subscription method (email, slack, webhook). 

#### **Email** 

1.  Enter your email address in the Email Address field and click Subscribe via email.
2.  You will be redirected to the subscription management page. 
3.  Select the components which status information you would like to receive and click the Save button.  
      
    <img src="https://support.gcore.com/hc/article_attachments/360015892637/_________email.png" alt="_________email.png">
4.  Confirm your subscription to get notifications about the status of incidents and scheduled works. To do this, click Confirm subscription in the email sent to the specified email address. <img src="https://support.gcore.com/hc/article_attachments/360015963638/_____________________email_________.png" alt="_____________________email_________.png">

#### **Slack** 

### How to unsubscribe from the old version of Status Page  

To correctly configure notifications from the new Status Page ([https://statuspage.gcore.com/](https://statuspage.gcorelabs.com/)), disable the notifications from the old Status Page: 

1\. Open your workspace in Slack. 

2\. On the left side of the workspace, click More, select Apps

<img src="https://support.gcore.com/hc/article_attachments/360016157957/more___apps.png" alt="more___apps.png" width="247" height="305">

3\. Enter Incoming WebHooks in the search bar.  
  
<img src="https://support.gcore.com/hc/article_attachments/360016157977/incoming.png" alt="incoming.png">

4\. Click the app to open its settings.

<img src="https://support.gcore.com/hc/article_attachments/360016157997/incoming_web_hooks.png" alt="incoming_web_hooks.png">

5\. Go to the Configuration section.  
  
<img src="https://support.gcore.com/hc/article_attachments/360016158037/configuration.png" alt="configuration.png">6\. Find the channel for which the notifications are configured. 

7\. Click on the pencil sign to go to the integration settings.  
  <img src="https://support.gcore.com/hc/article_attachments/360016227638/_____.png" alt="_____.png">

8\. In the upper-right corner, click Disable to switch off the integration and Remove to delete the integration.  
  
<img src="https://support.gcore.com/hc/article_attachments/360016158117/__________________.png" alt="__________________.png">9\. Confirm the action.

<img src="https://support.gcore.com/hc/article_attachments/360016158137/____________________.png" alt="____________________.png">

10\. Use the next paragraph to integrate this channel with the new Status Page. 

### Subscribe via Slack

<img src="https://support.gcore.com/hc/article_attachments/360015892657/slack_________.png" alt="slack_________.png">

1.  Click Subscribe via Slack.
2.  Enter your Slack workspace URL.
3.  Click Continue.

<img src="https://support.gcore.com/hc/article_attachments/360015963678/slack__________2.png" alt="slack__________2.png">

4.  Log in using your email address and password for the selected workspace in Slack.

<img src="https://support.gcore.com/hc/article_attachments/360015963698/slack__________3.png" alt="slack__________3.png">

5.  Read the channel information that will be provided for Status page. 

**Important!** If you want to use a private channel to send notifications, first add the Status Page app to the channel. To do this, open the channel details and click More -> Add Apps.

<img src="https://support.gcore.com/hc/article_attachments/360016252998/add_apps.png" alt="add_apps.png" width="376" height="396">

Enter Status page and click on the Add button next to the Status page app.

<img src="https://support.gcore.com/hc/article_attachments/360016186617/add_statuspage.png" alt="add_statuspage.png" width="450" height="201">

6.  On the page of integration, in the section Where should Status page post specify the channel that will be used to publish notifications. Click Allow.<img src="https://support.gcore.com/hc/article_attachments/360015892677/slack__________4.png" alt="slack__________4.png" width="399" height="484">  
    
7.  Next, you will receive a notification from Slack that notifications have been successfully configured, and you will also be automatically redirected to the subscription management page.

Select the components which status information you would like to receive and click the Save button.  

<img src="https://support.gcore.com/hc/article_attachments/360015892737/slack__________5.png" alt="slack__________5.png">

#### **Webhook** 

<img src="https://support.gcore.com/hc/article_attachments/360015892757/webhook__________1.png" alt="webhook__________1.png">

1\. In the first field, enter the URL for sending notifications. 

2\. In the second field, specify the email address for sending notifications if the above URL is unavailable. 

3\. Click Subscribe. 

4\. You will see a message that webhook notifications have been successfully configured.  
  
<img src="https://support.gcore.com/hc/article_attachments/360015963718/webhook__________2.png" alt="webhook__________2.png">5\. You will also receive a notification email about the configuration to the specified email.  
  
<img src="https://support.gcore.com/hc/article_attachments/360015963738/webhook__________3.png" alt="webhook__________3.png">6\. You can open documentation about how webhook works by clicking View documentation. 

7\. You can manage the subscription by clicking Manage your subscription. Select the components which status information you would like to receive and click the Save button. 

<img src="https://support.gcore.com/hc/article_attachments/360015963778/webhook_manage__________.png" alt="webhook_manage__________.png">  

### **Subscription management**  

How to change the subscription components 

#### **Email management** 

You can change the subscription from any notification sent by the system to your email address. 

1.  Open such a notification.
2.  At the bottom of the notification, find and click Manage your subscription.

<img src="https://support.gcore.com/hc/article_attachments/360015892817/emai_manage__________.png" alt="emai_manage__________.png">

3.  Edit the component subscription and click Save.

 <img src="https://support.gcore.com/hc/article_attachments/360015963858/email_manage_2.png" alt="email_manage_2.png">

#### **Slack management**

You can change your subscription from any notification sent by the system to Slack. 

1.  Find such notification in Slack.
2.  At the bottom of the notification, find and click Manage your subscription.

<img src="https://support.gcore.com/hc/article_attachments/360015892837/slack_manage_1.png" alt="slack_manage_1.png">

3.  Edit the component subscription and click Save.

  <img src="https://support.gcore.com/hc/article_attachments/360015963878/slack_manage_2.png" alt="slack_manage_2.png">

#### **Webhook management**  

You can change your subscription from any notification sent by the system to the URL specified during configuration.

1.  Open such a notification.
2.  At the bottom of the notification, find and click Manage your subscription.
3.  Edit the component subscription and click Save.

<img src="https://support.gcore.com/hc/article_attachments/360015892877/webhook_manage__________.png" alt="webhook_manage__________.png">

### How to unsubscribe from the updates 

To unsubscribe from the notifications, open the management subscription page and click Unsubscribe from the updates. 

<img src="https://support.gcore.com/hc/article_attachments/360015892917/___________email_1.png" alt="___________email_1.png">

Confirm the action. 

<img src="https://support.gcore.com/hc/article_attachments/360015963918/___________2.png" alt="___________2.png"> 

### **Components**

Components are grouped by services (the Cloud service is grouped by the option+location). 

Each service (or service+location) can also be divided by a geographical or functional basis. 

We use the Updates component (in Releases) to inform you about our releases biweekly. The Website component shows the company website status, and the Knowledge Base informs you about the knowledge base operating. 

#### **Components statuses**  

<img src="https://support.gcore.com/hc/article_attachments/360015963958/__________.png" alt="__________.png">

**Op****erational**: the component is operating normally. 

**Partial Outage:** the component is partially unavailable. 

**Major Outage:** the component is completely unavailable.  

**Under Maintenance:** the component is in the process of maintenance.  

### **Notification types** 

**Incident | Investigating:** a notification about the component partial or complete outage, the incident is under investigation. 

**Incident | Identified:** the details of the incident have been detected; we are taking steps to resolve it. 

**Incident | Monitoring:** the incident has been resolved, and the component is under monitoring. 

**Incident | Resolved:** the incident has been completely resolved.  

**Incident | Ret****rospective:** notification of the incident that has already occurred. 

**Maintenance | Scheduled:** notification of upcoming scheduled works. 

**Maintenance | In progress:** scheduled works have been started. 

**Maintenance |Completed:** scheduled works have been completed.
