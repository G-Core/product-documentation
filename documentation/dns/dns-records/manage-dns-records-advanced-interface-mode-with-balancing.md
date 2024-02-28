---
title: manage-dns-records-advanced-interface-mode-with-balancing
displayName: Manage DNS records (advanced mode)
published: true
order: 10
toc:
   --1--Create: "create-a-dns-record"
   --2--Step 1. Records settings: "1-go-to-records-settings"
   --2--Step 2. Record type: "2-select-the-record-type"
   --2--Step 3. Domain or subdomain(s): "specify-the-domain-or-subdomains"
   --2--Step 4. TTL: "4-specify-ttl"
   --2--(Optional) Step 5. Dynamic response: "optional-5-configure-dynamic-response"
   --2--Step 6. Content: "6-input-the-content-of-the-record"
   --2--(Optional) Step 7. Additional records: "optional-7-add-additional-records-of-the-selected-type"
   --2--Step 8. Completing the configuration: "8-complete-the-configuration"
   --1--Edit: "edit-a-dns-record"
   --1--Delete: "delete-a-dns-record"
pageTitle: Managing DNS records in advanced mode | Gcore
pageDescription: Learn how to add, edit, and delete DNS records in the advanced interface mode with Geo Proximity and Geobalancing.
---
# Manage DNS records (advanced interface mode with dynamic response)
    

This article explains how to create DNS record sets (RRSets) in <a href="https://gcore.com/dns" target="_blank">Gcore DNS Hosting</a> advanced mode. Interface mode differences are described in our article <a href="https://gcore.com/docs/dns/about-gcore-dns" target="_blank">about Gcore DNS</a>.

To check if advanced mode is enabled, navigate to the DNS section of the Gcore Customer Portal. Ensure the toggle is enabled/green in order to continue managing DNS records according to this guide: 

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12986908920977.png" alt="Manage DNS records" width="80%">  

## Create a DNS record

### 1. Go to records settings

In the Gcore Customer Portal DNS area, open the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> tab and select the domain zone for which you want to add records. Either click the domain zone (either via “Quick zone selection” list on the left or under "Zone" in the main table) or click on three dots opposite the domain zone and then choose **Go to records**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12987072566929.png" alt="All zones tab " width="80%">

The page with your existing DNS records will open. Click **Add record set**.


<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12987146006929.png" alt="DNS record management page" width="80%">

A new page will open. Perform steps 2-7 there. The numbering in the image below refers to the steps that follow.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/dnsset-config.png" alt="How to configure RRSets in advanced mode" width="80%">

### 2. Select the record type

In the “Type” section, select the type of DNS record you want to create: A, AAAA, NS, CNAME, MX, SRV, HTTPS, TXT, or CAA. Learn more about them in our article about <a href="https://gcore.com/docs/dns/dns-records/supported-dns-record-types" target="_blank">supported DNS record types</a>.

### 3. Specify the domain or subdomain(s)

In the “Name” field, specify to which domain or subdomain the record belongs. You have three options:

1. Leave the field empty to add a record for the main domain (apex/naked domain.)
2. Enter the subdomain part (e.g., in ```one.sampledomain.com```, ```one``` is a subdomain) to add a record for the particular subdomain.
3. Enter ```*``` to add a record for all subdomains at once (wildcard record.)

### 4. Specify TTL

In the "TTL" field, enter the interval in seconds for which your domain records should be cached. 

<expandable-element title="TTL operation">

Let's take an example of an A record with a TTL of 300 seconds, equal to 5 minutes. Say you change the value of this record from ```10.0.0.1``` to ```10.0.0.0```. For up to 5 minutes, users requesting your domain will get a server with IP ```10.0.0.1``` (this value will be stored in the cache of recursive DNS servers). However, within a maximum of 5 minutes, the DNS server will see the new value of the A record and refresh its cache. When your domain is requested, the DNS server will send users to the server with IP ```10.0.0.0```. 

The point within the 300-second interval at which you changed the record determines how long it will take for users to access the new record. If you change the record 240 seconds into the TTL, users will wait only one minute; if you change it at 1 second, they will wait 4 minutes and 59 seconds. So, choose a TTL duration according to your maximum wait-time tolerance.

</expandable-element>

### (Optional) 5. Configure dynamic response

<alert-element type="note" title="Note">

The dynamic response feature is also available for the Free plan, but to create more than one dynamic RRset you'll need a paid plan.

</alert-element>

Gcore's DNS servers can give different DNS records to different users. For example, you can opt to send users in Asia to an Asian server and users in Europe to a European one. This is called dynamic response. Learn how to configure it in detail in our <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing" target="_blank">dedicated article</a>.  

