---
title: integrate-cdn-resource-with-drupal
displayName: Drupal
published: true
order: 80
toc:
---
# Integrate CDN resource with Drupal

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to your Drupal site.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000108205/1.png" alt="">

Choose Modules in your Administration bar on top of the page.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000108225/2.png" alt="">

As soon as you have downloaded CDN Module from Drupal.org, choose **Install new module** and download ```.zip```. 

<img src="https://support.gcore.com/hc/ru/article_attachments/115000108245/3.png" alt="" width="50%">  
  
Upload CDN Module from your browser and install it.  

<img src="https://support.gcore.com/hc/ru/article_attachments/115000103169/4.png" alt="" width="50%">  
  
If the installation was successful, you will see the following. 

<img src="https://support.gcore.com/hc/ru/article_attachments/115000102709/5.png" alt="" width="50%">  
  
As soon as the CDN Module is successfully installed, get back to the modules list and scroll down to CDN. Choose **Enable** and Save configuration.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000102749/6.png" alt="" width="50%">

Select Configure in the CDN Module.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000102769/7.png" alt="" width="50%">  

Change the CDN module status to Enabled and save the setting by hitting the Save Configuration button.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000108285/8.png" alt="" width="50%">

Choose the "Details" tab on the right of the screen.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000108325/9.png" alt=""> 

For the Mode choose Origin Pull and enter CNAME specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>.

Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.  
  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000102869/10.PNG" alt="" width="70%">

Scroll down and choose Far Future expiration, then click Save Configuration.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000108425/11.png" alt="" width="70%">

These steps are needed if you are going to deliver your CDN content via HTTPS. Choose the Other tab on the right of the CDN Module configuration screen.  

<img src="https://support.gcore.com/hc/ru/article_attachments/115000102969/12.png" alt="">  

Enable HTTPS to support SSL.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000102989/13.png" alt=""  width="50%">

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.