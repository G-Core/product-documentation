---
title: integrate-cdn-resource-with-craft
displayName: Craft
published: true
order: 50
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to your Craft admin panel.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083605/1.JPG" alt="">

Go to Assets by clicking on the arrow next to the gear in the top right corner of the control panel.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083625/22.JPG" alt="">

Click +New Source to create a new folder for your static files.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083645/3.JPG" alt="">In the URL field type in the CNAME that you specified in the G-Core [control panel](https://control.gcdn.co/). Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration (eg, _http://cdn.site.com/path/to/your/assets_).

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083805/4.JPG" alt="">Go to the Assets tab, find previously created asset source and download your files.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000081769/5.JPG" alt="">Now you can use your asset at the website.

If you have already had created assets, edit them replacing URL with CNAME that you specified in the G-Core [control panel](https://control.gcdn.co/).  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000081889/6.JPG" alt="">

Save changes.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.