---
title: create-a-cdn-resource-for-the-entire-site
displayName: For the entire site
published: true
order: 20
toc:
   --1--What is the CDN resource for the entire site used for?: "what-is-the-cdn-resource-for-the-entire-site-used-for"
   --1--Create and integrate the CDN resource: "create-and-integrate-a-cdn-resource-for-the-entire-site"
   --2--Choose the acceleration type: "1-choose-the-acceleration-type"
   --2--Enter a site name: "2-enter-a-site-name"
   --2--Review your DNS records: "3-review-your-dns-records"
   --2--Change nameservers: "4-change-nameservers"
   --2--(Optional) Setup additional options: "5--optional--setup-additional-options"
---
  
:  
    1.  
    2.  
    3.  
    4.  
    5.  

What is the CDN resource for the entire site used for?
------------------------------------------------------

A CDN resource of this type is a feature that allows you to accelerate and protect the entire site with CDN and DNS services. This CDN resource helps accelerate both kinds of content delivery: static and dynamic. If you only need to deliver static assets, use a [separate CDN resource for static content](https://www.gcore.com/support/articles/213969429/).

We explain the difference in delivery in the "[How to speed up dynamic content delivery using a CDN](https://www.gcore.com/materials/how-to-speed-up-dynamic-content-delivery-using-cdn/)" article.

Create and integrate a CDN resource for the entire site
-------------------------------------------------------

You don't need to change the site's code to create and integrate a CDN resource for the entire site.

**Note:** If one of the services (CDN or DNS) stops working, the site will also stop accelerating and working.

To create a CDN resource for the entire site:

### 1\. Choose the acceleration type

Go to the [CDN resources](https://cdn.gcore.com/) tab and click **Create CDN resource**.

<img src="https://support.gcore.com/hc/article_attachments/13050309991441" alt="mceclip0.png" width="640" height="369">

The new page will open. Select "Accelerate and protect entire site" and click **Confirm**.

<img src="https://support.gcore.com/hc/article_attachments/13050295683601" alt="mceclip1.png" width="640" height="275">

### 2\. Enter a site name

**Note**: This step requires the creation of a DNS zone (similar to the site name) in the [Gcore DNS service](https://www.gcore.com/dns). In our example, a DNS zone will be _testdomain.com_. If you haven’t used the DNS service before, the Free plan will activate automatically at this step. If you have already used the DNS service, the specified DNS zone will also be created automatically, and you can view it in the [control panel](https://dns.gcore.com/).

Enter the domain of the site you want to create a CDN resource. You can use as a site name the following values:

*   a second-level domain (_testdomain.com_),
*   a third-level domain (_store.testdomain.com_, _blog.testdomain.com,_ etc.),
*   or a higher-level domain (_sales.store.testdomain.com_).

In all cases, a DNS zone in our control panel will be a second-level domain (e.g., _testdomain.com_). The only exception is for eTLD (effective top-level domains) like _co.uk_, where the DNS zone will consist of a subdomain and an effective top-level domain: _example.co.uk_.

You can also optionally enter the description of this CDN resource. The maximum comment length is 512 characters. When you complete the configuration, click **Confirm**.

<img src="https://support.gcore.com/hc/article_attachments/13050514395921" alt="mceclip2.png" width="639" height="359">

**Note**:

1\. If you try to specify a site name that already exists on another client's account, the procedure will be declined.

2\. If you specify a site whose domain matches an existing DNS zone in your account, this DNS zone will be used for settings. The zone is not duplicated.

### 3\. Review your DNS records

Our system looks for DNS records associated with your site domain at this step.

*   If DNS records exist, they will be displayed automatically. You can edit or delete them or add a new record if necessary. Alternatively, you can skip this step. Click **Confirm** when the configuration is complete.

<img src="https://support.gcore.com/hc/article_attachments/13050615347601" alt="mceclip3.png" width="640" height="450">

*   If no DNS records are found, a warning indicates that at least an A record should be added. Specify the subdomain or empty the "Name" field and the IP address. Then click **Add** and **Confirm**.

<img src="https://support.gcore.com/hc/article_attachments/13050648890385" alt="mceclip4.png" width="640" height="594">

### 4\. Change nameservers

If all the steps are completed successfully, a CDN resource and DNS zone will be automatically created for the site you specified in step 2.

To complete the site acceleration setup, log into your domain registrar account and replace the current nameservers with the Gcore Name Servers and click **Confirm**:

ns1.gcorelabs.net  
ns2.gcdn.services

**<img src="https://support.gcore.com/hc/article_attachments/13050764764177" alt="mceclip5.png" width="640" height="846">**

**Note**: The Name Servers can change. The current values will be specified on the wizard page.

Remember that the name server change can take up to 24 hours.

### 5\. (Optional) Setup additional options

Optionally, you can activate additional features for your CDN resource. You can skip this step and return to additional settings later. Click **Confirm** to complete the creation and setup of your CDN resource.

<img src="https://support.gcore.com/hc/article_attachments/13050821357329" alt="mceclip6.png" width="640" height="920">

After completing the creation and setup of your CDN resource, you will be automatically directed to the page of CDN resource settings. The resource settings header will show the name of the associated DNS zone. A warning will be displayed if the zone is not delegated to Gcore. This warning may persist for up to 24 hours until the NS servers are changed.

<img src="https://support.gcore.com/hc/article_attachments/13050904896913" alt="mceclip7.png" width="648" height="234">