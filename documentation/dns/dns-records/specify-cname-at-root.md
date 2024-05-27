---
title: specify-cname-at-root
displayName: CNAME flattening
published: true
order: 30
toc:
   --1--Challenge: "what-is-the-challenge-with-the-creation-of-records-in-the-root-zone-zone-apex"
   --1--How CNAME flattening works: "how-does-cname-flattening-work"
   --1--Configuration: "configuration-of-cname-flattening"
pageTitle: How to Create Records in Zone Apex (CNAME Flattening) | Gcore
pageDescription: Explore how CNAME flattening can bypass these restrictions for improved DNS resolution and performance.
---
# Create records in zone apex (CNAME flattening) 

## What is the challenge with the creation of records in the root zone (zone apex)?

<a href="https://gcore.com/docs/dns/dns-records/supported-dns-record-types#cname-record" target="_blank">CNAME records</a> are increasingly used to integrate domains with third-party solutions such as CDNs. Using an A record, which specifies the concrete IP address that resolves the domain, may not be suitable in cases where IP addresses change frequently based on the geolocation of requests.

According to the RFC 1034 specification, a CNAME record cannot coexist with other records. Therefore, it is impossible to specify a CNAME record for the root domain, also known as the "apex domain" (e.g., sample-test.com), because it has mandatory NS and SOA records.

While using a subdomain (e.g., cdn.sample-test.com) for CNAME record creation can be sufficient, some website owners may want to integrate their root domain. For this situation, Gcore Managed DNS provides the CNAME flattening feature.

## How does CNAME flattening work?

CNAME flattening is a mechanism that allows specification restrictions to be bypassed, enabling a CNAME to be specified for the root domain. It resolves the CNAME chain and uses the IP address of the final A or AAAA record. This synthetic record is then cached, respecting its TTL, and used to answer subsequent DNS queries for the apex domain on the Gcore DNS side.

By using CNAME flattening, we avoid specification violations and ensure proper DNS resolution in more cases. Due to the local cache layer, the total resolution time may significantly decrease, improving performance.

## Configuration of CNAME flattening

Gcore Managed DNS provides CNAME flattening to customers on all plans by default. To use this feature, you must:

1\. Remove the A record for the root domain before creating the CNAME record.

<img src="https://assets.gcore.pro/docs/dns/dns-records/specify-cname-at-root/records-in-the-apex-root.png" alt="Delete an A record" width="85%">

2\. Ensure that there is only one CNAME record to ensure that flattening works as expected.

<img src="https://assets.gcore.pro/docs/dns/dns-records/specify-cname-at-root/cname-flattening.png" alt="Ada a CNAME record to apex zone" width="85%">

You can check the CNAME record's value using the <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> tool.
