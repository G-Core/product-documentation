---
title: configure-and-use-dns-failover
displayName: Healthchecks
published: true
order: 20
toc:
   --1--Healthchecks: "what-are-healthchecks"
   --1--How it works: "how-do-healthchecks-work"
   --1--Configure: "configure-healthchecks"
   --1--Backup metadata: "enable-backup-metadata"
   --1--Check logs: "check-healthchecks-logs"

pageTitle: What is Healthcheck and How to Configure it? | Gcore
pageDescription: A comprehensive guide on how to configure and manage DNS Health Checks.
customUrl: /dns/dns-failover/configure-and-use-dns-failover
---
# What is Healthcheck and how to configure it?

## What are Healthchecks? 

Healthchecks is a feature that monitors the availability of your website or servers and excludes non-working IPs from DNS responses in case of issues. As a result, the traffic is redirected from the broken server to a working one, and your resource stays available for all users. Healthchecks are needed to make your site or application available for all users in case some servers are down.

<expandable-element title="Example of how Healthchecks works">

It’s especially important for business areas where the loss of availability means the loss of customers. Let’s use an example to explain. Imagine that you own an online store that works in Europe and the United States. Your site is on two servers: a European one and an American one. You use Geobalancing to route people from all over the world to the closest server so that the site loads faster. Customers from Paris, France, and Barcelona, Spain, are balanced to the European server, while users from Vancouver, Canada, and Chicago, United States, are balanced to the American one.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-1.png" alt="Healthchecks scheme: both servers work" width="80%">

One day, the European server crashes, and users who were being balanced to the European server get an error instead of your site. While the server is being fixed, customers go to a competitor’s site to make purchases faster.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-2.png" alt="Healthchecks scheme: one server is broken" width="80%">

Then you enable Healthchecks. This feature constantly monitors your servers’ availability. The next time the European server crashes, Healthchecks will tell the DNS server not to add the unavailable European server IP in DNS responses. All requests from your customers will be directed to the American server, so your web application will still be working. Customers will be able to make purchases with no problems.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-3.png" alt="Healthchecks scheme: redirecting requests to a working server" width="80%">

When your European server recovers, Healthchecks will detect that and return its IP in the DNS responses.

</expandable-element>

## How do Healthchecks work?

**In common:** 

Healthchecks send regular requests toward configured addresses to determine whether they are available. If a server doesn’t respond, DNS Healthchecks will send DNS servers the command to exclude its IP from DNS responses. When the server recovers, DNS Healthchecks will send DNS the command to return its IP to DNS responses.

By default, DNS Healthchecks uses round robin load balancing to distribute users’ requests across available web servers. However, you can enable Geobalancing during configuration.

**In detail:**

1\. DNS Healthchecks send requests to servers to check their availability. You configure request settings (protocol, frequency, and others) in the Gcore Customer Portal after the feature is enabled.

For example, you can set the configuration for Healthchecks requests as follows:

- protocol: ICMP
- frequency: 1 minute 
- timeout: 10 seconds 

So, DNS Healthchecks will send requests to web servers via ICMP protocol every 60 seconds.

2\. Requests are sent from all our locations where there are DNS servers. If your web servers send responses to Healthchecks within the set timeout (e.g., 10 seconds) in 85% of locations, the feature will mark them as available. If a web server doesn’t send a response to Healthchecks within the set timeout in 20% of locations, the feature will mark them as unavailable.

3\. If a web server is unavailable, Healthchecks will mark the corresponding record as unavailable and the DNS server excludes it from responses.

<alert-element type="info" title="Info">

If all Healthchecks are failed, all of their A records will be used in a DNS response respecting other filters like *geo county* or *first_n*.

</alert-element>

4\. The DNS server excludes the A record of the unavailable server from responses. All requests that were destined for this server are directed to other available servers.

The balancing mechanism determines which server responds to requests destined for the unavailable server. By default, DNS Healthchecks use round-robin, but you can configure your own mechanism, such as geobalancing. The configuration for this mechanism is described in the article <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing" target="_blank">Dynamic response</a>.

5\. Healthchecks keep sending requests to web servers. When the web server becomes available and responds, the feature will send the appropriate update to the DNS server. After that, the web server will go back online for end-users again.

<media-gallery>

<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-4.png" alt="Health Checks scheme" width="80%">
<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-5.png" alt="Health Checks scheme" width="80%">
<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-6.png" alt="Health Checks scheme" width="80%">
<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-7.png" alt="Health Checks scheme" width="80%">
<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-8.png" alt="Health Checks scheme" width="80%">
<img src="https://assets.gcore.pro/docs/dns/dns-failover/about-dns-failover/health-checks-9.png" alt="Health Checks scheme" width="80%">

