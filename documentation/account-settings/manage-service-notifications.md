---
title: manage-service-notifications
displayName: Notifications
published: true
order: 70
toc:
   --1--Manage notifications: "manage-notifications"
   --1--Limitation notifications: "limitation-notifications"
   --2--Configure CDN traffic consumption: "configure-cdn-traffic-consumption"
   --2--Configure limits for Object Storage: "configure-limits-for-object-storage"
pageTitle: Guide to managing product notifications | Gcore
pageDescription: Learn how to set up and manage your product notifications for CDN and Storage services, allowing for better control over traffic consumption and system usage.
---
# Manage service notifications and promotional emails

You can customize notification settings for users invited to your account. Important notifications are customized per user, while general notifications are common to all users.

In addition to the product notifications, you might also receive: 

* Technical notifications: We automatically subscribe all users to technical notifications. 

* Promotional emails: If get these notifications if you checked the box to receive promotional emails during the registration process. 

## Manage notifications

To view and configure product notifications and promotional emails:

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to the account settings in the top-right corner of the screen, and click **Profile**.

<img src="https://assets.gcore.pro/docs/account-settings/manage-service-notifications/dashboard-account-menu.png" alt="Profile section in the Customer Portal" width="80%">

2\. Open the **Notifications** page.

<img src="https://assets.gcore.pro/docs/account-settings/manage-service-notifications/notifications-section.png" alt="Notifications page in account settings" width="80%">

3\. Enable or disable relevant toggles to configure notifications and promotional emails. 

All notifications are divided into groups: 

* **Important notifications** about product availability and promotions. Each user in the account has individual settings for important notifications.

* **General notifications** about changes to your products. General notification settings are shared for all account users.

You can choose the settings for either a single notification or an entire group.

<alert-element type="tip" title="Tip">

We recommend keeping the **Service emails** toggle enabled to stay updated on any changes that could affect the performance of your products.
 
</alert-element>

## Limitation notifications

Limitation notifications are available for CDN and Object Storage (bucket) services.  

Traffic or another counting starts on the first day of each month. The traffic volume is checked once an hour at 00 minutes (±3 minutes).

If you set a traffic consumption level that has already been exceeded, then after the next check all the account users will receive a notification. For example, you have already used 2TB of traffic, at 12:21 you turned on the traffic control option and set the traffic consumption level equal to 1TB, at 13:00 all the account users will get the notification.

### Сonfigure CDN traffic consumption

You can configure this notification in the user account settings: 

1\. Specify the traffic limit in the **Traffic consumption level** field.

<img src="https://assets.gcore.pro/docs/account-settings/manage-service-notifications/cdn-notifications.png" alt="CDN traffic consumption level set to 200" width="80%">

2\. Click **Save** to apply the settings. 

<alert-element type="info" title="Info">

Traffic consumption level is not configured individually, it is the same for all users of the account who use this notification. 
 
</alert-element>

For example, there are three users in the account: User A, User B, and User C. 

Suppose that User A is the first to turn on this notification and sets the limit to 100 GB. User B and User C will see that the traffic consumption level has already been set by someone and is equal to 100 GB.  

User B agrees with the current traffic consumption level and doesn't change anything. User C believes that the traffic consumption should be changed to 70 GB. After User C makes the changes, the other two users will also receive notifications when the traffic consumption level reaches 70 GB. 

### Configure limits for Object Storage

You can receive notifications about objects, requests, used space, and traffic consumption.  

To manage the notification settings: 

1\. Navigate to the **Object Storage notifications** section. 

2\. Click **Add limit** button next to the setting you want to modify. 

3\. Enter the required limit. 

4\. Click **Save** to apply the changes. 

To do it go to the **Storage notifications** section, select Storage and Bucket (optional) and specify the limit. Then click **Save**.

<img src="https://assets.gcore.pro/docs/account-settings/manage-service-notifications/storage-notifications.png" alt="Configure notifications for Storage" width="70%">
