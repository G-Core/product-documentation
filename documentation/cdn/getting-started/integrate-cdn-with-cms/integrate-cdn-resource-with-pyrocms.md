---
title: integrate-cdn-resource-with-pyrocms
displayName: PyroCMS
published: true
order: 170
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you. 

Login to the PyroCMS admin panel.

Go to Settings –> Integration.

Type in the CNAME that you specified in the G-Core [control panel](https://control.gcdn.co/). Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration.

Save settings.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.