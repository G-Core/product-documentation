---
title: integrate-cdn-resource-with-typo3
displayName: Typo3
published: true
order: 190
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

This tutorial guides you through the CDN integration of [Typo3](https://typo3.org/) with the [smile\_cdn](http://typo3.org/extensions/repository/view/smile_cdn) extension. We used Typo3 6.2 LTS and smile\_cdn version 2.1.0 in the following example.

Login to the Typo3 backend.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083485/typo3-login.png" alt="">

Navigate to Extension Manager and install the extension smile\_cdn.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083505/typo3-get-extension-smile_cdn-1024x612.png" alt="">

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083525/typo3-cdn-install-smile-cdn-1024x186.png" alt="">Configure the smile\_cdn extension by defining the CNAME (without http://) that you specified in the G-CORE [control panel](https://control.gcdn.co/) and the desired filters to offload your assets. Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083565/typo3-cdn-configure-smile-cdn-1024x858.png" alt="">

Click Flush the Frontend Caches in the Typo3 backend.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083545/typo3-flush-cache-300x127.png" alt="">

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.