---
title: manage-dns-records-non-advanced-interface-mode
displayName: Manage DNS records
published: true
order: 10
toc:
   --1--Create a DNS record: "create-a-dns-record"
   --1--Manage a DNS record: "manage-a-dns-record"
   --1--Delete: "delete-a-dns-record"
pageTitle: How to manage DNS records in non-advanced mode | Gcore
pageDescription: Learn how to add, edit and delete DNS records in the non-advanced interface mode.
---
# Manage DNS records

In this article, you will learn how to create and manage DNS records in the Gcore interface.

<alert-element type="info" title="Info">

Please note that the article is referring to a non-advanced interface. The toggle switch is displayed in the "off" position in the accompanying image:

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/image_21__1_.png" alt="All zones" width="70%">

If you want to configure balancing and dynamic response use a separate guide: <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing" target="_blank">Advance managing with balancing</a>.

</alert-element>

## Create a DNS record

1\. Navigate the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> tab and select the domain zone you want to add records for. Or click three dots on the right and **Go to records**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-10.png" alt="Open a DNS zone" width="80%">

2\. Click **Add record**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-20.png" alt="Add a record" width="80%">

You will see the interface for adding new DNS record. Perform other steps in it.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-40.png" alt="DNS record configuration" width="80%">

3\. In the “Type” section, select the type of DNS record you want to create: A, AAAA, NS, CNAME, MX, SRV, HTTPS, TXT, or CAA. Learn more about them in the article <a href="https://gcore.com/docs/dns/dns-records/supported-dns-record-types" target="_blank">Supported DNS record types</a>.

4\. In the “Name” field, specify the subdomain the record belongs to. There are several options:

- Leave the field blank to add a record for the main domain (apex/naked domain; in the picture above it is `sample-test.com`).
- Enter the name of this subdomain to add a record for a specific subdomain (for example, if you enter `one`, the record will be created for `one.sample-test.com`).
- Enter an asterisk (*) to add a record for all subdomains at once (wildcard record).

5\. In the “TTL” field, specify the TTL (Time To Live) in seconds. For example, an A record has a TTL of 300. You have changed the value of this record from `1.2.3.4` to `5.6.7.8`. Within 5 minutes, when requesting your domain, users will be sent to a server with IP `1.2.3.4` (this value will be stored in the cache of recursive DNS servers). But after 5 minutes, the DNS server will check the settings and see the new value of the A record. Now, when your domain is requested, the DNS server will send users to the server with IP `5.6.7.8`.

6\. In the field, enter a value appropriate for your record type.

<expandable-element title="Examples of values for different record types">

| Record type | Value                                                                                                               |  
|-------------|---------------------------------------------------------------------------------------------------------------------|
| A           | The IP address (IPv4) of the server of the web page that will open by your domain name. Example: *128.128.128.128*    |  
| AAAA        | The IP address (IPv6) of the server of the web page that will open by your domain name. Example: *7625:0d18:1fa3:07d7:1f44:8a2e:07a0:678h*                                                                                             | 
| NS          | The name of the zone you want to delegate your domain to. Example: *ns1.smth.com*                                      | 
| CNAME       | The domain or domain zone name that your domain should refer to. Example: *uuuuu8.cdn.co*                             |   
| MX          | The name of the mail server that receives mail for your domain. Example: *ASPMX.L.GOOGLE.COM* If you are using multiple mail servers, fill in the “Priority” field for each server. The lower the value in this field, the higher the priority.                                       |   
| SRV         | The canonical name of the machine providing the service.  Example: *sip.example.com*                                  | 
| HTTPS       | HTTPS is a resource record that provides information and parameters for how to access a web service available via HTTTS. <br>Example: *example.com. 1800 IN HTTPS 1 . alpn=h3,h3-29,h2 ipv4hint=1.2.3.4,9.8.7.6<br> ipv6hint=2001:db8:3333:4444:5555:6666:7777:8888,<br>2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF*                                                                         |  
| TXT         | Text information the record should contain. Example: *logmein-verification-code=976afe6f-8039-40e4-95a5-261b462*      | 
| CAA         | Defines the certificate authorities who are allowed to issue an SSL/TLS-certificate for the domain name. The recording consists of three parts which are separated by a space. CAA [flags] [tag] "[value]" The "value" must be enclosed in double-quotes (""). Example: _0 issue "comodo.com"_ |  

</expandable-element>

7\. Click the **Add** button. 

That's it. The DNS record with specified parameters will be created. You can check if the created record has been added correctly using the <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> tool.

## Manage a DNS record

1\. Navigate the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> tab and select the domain zone in which you want to manage records (edit or delete). Or click three dots on the right and **Go to records**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-10.png" alt="Open a DNS zone" width="80%">

2\. To edit the record click the pencil icon next to the desired record. 

3\. In the expandable block, make necessary changes in TTL or/and value.

4\. To delete the record click the corresponding button. 

5\. Apply the new settings by clicking **Save**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-50.png" alt="Edit or delete a DNS record" width="80%">