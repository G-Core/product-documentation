---
title: supported-dns-record-types
displayName: DNS record types
published: true
order: 5
toc:
   --1--A record: "a-record"
   --1--AAAA record: "aaaa-record"
   --1--NS record: "ns-record"
   --1--CNAME record: "cname-record"
   --1--MX record: "mx-record"
   --1--TXT record: "txt-record"
   --1--SRV record: "srv-record"
   --1--CAA record: "caa-record"
   --1--HTTPS record: "https-record"
   --1--SVCB record: "svcb-record"
   --1--PTR record: "ptr-record"  
   --1--What's next?: "whats-next"
pageTitle: Overview of the record types supported in our system | Gcore
pageDescription: Find out what types of DNS records are supported in the Gcore interface. 
---
# Supported DNS record types

At the time of writing (June 2023,) <a href="https://gcore.com/dns" target="_blank">Gcore DNS Hosting</a> supports eleven record types. In this article, we provide brief information about each of them.

<img src="https://assets.gcore.pro/docs/dns/dns-records/supported-dns-record-types/dns-record-types-10.png" alt="Supported DNS record types">

You can check the resource records of your domain name using the <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> tool. 

## A record

An А record defines the IP address to which the domain corresponds. The value of the A record is the server IP address in IPv4 format associated with your domain name. 

Here’s an example of an A record response:

```
example.com. 1800 IN A 93.184.216.34
```

Let’s break down what the components of an A record mean:

- *example.com.* is the domain name that corresponds to the server.
- *1800* is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *A* is the record type.
- *93.184.216.34* is the IPv4 address of the server to which the domain name corresponds.

## AAAA record

An AAAA record defines the IP address to which the domain corresponds. The value of the AAAA record is the server IP address in IPv6 format that is associated with your domain name.

Here’s an example of an AAAA record response:

```
example.com. 16015 IN AAAA 2606:2800:220:1:248:1893:25c8:1946
```

In this record, here is what each component means:

- *example.com.* is the domain name that corresponds to the server.
- *16015* is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *AAAA* is the record type.
- *2606:2800:220:1:248:1893:25c8:1946* is the IPv6 address of the server to which the domain name corresponds.

## NS record

An NS record defines the name of the authoritative name servers (primary and secondary are mandatory) to which you delegate your domain zone (where your zone is hosted). <a href="https://gcore.com/dns" target="_blank">Gcore DNS hosting</a> provides the following name servers for your domains: *ns1.gcorelabs.net* and *ns2.gcdn.services*.  

Example of NS records response:

```
example.com. 1869 IN NS a.iana-servers.net
example.com. 1869 IN NS b.iana-servers.net
```

In these examples:

- *example.com.* is the domain name that delegates to the name servers.
- *1869* is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *NS* is the record type.
- *a.iana-servers.net* and *b.iana-servers.net* are the authoritative name servers that contain information about the domain zone, and all added DNS records.

## CNAME Record

A CNAME (canonical name) record redirects from the domain name it’s associated with to another domain name. They effectively create an alias, allowing one domain name to repeat the configuration of another. When the resolver receives CNAME as an answer, it makes another request, or potentially a chain of requests. Make sure your configuration does not result in a loop.

Here’s an example of a CNAME record response:

```
www.example.com. 3600 IN CNAME example.com.
```

For CNAME, here’s what each part of the record means:

- *www.example.com.* is the domain name that inherits all records from another domain.
- *3600* is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *CNAME* is the record type.
- *example.com.* is the target domain name whose records are inherited by the domain *www.example.com.*

## MX Record

An <a href="https://gcore.com/learning/dns-mx-record-explained/" target="_blank">MX record</a> defines the server that receives mail for the domain. 

Here’s an example of an MX record response:

```
example.com. 3600 IN MX 10 mail.example.com.
```

In the case of an MX record, here’s what each part means:

- *example.com.* is the domain name for which the MX record is created.
- *3600* is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *MX* is the record type.
- *10* is the priority of the mail server. If several servers are assigned for the domain, the server with the lowest priority will be the first to be contacted for mail delivery.
- *mail.example.com.* is the target host or the mail server which handles mail for *example.com.*

## TXT Record

A TXT record provides additional textual information about the domain. For example, you can use a TXT record to specify Sender Policy Framework (SPF) rules determining which mail servers are authorized to send emails to your domain.

Here’s an example of a TXT record response:

```
example.com. 15155 IN TXT "v=spf1 -all"
```

In this case:

