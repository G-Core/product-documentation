---
title: about-dns-failover
displayName: Overview
published: true
order: 10
toc:
   --1--Health Checks: "what-are-health-checks"
   --1--What it is used for: "what-are-health-checks-used-for"
   --1--How it works: "how-do-health-checks-work"
   --1--Configure: "how-to-configure-dns-health-checks"
pageTitle: Understanding DNS Health Checks | Gcore
pageDescription: What DNS Health Checks are, how they work and what they are for.
---
# About DNS Health Checks
  
## What are Health Checks?

Health Checks are a paid feature for Pro and Enterprise tariff plans that monitors the availability of your website or servers and excludes non-working IPs from DNS responses in case of issues. As a result, the traffic is redirected from the broken server to a working one, and your resource stays available for all users.

## What are Health Checks used for?

Health Checks are needed to make your site or application available for all users in case some servers are down.

It’s especially important for business areas where the loss of availability means the loss of customers. Let’s use an example to explain. Imagine that you own an online store that works in Europe and the United States. Your site is on two servers: a European one and an American one. You use Geobalancing to route people from all over the world to the closest server so that the site loads faster. Customers from Paris, France, and Barcelona, Spain, are balanced to the European server, while users from Vancouver, Canada, and Chicago, United States, are balanced to the American one.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-1.png" alt="Health Checks scheme" width="80%">

One day, the European server crashes, and users who were being balanced to the European server get an error instead of your site. While the server is being fixed, customers go to a competitor’s site to make purchases faster.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-2.png" alt="Health Checks scheme" width="80%">

Then you enable DNS Health Checks. This feature constantly monitors your servers’ availability. The next time the European server crashes, DNS Health Checks will tell the DNS server not to add the unavailable European server IP in DNS responses. All requests from your customers will be directed to the American server, so your web application will still be working. Customers will be able to make purchases with no problems.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-3.png" alt="Health Checks scheme" width="80%">

When your European server recovers, Health Checks will detect that and return its IP in the DNS responses.

## How do Health Checks work?

**In common.** Health Checks send regular requests toward configured addresses to determine whether they are available. If a server doesn’t respond, DNS Health Checks will send DNS servers the command to exclude its IP from DNS responses. When the server recovers, DNS Health Checks will send DNS the command to return its IP to DNS responses.

By default, DNS Health Checks uses round robin load balancing to distribute users’ requests across available web servers. However, you can enable Geobalancing during configuration.

**In detail:**

1\. DNS Health Checks send requests to servers to check their availability. You <a href="https://gcore.com/docs/dns/dns-failover/configure-and-use-dns-failover" target="_blank">configure</a> request settings (protocol, frequency, and others) in the control panel after the feature is enabled.

For example, you can set the configuration for Health Checks requests as follows: _protocol: ICMP, frequency: 1 minute, and timeout: 10 seconds_. So, DNS Health Checks will send requests to web servers via ICMP protocol every 60 seconds.

2\. Requests are sent from all our locations where there are DNS servers. If your web servers send responses to Health Checks within the set timeout (e.g., 10 seconds) in 85% of locations, the feature will mark them as available.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-4.png" alt="Health Checks scheme" width="80%">

If a web server doesn’t send a response to Health Checks within the set timeout in 20% of locations, the feature will mark them as unavailable.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-5.png" alt="Health Checks scheme" width="80%">

3\. If a web server is unavailable, Health Checks will mark the corresponding record as unavailable and the DNS server excludes it from responses.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-6.png" alt="Health Checks scheme" width="80%">

**Note**: If all health check are failed, all of their A records will be used in a DNS response respecting other filters like *geo county* or *first_n*.


4\. The DNS server excludes the A record of the unavailable server from responses. All requests that were destined for this server are directed to other available servers.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-7.png" alt="Health Checks scheme" width="80%">

The balancing mechanism determines which server responds to requests destined for the unavailable server. By default, DNS Health Checks use round-robin, but you can configure your own mechanism, such as Geobalancing. The configuration for this mechanism is described in the article <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing" target="_blank">Configure weight balancing and Geobalancing</a>.

5\. Health Checks keep sending requests to web servers. When the web server becomes available and responds, the feature will send the appropriate update to the DNS server.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-8.png" alt="Health Checks scheme" width="80%">

After that, the web server will go back online for end-users again.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-9.png" alt="Health Checks scheme" width="80%">

## How to configure DNS Health Checks?

We describe how to configure Health Checks in the "<a href="https://gcore.com/docs/dns/dns-failover/configure-and-use-dns-failover" target="_blank">Configure and use DNS Health Checks</a>" article.