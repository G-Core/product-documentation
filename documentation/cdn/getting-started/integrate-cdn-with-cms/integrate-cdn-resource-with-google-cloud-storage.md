---
title: integrate-cdn-resource-with-google-cloud-storage
displayName: Google Cloud Storage
published: true
order: 90
toc:
---
This guide describes how you could use [Google Cloud Storage](https://cloud.google.com/storage/) as an origin server.  

Create a Google Cloud Storage (GCS) bucket.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000081825/google-storage-create-bucket-1024x363.png" alt="" width="640" height="227">
======================================================================================================================================================

<img src="https://support.gcore.com/hc/ru/article_attachments/115000081845/google-storage-bucket-settings-1024x863.png" alt="" width="640" height="540">

Upload your data and mark it as Shared publicly.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000080269/google-storage-upload-file.png" alt="" width="1329" height="192">

Login to the G-CORE [control panel](https://control.gcorelabs.com) at our site and create a Resource using storage.googleapis.com as origin.

When your [CDN-Resource is created](https://support.gcore.com/hc/en-us/articles/213969429-How-to-set-up-a-CDN-service), check the accessibility of files through CDN. Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration.

(i) If you want to hide your cloud bucket name, use our [Rewrite option](https://support.gcore.com/hc/en-us/articles/115005353949).

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.