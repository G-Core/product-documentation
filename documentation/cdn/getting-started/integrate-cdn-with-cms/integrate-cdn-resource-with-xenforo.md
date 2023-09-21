---
title: integrate-cdn-resource-with-xenforo
displayName: XenForo
published: true
order: 240
toc:
pageTitle: Integrate CDN with XenForo Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with XenForo CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with XenForo

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Connect to your FTP account.

Go to library folder.

Edit config.php file and add two lines as in the example below:

```
$config ['externalDataUrl'] = 'http://cdn.site.com/data';  
$config ['javaScriptUrl'] = 'http://cdn.site.com/js';
```

Login to your XenForo admin area.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-xenforo/xenadmin.png" alt="Login to your XenForo admin area" width="50%">

Navigate to Style -> General -> Settings.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-xenforo/xensettings.png" alt="Settings"> 

Replace the Path to images field existing record (*/styles/default*) with the following:

```
http://cdn.site.com/styles/default
```

Instead of cdn.site.com type in the CNAME that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

Click **Update Style Properties** to save your settings.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.