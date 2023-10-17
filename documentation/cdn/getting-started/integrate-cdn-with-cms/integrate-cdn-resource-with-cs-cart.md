---
title: integrate-cdn-resource-with-cs-cart
displayName: Cs-cart
published: true
order: 60
toc:
pageTitle: Integrate CDN with Cs-cart Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Cs-cart CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with Cs-cart

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns plugin might not help you.

You need to buy the plugin (unfortunately, there are no free plugins at the moment). You can buy it <a href="https://marketplace.cs-cart.com/add-ons/site-management/content-delivery-network-cs-cart-addon.html" target="_blank">here</a>. Install the plugin.  
Login to the CMS administration panel and go the Add-ons sections, Manage Add-ons. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-cs-cart/1eng.PNG" alt="CMS administration panel " width="50%">

Click on **+**.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-cs-cart/2eng.PNG" alt="Plus Button"> 

Choose the way to install the file. Click **Upload & Install**. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-cs-cart/3eng.PNG" alt="Upload & Install" width="80%">  

Having installed Universal CDN Add-on, go to its settings.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-cs-cart/4eng.PNG" alt="settings"> 

In the CDN URL field insert CNAME that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>.

Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-cs-cart/1.png" alt="Apply settings" width="80%">

Apply settings and enable the plugin.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.