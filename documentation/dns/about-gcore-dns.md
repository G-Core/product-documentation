---
title: about-gcore-dns
displayName: Overview
published: true
order: 10
toc:
   --1--Overview: "gcore-dns-overview"
   --1--Interface mode comparison: "interface-modes-non-advanced-and-advanced"
---
  

Gcore DNS overview
------------------

The DNS service allows you to create, update, and delete DNS records for your domain. To manage your domain configuration, follow these steps:

1\. [Create a domain zone in your account](https://www.gcore.com/support/articles/360012064557/).  
2\. Specify Gcore nameservers (_ns1.gcorelabs.net_ and _ns2.gcdn.services_) in the domain settings on the registrar's website.  
3\. Configure DNS records in [non-advanced](https://www.gcore.com/support/articles/4432592889617/) or [advanced mode](https://www.gcore.com/support/articles/360012179878/). 

Interface modes: non-advanced and advanced
------------------------------------------

The DNS service interface offers two modes: non-advanced (for basic settings) and advanced. You can toggle between them on the page of any DNS zone.

<img src="https://support.gcore.com/hc/article_attachments/12990176402705" alt="mceclip0.png">

 

|                                                                 | Non-advanced mode                                                                                                                                                                                                                            | Advanced mode |
|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|
| \nAdd multiple valuesto one record at a time\n                  | ✖                                                                                                                                                                                                                                            | ✔             |
| \nConfigure balancingby coordinates (Geo Proximity)\n           | ✖                                                                                                                                                                                                                                            | ✔             |
| \nConfigure balancing by ASN, country, or continent (Geo DNS)\n | ✖                                                                                                                                                                                                                                            | ✔             |
| Configure integrationwith our CDN                               | \nYou cannot integrate records with the CDN. Still, you can edit records that were integrated previously. For example, if you integrated the record when creating a CDN resource with entire site acceleration, you can edit it afterward.\n | ✔             |
