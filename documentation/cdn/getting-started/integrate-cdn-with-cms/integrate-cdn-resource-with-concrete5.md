---
title: integrate-cdn-resource-with-concrete5
displayName: Concrete5
published: true
order: 40
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Create a CDN [CDN-Resource](https://support.gcore.com/hc/en-us/articles/213969429-How-to-set-up-a-CDN-service) before you start with integration.

Install one of [Concrete5](http://www.concrete5.org/) CDN extensions. Here are 3 of a large number of available extensions: 

*   [CDN Manager](https://www.concrete5.org/marketplace/addons/cdn-manager/)  A license costs $20.
*   [Content Delivery Network Manager](http://www.concrete5.org/marketplace/addons/content-delivery-network-cdn/). A license costs $45.
*   There’s also a [CDN package for Сoncrete5](https://github.com/concrete5/concrete5/pull/771) that allows you to transfer your static files to CDN. The package is free.

During or after the installation of an extension, you need to type in the CNAME that you specified in the G-Core [control panel](https://control.gcdn.co/). Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration (e.g. cdn.site.com).

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.