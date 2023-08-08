---
title: manage-service-notifications
displayName: Notifications
published: true
order: 70
toc:
   --1--Manage notifications: "manage-notifications"
   --1--Limitation notification: "limitation-notifications"
   --2--How does it work: "how-does-it-work"
   --2--Configure for CDN: "configure-for-cdn"
   --2--Configure for Storage: "configure-for-storage"
pageTitle: Guide to Managing Service Notifications | Gcore
pageDescription: Learn how to set up and manage your service notifications for CDN and Storage services, allowing for better control over traffic consumption and system usage.
---
# Manage service notifications and promotional emails

You have the ability to customize notification settings for users invited to your client account. Important notifications are customized per user, whereas general notifications are common to all users.

## Manage notifications

Here’s how to manage service notifications and promotional emails:

<img src="https://assets.gcore.pro/docs/account-settings/manage-service-notifications/image3.png" alt="">

1\. Click on the profile icon in the lower-left corner.

2\. Select **Profile**.

3\. Go to the Notifications section.

4\. Use toggle switches to configure notifications and/or promotional emails.

<img src="https://assets.gcore.pro/docs/account-settings/manage-service-notifications/image1.png" alt="">

All notifications are divided into groups: 

1. **Important notifications** about service availability and promotions. Each user with access to the client account has individual settings for important notifications.
2. **General notifications** about changes to your services. General notification settings are shared for all account users.

<img src="https://assets.gcore.pro/docs/account-settings/manage-service-notifications/image4.png" alt="">

You can choose the settings for either a single notification or an entire group.

**Note**: We advise that you leave *Service emails* turned on, in order to stay up-to-date about any changes that could affect your services’ performance.

## Limitation notifications

### How does it work

Limitation notifications are available for CDN and Storage (bucket) services.  

Traffic or another counting starts on the first day of each month.

The traffic volume is checked once an hour at 00 minutes (±3 minutes).

If you set a traffic consumption level that has already been exceeded, then after the next check all the account users will receive a notification. For example, you have already used 2TB of traffic, at 12:21 you turned on the traffic control option and set the traffic consumption level equal to 1TB, at 13:00 all the account users will get the notification.

### Сonfigure for CDN

Each user of the personal account can configure this notification.

To do it, specify the traffic limit in the Traffic consumption level field. Click **Save** to apply the settings.

<img src="https://assets.gcore.pro/docs/account-settings/manage-service-notifications/set-limit-20.png" alt="" width="50%">

**Note**: Traffic consumption level is _not configured_ individually, it is the same for all users of the account who use this notification.

For example, there are three users in the account: User A, User B, and User C. Suppose, User A is the first to turn on this notification and sets the limit to 100 GB. User B and User C will see that the traffic consumption level has already been set by someone and is equal to 100 GB. User B agrees with the current traffic consumption level and doesn't change anything. User B believes that the traffic consumption level equal to 100 GB should be changed and set it in his personal account to 70 GB. As a result of User B's changes, the other two users will also receive notifications when the traffic consumption level reaches 70 GB.

### Configure for Storage

You can receive notifications about:

- objects,
- requests,
- used space
- traffic consumption.

To do it go to the Storage notification section, select Storage and Bucket (optional) and specify the limit. Then click **Save**.

<img src="https://assets.gcore.pro/docs/account-settings/manage-service-notifications/storage-notifications-30.png" alt="" width="70%">

<expandable-element title="Why am I subscribed to certain notifications?">
Technical notifications: We automatically subscribe all users to technical notifications.

Promotional emails: You checked the box to receive promotional emails during the registration process.
 
</expandable-element>