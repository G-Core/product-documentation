---
title: manage-dns-records-advanced-interface-mode-with-balancing
displayName: Manage DNS records (advanced mode)
published: true
order: 10
toc:
   --1--Create: "create-a-dns-record"
   --2--Step 1. Records settings: "1-go-to-records-settings"
   --2--Step 2. Record type: "2-select-the-record-type"
   --2--Step 3. Domain or subdomain the record belongs to: "3-specify-the-subdomain-the-record-belongs-to"
   --2--Step 4. Content of the record: "4-specify-the-content-of-the-record"
   --2--Step 5. TTL: "5-specify-ttl"
   --2--(Optional) Step 6. Additional records of the selected type: "6-optional-add-additional-records-of-the-selected-type"
   --2--(Optional) Step 7. Balancing: "7-optional-configure-balancing"
   --2--Step 8. Completing the configuration: "8-complete-the-configuration-and-create-resource-records"
   --1--Edit: "edit-a-dns-record"
   --1--Delete: "delete-a-dns-record"
pageTitle: Managing DNS records in advanced mode | Gcore
pageDescription: Learn how to add, edit and delete DNS records in the advanced interface mode with Geo Proximity and Geobalancing.
---
# Manage DNS records (advanced interface mode with balancing)
    

This article explains how to create DNS records in the advanced mode of <a href="https://gcore.com/dns" target="_blank">Gcore DNS Hosting</a>. Interface mode differences are described in the "<a href="https://gcore.com/docs/dns/about-gcore-dns" target="_blank">About Gcore DNS</a>" article.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12986908920977.png" alt="Manage DNS records" width="80%">  

## Create a DNS record

### 1. Go to records settings

Open the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> tab and select the domain zone you want to add records for. Click the domain zone or click **Go to records** in the menu that appears when you click on three dots opposite the domain zone. Alternatively, click on the domain name in the "Quick zone selection" list on the left.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12987072566929.png" alt="All zones tab " width="80%">

The DNS record management page will open. Click **Add record set** there and proceed with other steps.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12987146006929.png" alt="DNS record management page" width="80%">

### 2. Select the record type

In the "Type" section, select the type of DNS record you want to create: A, AAAA, NS, CNAME, MX, SRV, HTTPS, TXT, or CAA. Learn more about them in the article <a href="https://gcore.com/docs/dns/dns-records/supported-dns-record-types" target="_blank">Supported DNS record types</a>.

### 3. Specify the subdomain the record belongs to

In the "Name" field, specify which domain or subdomain the record belongs to.

- Leave the field blank for the main domain (apex/naked domain),
- Enter the name of the specific subdomain for a subdomain (e.g., "one" for *one.testdomain.com*), or
- Enter an asterisk (*) for all subdomains simultaneously (wildcard record).

### 4. Specify the content of the record

Fill in the "Content" field with an appropriate value for the record type.
 
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

TTL (time to live) is the interval in seconds that servers on the internet use to check if the DNS records for your domain have changed. For example, an A-record has a TTL of 300. If you change the value of this record from "10.0.0.1" to "10.0.0.0", within 5 minutes, users requesting your domain will be sent to a server with IP 10.0.0.1 (this value will be stored in the cache of recursive DNS servers). However, after 5 minutes, the DNS server will check the settings and see the new value of the A-record. When your domain is requested, the DNS server will send users to the server with IP 10.0.0.0.

### 6. (Optional) Add additional records of the selected type

You can add multiple records of the same type to your domain. Click **Add record** to add another record.  A new line will appear, there you can enter the content of the second record and the associated metadata (read about metadata in <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#7-optional-configure-balancing
" target="_blank">step 7</a>). Any record can be deleted by clicking the "—" button next to it.

### 7. (Optional) Configure balancing

Our DNS server can give different DNS records to different users, for example, sending users from Asia to an Asian server and European users to a European one. This is called balancing. To enable balancing, move the slider in the "Records selection using" section. If balancing is not needed, leave the slider disabled and go to <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#9-complete-the-configuration-and-create-resource-records" target="_blank">step 8</a>.

We have dedicated a separate article to balancing: <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing" target="_blank">Configure weight balancing and Geobalancing</a>. Please acquaint yourself with it to set it up correctly. 

### 8. Complete the configuration and create resource records

After completing the configuration, click the **Create** button. DNS records with the specified parameters will be created.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12988802225041.png" alt="Complete the configuration and create resource records" width="80%">

You can check if the created record has been added correctly using the <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> tool.

## Edit a DNS record

1\. Open the record settings as described in <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#1-go-to-records-settings" target="_blank">step 1</a> of the instructions above.

2\. Click **Edit** in the menu that appears when you click on the three dots next to the desired resource record or on its name.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12989011552529.png" alt="Edit a DNS record" width="80%">

3\. Make the necessary changes.

4\. Click **Save** or **Save and Close** to apply the new settings.

## Delete a DNS record 

1\. Open the record settings as described in <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#1-go-to-records-settings" target="_blank">step 1</a> of the instructions above.

2\. Click **Delete** in the menu that appears when you click on the three dots next to the desired resource record.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12989062101393.png" alt="Delete a DNS record " width="80%">

3\. Confirm the deletion.