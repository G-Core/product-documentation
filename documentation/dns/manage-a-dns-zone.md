---
title: manage-a-dns-zone
displayName: Zone
published: true
order: 20
toc:
   --1--What is a DNS zone?: "what-is-a-dns-zone"
   --1--Manage a DNS zone: "manage-a-dns-zone"
   --2--Create: "create-a-dns-zone"
   --2--Edit: "edit-a-dns-zone"
   --2--Export in BIND: "export-a-dns-zone-in-bind-format"
   --2--Delete: "delete-a-dns-zone"
pageTitle: A DNS zone creation | Gcore
pageDescription: Step-by-step instructions on how to create a DNS zone and delegate it to Gcore NS servers.
---
# Manage a DNS zone

## What is a DNS zone

The DNS zone is the domain you delegate to Gcore authoritative NS servers. The following values can be used as the DNS zone: 

- a second-level domain (*testdomain.com*),
- a third-level domain (*store.testdomain.com*, *blog.testdomain.com*, etc.),
- or a higher-level domain (*sales.store.testdomain.com*).

When the DNS zone creation is completed, you can set the DNS records of your domain in <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode" target="_blank">non-advanced</a> and <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing" target="_blank">advanced</a> modes.

## Manage a DNS zone

### Create a DNS zone

1\. Go to the <a href="https://dns.gcore.com" target="_blank">DNS</a> section and click the **Add zone** button. 

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/13137090774673.png" alt="All zones">

2\. Enter a domain name for the DNS zone and click **Confirm**.

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/13137238972689.png" alt="Enter domain" width="80%">

3\. Review existing DNS records, and edit, delete, or add new records if necessary. Click **Confirm**. 

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/13137695150865.png" alt="Review records" width="80%">

4\. Go to your domain registrar account, replace the current name servers with the Gcore name servers (*ns1.gcorelabs.net* and *ns2.gcdn.services*), and click **Confirm**.

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/13138477756689.png" alt="Change nameservers" width="80%">

The created DNS zone will be displayed in the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> section. 

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/13138576729105.png" alt="The created DNS zone in the all zones" width="80%">

### Edit a DNS zone

1\. In the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> section, click the three dots icon next to the desired DNS zone and select **Settings**.

<img style="font-size: large;" src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/13138699078673.png" alt="Edit a DNS zone" width="80%">

The pop-up opens. Configure it according to the guide below and click **Save changes**. Configurations will be applied to the <a href="https://en.wikipedia.org/wiki/SOA_record#:~:text=A%20start%20of%20authority%20record,is%20specified%20in%20RFC%201035" target="_blank">SOA record</a> of this zone. 

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/13138956496401.png" alt="Zone settings" width="50%">

- **Domain name**. This parameter cannot be edited. Create a new zone with the required domain name following the <a href="https://gcore.com/docs/dns/manage-a-dns-zone#create-a-dns-zone" target="_blank">instructions above</a>.
- **Negative TTL**. This parameter is the time, in seconds, for which a negative response is cached. For example, a recursive DNS server requests an A-record for your domain, but that record does not exist on the authoritative NS servers. Even if you add the A record after, the DNS servers will still return a negative answer for the time specified in the "Negative TTL" field. 
- **Primary DNS (available only for Enterprise tariff)**. In this parameter, you can specify the primary NS server that contains the information about all domain records.
- **Contact (available starting from the Pro tariff).** In this parameter, you can specify the administrator's email address responsible for managing the DNS zone. 

### Export a DNS zone in BIND format

Gcore DNS API supports the BIND zone format for the DNS zone configuration. To export a zone in BIND:

1\. Go to <a href="https://dns.gcore.com/zones" target="_blank">All zones</a>, click three dots, and choose **Go to records** to open the records of the needed zone. 

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/export-bind-10.png" alt="export a zone in bind first step" width="80%">

2\. Click **Export records** to download the file.  

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/export-bind-20.png" alt="export a zone in bind second step" width="80%">

The file will be downloaded to your PC as a text file with the *.zone* extension, e.g., *test.dnsexample.com.zone*.

The downloaded file will contain information about the zone, including the domain name, TTL, RRset, time intervals (refresh, update, and expiry), and the authoritative NS server. For example:

```
$ORIGIN test.dnsexample.com.
$TTL 300
@ IN SOA ns1.gcorelabs.net. support.gcore.com. (
  1690969313 ; serial number
  5400 ; refresh
  3600 ; update retry
  1209600 ; expiry
  300 ; minimum
)
$TTL 3600
@ IN NS ns1.gcorelabs.net.
@ IN NS ns2.gcdn.services.
$TTL 600
@ IN A 1.2.3.4
@ IN A 4.5.6.7
* IN CNAME sample.domains.com.
* IN CNAME sample-2.domains.com.
```

### Delete a DNS zone 

1\. In the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> section, click the three dots icon next to the desired DNS zone and select **Delete zone**.

<img src="https://assets.gcore.pro/docs/dns/manage-a-dns-zone/13141470744849.png" alt="Delete a DNS zone" width="80%">

2\. Confirm the deletion in the pop-up window.