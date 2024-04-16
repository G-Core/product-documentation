---
title: manage-a-dns-zone
displayName: Getting started (Create a DNS zone)
published: true
order: 30
toc:
   --1--Create DNS zones: "create-dns-zones"
   --1--Manage DNS zones: "delete-dns-zones"
pageTitle: Getting started with Managed DNS | Gcore
pageDescription: Easy setup steps for DNS zones creation and management.
---
# Getting started with Managed DNS

To use Managed DNS, create a DNS zone for your domain or subdomain in the Gcore Customer Portal or via API and specify Gcore’s NS servers for your domain. After these actions, you can use Gcore's DNS infrastructure features.

## Create DNS zones

1\. Navigate to the <a href="https://dns.gcore.com/" target="_blank">DNS</a> section and click **Add zone**. 

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-10.png" alt="The All zones page" width="80%">

3\. Enter a domain or subdomain name for the DNS zone and click **Confirm**.

<alert-element type="tip" title="Tip">

You can optionally check the “Scip scanning” box to skip validation and automatic addition of domain DNS records created earlier. In this case, only step 5 (change the name servers of your domain) of this guide is left for you. 

</alert-element>

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-20.png" alt="The specify domain page" width="80%">

4\. The new page will display all previously created records, you can edit or delete them. Check and click **Confirm**.

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-30.png" alt="The existing DNS records page" width="80%">

5\. Go to the site where you manage your domain records (this can be your DNS provider's interface or other DNS hosting) and change your domain's current NS records to Gcore values (`ns1.gcorelabs.net` and `ns2.gcdn.services`). On the DNS zone creation page, click **Confirm**.

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-40.png" alt="The change nameservers page" width="75%">

That's it! Now you can add records and manage the zone in the Gcore interface.

<alert-element type="warning" title="Warning">

Pay attention to the NS records change notification. It can be kept for up to 24 hours after after changing nameservers. This is the time required to update the DNS cache.

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-50.png" alt="The change nameservers notion" width="75%">

</alert-element>

## Manage DNS zones

You can manage a zone in the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> section. In the row of the desired zone, tap the three dots icon and select the appropriate action:

1. **Turn off the zone.** Here you can disable a zone. It will continue to be displayed, but the records added in your Customer Portal will not be active. 
2. **Go to records.** Here you can go to creating, editing and deleting records.
3. **Settings.** Here you can edit the TTL of the records in the zone.
4. **Delete zone.** Here you can delete a zone. 

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/getting-started-dns-60.png" alt="Manage DNS zones" width="80%">