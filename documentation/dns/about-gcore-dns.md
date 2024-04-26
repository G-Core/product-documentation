---
title: about-gcore-dns
displayName: Overview
published: true
order: 10
toc:
   --1--Managed DNS: "managed-dns"
   --1--Public DNS: "public-dns"
   --1--Plans and features: "plans-and-features"
pageTitle: Overview of Managed DNS and Public DNS | Gcore
pageDescription: Discover Gcore's DNS products, offering domain protection, flexible balancing, increased resolution speed, and various tariff plans.
---
# Gcore DNS overview

You can learn more about how DNS works in our blog post: “<a href="https://gcore.com/learning/what-is-dns-how-does-it-work/" target="_blank">What Is Domain Name System (DNS)</a>.” As a DNS provider, we offer customers two products: <a href="https://gcore.com/dns" target="_blank">Managed DNS</a> and <a href="https://gcore.com/public-dns" target="_blank">Public DNS</a>.

## Managed DNS

Gcore Managed DNS is an authoritative DNS server for domain delegation. When delegating domains and creating a DNS zone, you gain access to the following features of the Managed DNS product:

- <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site" target="_blank">Creation of a CDN resource for the entire site</a>.
- DNS records management in the <a href="https://dns.gcore.com/zones" target="_blank">Gcore Customer Portal</a> and via the <a href="https://api.gcore.com/docs/dns" target="_blank">API</a>.
- AnycastDNS for redirecting requests to your domain to the nearest edge location.
- <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing" target="_blank">Flexible balancing to various IP addresses</a>, based on the geolocation of the user who requested the domain, metadata, or weight that you set.
- <a href="https://gcore.com/docs/dns/getting-started-with-dnssec" target="_blank">DNSSEC</a> for domain protection during resolving processes.
- <a href="https://gcore.com/docs/dns/dns-failover/configure-and-use-dns-failover" target="_blank">Health Checks</a> for checking the availability of IP addresses.
- <a href="https://gcore.com/docs/dns/dns-plugins/use-gcore-dns-as-a-secondary-dns-with-octodns" target="_blank">OctoDNS</a>, <a href="https://gcore.com/docs/dns/dns-plugins/get-a-let-s-encrypt-certificate-with-certbot" target="_blank">Certbot</a>, Kubernetes, and Terraform third-party solution integrations.
- <a href="https://gcore.com/docs/dns/dns-records/specify-cname-at-root" target="_blank">CNAME flattening</a> for using a subdomain at the root.
- <a href="https://gcore.com/docs/dns/dns-records/what-is-an-https-record-and-how-is-it-configured" target="_blank">Support for HTTPS records</a>.
- <a href="https://gcore.com/docs/dns/dns-records/supported-dns-record-types#aaaa-record" target="_blank">Support for IPv6 addresses</a>.

DNS record management is available in two modes: **non-advanced** and **advanced**. Use non-advanced mode if you need to add a single DNS record without additional balancing settings. Use advanced mode if you want to add RRsets or set additional settings, such as balancing and Health Checks.

## Public DNS 

Gcore Public DNS are **free** public DNS resolvers for converting names into IP addresses. You can use Gcore Public DNS instead of the resolvers provided by your internet provider to increase resolution speed and protect the domain from substitution.

## Plans and features 

You can find complete information about the available features on the <a href="https://gcore.com/pricing/edge-network#dns" target="_blank">DNS Pricing page</a>. Below, we will touch on the differences in tariffs so that you understand whether the features of the starter tariff are enough for you:

<table>
<thead>
<td><b>Feature</b></td>
<td><b>Free</b></td>
<td><b>Pro</b></td>
<td><b>Enterprise</b></td>
</thead>
<tbody>
<tr>
<td style="text-align: left">Minimum TTL</td>
<td style="text-align: left">120 s</td>
<td style="text-align: left">30 s</td>
<td style="text-align: left">1 s</td>
</tr>
<tr>
<td style="text-align: left">Number of Dynamic RRset</td>
<td style="text-align: left">1/zone</td>
<td style="text-align: left">Unlimited</td>
<td style="text-align: left">Unlimited</td>
</tr>
<tr>
<td style="text-align: left">Dynamic RRset size</td>
<td style="text-align: left">3 records/RRset</td>
<td style="text-align: left">9 records/RRset</td>
<td style="text-align: left">Unlimited</td>
</tr>
<tr>
<td style="text-align: left">Health Checks records</td>
<td style="text-align: left">1</td>
<td style="text-align: left">5</td>
<td style="text-align: left">Unlimited</td>
</tr>
<tr>
<td style="text-align: left">Health Checks frequency</td>
<td style="text-align: left">300 s</td>
<td style="text-align: left">60 s</td>
<td style="text-align: left">10 s</td>
</tr>
<tr>
<td style="text-align: left">Free trial</td>
<td style="text-align: left">-</td>
<td style="text-align: left">14 days</td>
<td style="text-align: left">Individual terms</td>
</tr>
</tbody>
</table>

Functions not mentioned in the table are available for all tariffs.

<alert-element type="tip" title="Tip">

If you are interested in services such as Vanity name servers, White label solution, as well as in developing solutions for your tasks, the “Enterprise” plan will suit you. Contact the [sales manager](mailto:support@gcore.com) to discuss the details.

</alert-element>