</media-gallery>

## Configure Healthchecks

1\. Navigate to the <a href="https://dns.gcore.com/zones" target="_blank">DNS</a> section in the Customer Portal.

2\. Click the domain name of the DNS zone where you intend to set up Healthchecks. 

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-10.png" alt="Open a DNS zone" width="80%">

A new page will open.

3\. Ensure that the advanced interface mode is enabled. In non-advanced mode, the Healthchecks feature isn't available.

<alert-element type="caution" title="Caution">

A Healthcheck picker can be applied only to **A**, **AAAA** or **CNAME** record type.

</alert-element>

4\. Click three dots and click **Edit record** in the row of the A, AAAA, or CNAME record. 

<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/healthchecks-10.png" alt="Open a Records list/Edit record set page" width="80%">

The “Records list/Edit record set” page will open. Perform the remaining steps there.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/healthchecks-20.png" alt="Select a Healthchecks picker" width="80%">

5\. Enable the **Dynamic response** toggle.

6\. Click a Healthcheck picker in the right list. 

7\. Click the edit icon when the picker is added to the left column.

A pop-up will open. Follow the rest of the steps there. The setting will differ depending on the protocol: TCP or UDP, ICMP and HTTP.

<tabset-element>

### TCP/UDP

<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/healthchecks-30.png" alt="Configure a Healthchecks picker: TCP or UDP" width="70%">

8\. In the "Protocol" block, select **TCP** or **UDP**.

9\. In the "Port" field, specify the connection port (e.g., 80 or 443).

10\. In the "Check Frequency" field, select the interval of checks from the list.

11\. In the "Timeout" field, set the time within which your web servers should give the response before being considered down.

12\. (Optional) In the "Command" field, enter the text that will be sent to the host of the site as plain text, e.g., `GET / HTTP/1.1\n\n`.

13\. (Optional) In the "Expected content regexp" field, enter a regular expression that would match the response body or leave it blank.

14\. Click **Save**.

### ICMP

<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/healthchecks-40.png" alt="Configure a Healthchecks picker: ICMP" width="70%">

8\. In the "Protocol" block, select **ICMP**.

9\. In the "Check Frequency" field, select the interval of checks from the list.

10\. In the "Timeout" field, set the time within which your web servers should give the response before being considered down.

11\. Click **Save**.

### HTTP

<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/healthchecks-50.png" alt="Configure a Healthchecks picker: HTTP" width="70%">

8\. In the "Protocol" block, select **HTTP**.

9\. In the "Port" field, specify the connection port (e.g., 80 or 443).

10\. In the "Check Frequency" field, select the interval of checks from the list.

11\. In the "Timeout" field, set the time within which your web servers should give the response before being considered down.

12\. (Optional) In the "Host" field, specify a value of the Host header to be passed during HTTP request.

13\. In the "Requested URL" field, enter the URL that will be requested for checks.

14\. In the "Requested Method" block, select the method for checking requests; e.g., GET.

15\. In the "Use TLS" block, choose whether TLS should be used.

16\. In the "HTTP status code" field, put the expected HTTP response code or leave it blank if any response is ok.

17\. (Optional) In the "Expected content regexp", enter a regular expression that would match the response body or leave it blank.

18\. Click **Save**.

</tabset-element>

The configuration is complete!

## Enable backup metadata

You can enable backup metadata for Healthchecks. In this case, records marked as backups will not participate in the response if at least one “healthy,” valid record exists. If all records not marked as backup are non-functional, the “healthy” backup records will appear in the response. 

To configure backup metadata, select which record will be used as a backup (Record 1 in the example,) choose “backup” from the dropdown list, and enable the toggle.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/healthchecks-60.png" alt="Configure backup metadata" width="70%">

By default, DNS Health Checks use round-robin balancing. You can configure logic that will be used to distribute requests among available servers when some of them are unavailable. Use <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing" target="_blank">our detailed guide</a> for more information.

## Check Healthchecks logs

Refresh your DNS cache renewal and Healthchecks will start to monitor your site’s availability.

You can also check for recent monitoring events in Healthchecks logs. Go to the page of the DNS zone for which your configured DNS Healthchecks. Select the needed record, click the three dots on the right, and click **Healthchecks logs**.

<img src="https://assets.gcore.pro/docs/dns/dns-failover/configure-and-use-dns-failover/healthchecks-70.png" alt="Check monitoring logs" width="80%"> 