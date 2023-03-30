---
title: integrate-cdn-resource-with-cs-cart
displayName: Cs-cart
published: true
order: 60
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns plugin might not help you.

You need to buy the plugin (unfortunately, there are no free plugins at the moment). You can buy it [here](https://marketplace.cs-cart.com/add-ons/site-management/content-delivery-network-cs-cart-addon.html). Install the plugin.  
Login to the CMS administration panel and go the Add-ons sections, Manage Add-ons.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000107505/1eng.PNG" alt="">

Click on +.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000101929/2eng.PNG" alt="">  
Choose the way to install the file. Click Upload & Install.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000107525/3eng.PNG" alt="">  
Having installed Universal CDN Add-on, go to its settings.  
<img src="https://support.gcore.com/hc/ru/article_attachments/115000102009/4eng.PNG" alt="">  
In the CDN URL field insert CNAME that you specified in the G-CORE [control panel](https://control.gcorelabs.com/).

Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-CNAME) in a proper way before using it for integration.

<img src="https://support.gcore.com/hc/article_attachments/115001968809/1.png" alt="1.png">Apply settings and enable the plugin.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.