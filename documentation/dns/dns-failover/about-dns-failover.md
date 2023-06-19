---
title: about-dns-failover
displayName: Overview
published: true
order: 10
toc:
   --1--What is DNS Failover?: "what-is-dns-failover"
   --1--What is it used for?: "what-is-dns-failover-used-for"
   --1--How it works: "how-dns-failover-works"
   --1--How to configure it: "configure-dns-failover"
---

# About DNS Failover 
  
## What is DNS Failover?

DNS Failover is a feature that monitors the availability of your website or servers and, in case of issues, excludes non-working IPs from DNS responses. As a result, the traffic is redirected from the broken server to a working one, and your resource stays available for all users.

It’s a paid feature that is currently available for free in beta version. If you want to use it, send a request to our support team via chat or email at [support@gcore.com](mailto:support@gcore.com).

## What is DNS Failover used for?

DNS Failover is needed to make your site or application available for all users in case some servers are down.

It’s especially important for business areas where the loss of availability means the loss of customers. Let’s use an example to explain. Imagine that you own an online store that works in Europe and the United States. Your site is on two servers: a European one and an American one. You use geo balancing to route people from all over the world to the closest server so that the site loads faster. Customers from Paris, France, and Barcelona, Spain, are balanced to the European server, while users from Vancouver, Canada, and Chicago, United States, are balanced to the American one.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/9684855295377.png" alt="" width="70%">

One day, the European server crashes, and users who were being balanced to the European server get an error instead of your site. While the server is being fixed, customers go to a competitor’s site to make purchases faster.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/9684878611345.png" alt="" width="70%">

Then you enable DNS Failover. This feature constantly monitors your servers’ availability. The next time the European server crashes, DNS Failover will tell the DNS server not to add the unavailable European server IP in DNS responses. All requests from your customers will be directed to the American server, so your web application will still be working. Customers will be able to make purchases with no problems.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/9684855397905.png" alt="" width="70%">

When your European server recovers, DNS Failover will detect that and return its IP in the DNS responses.

## How DNS Failover works

**In common.** DNS Failover sends regular requests toward configured addresses to determine whether they are available. If a server doesn’t respond, DNS Failover will send DNS servers the command to exclude its IP from DNS responses. When the server recovers, DNS Failover will send DNS the command to return its IP to DNS responses.

By default, DNS Failover uses round robin load balancing to distribute users’ requests across available web servers. However, you can enable geo balancing during configuration.

**In detail:**

1\. DNS Failover sends requests to servers to check their availability. You <a href="https://gcore.com/docs/dns/dns-failover/configure-and-use-dns-failover" target="_blank">configure</a> request settings (protocol, frequency, and others) in the control panel after the feature is enabled.

For example, you can set the configuration for DNS Failover requests as follows: _protocol: ICMP, frequency: 1 minute, and timeout: 10 seconds_. So, DNS Failover will send requests to web servers via ICMP protocol every 60 seconds.

2\. Requests are sent from all our locations where there are DNS servers. If your web servers send responses to DNS Failover within the set timeout (e.g., 10 seconds) in 85% of locations, the feature will mark them as available.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/9684855402769.png" alt="" width="70%">

If a web server doesn’t send a response to DNS Failover within the set timeout in 20% of locations, the feature will mark them as unavailable.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/9684855522193.png" alt="" width="70%">

3\. If a web server is unavailable, DNS Failover will notify the DNS server: *"Stop responding with the … IP (address of the unavailable server)"*.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/9684878905617.png" alt="" width="70%">

**Note:** If all web servers don’t respond, all of their A records will be added to the DNS response regarding other filters like geo or *first_n*.

4\. The DNS server excludes the A record of the unavailable server from responses. All requests that were destined for this server are directed to other available servers.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/9684879021841.png" alt="" width="70%">

The balancing mechanism determines which server responds to requests destined for the unavailable server. By default, DNS Failover uses round-robin, but you can configure your own mechanism, such as geo balancing. The configuration for this mechanism is described in the article "<a href="https://gcore.com/docs/dns/dns-failover/configure-and-use-dns-failover" target="_blank">DNS Failover. Configure and use</a>".

5\. DNS Failover keeps sending requests to web servers. When the web server becomes available and responds, the feature will send the appropriate update to the DNS server.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/9684879045649.png" alt="" width="70%">

After that, the web server will go back online for end-users again.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/9684879172113.png" alt="" width="70%">

## Configure DNS Failover

We describe how to configure DNS failover in the "<a href="https://gcore.com/docs/dns/dns-failover/configure-and-use-dns-failover" target="_blank">DNS Failover. Configure and use</a>" article.