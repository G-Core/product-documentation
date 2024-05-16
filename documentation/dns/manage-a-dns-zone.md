---
title: manage-a-dns-zone
displayName: Getting started (Create a DNS zone)
published: true
order: 30
toc:
   --1--Create DNS zones: "create-dns-zones"
   --1--Manage DNS zones: "delete-dns-zones"
pageTitle: Getting Started with Managed DNS | Gcore
pageDescription: Easy setup steps for DNS zone creation and management.
---
# Getting started with Managed DNS

To use Managed DNS, you need to create a DNS zone for your domain or subdomain in the Gcore Customer Portal or via API and specify Gcore’s NS servers for your domain. You can then use Gcore's DNS infrastructure features.

## Create DNS zones

1\. Navigate to <a href="https://dns.gcore.com/" target="_blank">DNS</a> in the Gcore Customer Portal and click **Add zone**. 

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-10.png" alt="The All zones page" width="80%">

3\. Enter a domain or subdomain name for the DNS zone and click **Confirm**.

<alert-element type="tip" title="Tip">

You can opt to skip validation and automatic addition of domain DNS records created earlier by checking the “Skip scanning” box. If you choose this option, go to step 5.

</alert-element>

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-20.png" alt="The specify domain page" width="80%">

4\. The new page will display all previously created records; you can edit or delete them. Once everything's correct, click **Confirm**.

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-30.png" alt="The existing DNS records page" width="80%">

5\. Go to the site where you manage your domain records (this may be your DNS provider's interface or other DNS hosting) and change your domain's current NS records to Gcore values: `ns1.gcorelabs.net` and `ns2.gcdn.services`. On the DNS zone creation page, click **Confirm**.

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-40.png" alt="The change nameservers page" width="75%">

That's it! Now, you can add records and manage the DNS zone in the Gcore Customer Portal.

<alert-element type="warning" title="Warning">

Please be aware of the NS records change notification. It may remain active for up to 24 hours after changing nameservers. This duration is necessary in order to update the DNS cache.

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-50.png" alt="The change nameservers notion" width="75%">

</alert-element>

## Manage DNS zones

You can manage a DNS zone in the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> section. In the row of the desired zone, click the three-dot icon and select the required action:

1. **Turn off the zone.** Disable a zone. It will continue to be displayed, but the records added in your Customer Portal will not be active. 
2. **Go to records.** Create, edit, and delete records.
3. **Settings.** Edit the TTL of the records in the zone.
4. **Delete zone.** Delete zones. 

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-60.png" alt="Manage DNS zones" width="80%">
