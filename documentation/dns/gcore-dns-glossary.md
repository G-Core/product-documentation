---
title: gcore-dns-glossary
displayName: Glossary
published: true
order: 20
toc: 
pageTitle: Key Terms Explained in the Gcore Managed DNS Glossary | Gcore
pageDescription: Master the language of DNS with Gcore's comprehensive DNS glossary.
---
# Gcore Managed DNS Glossary

Examine the definitions for terminology commonly used throughout Gcore's Managed DNS documentation.

<p id="a-record"><b>A record</b> is a record that maps a domain name to its corresponding IPv4 address. For more details refer to Supported DNS record types.</p>

<p id="aaaa-record"><b>AAAA record</b> is a record that maps a domain name to its corresponding IPv6 address. For more details refer to Supported DNS record types.</p>

<p id="authoritative"><b>Authoritative name servers</b> are servers responsible for directly answering queries for records in their specific domains, distinguishing them from non-authoritative or caching servers that temporarily store DNS query results.</p> 

<p id="cname"><b>CNAME record</b> is a record that allows to alias a domain name to another. It is commonly used for associating a subdomain with another domain’s DNS records. For more details refer to Supported DNS record types.</p> 

<p id="dns-propagation"><b>DNS propagation</b> is the process of updating all servers with new information about the DNS. It involves the spreading or “propagation” of the new DNS information from one DNS server to another. This process can take anywhere from a few minutes to 48 hours.</p> 

<p id="dns-record"><b>DNS record</b> is a database entry within the Domain Name System (DNS) that maps a domain name to various data types, like an IP address (an A record). They tell the DNS where to send a user when they type in a specific domain name or request a certain piece of information, like email servers for a domain. For more details refer to Supported DNS record types and Manage DNS records.</p> 

<p id="dns-zone"><b>DNS zone</b> is a conceptual name used in administration to delegate control over DNS settings across various domains and subdomains. It represents a portion of the domain name space in the DNS and includes the records for the domains within that zone. Use Getting started with Managed DNS to learn how to create DNS zones in Gcore.</p>

<p id="dnssec"><b>DNSSEC (Domain Name System Security Extensions)</b> is a suite of IETF specifications used to add a layer of security to the DNS to protect against certain attacks, such as forging or manipulating DNS data, by verifying the authenticity and integrity of the data with digital signatures. Learn how to configure DNSSEC in Getting started with DNSSEC.</p>

<p id="dns-query"><b>DNS query</b> is a request for information sent from a client device to the DNS. The query is made to retrieve specific DNS records associated with a domain name, such as an IP address for a website. The DNS server responds to the query by providing the requested information back to the client device, enabling it to connect with the desired web server.</p>

<p id="domain"><b>Domain (domain name)</b> is a name that identifies a website. It is a unique string of characters (e.g., gcore.com or google.com, etc.) that serves as an address used to access a website on the Internet.</p> 

<p id="domain-registrar">Domain registrar</b> is a company that manages the reservation of Internet domain names. They can register domain names for individuals or companies who want to own a particular website address. They also interact with the global DNS database to ensure those domain names are accessible worldwide.</p>

<p id="mx"><b>MX record</b> is a record that is used to specify the mail servers responsible for receiving email on behalf of a domain. For more details refer to Supported DNS record types.</p>

<p id="name-server"><b>Name servers</b> in this documentation name servers usually refer to the Gcore authoritative name servers: ns1.gcorelabs.net and ns2.gcdn.services.</p>

<p id="ns"><b>NS record</b> is a record indicating which servers are authoritative for a particular zone. For more details refer to Supported DNS record types.</p>

<p id="recursors"><b>Recursors (recursive resolvers)</b> are servers designed to receive DNS queries from client machines through web browsers and other such devices. When a recursor receives a query, it interprets and forwards the request to the appropriate DNS authoritative name servers. If the recursor has the answer in its cache, it will return the cached answer to the client. If not, it will query the authoritative servers to find the answer. This process is known as recursion.</p>

<p id="reverse"><b>Reverse DNS lookups</b> is a process for determining the domain name associated with a given IP address. This is the opposite of the more commonly used forward DNS lookup, which turns domain names into IP addresses.</p>

<p id="soa"><b>SOA record</b> is a record that provides information about the domain and the zone, including the primary name server, the email of the domain administrator, the domain serial number, and timers.</p>

<p id="srv"><b>SRV record</b> is a record used to identify the hostname and port number for specific services, such as VOIP or instant messaging.</p>

<p id="subdomain"><b>Subdomain</b>is a separate part of your website that operates under the same primary domain name. For example, if your domain is sample-test.com, then a subdomain can be store.sample-test.com or blog.sample-test.com. Subdomains are commonly used to organize or divide content into distinct sections.</p>  

<p id="ttl"><b>TTL (Time To Live)</b> is a value in seconds that specifies how long a DNS record can be cached by resolving name servers, browsers, or operating systems before it needs to be refreshed.</p>

<p id="zone-apex"><b>Zone apex (root zone)</b>is the top-most part of the DNS hierarchy. It represents the namespace for which a DNS server has the authority and contains information about the domain and its subdomains. For example, in the domain name store.sample-test.com, sample-test.com would be the zone apex.</p>
