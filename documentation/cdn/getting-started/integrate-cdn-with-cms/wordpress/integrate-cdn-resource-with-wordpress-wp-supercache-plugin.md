---
title: integrate-cdn-resource-with-wordpress-wp-supercache-plugin
displayName: WP SuperCache plugin
published: true
order: 40
toc:
pageTitle: Integrate CDN with WP SuperCache plugin for WordPress Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with the WP SuperCache plugin for CMS WordPress to enhance your site's speed and user experience.
---
# Integrate CDN resource with WordPress (WP SuperCache plugin)

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Install the WP Super Cache plugin (there are two options to accomplish this)Log into your WordPress administration dashboard.

1. Click Search link below the Install Plugin title.
2. Enter WP Super Cache in the input and click on Search Plugins.     
3. Press Select and Install now. 
4. Click Activate to enable the plugin.

Click "Settings" in the left navigation bar and select WP Super Cache.

Select the "CDN" tab.

Check **Enable CDN Support**.

Enter your CNAME in the Off-site URL field that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

Check "Skip Https URLs To Avoid Mixed Content Errors", if you do not use custom SSL in your CDN settings.

Click **Save Changes**.
   
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-wp-supercache-plugin/wp-super-cache.png" alt="Cache" width="80%">

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.