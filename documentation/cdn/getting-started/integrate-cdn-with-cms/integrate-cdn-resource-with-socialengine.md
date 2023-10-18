---
title: integrate-cdn-resource-with-socialengine
displayName: SocialEngine
published: true
order: 180
toc:
pageTitle: Integrate CDN with SocialEngine Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with SocialEngine CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with SocialEngine

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Log into your SocialEngine admin panel.

Go to Settings/General Settings.

Enter your CNAME from the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>.

Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-socialengine/socialenginev1.jpeg" alt="Integrate CDN resource with SocialEngine" width="80%">

Click **Save Changes** button at the bottom of the page.  
  
Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.