---
title: integrate-cdn-resource-with-prestashop
displayName: PrestaShop
published: true
order: 160
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Log into your PrestaShop admin bar (back-office).

Go to Advanced Parameters/Performance.

Configure CCC (Combine, Compress and Cache) settings as in the picture below.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000082909/prestashop.jpeg" alt="">Type in the CNAME in the Madia Server#1 field that you specified in the G-Core [control panel](https://control.gcdn.co/). Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000082929/prestashop2v1.jpeg" alt="">Click Save at the top of the page.

  
Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.