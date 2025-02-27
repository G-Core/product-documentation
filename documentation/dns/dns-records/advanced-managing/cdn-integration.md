---
title: cdn-integration
displayName: CDN integration 
published: true
order: 30
toc:
pageTitle: Configure CDN Integration | Gcore
pageDescription: Learn how to configure dynamic responses, select pickers, and specify metadata with Gcore CDN.
---
# Configure CDN integration

If you use both Gcore DNS and Gcore CDN you can configure A/AAAA DNS record to resolve exactly to our CDN addresses.
CDN integration allows you to avoid CNAME configuration and additional lookup on the end user side.
Gcore DNS will resolve the record to the best possible CDN address.

To configure integration:

1\. Navigate to <a href="https://dns.gcore.com/zones" target="_blank">DNS</a> in the Gcore Customer Portal.

2\. Click the domain name of the DNS zone where you intend to set up CDN integration. 

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-10.png" alt="Open a DNS zone" width="80%">

A new page will open.

<alert-element type="note" title="Note">

The feature is available only for an **A/AAAA** record types.

</alert-element>

3\. Click the three-dot icon.

4\. Click **CDN integration** in the row of the relevant A record. 

<img src="https://assets.gcore.pro/docs/dns/dns-records/advanced-managing/cdn-integration/cdn-integration-10.png" alt="Open a Records list/Edit record set page" width="80%">

5\. In the pop-up window, you'll see the lookup value is predefined for your account. Click **Save changes**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/advanced-managing/cdn-integration/cdn-integration-20.png" alt="Open a Records list/Edit record set page" width="60%">

That's it. Your domain zone will be integrated with Gcore CDN.
