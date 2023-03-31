---
title: manage-a-dns-zone
displayName: DNS zone
published: true
order: 20
toc:
   --1--What is a DNS zone?: "what-is-a-dns-zone"
   --1--Manage a DNS zone: "manage-a-dns-zone"
   --2--Create: "create-a-dns-zone"
   --2--Edit: "edit-a-dns-zone"
   --2--Delete: "delete-a-dns-zone"
---


What is a DNS zone
------------------

The DNS zone is the domain you delegate to Gcore authoritative NS servers. The following values can be used as the DNS zone: 

*   a second-level domain (_testdomain.com_),
*   a third-level domain (_store.testdomain.com_, _blog.testdomain.com,_ etc.),
*   or a higher-level domain (_sales.store.testdomain.com_).

When the DNS zone creation is completed, you can set the DNS records of your domain in [non-advanced](https://www.gcore.com/support/articles/4432592889617/) and [advanced](https://www.gcore.com/support/articles/360012179878/) modes.

Manage a DNS zone
-----------------

### Create a DNS zone

1\. Go to the [DNS](https://dns.gcore.com/) section and click the **Add zone** button. 

<img src="https://support.gcore.com/hc/article_attachments/13137090774673" alt="mceclip0.png">

2\. Enter a domain name for the DNS zone and click **Confirm**.

<img src="https://support.gcore.com/hc/article_attachments/13137238972689" alt="mceclip1.png">

3\. Review existing DNS records, and edit, delete, or add new records if necessary. Click **Confirm**. 

<img src="https://support.gcore.com/hc/article_attachments/13137695150865" alt="mceclip2.png">

4\. Go to your domain registrar account, replace the current nameservers with the Gcore Name Servers (ns1.gcorelabs.net and ns2.gcdn.services), and click **Confirm**.

<img src="https://support.gcore.com/hc/article_attachments/13138477756689" alt="mceclip3.png">

The created DNS zone will be displayed in the [All zones](https://dns.gcore.com/zones) section. 

<img src="https://support.gcore.com/hc/article_attachments/13138576729105" alt="mceclip4.png">

### Edit a DNS zone

1\. In the [All zones](https://dns.gcore.com/zones) section, click the three dots icon next to the desired DNS zone and select **Settings**.

<img style="font-size: large;" src="https://support.gcore.com/hc/article_attachments/13138699078673" alt="mceclip5.png">

The pop-up opens. Configure it according to the guide below and click **Save changes**. Configurations will be applied to the [SOA record](https://en.wikipedia.org/wiki/SOA_record#:~:text=A%20start%20of%20authority%20record,is%20specified%20in%20RFC%201035.) of this zone. 

<img src="https://support.gcore.com/hc/article_attachments/13138956496401" alt="mceclip6.png">

*   **Domain name**. This parameter cannot be edited. Create a new zone with the required domain name following the [instructions above](#create-a-dns-zone).
*   **Negative TTL**. This parameter is the time, in seconds, for which a negative response is cached. For example, a recursive DNS server requests an A-record for your domain, but that record does not exist on the authoritative NS servers. Even if you add the A record after, the DNS servers will still return a negative answer for the time specified in the "Negative TTL" field. 
*   **Primary DNS (available only for Enterprise tariff)**. In this parameter, you can specify the primary NS server that contains the information about all domain records.
*   **Contact (available starting from the Pro tariff).** In this parameter, you can specify the administrator's email address responsible for managing the DNS zone. 

### Delete a DNS zone 

1\. In the [All zones](https://dns.gcore.com/zones) section, click the three dots icon next to the desired DNS zone and select **Delete zone**.

<img src="https://support.gcore.com/hc/article_attachments/13141470744849" alt="mceclip7.png">

2\. Confirm the deletion in the pop-up window.