To enable dynamic response, enable the "Dynamic response" toggle. If you don't require balancing, leave it disabled and go to <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#6-input-the-content-of-the-record" target="_blank">step 6</a>.

<alert-element type="tip" title="Tip">

You can also configure the dynamic response feature via API requests using dynamic RRsets. For more information about pickers and selectors, read the <a href="https://api.gcore.com/docs/dns#tag/RRsets/operation/CreateRRSet" target="_blank">API documentation</a>.

</alert-element>

### 6. Input the content of the record 

Fill in the “Content” field with an appropriate value for your record type:

<table>
<thead>
<tr>
<td>Record type</td>
<td>Value</td>
<tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">A</td>
<td style="text-align: left">The IP address (IPv4) of the server of the web page that will open by your domain name.<br> Example: ```128.128.128.128```</td>
</tr>
<tr>
<td style="text-align: left">AAAA</td>
<td style="text-align: left">The IP address (IPv6) of the server of the web page that will open by your domain name.<br> Example: ```7625:0d18:1fa3:07d7:1f44:8a2e:07a0:678h```</td>
</tr>
<tr>
<td style="text-align: left">NS</td>
<td style="text-align: left">The name of the zone you want to delegate your domain to. <br>Example: ```ns1.smth.com```</td>
</tr>
<tr>
<td style="text-align: left">CNAME</td>
<td style="text-align: left">The domain or domain zone name that your domain should refer to. <br>Example: ```uuuuu8.cdn.co```</td>
</tr>
<tr>
<td style="text-align: left">MX</td>
<td style="text-align: left">The name of the mail server that receives mail for your domain. Example: ```ASPMX.L.GOOGLE.COM``` <br>If you are using multiple mail servers, fill in the “Priority” field for each server.<br> The lower the value in this field, the higher the priority.</td>
</tr>
<tr>
<td style="text-align: left">SRV</td>
<td style="text-align: left">The canonical name of the machine providing the service.<br> Example: ```_sip._tcp.example.com. 3600 IN SRV 10 50 5060 sipserver.example.com```</td>
</tr>
<tr>
<td style="text-align: left">HTTPS</td>
<td style="text-align: left">HTTPS is a resource record that provides information and parameters for how to access a web service available via HTTTS.<br> Example: *example.com. 1800 IN HTTPS 1 . alpn=h3,h3-29,h2 ipv4hint=1.2.3.4,9.8.7.6
ipv6hint=2001:db8:3333:4444:5555:6666:7777:8888,
2001:db8:3333:4444:CCCC:DDDD:EEEE:FFFF*</td>
</tr>
<tr>
<td style="text-align: left">TXT</td>
<td style="text-align: left">Text information the record should contain.<br> Example: ```logmein-verification-code=976afe6f-8039-40e4-95a5-261b462```</td>
</tr>
<tr>
<td style="text-align: left">CAA</td>
<td style="text-align: left">Defines the certificate authorities who are allowed to issue an SSL/TLS-certificate for the domain name.<br> The recording consists of three parts which are separated by a space.<br> ```CAA [flags] [tag] "[value]"``` <br>The "value" must be enclosed in double-quotes ("").<br> Example: 0 issue "comodo.com"</td>
</tr>
</tbody>
</table>

You can also specify associated metadata, which is used for dynamic response configuration. Learn more in our <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing" target="_blank">dedicated metadata guide</a>.


### (Optional) 7. Add additional records of the selected type

To add multiple records of the same type, click **Add record**. A new line will appear. There, enter the content of the next record and associated metadata if needed. You can also delete any record by clicking the "—" button next to it or disable it via its toggle.

### 8. Complete the configuration

After completing the configuration, click the **Create** button. DNS records with the specified parameters will be created.

You can check if the created record has been added correctly using the <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> tool.

## Edit a DNS record

1\. Open the record settings as described in <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#1-go-to-records-settings" target="_blank">step 1</a> of the instructions above.

2\. Click on the three dots next to the desired resource record or on its name. In the menu that appears, click **Edit**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12989011552529.png" alt="Edit a DNS record" width="80%">

3\. Make the necessary changes.

4\. Click **Save** or **Save and Close** to apply the new settings.

## Delete a DNS record 

1\. Open the record settings as described in <a href="https://gcore.com/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing#1-go-to-records-settings" target="_blank">step 1</a> of the instructions above.

2\. Click on the three dots next to the desired resource record or on its name. In the menu that appears, click **Delete**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/12989062101393.png" alt="Delete a DNS record " width="80%">

3\. Confirm the deletion when prompted.