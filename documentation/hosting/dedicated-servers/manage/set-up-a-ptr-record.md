---
title: set-up-a-ptr-record
displayName: PTR record
published: true
order: 60
toc:
--1--What is PTR record used for: "what-is-ptr-record-used-for"
--1--How to set it up: "how-to-set-it-up"
pageTitle: Set up a PTR record | Gcore
pageDescription: Learn how to set up a PTR (Pointer) record to map an IP address to a domain name effectively.
---
# Set up a PTR record

A PTR record maps an IP address to a domain name as opposed to an A record which points a domain name to an IP address.

## What is PTR record used for?

Usually, PTR records are used for outbound email servers since incoming mail servers might not even consider accepting a message from an IP address which does not identify itself with a PTR record. If there is a PTR record and it matches the domain name from which an email has been received it is one of the ways not to get an email into the spam folder.

## How to set it up?

Choose a server in the Control Panel and click on IP addresses.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/set-up-a-ptr-record/joxi_screenshot_1529505255384.png" alt="" width="80%">

Choose the IP address for which you want to set or change a PTR record and click on Edit.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/set-up-a-ptr-record/joxi_screenshot_1529505519458__1_.png" alt="" width="80%">

In a new window put a domain name into Domain field. The PTR record will be created automatically.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/set-up-a-ptr-record/joxi_screenshot_1529506438819.png" alt="">