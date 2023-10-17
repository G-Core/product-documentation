---
title: integrate-cdn-resource-with-ips
displayName: IPS
published: true
order: 110
toc:
pageTitle: Integrate CDN with IPS Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with IPS CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with IPS

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to your IPS Community Admin area.

Click **System/System Settings** as in the picture below  
  
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-ips/ips-settings.jpeg" alt="System Settings" width="80%">

Click **General Configuration** as in the picture below.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-ips/ips-general-configuration.jpeg" alt="General Configuration" width="80%">

Scroll down to CDN Settings.

Type in your CNAME that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.  
  
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-ips/ips-cdn-settingsv1.jpeg" alt="CDN Settings" width="80%">

Click the **Update Settings** button at the bottom of the page.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.