---
title: integrate-cdn-resource-with-kirby
displayName: Kirby
published: true
order: 130
toc:
pageTitle: Integrate CDN with Kirby Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Kirby CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with Kirby

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

There is currently no plugin available for automatic CDN integration with <a href="https://getkirby.com" target="_blank">Kirby</a>. You need to change manually the path for your CSS and JS files in the header.php but there is the Kirby GetImages plugin for your images. For more details visit <a href="https://github.com/RobBrazier/kirby-getimage" target="_blank">GitHub</a>.

We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.