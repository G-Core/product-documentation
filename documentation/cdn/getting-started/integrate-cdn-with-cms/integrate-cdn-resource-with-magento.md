---
title: integrate-cdn-resource-with-magento
displayName: Magento
published: true
order: 140
toc:
pageTitle: Integrate CDN with Magento Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Magento CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with Magento

Before you take any steps, please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.
 
For additional information about the Magento platform, please refer to the <a href="https://business.adobe.com/products/magento/magento-commerce.html" target="_blank">Magento official website</a>.

Login to your Magento Admin Panel. Click the System tab at the top navigation bar and choose Configuration as shown in the picture below.

Scroll down to the bottom. In the Advanced section select Developer where you will see two sections: JavaScript Settings and CSS Settings. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-magento/magento2.png" alt="Advanced section " width="80%">  

Choose Merge JavaScript Files and Merge CSS Filesoptions. Note that this may affect the design of some e-shops so you need to test this. But in general, it is recommended to enable these options to reduce the number of requests.

Then go to the General section and select the Web. Here you will find two sections: Unsecure and Secure.

If your website is operating without SSL certificate (HTTP), you should select the Unsecure section. If your website is operating with SSL certificate (HTTPS), you should select the Secure section.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-magento/magento3.png" alt="Secure section" width="80%"> 

Type in your CNAME that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

Click Save Config to save changes.

Use the Current Configuration Scope drop-down menu to choose Main Website.

Starting with sidebar follow this way: Web > Unsecure > Base Skin URL. Remove the tick from the Use Default box and type in your CNAME in the Base Skin URL field.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-magento/magento4.png" alt="Base Skin URL" width="80%">  
   

Save changes.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that, press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.