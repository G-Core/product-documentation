---
title: set-up-cname-flattening
displayName: Set up CNAME flattening
published: true
order: 30
toc:
   --1--Domain root: "domain-root"
   --1--Issue: "issue"
   --1--Solution: "solution"
   --1--How it works: "how-it-works"
   --1--How to enable: "how-to-enable"
---
Domain root
-----------

The root of a domain also known as zone apex represented by an empty label (i.e., no subdomain). For instance, the zone apex for the domain  _example.com_  is simply _example.com_.

Issue
-----

According to the rfc1034 3.6.2: if a CNAME resource record is present, no other data should be present for the same label. Nevertheless, there are always mandatory NS and SOA records at zone apex (which label are empty). Thus, it means that it’s not possible to have a CNAME at zone apex according to the current DNS specification.

Because for some usecases it could be quite convenient to have CNAME at apex (like integration with 3rd parties like CDNs, site or blog builders, etc.), Gcore DNS provides this capability to its customers on all plans, only showing a disclaimer that unpredictable behavior could be expected because of RFCs violation.

Solution
--------

To address the issue, we introduce a CNAME flattening feature. CNAME flattening allows to have a CNAME at zone apex and the same time to comply with DNS specifications and speeding up the resolution process.

How it works
------------

CNAME flattening involves synthesizing an A or AAAA record for the zone apex by resolving the CNAME chain and using the IP address of the final A or AAAA record. This synthetic record is then cached respecting its TTL and used to answer subsequent DNS queries for the zone apex on Gcore DNS side. By doing so we avoid specification violation thus ensuring proper DNS resolution in more cases. Because of the local cache layer the total resolution time may decrease significantly in some cases.

How to enable
-------------

CNAME flattening is enabled by default for all CNAMEs at apex with exactly 1 resource record since release date.