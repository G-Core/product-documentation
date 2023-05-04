---
title: integrate-cdn-resource-with-typo3
displayName: Typo3
published: true
order: 190
toc:
---
# Integrate CDN resource with Typo3

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

This tutorial guides you through the CDN integration of <a href="https://typo3.org/" target="_blank">Typo3</a> with the <a href="http://typo3.org/extensions/repository/view/smile_cdn" target="_blank">smile_cdn</a> extension. We used Typo3 6.2 LTS and smile_cdn version 2.1.0 in the following example.

Login to the Typo3 backend.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083485/typo3-login.png" alt="">

Navigate to Extension Manager and install the extension smile\_cdn.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083505/typo3-get-extension-smile_cdn-1024x612.png" alt="" width="70%">

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083525/typo3-cdn-install-smile-cdn-1024x186.png" alt="" width="70%">

Configure the smile_cdn extension by defining the CNAME (without ```http://```) that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a> and the desired filters to offload your assets. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083565/typo3-cdn-configure-smile-cdn-1024x858.png" alt="" width="70%">

Click Flush the Frontend Caches in the Typo3 backend.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000083545/typo3-flush-cache-300x127.png" alt="">

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.