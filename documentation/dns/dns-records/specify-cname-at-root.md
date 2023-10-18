---
title: specify-cname-at-root
displayName: Set up CNAME flattening
published: true
order: 30
toc:
   --1--What is CNAME: "what-is-a-cname-record"
   --1--What is the challenge with it: "what-is-the-challenge-with-cname-records"
   --1--How CNAME Flattening works: "how-does-cname-flattening-work"
   --1--Configuration: "configuration-of-cname-flattening"
pageTitle: Guide to CNAME Flattening at Root Domain | Gcore
pageDescription: Explore how CNAME Flattening can bypass these restrictions for improved DNS resolution and performance.
---

# Specify CNAME at root

## What is a CNAME record?

A CNAME record, also known as a Canonical Name record, is a type of DNS record that associates an alias name with the actual or canonical domain name. Typically, CNAME records were used to map a subdomain such as www (e.g., *www.example.com*) to the domain that hosts the subdomain's content (*example.com*).

Nowadays CNAME records are increasingly used to integrate domains with third-party solutions such as CDNs. This is because using an A record, which specifies the concrete IP address that resolves the domain, may not be suitable in cases where the IP addresses change frequently based on the geolocation of requests.

## What is the challenge with CNAME records?

According to the RFC 1034 specification, a CNAME record cannot coexist with other records. Therefore, it is impossible to specify a CNAME record for the root domain, also known as the "apex domain" (e.g., *example.com*), because it has mandatory NS and SOA records.

While using a subdomain (e.g., *cdn.example.com*) for CNAME record creation can be sufficient, some website owners may want to integrate their root domain. For this situation, Gcore DNS provides the CNAME Flattening feature.

## How does CNAME Flattening work?

CNAME Flattening is a mechanism that allows specification restrictions to be bypassed and a CNAME to be specified for the root domain. It resolves the CNAME chain and uses the IP address of the final A or AAAA record. This synthetic record is then cached, respecting its TTL, and used to answer subsequent DNS queries for the apex domain on the Gcore DNS side.

By using CNAME Flattening, we avoid specification violations and ensure proper DNS resolution in more cases. Due to the local cache layer, the total resolution time may significantly decrease, which improves performance.

## Configuration of CNAME Flattening

Gcore DNS provides CNAME Flattening to customers on all plans by default. To use this feature, you must:

1\. Remove the A record for the root domain before creating the CNAME record.

2\. Ensure that there is only one CNAME record to ensure that flattening works as expected.

You can check the CNAME record's value using the <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> tool.