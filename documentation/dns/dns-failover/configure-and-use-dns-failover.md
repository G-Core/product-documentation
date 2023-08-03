---
title: configure-and-use-dns-failover
displayName: Configure and use
published: true
order: 20
toc:
pageTitle: Configuring and usage of the DNS Health checks technology | Gcore
pageDescription: A comprehensive guide on how to configure and manage DNS Health checks.
---
# Configure and use DNS Health checks

1\. Open the <a href="https://dns.gcore.com/" target="_blank">DNS interface</a>.

2\. Go to the DNS zone of the site or application that you want to use with DNS Health checks.

3\. Enable the **Advanced interface mode**. In the non-advanced mode, the Health checks feature will not appear.

4\. Go to the settings of the appropriate A, AAAA, or CNAME record. To do this click, the domain name or press the "···" icon on the right and click **Edit record**.


<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/configure-health-checks-10.png" alt="" width="80%">

The **Records list/Edit record set** page will open. Complete the remaining steps in it.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/configure-health-checks-20.png" alt="" width="80%">

5\. Enable the **Health checks** feature.

6\. Choose the appropriate type of protocol that Health checksr will use when sending requests to web servers. The choice depends on how you want to monitor the web servers of your site or application.

7\. Set the check options. Different protocols have their own set of options.

**Check by TCP/UDP**

- Port is where you specify the port to connect to. For example, 80, 443, or another one.
- Check Frequency lets you choose the interval of checks from the list.
- Timeout sets the time that your web servers should give the response.
- (optional) Command allows you to enter the text that will be sent to the host of the site as plain text, e.g., *GET/HTTP/1.1*.

**Check by ICMP**

- Check Frequency lets you choose the interval of checks from the list.
- Timeout sets the time that your servers should give the response.

**Check by HTTP**

- Port is where you specify the port to connect to. For example, 80, 443, or another one.
- Check Frequency lets you choose the interval of checks from the list.
- Timeout sets the time that your web servers should give the response.
- Requested URL is where you enter the URL that will be requested for checks.
- Requested Method lets you choose the method for checking requests. For example, GET.
- Use TLS lets you choose whether TLS should be used.
- HTTP status code is used to put the expected HTTP response code or leave it blank if any response is ok.
- Expected content regexp is where you enter a regular expression that would match the response body or leave it blank.

8\. Here, you can set IP addresses and logic that will be used to distribute requests among available servers when some of them are unavailable. By default, DNS Health checks uses round-robin balancing. If it's suitable for you, just go to the next step of this guide. If you want to change the criteria of balancing according to the "<a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing" target="_blank">Manage DNS records (advanced interface mode with balancing)</a>".

9\. Save the changes.

Configuration is complete! Now Health checks monitors the availability of your site.

Also, you can check for recent monitoring events in Health checks logs.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/configure-health-checks-30.png" alt="" width="80%"> 