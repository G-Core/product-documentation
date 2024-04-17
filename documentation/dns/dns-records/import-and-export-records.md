---
title: import-and-export-records
displayName: Import and export
published: true
order: 20
toc:
   --1--Export: "export"
   --1--Import: "import"
pageTitle: How to Import and Export Records | Gcore
pageDescription: Learn how to import and export DNS records in the non-advanced interface mode.
---
# Import and export records

Use import and export to gain more control over DNS records and make domain migration easier.

1\. Navigate the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> tab and select the domain zone into which you want to import the records.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-10.png" alt="All zones" width="70%">

2\. Click **Export records** or **Import records** depending on your task and follow the appropriate instructions. 

<img src="https://assets.gcore.pro/docs/dns/dns-records/import-and-export-records/import-export-10.png" alt="Import or export records" width="80%">

<tabset-element>

## Export

After clicking **Export records**, the BIND zone file will be downloaded to your PC as a text file with the .zone extension, e.g., `sample-test.com.zone`.

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

## Import

After clicking **Import records**, the new pop-up appear. Specify the content of the BIND zone file for your domain or click **Upload zone file** to import records from the file with the .zone extension. Then click **Import**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/import-and-export-records/import-export-20.png" alt="Import records" width="80%">

</tabset-element>