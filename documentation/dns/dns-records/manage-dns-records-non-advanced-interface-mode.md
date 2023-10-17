---
title: manage-dns-records-non-advanced-interface-mode
displayName: Manage DNS records (non-advanced)
published: true
order: 20
toc:
   --1--Create: "create-a-dns-record"
   --2--Step 1. Records settings: "1-go-to-records-settings"
   --2--Step 2. Record type: "2-select-record-type"
   --2--Step 3. Domain or subdomain the record belongs to: "3-specify-subdomain-record-belongs-to"
   --2--Step 4. Content of the record: "4-specify-content-of-record"
   --2--Step 5. TTL: "5-specify-ttl"
   --2--Step 6. Completing the configuration: "6-complete-configuration-and-create-resource-record"
   --1--Edit: "edit-a-dns-record"
   --1--Delete: "delete-a-dns-record"
pageTitle: Managing DNS records in non-advanced mode | Gcore
pageDescription: Learn how to add, edit and delete DNS records in the non-advanced interface mode.
---
  
# Manage DNS records (non-advanced interface mode)
    
This article describes operations in the non-advanced mode of the "DNS" product interface. Differences in interfaces modes are described in the article "<a href="https://gcore.com/docs/dns/about-gcore-dns" target="_blank">About Gcore DNS</a>".

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/image_21__1_.png" alt="All zones" width="50%">

## Create a DNS record

### 1. Go to records settings

Open the “All zones” tab and select the domain zone you want to add records for. Click it or the **Go to records** button next to it.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/mceclip0.png" alt="All zones" width="80%">

Click **Add record**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/image_14__2_.png" alt="Add record" width="80%">

You will see the interface for adding new DNS record. Perform other steps in it.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/mceclip1.png" alt="DNS record" width="80%">

### 2. Select record type

In the "Type" section, select the type of DNS record you want to create: A, AAAA, NS, CNAME, MX, SRV, HTTPS, TXT, or CAA. Learn more about them in the article <a href="https://gcore.com/docs/dns/dns-records/supported-dns-record-types" target="_blank">Supported DNS record types</a>.

### 3. Specify subdomain record belongs to

In the “Name” field, specify the subdomain the record belongs to. To add a record for:

- main domain (apex/naked domain; in the picture above it is examplesite.co) — leave the field blank;
- apecific subdomain — enter the name of this subdomain (for example, if you enter "one", the record will be created for *one.example.com*);
- all subdomains at once (wildcard record) — enter an asterisk (*).

### 4. Specify content of record

Fill in the "Content" field. Enter a value appropriate for your record type.

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

### 5. Specify TTL

TTL (time to live) is the interval in seconds used by servers on the Internet to check if the DNS records for your domain have changed.

Example: A-record has a TTL of 300. You have changed the value of this record from “128.0.0.8” to “127.0.0.7”. Within 5 minutes, when requesting your domain, users will be sent to a server with IP 128.0.0.8 (this value will be stored in the cache of recursive DNS servers). But after 5 minutes, the DNS server will check the settings and see the new value of the A-record. Now, when your domain is requested, the DNS server will send users to the server with IP 127.0.0.7.

### 6. Complete configuration and create resource record

After completing the configuration, click the **Add** button. The DNS record with specified parameters will be created.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/image_20__1_.png" alt="All zones" width="80%">

You can check if the created record has been added correctly using the <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> tool.

## Edit a DNS record

1\. Go to records of the required DNS zone by clicking the zone name or the "Go to records" button. 

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/mceclip0.png" alt="Add record" width="80%">

2\. Click on the pencil icon next to the desired resource record.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/image_15.png" alt="DNS record" width="80%">

3\. Make changes. 

4\. Apply the new settings by clicking **Save**.

##  Delete a DNS record

1\. Go to records of the required DNS zone by clicking the zone name or the **Go to records** button. 

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/mceclip0.png" alt="DNS zone " width="80%">

2\. Click the wastebasket icon next to the desired resource record.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/image_17.png" alt="record" width="80%">

3\. Confirm deletion.
