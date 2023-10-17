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
   --2--Change name servers: "4-change-name-servers"
   --2--(Optional) Setup additional options: "5-optional-setup-additional-options"
pageTitle: Guide to Create a CDN Resource for the Entire Site | Gcore
pageDescription: Detailed instructions on how to set up a CDN resource for the entire website.
---
# Create a CDN resource for the entire site

## What is the CDN resource for the entire site used for?

A CDN resource of this type is a feature that allows you to accelerate and protect the entire site with CDN and DNS services. This CDN resource helps accelerate both kinds of content delivery: static and dynamic. If you only need to deliver static assets, use a <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">separate CDN resource for static content</a>.

We explain the difference in delivery in the "<a href="https://gcore.com/blog/how-to-speed-up-dynamic-content-delivery-using-cdn/" target="_blank">How to speed up dynamic content delivery using a CDN</a>" article.

## Create and integrate a CDN resource for the entire site

You don't need to change the site's code to create and integrate a CDN resource for the entire site.

**Note**: If one of the services (CDN or DNS) stops working, the site will also stop accelerating and working.

To create a CDN resource for the entire site:

### 1. Choose the acceleration type

Go to the <a href="https://cdn.gcore.com" target="_blank">CDN resources</a> tab and click **Create CDN resource**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site/13050309991441.png" alt="Choose the acceleration type">

The new page will open. Select "Accelerate and protect entire site" and click **Confirm**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site/13050295683601.png" alt="Acceleration and protection type" width="50%">

### 2. Enter a site name

**Note**: This step requires the creation of a DNS zone (similar to the site name) in the <a href="https://gcore.com/dns" target="_blank">Gcore DNS service</a>. In our example, a DNS zone will be *testdomain.com*. If you haven’t used the DNS service before, the Free plan will activate automatically at this step. If you have already used the DNS service, the specified DNS zone will also be created automatically, and you can view it in the <a href="https://dns.gcore.com" target="_blank">Control panel</a>.

Enter the domain of the site you want to create a CDN resource. You can use as a site name the following values:

- a second-level domain (*testdomain.com*),
- a third-level domain (*store.testdomain.com*, *blog.testdomain.com*, etc.),
- or a higher-level domain (*sales.store.testdomain.com*).

In all cases, a DNS zone in our control panel will be a second-level domain (e.g., *testdomain.com*). The only exception is for eTLD (effective top-level domains) like *co.uk*, where the DNS zone will consist of a subdomain and an effective top-level domain: *example.co.uk*.

You can also optionally enter the description of this CDN resource. The maximum comment length is 512 characters. When you complete the configuration, click **Confirm**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site/13050514395921.png" alt="Choose the acceleration type" width="50%">

**Note**:

1. If you try to specify a site name that already exists on another client's account, the procedure will be declined.

2. If you specify a site whose domain matches an existing DNS zone in your account, this DNS zone will be used for settings. The zone is not duplicated.

### 3. Review your DNS records

Our system looks for DNS records associated with your site domain at this step.

- If DNS records exist, they will be displayed automatically. You can edit or delete them or add a new record if necessary. Alternatively, you can skip this step. Click **Confirm** when the configuration is complete.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site/13050615347601.png" alt="If DNS records exist," width="80%">

- If no DNS records are found, a warning indicates that at least an A record should be added. Specify the subdomain or empty the "Name" field and the IP address. Then click **Add** and **Confirm**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site/13050648890385.png" alt="If no DNS records are found" width="80%">

### 4. Change name servers

If all the steps are completed successfully, a CDN resource and DNS zone will be automatically created for the site you specified in step 2.

To complete the site acceleration setup, log into your domain registrar account and replace the current name servers with the Gcore name servers and click **Confirm**:

```
ns1.gcorelabs.net  
ns2.gcdn.services
```

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site/13050764764177.png" alt="mceclip5.png" width="80%">

**Note**: The name servers can change. The current values will be specified on the wizard page.

Remember that the name server change can take up to 24 hours.

### 5. (Optional) Setup additional options

Optionally, you can activate additional features for your CDN resource. You can skip this step and return to additional settings later. Click **Confirm** to complete the creation and setup of your CDN resource.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site/13050821357329.png" alt="Setup additional options" width="80%">

After completing the creation and setup of your CDN resource, you will be automatically directed to the page of CDN resource settings. The resource settings header will show the name of the associated DNS zone. A warning will be displayed if the zone is not delegated to Gcore. This warning may persist for up to 24 hours until the NS servers are changed.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site/13050904896913.png" alt="Warning" width="50%">
