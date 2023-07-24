---
title: integrate-cdn-resource-with-ipb
displayName: IPB
published: true
order: 100
toc:
pageTitle: Integrate CDN with IPB Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with IPB CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with IPB 

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns plugin might not help you.

IPB version 3.2. and newer ones support automatic integration with the CDN

Login to the administration management console.

Go to System settings → General configuration settings

Scroll down to images, CSS and JS URL settings.

In CNAME field type CNAME that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

Save the settings.

Integration has been completed! We highly recommend you to check the HTML code of your webpage to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.