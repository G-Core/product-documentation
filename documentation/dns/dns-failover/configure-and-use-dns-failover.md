---
title: configure-and-use-dns-failover
displayName: Configure and use
published: true
order: 20
toc:
---

# Configure and use DNS Failover

1\. To enable the DNS Failover feature, send us a request by email at [support@gcore.com](mailto:support@gcore.com) or the chat window in the bottom-right corner of <a href="https://gcore.com/" target="_blank">our website</a>. Please specify your ID in the request, so we can identify your account. You can find it on the main page of your <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>.

<img src="https://support.gcore.com/hc/article_attachments/9619861814417" alt="">

The message template: *"Good afternoon! Please enable the DNS Failover imitation feature for the account with ID … (your ID)"*.

We will notify you when the feature is activated. After that, you will be able to use it for your site or application.

2\. Open the <a href="https://dns.gcore.com/" target="_blank">DNS interface</a>.

3\. Go to the DNS zone of the site or application that you want to use with DNS Failover.

<img src="https://support.gcore.com/hc/article_attachments/9619861818513" alt="">

The **DNS records** section will open. Do the next steps in it.

<img src="https://support.gcore.com/hc/article_attachments/9619861864721" alt="">

4\. Enable the **Advanced interface mode.** In the non-advanced mode, the DNS Failover feature will not appear.

5\. Go to the settings of the appropriate A, AAAA, or CNAME record. To do this click, the domain name or press the "···" icon on the right and click **Edit record**.

The **Records list/Edit record set** page will open. Complete the remaining steps in it.

<img src="https://support.gcore.com/hc/article_attachments/9619897145361" alt="">

6\. Enable the **Failover checks (beta)** service.

7\. Choose the appropriate type of protocol that DNS Failover will use when sending requests to web servers. The choice depends on how you want to monitor the web servers of your site or application.

8\. Set the check options. Different protocols have their own set of options.

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

9\. Here, you can set IP addresses and logic that will be used to distribute requests among available servers when some of them are unavailable. By default, DNS Failover uses round-robin balancing. If it's suitable for you, just go to the next step of this guide. If you want to change the criteria of balancing according to the "<a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing" target="_blank">Manage DNS records (advanced interface mode with balancing)</a>".

10\. Save the changes.

Configuration is complete! Now DNS Failover monitors the availability of your site.

Also, you can check for recent monitoring events in Failover logs.

<img src="https://support.gcore.com/hc/article_attachments/9619897190417" alt="">

Please note that this is a beta version, and the feature may be unstable. Write to us via [support@gcore.com](mailto:support@gcore.com) or the chat window in the bottom-right corner of <a href="https://gcore.com/" target="_blank">our website</a>. Describe options you would like to see in the final version of the product.