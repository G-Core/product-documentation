---
title: about-gcore-dns
displayName: Overview
published: true
order: 10
toc:
   --1--Overview: "gcore-dns-overview"
   --1--Interface mode comparison: "interface-modes-non-advanced-and-advanced"
pageTitle: Understanding DNS Hosting | Gcore 
pageDescription: Learn how to manage your domain zone with Gcore DNS and what are two interface modes.
---

# About Gcore DNS

## Gcore DNS overview

The DNS service allows you to create, update, and delete DNS records for your domain. To manage your domain configuration, follow these steps:

1\. <a href="https://gcore.com/docs/dns/manage-a-dns-zone" target="_blank">Create a domain zone in your account</a>.  

2\. Specify Gcore name servers (*ns1.gcorelabs.net* and *ns2.gcdn.services*) in the domain settings on the registrar's website.  

3\. Configure DNS records in <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode" target="_blank">non-advanced</a> or <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing" target="_blank">advanced mode</a>. 

## Interface modes: non-advanced and advanced

The DNS service interface offers two modes: non-advanced (for basic settings) and advanced. You can toggle between them on the page of any DNS zone.

<img src="https://assets.gcore.pro/docs/dns/about-gcore-dns/12990176402705.png" alt="Interface modes">

|                                                              | Non-advanced mode                                                                                                                                                                                                                        | Advanced mode  | 
|--------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| Add multiple values to one record at a time                  | ✖                                                                                                                                                                                                                                        | ✔              | 
| <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#balancing-by-coordinates-geo-proximity" target="_blank">Configure balancingby coordinates (Geo Proximity)</a>            | ✖                                                                                                                                                                                                                                        | ✔              |  
| <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#balancing-by-asn-country--or-continent--geo-dns" target="_blank">Configure balancing by ASN, country, or continent (Geo DNS)</a>  | ✖                                                                                                                                                                                                                                        | ✔              |   
| Configure integration with our CDN                           | You cannot integrate records with the CDN. Still, you can edit records that were integrated previously. For example, if you integrated the record when <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site" target="_blank">creating a CDN resource with entire site acceleration</a>, you can edit it afterward. | ✔              | 