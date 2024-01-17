---
title: integrate-cdn-resource-with-google-cloud-storage
displayName: Google Cloud Storage
published: true
order: 90
toc:
pageTitle: Integrate CDN with Google Cloud Storage Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Google Cloud Storage to enhance your site's speed and user experience.
---
# Integrate CDN resource with Google Cloud Storage

This guide describes how you could use <a href="https://cloud.google.com/storage" target="_blank">Google Cloud Storage</a> as an origin server.  

Create a Google Cloud Storage (GCS) bucket.

<media-gallery>
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-google-cloud-storage/google-storage-create-bucket-1024x363.png" alt="Create a Google Cloud Storage (GCS) bucket." width="50%">
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-google-cloud-storage/google-storage-bucket-settings-1024x863.png" alt="Create a Google Cloud Storage (GCS) bucket.">
</media-gallery>

Upload your data and mark it as Shared publicly.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-google-cloud-storage/google-storage-upload-file.png" alt="Upload your data and mark it as Shared publicly" width="80%">

Login to the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a> at our site and <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">create a CDN resource</a> using ```storage.googleapis.com``` as origin.

When your CDN resource is created, check the accessibility of files through CDN. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

**Note**: If you want to hide your cloud bucket name, use our <a href="https://gcore.com/docs/cdn/cdn-resource-options/rewrite-redirect-requests-from-the-cdn-to-the-origin" target="_blank">Rewrite</a> option.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.