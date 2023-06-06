---
title: manage-dns-records-advanced-interface-mode-with-balancing
displayName: Manage DNS records (advanced mode)
published: true
order: 10
toc:
   --1--Create: "create-a-dns-record"
   --2--Records settings: "1-go-to-records-settings"
   --2--Record type: "2-select-the-record-type"
   --2--Domain or subdomain the record belongs to: "3-specify-the-subdomain-the-record-belongs-to"
   --2--Content of the record: "4-specify-the-content-of-the-record"
   --2--TTL: "5-specify-ttl"
   --2--(Optional) Additional records of the selected type: "6-optional-add-additional-records-of-the-selected-type"
   --2--(Optional) Balancing: "7-optional-configure-balancing"
   --3--by coordinates (Geo Proximity): "balancing-by-coordinates-geo-proximity"
   --3--by ASN, country, or continent (Geo DNS): "balancing-by-asn-country-or-continent-geo-dns"
   --2--(Optional) A maximum number of responses: "8-optional-specify-the-maximum-number-of-responses"
   --2--Completing the configuration: "9-complete-the-configuration-and-create-resource-records"
   --1--Edit: "edit-a-dns-record"
   --1--Delete: "delete-a-dns-record"
---

# Manage DNS records (advanced interface mode with balancing)
    

This article explains how to create DNS records in the advanced mode of <a href="https://gcore.com/dns" target="_blank">Gcore DNS Hosting</a>. Interface mode differences are described in the "<a href="https://gcore.com/docs/dns/about-gcore-dns" target="_blank">About Gcore DNS</a>" article.

<img src="https://support.gcore.com/hc/article_attachments/12986908920977" alt="">  

## Create a DNS record

### 1. Go to records settings

Open the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> tab and select the domain zone you want to add records for. Click the domain zone or click **Go to records** in the menu that appears when you click on three dots opposite the domain zone. Alternatively, click on the domain name in the "Quick zone selection" list on the left.

<img src="https://support.gcore.com/hc/article_attachments/12987072566929" alt="">

The DNS record management page will open. Click **Add record set** there and proceed with other steps.

<img src="https://support.gcore.com/hc/article_attachments/12987146006929" alt="">

### 2. Select the record type

In the "Type" section, select the type of DNS record. Our service supports the following types:

1. **А record**, which defines the IP address the domain corresponds to. A record is for IPv4 addresses of the form 128.128.128.128.
2. **AAAA record**, which defines the IP address the domain corresponds to. AAAA record is for IPv6 addresses of the form 7625: 0d18: 1fa3: 07d7: 1f44: 8a2e: 07a0: 678h.
3.  **NS** — defines addresses of DNS servers serving the domain.
4.  **CNAME record**, which maps resource records of one domain to resource records of another. If you specify a CNAME record for site.com with the value “anothersite.com", then when you open site.com it will have the same DNS records as anothersite.com has (for example, it will requests the same IP if A/AAAA records for anothersite.com exists).
5.  **MX record**, which defines the server that receives mail for the domain.
6.  **TXT record**, which defines auxiliary information about the domain. For example, you can specify Sender Policy Framework (SPF) rules that determine mail servers allowed to receive mail.
7.  **SRV record**, which defines the server that operates certain services for the domain.
8.  **CAA record** which defines the certificate authorities who are allowed to issue an SSL/TLS-certificate for the domain name.

### 3. Specify the subdomain the record belongs to

In the "Name" field, specify which domain or subdomain the record belongs to.

- Leave the field blank for the main domain (apex/naked domain),
- Enter the name of the specific subdomain for a subdomain (e.g., "one" for *one.testdomain.com*), or
- Enter an asterisk (*) for all subdomains simultaneously (wildcard record).

### 4. Specify the content of the record

Fill in the "Content" field with an appropriate value for the record type.

