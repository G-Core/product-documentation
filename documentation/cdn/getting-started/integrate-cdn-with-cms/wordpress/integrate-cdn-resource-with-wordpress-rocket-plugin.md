---
title: integrate-cdn-resource-with-wordpress-rocket-plugin
displayName: Rocket plugin
published: true
order: 20
toc:
pageTitle: Integrate CDN with Rocket plugin for WordPress Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with the Rocket plugin for CMS WordPress to enhance your site's speed and user experience.
---
# Integrate CDN resource with WordPress (Rocket plugin)

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

<a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">Create a CDN resource</a> before you start the CDN integration.

Login to your WordPress admin dashboard and navigate to Plugins > Add New.

Upload the plugin.

When the plugin is activated, please go to the configuration area of the plugin.

Go to CDN and type in the CNAME from the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

Update the Replace Site’s Hostname field. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-rocket-plugin/WPRocket.png" alt="CDN " width="80%"> 


Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.