- *example.com.* is the domain for which the SPF rules are set
- *15155* is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *TXT* is the record type.
- *"v=spf1 -all"* is the actual SPF rule. v=spf1 indicates the SPF version being used, and -all means that no IP addresses are authorized to send an email for the domain. Any email that claims to be from this domain should be considered spoofed and can be safely rejected or marked as spam.

## SRV Record

An SRV record identifies the server that provides specific services for the domain. For example, it can indicate the server providing internet telephony service (ITSP) for your domain.

Example of an SRV record response:

```
_sip._tcp.example.com. 3600 IN SRV 10 50 5060 sipserver.example.com.
```

For SRV records:

- *_sip._tcp.example.com.* is the name of the service and protocol used, as well as the domain that provides the service.
- *3600* is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *SRV* is the record type.
- *10* is the priority, with a smaller number having a higher priority.
- *50* is the weight used at equal priority for load balancing.
- *5060* is the port on which the service is provided.
- *sipserver.example.com.* is the target host or server providing the service.

## CAA Record

A CAA record specifies the certificate authorities (CAs) that are permitted to issue SSL/TLS certificates for the domain.

Here’s an example of a CAA record response:

```
example.com. IN CAA 0 issue "letsencrypt.org"
```

In this instance:

- *example.com.* is the domain for which the CAA record is set.
- *IN* is the class that stands for "internet."
- *CAA* is the record type.
- *0* is the flag value which can indicate specific policy restrictions for the record.
- *issue* is a tag that means that certificates can be issued by the specified certificate authority.
- *"letsencrypt.org"* is a value that points to a specific Certificate Authority. In this case, Let's Encrypt is the issuing CA for "example.com", and only this CA can issue the certificates for the domain.

## HTTPS Record

An HTTPS record provides information and connection parameters for accessing a web service via HTTPS.

Here’s an example of an HTTPS record response:

```
example.com.     	1800	IN	HTTPS	1 . alpn=h3,h3-29,h2 ipv4hint=1.2.3.4,9.8.7.6 ipv6hint=2001:db8:3333:4444:5555:6666:7777:8888,2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF
```

In this instance:

- *example.com.* is the domain for which the HTTPS record is defined.
- *1800* is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *HTTPS* is the record type.
- *1* is the priority, i.e., the number in the queue.
- *.* stands for the host if it is the same as the domain name.
- *alpn=h3,h3-29,h2* specifies the application protocol versions.
- *ipv4hint=1.2.3.4,9.8.7.6* specifies IPv4 addresses.
- *ipv6hint=2001:db8:3333:4444:5555:6666:7777:8888,2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF* specifies IPv6 addresses.

## SVCB Record

An SVCB record specifies the transport protocols supported by the service and any associated optional parameters. This includes, for example, HTTP/2 and HTTP/3 over QUIC, but the specification is general and not limited to HTTP.

Here’s an example of an SVCB record response:

```
example.com. 7200 IN SVCB 1 . alpn=h3
```

In an SVCB record:

- *example.com.* is the domain for which the SVCB record is set.
- *7200* is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *SVCB* is the record type.
- *1* is the record priority. The lower the number, the higher the priority. The value 0 is reserved for alias mode, and 1 or higher is for service mode.
- *.* is the TargetName. It's the domain name of the server providing the service. In this case, the “.” means the service is offered from the same domain as the one making the request, i.e., example.com.
- *alpn=h3* is a key-value pair from the SvcParamList. Here, alpn stands for "Application-Layer Protocol Negotiation" and h3 indicates support for HTTP/3.

## PTR Record

A PTR record maps an IP address to a domain or hostname. PTR records are primarily used for <a href="" target="_blank">reverse DNS lookups</a> and are necessary for certain applications, like some mail servers, that require sender domain verification.

**Note**: You can add a PTR record only if your zone is under the top-level domain (TLD) in-addr.arpa (for IPv4) or ip6.arpa (for IPv6). After creating a zone under these TLDs, you can create a PTR record in the UI.

Here’s an example of a PTR record response:

```
123.0.0.67.in-addr.arpa. 3600 IN PTR example.com.
```

In this case:

- *123.0.0.67.in-addr.arpa.* is the reverse DNS format of the IP address. It's written in the reverse order of the actual IP address, followed by in-addr.arpa for IPv4 addresses.
- *3600*  is the Time to Live (TTL) for the DNS record in seconds, which indicates how long the record is cached by servers or resolvers.
- *IN* is the class that stands for "internet."
- *PTR* is the record type.
- *example.com.* is the hostname or domain to which the IP address resolves.

## What's next?

Add the record you want according to the instructions: 

- <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing" target="_blank">Manage DNS records (advanced interface mode with balancing)</a>
- <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode" target="_blank">Manage DNS records (non-advanced interface mode)</a>
