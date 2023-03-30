---
title: create-a-cdn-resource-for-only-static-files
displayName: For static files
published: true
order: 10
toc:
---
You can create up to 30 CDN resources in one account. 

1\. In the "CDN" section, click "Create CDN resource".

<img src="https://support.gcore.com/hc/article_attachments/12946795803153" alt="mceclip0.png">  

2\. On the page that opens, select "Accelerate and protect only static files"

<img src="https://support.gcore.com/hc/article_attachments/5892806391441/image_1460.png" alt="image_1460.png">  

3\. Set up an initial configuration of your CDN resource. 

**Description (optional)**. You can add an internal comment about the CDN resource. It will not affect any setting, but it will be only displayed in the "[CDN resources](https://cdn.gcore.com/resources)" section next to the resource CNAME.  

**Origin.** If you have already created [origin groups](https://www.gcore.com/support/articles/214472385/), select the one you need from the list. If you don't have groups, specify a domain name or an IP address of a website that hosts the static content — the CDN will pull it from there. By default, the CDN connects to an origin via port 80 or 443. If you want to use a custom port, disable the "Use default port" option and indicate the required port. 

**Custom domain**. Create a [custom domain](https://www.gcore.com/support/articles/213969769/) as _cdn.\[your website domain\]_ for delivering static files via the CDN. For example, if your website is _yourdomain.com_, enter _cdn.yourdomain.com_. Dynamic content will be sent to users from _yourdomain.com_, while static files will be delivered from _cdn.yourdomain.com_. You can specify multiple domains in one go by clicking the "+" icon. Later in Step 5, you can configure your website to deliver different types of static files from separate domains. Please note that a custom domain such as _cdn__.yourdomain.com_ cannot be changed after creating a CDN resource. 

**SSL**. If you want to make your static files accessible over HTTPS, toggle on the "Enable HTTPS" feature. Choose one of two options: "Get free Let's Encrypt certificate" or "Add or select your own SSL certificate". When choosing the first one, an SSL certificate will be issued automatically for a domain of your CDN resource (_cdn.yourdomain.com)_ after Step 4 of this instruction. If you select the second option, you can add your own certificate using the instruction [Add an SSL certificate to transfer content over HTTPS](https://www.gcore.com/support/articles/213970109/).

<img src="https://support.gcore.com/hc/article_attachments/5892823242001/image_1461.png" alt="image_1461.png" width="459" height="647">

4\. Add a CNAME record for the domain that you specified in Step 3 as _cdn.yourdomain.com_. You need to do it in your DNS provider's personal account. For a CNAME value, enter a subdomain shown in our personal account as _\*.gcdn.co_. For example, in the screenshot below it is written as _cl-2db15545.gcdn.co_, so, for the _cdn.yourdomain.com_ subdomain, you need to create a CNAME record with the value _cl-2db15545.gcdn.co_. 

If you specified additional domain names in Step 3, create CNAME records for them with the same value as well.

<img src="https://support.gcore.com/hc/article_attachments/5892824019857/image_1462.png" alt="image_1462.png">  

5\. In the path of static files, replace the source domain with a custom domain of the CDN resource. For example, if a file path used to be _yourdomain.com/images/image.jpg_, change it to _cdn.yourdomain.com/images/image.jpg._ As a result, users will receive static files from the CDN cache, and only the requests to the files that haven't yet been cashed will be forwarded to your origin server.

*   **If your site is built on a CMS** (WordPress, Joomla, Drupal or other), you can replace a domain name in file paths using special plugins. You can find a necessary plugin and instructions for replacing the URLs in the [CMS Integration](https://www.gcore.com/support/sections/115001163705/) section.
*   **If your site is not built on a CMS**, replace a domain name in the URLs of static files manually.

<img src="https://support.gcore.com/hc/article_attachments/5892853730321/image_1463.png" alt="image_1463.png" width="602" height="395">  

6\. Optionally, you can activate additional features for your CDN resource. You can skip this step; you'll always be able to return to additional settings later.

Click "Confirm" to complete the creation and set-up of your CDN resource.

<img src="https://support.gcore.com/hc/article_attachments/9172768411665/mceclip0.png" alt="mceclip0.png">

The resource will be created automatically. You will see a page with its advanced settings. If there is no text box "... steps left" in the upper-right corner, everything is ok and the resource is working. 

If you see the "... steps left" text box, it means that something went wrong while creating or integrating the CDN resource. 

<img src="https://support.gcore.com/hc/article_attachments/5892906911249/image_1465.png" alt="image_1465.png" width="618" height="211">  
To find out exactly where an error occurred, click the "Setup guide" button at the top. You will see a sliding panel indicating the status of each step of CDN resource creation.

<img src="https://support.gcore.com/hc/article_attachments/5892871145617/image_1466.png" alt="image_1466.png" width="480" height="484">  
If a step is configured correctly, it will be shown in the UI.

<img src="https://support.gcore.com/hc/article_attachments/5892893732625/image_1468.png" alt="image_1468.png">  

If an error occurs, a corresponding message will appear.

<img src="https://support.gcore.com/hc/article_attachments/5892915910033/image_1467.png" alt="image_1467.png">  

In case of an error, go back to the instruction above and perform the necessary step again. If you need help, contact our support team via a live chat or [support@gcore.com](mailto:support@gcorelabs.com) — we will help you.