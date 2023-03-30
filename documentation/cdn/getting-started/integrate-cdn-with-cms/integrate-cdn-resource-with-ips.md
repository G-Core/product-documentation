---
title: integrate-cdn-resource-with-ips
displayName: IPS
published: true
order: 110
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to your IPS Community Admin area.

Click System/System Settings as in the picture below  
  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000082609/ips-settings.jpeg" alt="">

 Click General Configuration as in the picture below.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000084705/ips-general-configuration.jpeg" alt="">

 Scroll down to CDN Settings.

Type in your CNAME that you specified in the G-CORE [control panel](https://control.gcdn.co/). Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration.  
  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000084885/ips-cdn-settingsv1.jpeg" alt="">

Click the Update Settings button at the bottom of the page.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.