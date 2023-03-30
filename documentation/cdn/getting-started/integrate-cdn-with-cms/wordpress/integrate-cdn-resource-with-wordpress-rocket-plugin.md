---
title: integrate-cdn-resource-with-wordpress-rocket-plugin
displayName: Rocket plugin
published: true
order: 20
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

[Create](https://support.gcore.com/hc/en-us/articles/213969429-How-to-set-up-a-CDN-service) a CDN Resources before you start the CDN integration.

Login to your WordPress admin dashboard and navigate to Plugins -> Add New.

Upload the plugin.

When the plugin is activated, please go to the configuration area of the plugin.

Go to CDN and type in the CNAME from the G-CORE CDN [control panel](https://control.gcdn.co/). Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration.

Update the Replace Site’s Hostname field. <img src="https://support.gcore.com/hc/ru/article_attachments/115000109125/WPRocket.png" alt="">  
Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.