| Record type | Value                                                                                                               |  
|-------------|---------------------------------------------------------------------------------------------------------------------|
| A           | The IP address (IPv4) of the server of the web page that will open by your domain name. Example: *1.2.3.4*    |  
| AAAA        | The IP address (IPv6) of the server of the web page that will open by your domain name. Example: *7625:0d18:1fa3:07d7:1f44:8a2e:07a0:678h*                                                                                             | 
| NS          | The name of the zone you want to delegate your domain to. Example: *ns1.example.com*                                      | 
| CNAME       | The domain or domain zone name that your domain should refer to. Example: *cdn.testdomain.com*                             |   
| MX          | The name of the mail server that receives mail for your domain. Example: *ASPMX.L.GOOGLE.COM* If you are using multiple mail servers, fill in the “Priority" field for each server. The lower the value in this field, the higher the priority.                                       |   
| SRV         | The canonical name of the machine providing the service.  Example: *sip.example.com*                                  |   
| HTTPS       | HTTPS is a resource record that provides information and parameters for how to access a web service available via HTTTS. <br>Example: *example.com. 1800 IN HTTPS 1 . alpn=h3,h3-29,h2 ipv4hint=1.2.3.4,9.8.7.6<br> ipv6hint=2001:db8:3333:4444:5555:6666:7777:8888,<br>2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF*                                                                         |
| TXT         | Text information the record should contain. Example: *logmein-verification-code=976afe6f-8039-40e4-95a5-261b462*      | 
| CAA         | Defines the certificate authorities who are allowed to issue an SSL/TLS-certificate for the domain name. The recording consists of three parts which are separated by a space. CAA [flags] [tag] "[value]" The "value" must be enclosed in double-quotes (""). Example: _0 issue "comodo.com"_ |  


### 5. Specify TTL

TTL (time to live) is the interval in seconds that servers on the internet use to check if the DNS records for your domain have changed. For example, an A-record has a TTL of 300. If you change the value of this record from "10.0.0.1" to "10.0.0.0", within 5 minutes, users requesting your domain will be sent to a server with IP 10.0.0.1 (this value will be stored in the cache of recursive DNS servers). However, after 5 minutes, the DNS server will check the settings and see the new value of the A-record. When your domain is requested, the DNS server will send users to the server with IP 10.0.0.0.

### 6. (Optional) Add additional records of the selected type

