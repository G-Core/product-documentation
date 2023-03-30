---
title: integrate-cdn-resource-with-wordpress-w3-total-cache-plugin
displayName: W3 Total Cache plugin
published: true
order: 30
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns plugin might not help you.

Login to your Wordpress blog at _yoursite.com/wp-admin_ and click Enter.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000110485/01.PNG" alt="">  
  
Add new plugin in the Plugins section.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000105429/02.PNG" alt="">  
  
Find the W3 Total Cache plugin using the search field of the Plugins section.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000105449/03.PNG" alt="">  
  
Install the W3 Total Cache plugin.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000110525/04.PNG" alt="">  
  
Enable the installed plugin by clicking Activate Plugin.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000108509/05.PNG" alt="">  
  
In the Performance section choose General Settings.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000108589/06.PNG" alt="">  
  
In the General Settings section scroll down to the CDN section. Tick Enable field. In CDN Type choose Generic Mirror. Then click Save all settings.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000113565/07.PNG" alt="">  
  
After having settings accepted, a warning of incorrect CDN settings will appear at the top of the General Settings section. Click Specify It Here in this warning message.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000109445/10.PNG" alt="">

Or go to the CDN section of the Performance menu.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000113585/08.PNG" alt="">  
  
Enter your CNAME (you can find it in your G-CORE CDN [control panel](https://control.gcdn.co/)) in Replace Site's Hostname With. Then click Save All Settings. Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000113625/09.PNG" alt="">

Integration has been completed! We highly recommend you to check the HTML code of your webpage to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.