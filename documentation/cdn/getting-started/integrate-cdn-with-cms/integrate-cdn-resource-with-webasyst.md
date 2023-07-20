---
title: integrate-cdn-resource-with-webasyst
displayName: Webasyst
published: true
order: 210
toc:
pageTitle: Integrate CDN with Webasyst Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Webasyst to enhance your site's speed and user experience.
---
# Integrate CDN resource with Webasyst

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to Webasyst administration area.

On the top bar find Site.

Go Settings.

In the CDN field write your CNAME from the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration

Save changes.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.