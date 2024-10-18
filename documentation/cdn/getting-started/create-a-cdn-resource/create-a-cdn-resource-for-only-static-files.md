---
title: create-a-cdn-resource-for-only-static-files
displayName: For static files
published: true
order: 10
toc:
   --1--1. Start creation: "step-1-start-creation"
   --1--2. Choose acceleration type: "step-2-choose-acceleration-type"
   --1--3. Configure: "step-3-set-up-the-initial-configuration"
   --1--4. Set up DNS (add CNAME): "step-4-set-up-dns-add-cname"
   --1--5. Integrate with website: "step-5-integrate-the-cdn-resource-with-your-website"
   --1--Troubleshoot resource creation: "troubleshoot-resource-creation"
pageTitle: Guide to Create a CDN Resource for Static Assets | Gcore
pageDescription: Detailed instructions on how to set up a CDN resource for accelerating and protecting static assets on your website.
---
# Create a CDN resource for static assets 

## Step 1. Start creation 

Go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN</a> page and click **Create CDN resource**. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/cdn-resource-10.png" alt="Create CDN resource button" width="80%">  

## Step 2. Choose acceleration type

Select **Accelerate and protect static assets only** and then click **Confirm**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/cdn-resource-20.png" alt="Acceleration and protection type" width="50%">  

## Step 3. Set up the initial configuration

Fill in the fields to configure your CDN resource on the **Set up initial configuration** page.  

### 1. Specify a custom domain

Assign a custom domain as `cdn.<your website domain>` for delivering static files via Gcore CDN.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/add-custom-domain.png" alt="Initial configuration" width="80%">

For example, if your website is `yourwebsite.com`, enter `cdn.yourwebsite.com`. You will use that CNAME later to rewrite URLs in your website's source to deliver those resources through CDN. 

You can specify multiple domains by clicking the plus (+) icon. In <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files#step-5-integrate-the-cdn-resource-with-your-website" target="_blank">Step 5</a> you can configure your website to deliver different types of static files from separate domains. 

<alert-element type="warning" title="Warning">
 
After you create a CDN resource, you can’t change your custom domain, such as `cdn.yourdomain.com`. 
 
</alert-element>

### 2. Configure origin

An origin is a source (e.g., a website, an application, a private bucket) from where the CDN resource will request your content. In the Gcore Customer Portal, each origin is allocated to an <a href="https://gcore.com/docs/cdn/add-an-origin-group" target="_blank">origin group</a>. 

There are two options for configuring an origin: 

* **Specify content origin**. Select this option if you haven't previously created an origin group. Follow our instructions to <a href="https://gcore.com/docs/cdn/add-an-origin-group#step-2-enter-the-origin-group-name" target="_blank">add an origin group (step 2)</a>.

* **Select origins group**. Select this option if you already created the necessary origin group. Click the **Select the origin group** radio button, and choose the required group. This option is available only if you have existing groups.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/choose-origin-group.png" alt="Initial configuration" width="80%">

### 3. Add a description (optional)

Provide additional information about the CDN resource. This will not affect any settings but will only be displayed in the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN resources</a> section next to the resource CNAME.

## Step 4. Set up DNS (add CNAME)

Add a <a href="https://gcore.com/docs/dns/dns-records/supported-dns-record-types#cname-record" target="_blank">CNAME record</a> for the domain specified in <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files#step-3-set-up-the-initial-configuration" target="_blank">Step 3</a> as `cdn.yourwebsite.com`. Do so in your DNS provider's personal account. For a CNAME value, enter a subdomain shown in your Gcore Customer Portal as `*.gcdn.co`.

For example, in the following screenshot, the subdomain is `cl-1ab23456.gcdn.co`, so, for the `cdn.yourdomain.com` subdomain, you need to create a CNAME record with the value `cl-1ab23456.gcdn.co`. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/cdn-resource-40.png" alt="DNS setting" width="80%">  

If you specified additional domain names in <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files#step-3-set-up-the-initial-configuration" target="_blank">Step 3</a>, create CNAME records for them with the same value.

## Step 5. Integrate the CDN resource with your website

1\. Go to the admin panel of your origin website and change the URLs of static files. Replace the origin source domain with a custom domain of the CDN resource either by script or manually. 

For example, if a file path used to be `yourwebsite.com/images/image.jpg`, change it to `cdn.yourwebsite.com/images/image.jpg`. As a result, users will get static files from the CDN cache, and only the requests to the files that haven't yet been cached will be forwarded to your origin server.

If your site is built on a CMS (such as WordPress, Joomla, or Drupal) you can replace a domain name in file paths using special plugins. Find the right plugin and discover instructions for replacing the URLs in our guide on <a href="https://gcore.com/docs/cdn/getting-started/integrate-cdn-with-cms" target="_blank">integrating CDN with CMS</a>.

2\. Go back to the Gcore Customer Portal and click **Confirm**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/cdn-resource-50.png" alt="Integration" width="65%">  

That’s it! The CDN resource creation is completed. Click **Open resource settings** to view the resources and set up advanced settings.

If there is no text **... steps left** box in the upper-right corner of the screen, this means that the resource is correctly created and everything is working. If there are still some unfinished steps, check out the following section.

## Troubleshoot resource creation

If you see the **... steps left** box, something went wrong while creating or integrating the CDN resource. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/cdn-resource-60.png" alt="Issues" width="70%">  

To find out exactly where an error occurred:

1\. Click **Setup guide**. You will see a sliding panel indicating the status of each step of CDN resource creation. 

2\. Click **Check DNS setup status**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/cdn-resource-70.png" alt="Check DNS setup" width="70%">  

- If a CNAME record is configured correctly, it will be shown in the UI:

   <img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/image_1468.png" alt="Configured correctly" width="50%">  

- If an error occurs, a corresponding message will appear.

   <img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/cdn-resource-90.png" alt="Error message" width="50%">  

3\. Click **Next** in the **Setup your DNS section**. Click **Check your integration**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/cdn-resource-100.png" alt="Check your integration" width="70%"> 

If there are integration issues, you will see an error message. Contact [Gcore support](maito:support@gcore.com) or retry the integration according to our <a href="https://gcore.com/docs/cdn/getting-started/integrate-cdn-with-cms" target="_blank">instructions</a>.