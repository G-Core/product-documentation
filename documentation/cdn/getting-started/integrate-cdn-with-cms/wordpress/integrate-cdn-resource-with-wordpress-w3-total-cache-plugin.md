---
title: integrate-cdn-resource-with-wordpress-w3-total-cache-plugin
displayName: W3 Total Cache plugin
published: true
order: 30
toc:
pageTitle: Integrate CDN with W3 Total Cache plugin for WordPress Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with the W3 Total Cache plugin for CMS WordPress to enhance your site's speed and user experience.
---
# Integrate CDN resource with WordPress (W3 Total Cache plugin)

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns plugin might not help you.

Login to your Wordpress blog at *yoursite.com/wp-admin* and click **Enter**.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/01.PNG" alt="Login to your Wordpress blog" width="50%">  
  
Add new plugin in the "Plugins" section.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/02.PNG" alt="Plugins" width="50%">  
  
Find the W3 Total Cache plugin using the search field of the Plugins section.  
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/03.PNG" alt="W3 Total Cache plugin">  
  
Install the W3 Total Cache plugin.  
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/04.PNG" alt="Install the W3 Total Cache plugi" width="50%">  
  
Enable the installed plugin by clicking Activate Plugin. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/05.PNG" alt="Enable the installed plugin" width="50%">  
  
In the Performance section choose "General Settings".

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/06.PNG" alt="Performance section " width="80%">  
  
In the "General Settings" section scroll down to the CDN section. Tick "Enable" field. In CDN Type choose Generic Mirror. Then click **Save all** settings.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/07.PNG" alt="General Settings" width="80%">  
  
After having settings accepted, a warning of incorrect CDN settings will appear at the top of the General Settings section. Click Specify It Here in this warning message.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/10.PNG" alt=" warning message" width="80%">

Or go to the CDN section of the Performance menu. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/08.PNG" alt="CDN section " width="80%">  
  
Enter your CNAME (you can find it in your Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>) in Replace Site's Hostname With. Then click **Save All Settings**. Ensure that <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-w3-total-cache-plugin/09.PNG" alt="Configurations" width="80%">

Integration has been completed! We highly recommend you to check the HTML code of your webpage to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.