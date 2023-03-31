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
   --3--by ASN, country, or continent (Geo DNS): "balancing-by-asn-country--or-continent--geo-dns"
   --2--(Optional) A maximum number of responses: "8--optional--specify-the-maximum-number-of-responses"
   --2--Completing the configuration: "9-complete-the-configuration-and-create-resource-records"
   --1--Edit: "edit-a-dns-record"
   --1--Delete: "delete-a-dns-record"
---
  
   
  

This article explains how to create DNS records in the advanced mode of [Gcore DNS Hosting](https://gcore.com/dns). Interface mode differences are described in the "[Getting started with DNS](https://www.gcore.com/support/articles/360012142817/)" article.

<img src="https://support.gcore.com/hc/article_attachments/12986908920977" alt="mceclip0.png">  

## Create a DNS record

### 1. Go to records settings

Open the [All zones](https://dns.gcore.com/zones) tab and select the domain zone you want to add records for. Click the domain zone or click **Go to records** in the menu that appears when you click on three dots opposite the domain zone. Alternatively, click on the domain name in the "Quick zone selection" list on the left.

<img src="https://support.gcore.com/hc/article_attachments/12987072566929" alt="mceclip1.png">

The DNS record management page will open. Click **Add record set** there and proceed with other steps.

<img src="https://support.gcore.com/hc/article_attachments/12987146006929" alt="mceclip2.png">

### 2. Select the record type

In the "Type" section, select the type of DNS record. Our service supports the following types:

*   **A record**, which defines the IPv4 address the domain corresponds to. A record is for IPv4 addresses in the format _1.2.3.4_.
*   **AAAA record**, which defines the IPv6 address the domain corresponds to. AAAA record is for IPv6 addresses in the format _7625: 0d18: 1fa3: 07d7: 1f44: 8a2e: 07a0:_ _678h._ 
*   **NS record**, which defines the addresses of DNS servers serving the domain
*   **CNAME record**, which maps resource records of one domain to resource records of another
*   **MX record**, which defines the server that receives mail for the domain
*   **TXT record**, which defines auxiliary information about the domain, such as SPF rules
*   **SRV record**, which defines the server that operates certain services for the domain
*   **CAA record**, which defines the certificate authorities allowed issuing an SSL/TLS certificate for the domain name.

### 3. Specify the subdomain the record belongs to

In the "Name" field, specify which domain or subdomain the record belongs to.

*   Leave the field blank for the main domain (apex/naked domain),
*   Enter the name of the specific subdomain for a subdomain (e.g., "one" for _one.testdomain.com_), or
*   Enter an asterisk (\*) for all subdomains simultaneously (wildcard record).

### 4. Specify the content of the record

Fill in the "Content" field with an appropriate value for the record type.

| Record type | Value                                                                                                                                                                                                                                                                                       |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A           | The IPv4 address of the server hosting your website.Example: 1.2.3.4                                                                                                                                                                                                                      |
| AAAA        | The IPv6 address of the server hosting your website.Example: 7625:0d18:1fa3:07d7:1f44:8a2e:07a0:678h                                                                                                                                                                                      |
| NS          | The name of the zone you want to delegate your domain to.Example: ns1.example.com                                                                                                                                                                                                         |
| CNAME       | The domain or domain zone name that your domain should reference.Example: cdn.testdomain.com                                                                                                                                                                                              |
| MX          | The name of the mail server that receives mail for your domain.Example: ASPMX.L.GOOGLE.COMIf you use multiple mail servers, fill in the \"Priority\" field for each server. The lower the value in this field, the higher the priority.                                                 |
| SRV         | The canonical name of the machine providing the service. The SRV record contains 4 elements: priority, weight, port, and target.Example: 0 5 5060 sipserver.example.com                                                                                                                   |
| TXT         | Textual information the record should contain.Example: logmein-verification-code=976afe6f-8039-40e4-95a5-261b462                                                                                                                                                                          |
| CAA         | Defines the certificate authorities that are allowed to issue an SSL/TLS certificate for the domain name. The record consists of three parts separated by a space:CAA [flags] [tag] \"[value]\"The \"value\" must be enclosed in double-quotes (\"\").Example: 0 issue \"comodo.com\" |


### 5. Specify TTL

TTL (time to live) is the interval in seconds that servers on the internet use to check if the DNS records for your domain have changed. For example, an A-record has a TTL of 300. If you change the value of this record from "10.0.0.1" to "10.0.0.0", within 5 minutes, users requesting your domain will be sent to a server with IP 10.0.0.1 (this value will be stored in the cache of recursive DNS servers). However, after 5 minutes, the DNS server will check the settings and see the new value of the A-record. When your domain is requested, the DNS server will send users to the server with IP 10.0.0.0.

### 6. (Optional) Add additional records of the selected type

You can add multiple records of the same type to your domain. Click **Add record** to add another record.  A new line will appear, there you can enter the content of the second record and the associated metadata (read about metadata in [step 7](#)). Any record can be deleted by clicking the **—** button next to it.

### 7. (Optional) Configure balancing

Our DNS server can give different DNS records to different users, for example, sending users from Asia to an Asian server and European users to a European one. This is called balancing. To enable balancing, move the slider in the "Records selection using metadata" section. If balancing is not needed, leave the slider disabled and go to [step 8](#8--optional--specify-the-maximum-number-of-responses).

Balancing is based on the metadata you add to each record. You can add seven types of data: coordinates, ASN, continent, country, fallback, or notes. The system will check if a user corresponds to the specified parameters: if they do, the system will give the record; if not, it will not. For example, you can add metadata of the "continent" type with the value "Africa" to a record, which will only be given to users from Africa.

There are two types of balancing available: by coordinates and by ASN/country/continent.

#### **Balancing by coordinates (Geo Proximity)**

To assign coordinates to each record, add the **latlong** (latitude and longitude) type metadata to the records. When a user requests your domain, they will receive the record with the nearest coordinates. You can use the map icon to ensure you've entered the correct coordinates. Just click on the icon, and you'll see the location corresponding to your parameters.

For example, a user closer to the coordinate _51.52318152049715/-0.13458412218999416_ (the center of London) will receive an A-record with the value "10.0.0.1," while a user nearer to _48.859741241898114/2.3415648470109653_ (the center of Paris) will receive an A-record with the value "10.0.0.2."

<img src="https://support.gcore.com/hc/article_attachments/12988137986449" alt="mceclip3.png">

The configuration is complete. As soon as you finish creating records, balancing will work.

#### **Balancing by ASN, country, or continent (Geo DNS)**

You add metadata of different types to each record. When requesting a domain, a user will receive the record, if its metadata matches the users' characteristics.

You can add the metadata of five types:

*   asn — autonomous system number,
*   continents — continent,
*   countries — country,
*   fallback — add fallback metadata to the records, that should be sent if the user does not correspond to other metadata,
*   notes — any comments, this metadata type can be used as a field for notes; for example, you can specify a city, data center name, or a cluster name.

Our system will check if a user matches criteria from the metadata in the following order: ANS, country, continent. The choice of the answer is as follows:

1.  Our DNS server receives a request to the domain.
2.  The DNS server compares the user's ASN with the ASNs from the metadata. If they match, the server sends the record for which the user's ASN matches.
3.  If ASN doesn’t match or is not specified in the metadata, the server compares the user's country with the countries from the metadata. If they match, the server sends the record for which the user's country matches.
4.  If the ASN, and country do not match or are not specified in the metadata, the server compares the user's continent with the continents from the metadata. If they match, the server sends the record for which the user's continent matches.
5.  If the user does not match all the criteria above, then the server sends a record with fallback type metadata.

To start balancing by ASN, country, or continent, select "by non-coordinates meta". Add the required metadata for each record. To add multiple metadata to a single record, click the "+" button on the right. Metadata can be deleted using the "—" button.

**Example**. A Danish user with ASN 20001 makes a request to _testdomain.com_. Our DNS server will:

1.  Compare the ASN of the user with the ASN from the metadata. The number is specified for the upper record (123456), it does not match the user’s number (20001), and the upper record is not sent. The same for the lower record.
2.  Compare the user's country with the countries specified in the metadata. The country is specified only for the lower record (Finland), it does not match the user's country (Denmark), and the lower record is not sent.
3.  Compare the user's continent to the continents specified in the metadata. The continent is specified only for the upper record (Europe), it matches the user's continent (Europe). The upper record is sent, and the user goes to the server with IP 10.0.0.1.

<img src="https://support.gcore.com/hc/article_attachments/12988738927249" alt="mceclip5.png">

### 8. (Optional) Specify the maximum number of responses

If you use load balancing, fill in the "Max records per response" field. Here, you can specify the maximum number of records of the same type that can be sent to the user in a single response.

<img src="https://support.gcore.com/hc/article_attachments/12988743231249" alt="mceclip6.png">

**An example balancing by ASN/country/continent**. As a result of balancing, it turned out that four A-records are suitable for the user at once. If you enter the number "2" in the "Max records per response", our DNS server will send only two A-records. These records will be randomly selected from the four ones that match.

**An example balancing by coordinates**. Four A-records with different coordinates are available, and the number "2" is specified in the "Max records per response". Our DNS server will send the user two records with the nearest coordinates.

### 9. Complete the configuration and create resource records

After completing the configuration, click the **Create** button. DNS records with the specified parameters will be created.

<img src="https://support.gcore.com/hc/article_attachments/12988802225041" alt="mceclip7.png">

## Edit a DNS record

1. Open the record settings as described in [step 1](#1-go-to-records-settings) of the instructions above.

2. Click **Edit** in the menu that appears when you click on the three dots next to the desired resource record or on its name.

<img src="https://support.gcore.com/hc/article_attachments/12989011552529" alt="mceclip8.png">

3. Make the necessary changes.

4. Click **Save** or **Save and Close** to apply the new settings.

## Delete a DNS record 

1. Open the record settings as described in [step 1](#1-go-to-records-settings) of the instructions above.

2. Click **Delete** in the menu that appears when you click on the three dots next to the desired resource record.

<img src="https://support.gcore.com/hc/article_attachments/12989062101393" alt="mceclip9.png">

3. Confirm the deletion.
