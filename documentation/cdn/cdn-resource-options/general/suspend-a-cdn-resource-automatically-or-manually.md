---
title: suspend-a-cdn-resource-automatically-or-manually
displayName: Suspend a CDN resource
published: true
order: 60
toc:
   --1--Automatic CDN resource suspension: "automatic-cdn-resource-suspension"
   --1--Manual CDN resource suspension: "manual-cdn-resource-suspension"
---
Automatic CDN resource suspension
=================================

If a resource is active, but there has not been traffic in 90 days, it will be automatically suspended by the system.

1\. 7 days before the resources are going to be suspended, all users with the **administrator** and **engineer** roles will receive an email with a list of resources that will be suspended.

In the resource settings you will see the time when it will be stopped:

<img src="https://support.gcore.com/hc/article_attachments/4402974781713/________________________________.png" alt="________________________________.png">

A red sign will be displayed in CDN Resources section next to the resources that are going to be stopped:

<img src="https://support.gcore.com/hc/article_attachments/4402979315345/_______________________.png" alt="_______________________.png">

2\. After the resource suspension, all users with the administrator and engineer roles will receive an email with a list of stopped resources.

**Note!** If you start to deliver traffic via the resource after receiving the first email:

*   The second email about the suspension will not be sent.
*   The resource will not be suspended.

After enabling a resource that was suspended, you will see a message that the CDN resource was suspended because there has not been traffic in 90 days.

If there is still no traffic after enabling the resource, it will be suspended again in 7 days.

To avoid suspension of the resources without traffic, contact our technical support.

Manual CDN resource suspension
==============================

You can suspend a CDN Resource in your personal account. 

Go to the CDN Resources settings and find the Content availability option.  
  
<img src="https://support.gcore.com/hc/article_attachments/4402974828561/_________________________.png" alt="_________________________.png">

Move the slider to the left to disable your CDN Resource. Click Save changes.

<img src="https://support.gcore.com/hc/article_attachments/4402974858385/_______________________.png" alt="_______________________.png">

Move the slider to the right to enable it. Click Save changes. 

<img src="https://support.gcore.com/hc/article_attachments/4402974864273/______________.png" alt="______________.png">

 The settings will be applied within 30-60 seconds.