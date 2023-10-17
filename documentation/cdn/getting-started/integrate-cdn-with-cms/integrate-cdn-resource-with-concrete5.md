---
title: integrate-cdn-resource-with-concrete5
displayName: Concrete5
published: true
order: 40
toc:
pageTitle: Integrate CDN with Concrete5 Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Concrete5 CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with Concrete5

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Create a <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">CDN resource</a> before you start with integration.

Install one of <a href="https://concrete5.org" target="_blank">Concrete5</a> CDN extensions. Here are 3 of a large number of available extensions: 

- <a href="https://concrete5.org/marketplace/addons/cdn-manager" target="_blank">CDN Manager</a>
- <a href="https://marketplace.concretecms.com/marketplace/addons/content-delivery-network-cdn/" target="_blank">Content Delivery Network (CDN)</a>
- There’s also a <a href="https://github.com/concrete5/concrete5/pull/771" target="_blank">CDN package for Сoncrete5</a> that allows you to transfer your static files to CDN. The package is free

During or after the installation of an extension, you need to type in the CNAME that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration (e.g., *cdn.site.com*).

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.