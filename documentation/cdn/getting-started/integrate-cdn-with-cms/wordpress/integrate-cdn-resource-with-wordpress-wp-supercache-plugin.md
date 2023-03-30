---
title: integrate-cdn-resource-with-wordpress-wp-supercache-plugin
displayName: WP SuperCache plugin
published: true
order: 40
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Install the WP Super Cache plugin (there are two options to accomplish this)Log into your WordPress administration dashboard.

     Click Search link below the Install Plugin title.

     Enter WP Super Cache in the input and click on Search Plugins.     

     Press Select and Install now. 

     Click Activate to enable the plugin.

Click Settings in the left navigation bar and select WP Super Cache.

Select the CDN tab.

Check Enable CDN Support.

Enter your CNAME in the Off-site URL field that you specified in the G-CORE [control panel](https://control.gcdn.co/). Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration.

Check Skip Https URLs To Avoid Mixed Content Errors, if you do not use custom SSL in your CDN settings.

Click Save Changes.   
<img src="https://support.gcore.com/hc/ru/article_attachments/115000103969/wp-super-cache.png" alt="">

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.