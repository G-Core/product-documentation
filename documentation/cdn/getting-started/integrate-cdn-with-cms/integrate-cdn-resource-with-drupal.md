---
title: integrate-cdn-resource-with-drupal
displayName: Drupal
published: true
order: 80
toc:
pageTitle: Integrate CDN with Drupal Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Drupal CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with Drupal

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to your Drupal site.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/1.png" alt="Login to your Drupal site">

Choose Modules in your Administration bar on top of the page.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/2.png" alt="Modules in your Administration bar">

As soon as you have downloaded CDN Module from Drupal.org, choose **Install new module** and download ```.zip```. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/3.png" alt=" CDN Module" width="50%">  
  
Upload CDN Module from your browser and install it.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/4.png" alt="Upload CDN Module" width="50%">  
  
If the installation was successful, you will see the following. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/5.png" alt="successful" width="50%">  
  
As soon as the CDN Module is successfully installed, get back to the modules list and scroll down to CDN. Choose **Enable** and Save configuration.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/6.png" alt="get back to the modules list" width="50%">

Select Configure in the CDN Module.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/7.png" alt="Select Configure in the CDN Module" width="50%">  

Change the CDN module status to Enabled and save the setting by hitting the Save Configuration button.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/8.png" alt="Change the CDN module status" width="50%">

Choose the "Details" tab on the right of the screen.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/9.png" alt="Details"> 

For the Mode choose Origin Pull and enter CNAME specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>.

Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.  
  
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/10.PNG" alt="Mode choose " width="80%">

Scroll down and choose Far Future expiration, then click Save Configuration.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/11.png" alt=" Far Future expiration" width="80%">

These steps are needed if you are going to deliver your CDN content via HTTPS. Choose the Other tab on the right of the CDN Module configuration screen.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/12.png" alt="Other ">  

Enable HTTPS to support SSL.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-drupal/13.png" alt="Enable HTTPS to support SSL."  width="50%">

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.