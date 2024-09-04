---
title: create-and-set-a-custom-domain-for-the-content-delivery-via-cdn
displayName: Create a custom domain (CNAME)
published: true
order: 30
toc:
   --1--What is a custom domain?: "what-is-a-custom-domain"
   --1--Set a custom domain: "set-a-custom-domain-only-for-static-cdn-recources"
   --1--Check DNS: "check-the-dns-setup-status"
   --1--Set an additional domain: "specify-additional-domain-only-for-static-cdn-recources"
pageTitle: Create and set a custom domain for content delivery via CDN | Gcore
pageDescription: A comprehensive guide on how to set up a custom domain (CNAME) in the Gcore Customer Portal and via Managed DNS for content delivery via CDN.
---
# Create and set a custom domain for the content delivery via CDN
  
## What is a custom domain?

A custom domain is a unique, branded domain name used for content delivery through a CDN. For example, if you have a website with the domain mywebsite.com, you create a CDN resource for static content delivery and specify a custom domain for it, such as cdn.mywebsite.com. This way, your static assets will be delivered to end users with URLs like cdn.mywebsite.com/sample.jpg. 

When specifying a custom domain, you can use any domain or subdomain for which you can edit the DNS records. Usually, for <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">CDN resources intended to deliver static assets</a>, our customers use a third-level domain based on their website domain, e.g. cdn.mywebsite.com. For <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site" target="_blank">CDN resources integrated with the entire site</a>—second-level domains, e.g., *mywebsite.com*. 

<alert-element type="caution" title="Caution">

You cannot change the custom domain once the CDN resource has been created. If you need to change domains, use [additional (multiple) domains](https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn#specify-additional-domain). This option is only available for CDN resources for static content, not for CDN resources integrated with the entire sites.

</alert-element>

## Set a custom domain (only for static CDN recources)

The instructions below describe how to set up a custom domain for static CDN resources with the addition of a CNAME record. Setting up a custom domain for CDN resources integrated with the entire site is different and involves delegating the domain to Gcore's NS servers. Check out the article to learn more: <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-the-entire-site#create-and-integrate-a-cdn-resource-for-the-entire-site" target="_blank">Create a CDN resource for the entire site</a>.   

1\. When <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">creating a CDN resource</a>, enter your desired domain or subdomain name in the "Custom domain" section. Specify additional domains by clicking the "+" icon. 

<alert-element type="warning" title="Warning">

You can only add additional (multiple) custom domains if you are creating a CDN resource for static assets. If you are creating a CDN resource for the entire site, adding additional custom domains is not possible.

</alert-element>

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865716431377.png" alt="Custom domain" width="70%">

2\. Copy the value _cl-\*\*\*\*.gcdn.co_ (which is unique for every account and the same for all custom domains of your account) from the "Set up your DNS" page. Click **Confirm**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865779424017.png" alt="Copy the value"  width="70%">

3\. Go to your DNS provider’s website and create a <a href="https://gcore.com/learning/dns-cname-record-explained/" target="_blank">CNAME record</a> for the custom domain with the value in the previous step. The CNAME record should be specified as follows:

```
cdn mywebsite.com. cl-****.gcdn.co 
```

Replace _cl-\*\*\*\*.gcdn.co_ with the value specific to your account.

If you specified multiple custom domains in step 1, add CNAME records for all additional custom domains.

Use the ```dig``` command in the terminal or an <a href="https://gcore.com/dev-tools/dns-lookup" target="_blank">online dig tool</a> to check the record. If the record was added correctly, you will receive a response similar to the one specified above.

4\. Complete the CDN resource creation. You will see the following pop-up window when all configurations are completed:

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865856535057.png" alt="Complete the CDN resource creation" width="50%">

## Check the DNS setup status

Our setup guide will verify that the configuration was completed successfully and identify any issues requiring resolution.

1\. Open the settings of the CDN resource that you created.

2\. Click "Setup guide".

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865899219729.png" alt="Setup guide" width="80%">

3\. A checklist will open, displaying each step of the configuration process. A check mark indicates that the step was successful. If any stage lacks a check mark, click on the step and follow the instructions to complete the configuration. When you're done, click **Check DNS setup status**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865917904145.png" alt="Setup Status" width="80%">

If you see the message "DNS record hasn’t been set up", check your Managed DNS settings for configuration errors.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865924935057.png" alt="check the DNS" width="50%">

If you see the message "DNS record has been successfully set up", the configuration has been completed correctly.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12865958946065.png" alt="completed correctly" width="50%">

To check the frontend of your integrated website, right-click on any static files and choose "Inspect". This will show you the content delivery URL where your file is served.

## Specify additional domain (only for static CDN resources)

1\. Go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN resource list</a> and click on the custom domain of the resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/cdn-resource-name.png" alt="CDN resource list " width="80%">

2\. In the "Custom domain" section, click the plus sign (+) next to the "Domain" field and enter your desired domain name(s).

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn/12866081938961.png" alt="Custom domain" width="80%">

3\. Click **Save changes** at the bottom of the page.

**Note**: Add a CNAME record to your DNS following the [instructions above](https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn#set-a-custom-domain) for each additional domain.

Once the additional domains are set up, you can configure your website to deliver different types of static files from separate domains.