You can add multiple records of the same type to your domain. Click **Add record** to add another record.  A new line will appear, there you can enter the content of the second record and the associated metadata (read about metadata in [step 7](#7-optional-configure-balancing)). Any record can be deleted by clicking the "—" button next to it.

### 7. (Optional) Configure balancing

Our DNS server can give different DNS records to different users, for example, sending users from Asia to an Asian server and European users to a European one. This is called balancing. To enable balancing, move the slider in the "Records selection using metadata" section. If balancing is not needed, leave the slider disabled and go to [step 8](#8-optional-specify-the-maximum-number-of-responses).

Balancing is based on the metadata you add to each record. You can add seven types of data: coordinates, ASN, continent, country, fallback, or notes. The system will check if a user corresponds to the specified parameters: if they do, the system will give the record; if not, it will not. For example, you can add metadata of the "continent" type with the value "Africa" to a record, which will only be given to users from Africa.

There are two types of balancing available: by coordinates and by ASN/country/continent.

#### Balancing by coordinates (Geo Proximity)

To assign coordinates to each record, add the **latlong** (latitude and longitude) type metadata to the records. When a user requests your domain, they will receive the record with the nearest coordinates. You can use the map icon to ensure you've entered the correct coordinates. Just click on the icon, and you'll see the location corresponding to your parameters.

For example, a user closer to the coordinate *51.52318152049715/-0.13458412218999416* (the center of London) will receive an A-record with the value "10.0.0.1", while a user nearer to *48.859741241898114/2.3415648470109653* (the center of Paris) will receive an A-record with the value "10.0.0.2".

<img src="https://support.gcore.com/hc/article_attachments/12988137986449" alt="" width="70%">

The configuration is complete. As soon as you finish creating records, balancing will work.

#### Balancing by ASN, country, or continent (Geo - DNS) 

You add metadata of different types to each record. When requesting a domain, a user will receive the record, if its metadata matches the users' characteristics.

You can add the metadata of five types:

- asn — autonomous system number,
- continents — continent,
- countries — country,
- fallback — add fallback metadata to the records, that should be sent if the user does not correspond to other metadata,
- notes — any comments, this metadata type can be used as a field for notes; for example, you can specify a city, data center name, or a cluster name.

Our system will check if a user matches criteria from the metadata in the following order: ANS, country, continent. The choice of the answer is as follows:

1.  Our DNS server receives a request to the domain.
2.  The DNS server compares the user's ASN with the ASNs from the metadata. If they match, the server sends the record for which the user's ASN matches.
3.  If ASN doesn’t match or is not specified in the metadata, the server compares the user's country with the countries from the metadata. If they match, the server sends the record for which the user's country matches.
4.  If the ASN, and country do not match or are not specified in the metadata, the server compares the user's continent with the continents from the metadata. If they match, the server sends the record for which the user's continent matches.
5.  If the user does not match all the criteria above, then the server sends a record with fallback type metadata.

To start balancing by ASN, country, or continent, select "by non-coordinates meta". Add the required metadata for each record. To add multiple metadata to a single record, click the "+" button on the right. Metadata can be deleted using the "—" button.

**Example**. A Danish user with ASN 20001 makes a request to *testdomain.com*. Our DNS server will:

1.  Compare the ASN of the user with the ASN from the metadata. The number is specified for the upper record (123456), it does not match the user’s number (20001), and the upper record is not sent. The same for the lower record.
2.  Compare the user's country with the countries specified in the metadata. The country is specified only for the lower record (Finland), it does not match the user's country (Denmark), and the lower record is not sent.
3.  Compare the user's continent to the continents specified in the metadata. The continent is specified only for the upper record (Europe), it matches the user's continent (Europe). The upper record is sent, and the user goes to the server with IP 10.0.0.1.

<img src="https://support.gcore.com/hc/article_attachments/12988738927249" alt="" width="70%">

### 8. (Optional) Specify the maximum number of responses

If you use load balancing, fill in the "Max records per response" field. Here, you can specify the maximum number of records of the same type that can be sent to the user in a single response.

<img src="https://support.gcore.com/hc/article_attachments/12988743231249" alt="" width="70%">

**An example balancing by ASN/country/continent**. As a result of balancing, it turned out that four A-records are suitable for the user at once. If you enter the number "2" in the "Max records per response", our DNS server will send only two A-records. These records will be randomly selected from the four ones that match.

**An example balancing by coordinates**. Four A-records with different coordinates are available, and the number "2" is specified in the "Max records per response". Our DNS server will send the user two records with the nearest coordinates.

### 9. Complete the configuration and create resource records

After completing the configuration, click the **Create** button. DNS records with the specified parameters will be created.

<img src="https://support.gcore.com/hc/article_attachments/12988802225041" alt="" width="70%">

## Edit a DNS record

1\. Open the record settings as described in [step 1](#1-go-to-records-settings) of the instructions above.

2\. Click **Edit** in the menu that appears when you click on the three dots next to the desired resource record or on its name.

<img src="https://support.gcore.com/hc/article_attachments/12989011552529" alt="">

3\. Make the necessary changes.

4\. Click **Save** or **Save and Close** to apply the new settings.

## Delete a DNS record 

1\. Open the record settings as described in [step 1](#1-go-to-records-settings) of the instructions above.

2\. Click **Delete** in the menu that appears when you click on the three dots next to the desired resource record.

<img src="https://support.gcore.com/hc/article_attachments/12989062101393" alt="">

3\. Confirm the deletion.