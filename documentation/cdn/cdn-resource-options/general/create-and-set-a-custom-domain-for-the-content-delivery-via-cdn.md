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
---
  
  
  

What is a custom domain?
------------------------

A custom domain is a domain name used for content delivery through a CDN. For example, if you have a website with the domain _mywebsite.com_, you create a CDN resource for static content delivery and specify a custom domain for the resource, such as _cdn.mywebsite.com._ This way, your static assets will be delivered to end-users with URLs like _cdn.mywebsite.com/sample.jpg_. 

When specifying a custom domain, you can use any domain or subdomain for which you can edit the DNS records (typically, our clients use a third-level subdomain based on the website domain). 

**Note:** The main custom domain must be specified when creating the CDN resource and cannot be changed afterward. If you want to use a different domain, you’ll need to add multiple domains. Learn how to do this in the [Specify additional domain](#specify-additional-domain) module.

Set a custom domain
-------------------

1\. When [creating a CDN resource](https://www.gcore.com/support/articles/213969429/), enter your desired domain or subdomain name in the "Custom domain" section (Step #3). You can also specify multiple domains by clicking the "+" icon.  

<img src="https://support.gcore.com/hc/article_attachments/12865716431377" alt="mceclip0.png">2\. Continue with the creation of the CDN resource.

3\. Copy the value _cl-\*\*.gcdn.co_ (which is unique for every account and the same for all custom domains of your account) from the "Set up your DNS" page. You can click **Confirm** at this step or later.

<img src="https://support.gcore.com/hc/article_attachments/12865779424017" alt="mceclip1.png">4\. Go to your DNS provider’s website. 

5\. Create a [CNAME record](https://en.wikipedia.org/wiki/CNAME_record) for the custom domain with the value copied in step 3 of this guide. The CNAME record should be specified as follows:

cdn mywebsite.com. cl-\*\*\*\*.gcdn.co 

Replace _cl-\*\*\*\*.gcdn.co_ will the value specific to your account.

If you specified multiple custom domains in step 1, add CNAME records for all additional custom domains.

You can use the _dig_ command in the terminal or an [online dig tool](https://toolbox.googleapps.com/apps/dig/) to check the record. If the record was added correctly, you should receive a response similar to the one specified above.

6\. Complete the CDN resource creation. You will see the following pop-up when all configurations are completed:

<img src="https://support.gcore.com/hc/article_attachments/12865856535057" alt="mceclip2.png">

Check the DNS setup status
--------------------------

The "Setup Guide" will help verify that the configuration was completed successfully. If you see this message, this indicates that something is incorrect or missing in the configuration.

1\. Open the settings of the created CDN resource.

2\. Click on "Setup guide".

<img src="https://support.gcore.com/hc/article_attachments/12865899219729" alt="mceclip3.png">

3\. A drawer will open, displaying each step of the configuration process. A check mark indicates that the step was successful. If there is no check mark, click on the step and follow the instructions to complete the configuration. When the setup is finished, click **Check DNS Setup Status**.

<img src="https://support.gcore.com/hc/article_attachments/12865917904145" alt="mceclip4.png">

*   If you see the message "DNS record hasn’t been set up", something has gone wrong. Please check the DNS hosting settings.

<img src="https://support.gcore.com/hc/article_attachments/12865924935057" alt="mceclip5.png">

*   If you see the message "DNS record has been successfully set up", the configuration has been completed correctly.

<img src="https://support.gcore.com/hc/article_attachments/12865958946065" alt="mceclip6.png">

To check the front end of your integrated website, right-click on any static files and choose "Inspect". This will show you the content delivery URL where your file is served.

Specify additional domain
-------------------------

1\. Go to the [CDN resource list](https://www.cdn.gcore.com/resources/list) and click on the custom domain of the resource you want to configure.

<img src="https://support.gcore.com/hc/article_attachments/12866059375761" alt="mceclip7.png">

2\. In the "Custom domain" section, click the plus sign (+) next to the "Domain" field and enter your desired domain name. You can add several domains.

<img src="https://support.gcore.com/hc/article_attachments/12866081938961" alt="mceclip8.png">3\. Click **Save changes** at the bottom of the page.

**Note**: You need to add a CNAME record to your DNS following the [instructions above](#set-a-custom-domain) for each additional domain.

Once the additional domains are set up, you can configure your website to deliver different types of static files from separate domains.