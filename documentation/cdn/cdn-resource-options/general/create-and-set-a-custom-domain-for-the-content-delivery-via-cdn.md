---
title: create-and-set-a-custom-domain-for-the-content-delivery-via-cdn
displayName: Create a custom domain (CNAME)
published: true
order: 30
toc:
   --1--What is a custom domain?: "what-is-a-custom-domain"
   --1--Set a custom domain: "set-a-custom-domain"
   --1--Check DNS: "check-the-dns-setup-status"
   --1--Set an additional domain: "specify-additional-domain"
pageTitle: Understanding a CDN Domain | Gcore
pageDescription: A comprehensive guide on how to set up a custom domain in the control panel and on the DNS hosting side for content delivery via CDN.
---
# Create and set a custom domain for the content delivery via CDN
  
## What is a custom domain?

A custom domain is a domain name used for content delivery through a CDN. For example, if you have a website with the domain _mywebsite.com_, you create a CDN resource for static content delivery and specify a custom domain for the resource, such as _cdn.mywebsite.com._ This way, your static assets will be delivered to end-users with URLs like _cdn.mywebsite.com/sample.jpg_. 

When specifying a custom domain, you can use any domain or subdomain for which you can edit the DNS records (typically, our clients use a third-level subdomain based on the website domain). 

**Note:** The main custom domain must be specified when creating the CDN resource and cannot be changed afterward. If you want to use a different domain, you’ll need to add multiple domains. Learn how to do this in the [Specify additional domain](https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn#specify-additional-domain) module.

## Set a custom domain

1\. When <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">creating a CDN resource</a>, enter your desired domain or subdomain name in the "Custom domain" section (Step #3). You can also specify multiple domains by clicking the "+" icon.  

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865716431377.png" alt="Custom domain" width="50%">

2\. Continue with the creation of the CDN resource.

3\. Copy the value _cl-\*\*\*\*.gcdn.co_ (which is unique for every account and the same for all custom domains of your account) from the "Set up your DNS" page. You can click **Confirm** at this step or later.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865779424017.png" alt="Copy the value"  width="50%">

4\. Go to your DNS provider’s website. 

5\. Create a <a href="https://en.wikipedia.org/wiki/CNAME_record" target="_blank">CNAME record</a> for the custom domain with the value copied in step 3 of this guide. The CNAME record should be specified as follows:

```
cdn mywebsite.com. cl-****.gcdn.co 
```

Replace _cl-\*\*\*\*.gcdn.co_ will the value specific to your account.

If you specified multiple custom domains in step 1, add CNAME records for all additional custom domains.

You can use the ```dig``` command in the terminal or an <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">online dig tool</a> to check the record. If the record was added correctly, you should receive a response similar to the one specified above.

6\. Complete the CDN resource creation. You will see the following pop-up when all configurations are completed:

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865856535057.png" alt="Complete the CDN resource creation" width="50%">

## Check the DNS setup status

The "Setup Guide" will help verify that the configuration was completed successfully. If you see this message, this indicates that something is incorrect or missing in the configuration.

1\. Open the settings of the created CDN resource.

2\. Click on "Setup guide".

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865899219729.png" alt="Setup guide" width="80%">

3\. A drawer will open, displaying each step of the configuration process. A check mark indicates that the step was successful. If there is no check mark, click on the step and follow the instructions to complete the configuration. When the setup is finished, click **Check DNS Setup Status**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865917904145.png" alt="Setup Status" width="80%">

- If you see the message "DNS record hasn’t been set up", something has gone wrong. Please check the DNS hosting settings.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865924935057.png" alt="check the DNS" width="50%">

- If you see the message "DNS record has been successfully set up", the configuration has been completed correctly.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865958946065.png" alt="completed correctly" width="50%">

To check the front end of your integrated website, right-click on any static files and choose "Inspect". This will show you the content delivery URL where your file is served.

## Specify additional domain

1\. Go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN resource list</a> and click on the custom domain of the resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12866059375761.png" alt="CDN resource list " width="80%">

2\. In the "Custom domain" section, click the plus sign (+) next to the "Domain" field and enter your desired domain name. You can add several domains.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12866081938961.png" alt="Custom domain" width="80%">

3\. Click **Save changes** at the bottom of the page.

**Note**: You need to add a CNAME record to your DNS following the [instructions above](https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn#set-a-custom-domain) for each additional domain.

Once the additional domains are set up, you can configure your website to deliver different types of static files from separate domains.