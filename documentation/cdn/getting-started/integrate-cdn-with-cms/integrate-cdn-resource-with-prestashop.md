---
title: integrate-cdn-resource-with-prestashop
displayName: PrestaShop
published: true
order: 160
toc:
pageTitle: Integrate CDN with PrestaShop Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with PrestaShop CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with PrestaShop

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Log into your PrestaShop admin bar (back-office).

Go to Advanced Parameters/Performance.

Configure CCC (Combine, Compress and Cache) settings as in the picture below.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-prestashop/prestashop.jpeg" alt="Madia Server" width="80%">

Type in the CNAME in the Madia Server#1 field that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.  

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-prestashop/prestashop2v1.jpeg" alt="Madia Server" width="80%">

Click **Save** at the top of the page.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.