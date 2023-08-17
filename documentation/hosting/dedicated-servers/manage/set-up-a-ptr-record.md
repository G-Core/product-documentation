---
title: set-up-a-ptr-record
displayName: PTR record
published: true
order: 60
toc:
--1--What is a PTR record used for?: "what-is-a-ptr-record-used-for"
--1--Set up on new interface: "set-up-on-new-interface"
--1--Set up on old interface: "set-up-on-old-interface"
pageTitle: Set up a PTR record | Gcore
pageDescription: Learn how to set up a PTR (Pointer) record to map an IP address to a domain name effectively.
---
# Set up a PTR record

A PTR record maps an IP address to a domain name, as opposed to an A record which points a domain name to an IP address.

## What is a PTR record used for?

PTR records are normally used for outbound email servers, since incoming mail servers may not accept a message from an IP address which does not identify itself with a PTR record. A PTR record which matches the domain name from which an email has been received is one of the signals that the email should not be marked as spam.

## Set up on new interface

1. Navigate to the **Dedicated servers** section on the left-side menu.

2. Mark the checkbox next to the server for which you wish to edit PTR records and click on **IP addresses**.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/set-up-a-ptr-record/1-id-ip-address-new.png" alt="">

3. In the newly opened window, mark the checkbox next to the IP for which you wish to edit PTR records and click on **Edit**.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/set-up-a-ptr-record/2-ip-address-edit-new.png" alt="">

4. In the newly opened window, put a domain name into the **Domain** field and click **OK**. The PTR record will be created automatically.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/set-up-a-ptr-record/3-domain-new.png" alt="">

## Set up on old interface

1. Navigate to the **Dedicated servers** section on the left-side menu.

2. Click on the server for which you want to create PTR records, and then click on **IP addresses**.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/set-up-a-ptr-record/4-ip-addressess-old.png" alt="">

3. Choose the IP address for which you want to set or change a PTR record and click on **Edit**.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/set-up-a-ptr-record/5-edit-old.png" alt="">

4. In the newly opened window, put a domain name into the **Domain** field and click **OK**. The PTR record will be created automatically.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/set-up-a-ptr-record/6-domain-old.png" alt="">
