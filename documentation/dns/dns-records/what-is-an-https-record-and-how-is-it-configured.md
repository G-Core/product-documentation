---
title: what-is-an-https-record-and-how-is-it-configured
displayName: HTTPS record
published: true
order: 60
toc:
    --1--What is the HTTPS record?: 'what-is-an-https-record'
    --1--What problem does it solve?: 'what-problem-does-the-https-record-solve'
    --1--How does it work?: 'how-do-https-records-work'
    --1--Configure HTTPS: 'how-to-configure-https-records'
pageTitle: What Is an HTTPS Record and How Is it Configured? | Gcore
pageDescription: Discover what an HTTPS record is, how it enhances secure internet connections, and how to configure it in the Gcore Customer Portal.
---
# What is an HTTPS record and how is it configured?

## What is an HTTPS record?

<a href="https://gcore.com/dns" target="_blank">Gcore Managed DNS</a> supports HTTPS record creation. The HTTPS record is a specialized form of the Service Binding (SVCB) DNS record. These record types have been established by the Internet Engineering Task Force (IETF) to enhance the flexibility of secure internet connections, making them more reliable and faster. HTTPS records achieve this by reducing the number of round trips required to establish a connection and by supporting future protocol upgrades.

The HTTPS DNS record provides more detailed information than other record types (like A or AAAA) about the services available for a specific domain. This record type plays a crucial role in establishing secure network connections like HTTPS by providing essential details. For example, HTTPS DNS can communicate information about supported protocols and ports, and can even specify alternate servers to which clients can connect.

The availability of extended information in the HTTPS record allows a client to fetch the necessary parameters to connect to a service securely via a single DNS query, rather than having to perform multiple queries or connections. This streamlined process significantly enhances efficiency and security in network connections.

## What problem does the HTTPS record solve?

Traditional methods of establishing secure connections, like HTTPS, often necessitate multiple round trips between the client and the server, resulting in latency. Consider the following example: when you type `www.sample-test.com` into the browser, the following processes occur:

1\. A lookup is performed for A or AAAA records for `www.sample-test.com`.

2\. A connection to `http://www.sample-test.com` is made, which results in a redirect to `https://www.sample-test.com`.

3\. A TLS connection to `https://www.sample-test.com` is established, which may be upgraded to HTTP/3 over the <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Alt-Svc" target="_blank">Alt-Svc header</a>

These three steps can add significant latency due to the multiple round trips required to establish the optimal connection type with the web server. These steps also pose a security risk, as they create an opportunity to inject malicious ads or captive portals during the upgrade from HTTP to HTTPS.

## How do HTTPS records work?

An HTTPS record can be set up for the domain `sample-test.com` as shown below:

```
www.sample-test.com.     	1800	IN	HTTPS	1 . alpn=h3,h3-29,h2 ipv4hint=1.2.3.4,9.8.7.6 ipv6hint=2001:db8:3333:4444:5555:6666:7777:8888,2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF

```

Here's what each element represents:

-   `www.sample-test.com` is the domain name.
-   `1800` is the Time To Live (TTL).
-   `IN` represents the class.
-   `HTTPS` signifies the record type.
-   `1` is the priority, i.e., the number in the queue.
-   `.` stands for the host if it is the same as the domain name.
-   `alpn=h3,h3-29,h2` specifies the application protocol versions.
-   `ipv4hint=1.2.3.4,9.8.7.6` specifies IPv4 addresses (this is optional.)
-   `ipv6hint=2001:db8:3333:4444:5555:6666:7777:8888,2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF` specifies IPv6 addresses (this is also optional.)

When a browser requests the HTTPS record from the DNS server, it receives all necessary information in the response that is required to establish a secure connection to `https://sample-test.com`. This includes:

1. The exact protocol configuration required to reach example.com and its preferences.
2. IP addresses of web servers serving example.com, which could be from multiple CDNs or providers, effectively resolving other limitations with records at the <a href="https://gcore.com/docs/dns/dns-records/specify-cname-at-root" target="_blank">domain apex</a>.

Combining all relevant parameters into a single lookup response reduces the number of round trips required to connect to a web server. When used together with <a href="https://datatracker.ietf.org/doc/html/rfc3168" target="_blank">ECN configuration</a>, this eliminates the need for multiple rounds of TLS negotiation while still supporting cutting-edge multi-CDN scenarios.

## How to configure HTTPS records

1\. Navigate to <a href="https://dns.gcore.com" target="_blank">DNS</a> in the Gcore Customer Portal. Click on the zone of the domain where you wish to add the HTTPS record.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-10.png" alt="All zones" width="70%">

2\. Click **Add record**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/what-is-an-https-record-and-how-is-it-configured/https-conf-10.png" alt="Add a record" width="80%">

Refer to the following screenshot while following the rest of the steps after it.

<img src="https://assets.gcore.pro/docs/dns/dns-records/what-is-an-https-record-and-how-is-it-configured/https-conf-20.png" alt="attribute configurations" width="80%">

3\. **Type.** Select “HTTPS”.

4\. (Optional) **Name.** Leave this field empty if you're creating an HTTPS record type for the zone apex. If you want to work with, say, www.`sample-test.com`, add `www`.

5\. (Optional) **TTL.** Leave empty or fill with a sensible value. For testing, 300 seconds is acceptable, but for production, consider a higher value like 1800 or more. This ensures that the records do not expire too quickly and that recursive name servers can cache them effectively.

6\. **Priority.** Set the priority for the records. Common values are 1, 2, 3, or 10, 20, or 30. This setting is used if multiple HTTPS records are available for the same name.

7\. **TargetName.** Type a valid domain name or leave it as the `.` sign.

8\. Select the `alpn` attributes of the HTTPS record from the list. The `alpn` attribute is often used by browsers to recognize protocols supported by your web server.

9\. Select or type the relevant values, such as `https/1.1`, `http/2`, `http/3`, or others. You can choose several values from the list.

10\. Select the `ipv4hint` or `ipv6hint`. These attributes are helpful because browsers do not need to perform additional DNS lookups for your web servers' IP addresses.

11\. Type the IP address.

12\. Click **Add**.

After configuration, the record should look something like this:

<img src="https://assets.gcore.pro/docs/dns/dns-records/what-is-an-https-record-and-how-is-it-configured/https-conf-30.png" alt="record " width="80%">

You can verify the responses with kdig (a version of “dig” from Knot DNS). If you're using “dig,” please ensure you have the latest version, as older versions do not support HTTPS record types. You can also check if the new record has been added correctly using the <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> tool.

```
kdig https sample-test.com @ns1.gcorelabs.net

;; ->>HEADER<<- opcode: QUERY; status: NOERROR; id: 34710
;; Flags: qr aa rd; QUERY: 1; ANSWER: 1; AUTHORITY: 0; ADDITIONAL: 0

;; QUESTION SECTION:
;;sample-test.com.   		 IN    HTTPS

;; ANSWER SECTION:
sample-test.com.   	 1800    IN    HTTPS    1 . alpn=h3,h2,http/1.1 ipv4hint=1.2.3.4,9.8.7.6 ipv6hint=2001:db8:3333:4444:5555:6666:7777:8888,2001:db8:3333:4444:cccc:dddd:eeee:ffff
```

That’s it! You’ve configured your HTTPS record.