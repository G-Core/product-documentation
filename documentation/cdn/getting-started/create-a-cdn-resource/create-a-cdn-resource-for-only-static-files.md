---
title: create-a-cdn-resource-for-only-static-files
displayName: For static files
published: true
order: 10
toc:
pageTitle: Guide to Create a CDN Resource for Static Assets | Gcore
pageDescription: Detailed instructions on how to set up a CDN resource for accelerating and protecting static assets on your website.
---
# Create a CDN resource for static assets only 

You can create up to 30 CDN resources in one account. 

1\. In the "CDN" section, click "Create CDN resource".

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/12946795803153.png" alt="CDN resource">  

2\. On the page that opens, select "Accelerate and protect only static files".

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/general/use-a-private-bucket-as-an-origin/image_1460.png" alt="Acceleration and protection type" width="50%">  

3\. Set up an initial configuration of your CDN resource. 

**Description (optional)**. You can add an internal comment about the CDN resource. It will not affect any setting, but it will be only displayed in the "<a href="https://cdn.gcore.com/resources" target="_blank">CDN resources</a>" section next to the resource CNAME.  

**Origin**. An origin is a source (e.g., a website, an application, a private bucket) from where the CDN resource will request the content. In the Gcore control panel, each origin is allocated to an origin group.

**Note**: The default timeout for CDN resources is set to 30 seconds. If the edge servers do not receive a response from the origin within this timeframe, they will respond either with an error or with an outdated cache file if <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/always-online-provide-the-stale-cache-if-the-origin-is-unavailable" target="_blank">Always Online</a> is enabled.

- If you didn’t create the origin group, choose the **Specify content origin** option and follow our instructions to <a href="https://gcore.com/docs/cdn/add-an-origin-group#step-3-select-the-type-of-origin-authentication" target="_blank">add an origin group (step 3)</a>. 
- If you created the origin group previously, choose the **Select origins group** option, click on the field, and select the required origin group.

**Custom domain**. Create a <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">custom domain</a> as *cdn.[your website domain]* for delivering static files via the CDN. For example, if your website is *yourdomain.com*, enter *cdn.yourdomain.com*. Dynamic content will be sent to users from *yourdomain.com*, while static files will be delivered from *cdn.yourdomain.com*. You can specify multiple domains in one go by clicking the "+" icon. Later in Step 5, you can configure your website to deliver different types of static files from separate domains. Please note that a custom domain such as *cdn.yourdomain.com* cannot be changed after creating a CDN resource. 

**SSL**. If you want to make your static files accessible over HTTPS, toggle on the "Enable HTTPS" feature. Choose one of two options: "Get free Let's Encrypt certificate" or "Add or select your own SSL certificate". When choosing the first one, an SSL certificate will be issued automatically for a domain of your CDN resource (*cdn.yourdomain.com*) after Step 4 of this instruction. If you select the second option, you can add your own certificate using the instruction <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/add-an-ssl-certificate-to-deliver-content-over-https" target="_blank">Add an SSL certificate to transfer content over HTTPS</a>.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/image1.png" alt="Initial configuration" width="80%">

4\. Add a CNAME record for the domain that you specified in Step 3 as *cdn.yourdomain.com*. You need to do it in your DNS provider's personal account. For a CNAME value, enter a subdomain shown in your Gcore personal account as _*.gcdn.co_. For example, in the screenshot below it is written as *cl-2db15545.gcdn.co*, so, for the *cdn.yourdomain.com* subdomain, you need to create a CNAME record with the value *cl-2db15545.gcdn.co*. 

If you specified additional domain names in Step 3, create CNAME records for them with the same value as well.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/image_1462.png" alt="DNS setting" width="80%">  

5\. In the path of static files, replace the source domain with a custom domain of the CDN resource. For example, if a file path used to be *yourdomain.com/images/image.jpg*, change it to *cdn.yourdomain.com/images/image.jpg*. As a result, users will receive static files from the CDN cache, and only the requests to the files that haven't yet been cashed will be forwarded to your origin server.

- **If your site is built on a CMS** (WordPress, Joomla, Drupal or other), you can replace a domain name in file paths using special plugins. You can find a necessary plugin and instructions for replacing the URLs in the "CMS Integration" section.
- **If your site is not built on a CMS**, replace a domain name in the URLs of static files manually.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/image_1463.png" alt="Integrate with your project" width="50%">  

6\. Optionally, you can activate additional features for your CDN resource. You can skip this step; you'll always be able to return to additional settings later.

Click "Confirm" to complete the creation and set-up of your CDN resource.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/mceclip0.png" alt="Quick option setup" width="80%">

The resource will be created automatically. You will see a page with its advanced settings. If there is no text box ```... steps left``` in the upper-right corner, everything is ok and the resource is working. 

If you see the ```... steps left``` text box, it means that something went wrong while creating or integrating the CDN resource. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/image_1465.png" alt="Setup guide in Control panel" width="80%"> 

To find out exactly where an error occurred, click the "Setup guide" button at the top. You will see a sliding panel indicating the status of each step of CDN resource creation.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/image_1466.png" alt="Setup guide" width="80%"> 

If a step is configured correctly, it will be shown in the UI.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/image_1468.png" alt="Configured correctly" width="50%">  

If an error occurs, a corresponding message will appear.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files/image_1467.png" alt="Error message" width="50%">  

In case of an error, go back to the instruction above and perform the necessary step again. If you need help, contact our support team via a live chat or [support@gcore.com](mailto:support@gcore.com) — we will help you.