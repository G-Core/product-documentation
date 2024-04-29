---
title: advance-managing
displayName: Manage DNS records (advanced mode)
published: true
toc:
   --1--Create: "create-a-dns-record"
   --1--Manage: "edit-a-dns-record"
pageTitle: Manage DNS Records (Advanced Interface Mode with Dynamic Response) | Gcore
pageDescription: Learn how to add, edit, and delete DNS records in the advanced interface mode with Geo Proximity and Geobalancing.
customUrl: /dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing
---
# Manage DNS records (advanced interface mode with dynamic response)
    
This article explains how to create DNS record sets (RRSets) in <a href="https://gcore.com/dns" target="_blank">Gcore Managed DNS</a> advanced mode. 

To check if advanced mode is enabled, navigate to <a href="https://dns.gcore.com/" target="_blank">DNS</a> and open records page of the desired DNS zone by clicking on the domain:

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-10.png" alt="Open a DNS zone" width="80%">

Ensure the toggle is enabled/green in order to continue managing DNS records according to this guide: 

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/advanced-mode-dns-10.png" alt="How to ensure that advanced more is enabled" width="80%">  

## Create a DNS record

1\. Navigate the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> tab and select the domain zone you want to add records for. Or click three dots on the right and **Go to records**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-10.png" alt="Open a DNS zone" width="80%">

2\. The page with your existing DNS records will open. Click **Add record set**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/advanced-mode-dns-20.png" alt="Adding a record set (RRset)" width="80%">

A new page will open. Perform the remaining steps there.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/advanced-mode-dns-30.png" alt="How to configure RRSets in advanced mode" width="85%">

3\. In the “Type” section, select the type of DNS record you want to create: A, AAAA, NS, CNAME, MX, SRV, HTTPS, TXT, or CAA. Learn more about them in our article about <a href="https://gcore.com/docs/dns/dns-records/supported-dns-record-types" target="_blank">supported DNS record types</a>.

4\. In the “Name” field, specify the subdomain the record belongs to. There are several options:

- Leave the field blank to add a record for the main domain (apex/naked domain; in the picture above it is `sample-test.com`).
- Enter the name of this subdomain to add a record for a specific subdomain (for example, if you enter `one`, the record will be created for `one.sample-test.com`).
- Enter an asterisk (*) to add a record for all subdomains at once (wildcard record).

5\. In the “TTL” field, specify the TTL (Time To Live) in seconds. 

<expandable-element title="TTL operation">

Let's take an example of an A record with a TTL of 300 seconds, equal to 5 minutes. Say you change the value of this record from ```10.0.0.1``` to ```10.0.0.0```. For up to 5 minutes, users requesting your domain will get a server with IP ```10.0.0.1``` (this value will be stored in the cache of recursive DNS servers). However, within a maximum of 5 minutes, the DNS server will see the new value of the A record and refresh its cache. When your domain is requested, the DNS server will send users to the server with IP ```10.0.0.0```. 

The point within the 300-second interval at which you changed the record determines how long it will take for users to access the new record. If you change the record 240 seconds into the TTL, users will wait only one minute; if you change it at 1 second, they will wait 4 minutes and 59 seconds. So, choose a TTL duration according to your maximum wait-time tolerance.

</expandable-element>

6\. (Optional) Configure dynamic response.

<alert-element type="warning" title="Warning">

The dynamic response feature is also available for the Free plan, but to create more than one dynamic RRset you'll need a paid plan.

</alert-element>

Gcore's DNS servers can give different DNS records to different users. For example, you can opt to send users in Asia to an Asian server and users in Europe to a European one. This is called dynamic response. Learn how to configure it in detail in our <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing" target="_blank">dedicated article</a>.  

To enable dynamic response, enable the "Dynamic response" toggle. If you don't require balancing, leave it disabled and go to the next step.

You can also configure the dynamic response feature via API requests using dynamic RRsets. For more information about pickers and selectors, read the <a href="https://api.gcore.com/docs/dns#tag/RRsets/operation/CreateRRSet" target="_blank">API documentation</a>.

7\. Enable the toggle to make the value of the record active.

8\. In the field, enter a value appropriate for your record type.

<expandable-element title="Examples of values for different record types">

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

</expandable-element>

9\. You can also specify associated metadata, which is used for dynamic response configuration. Learn more in our <a href="https://gcore.com/docs/dns/dns-records/configure-weight-balancing-and-geobalancing" target="_blank">dedicated metadata guide</a>.

10\. (Optional) Click **Add record** if you want to specify several values for one record.

11\. A new module will appear. There, enter the content of the next record and associated metadata if needed. You can also delete any record by clicking the "—" button next to it or disable it via its toggle.

12\. Click **Create**. 

That's it! The DNS records with the specified parameters will be created. You can check if the created record has been added correctly using the <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">Gcore DNS Lookup</a> tool.

## Manage a DNS record

1\. Navigate the <a href="https://dns.gcore.com/zones" target="_blank">All zones</a> tab and select the domain zone in which you want to manage records (edit or delete). Or click three dots on the right and **Go to records**.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-non-advanced-interface-mode/dns-record-10.png" alt="Open a DNS zone" width="80%">

The new page will open. Perform the remaining steps there.

<img src="https://assets.gcore.pro/docs/dns/dns-records/manage-dns-records-advanced-interface-mode-with-balancing/advanced-mode-dns-40.png" alt="Manage DNS records" width="80%">

2\. Click on the three dots next to the desired resource record or on its name. 

3\. In the menu that appears, click **Edit record** if you want to edit the record.

4\.  In the menu that appears, click **Delete** if you want to delete the record.

