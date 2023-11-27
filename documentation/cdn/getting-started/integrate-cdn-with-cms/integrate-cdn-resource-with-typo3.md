---
title: integrate-cdn-resource-with-typo3
displayName: Typo3
published: true
order: 190
toc:
pageTitle: Integrate CDN with Typo3 Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Typo3 CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with Typo3

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

This tutorial guides you through the CDN integration of <a href="https://typo3.org" target="_blank">Typo3</a> with the <a href="https://typo3.org/extensions/repository/view/smile_cdn" target="_blank">smile_cdn</a> extension. We used Typo3 6.2 LTS and smile_cdn version 2.1.0 in the following example.

Login to the Typo3 backend.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-typo3/typo3-login.png" alt="Login to the Typo3 backend">

Navigate to Extension Manager and install the extension smile\_cdn.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-typo3/typo3-get-extension-smile_cdn-1024x612.png" alt=" Extension Manage" width="80%">

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-typo3/typo3-cdn-install-smile-cdn-1024x186.png" alt="Get extensions" width="80%">

Configure the smile_cdn extension by defining the CNAME (without ```http://```) that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a> and the desired filters to offload your assets. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-typo3/typo3-cdn-configure-smile-cdn-1024x858.png" alt=" Control panel a" width="80%">

Click Flush the Frontend Caches in the Typo3 backend.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-typo3/typo3-flush-cache-300x127.png" alt="Typo3 backend">

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.