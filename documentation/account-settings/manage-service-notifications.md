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

# Manage service notifications

## Manage notifications

A user who has access to the personal account can configure sending notifications to an email.

<img src="https://assets.gcore.pro/docs/account-settings/notifications/set-notifications-10.png" alt="">

1\. Click on the profile icon in the lower-left corner and select **Profile**.

2\. Go to the Notifications section.

3\. Use toggle switches to configure notifications.

All notifications are divided into groups: general notifications and groups based on the services available to you (for example, CDN, Cloud, Streaming). 

You can disable both a single notification and an entire group.

## Limitation notifications

### How does it work

Limitation notifications are available for CDN and Storage (bucket) services.  

Traffic or another counting starts on the first day of each month.

The traffic volume is checked once an hour at 00 minutes (±3 minutes).

If you set a traffic consumption level that has already been exceeded, then after the next check all the account users will receive a notification. For example, you have already used 2TB of traffic, at 12:21 you turned on the traffic control option and set the traffic consumption level equal to 1TB, at 13:00 all the account users will get the notification.

### Сonfigure for CDN

Each user of the personal account can configure this notification.

To do it, specify the traffic limit in the Traffic consumption level field. Click **Save** to apply the settings.

<img src="https://assets.gcore.pro/docs/account-settings/notifications/set-limit-20.png" alt="" width="80%">

**Note**: Traffic consumption level is _not configured_ individually, it is the same for all users of the account who use this notification.

For example, there are three users in the account: User A, User B, and User C. Suppose, User A is the first to turn on this notification and sets the limit to 100 GB. User B and User C will see that the traffic consumption level has already been set by someone and is equal to 100 GB. User B agrees with the current traffic consumption level and doesn't change anything. User B believes that the traffic consumption level equal to 100 GB should be changed and set it in his personal account to 70 GB. As a result of User B's changes, the other two users will also receive notifications when the traffic consumption level reaches 70 GB.

### Configure for Storage

You can receive notifications about:

- objects,
- requests,
- used space
- traffic consumption.

To do it go to the Storage notification section, select Storage and Bucket (optional) and specify the limit. Then click **Save**.

<img src="https://assets.gcore.pro/docs/account-settings/notifications/storage-notifications-30.png" alt="" width="80%">