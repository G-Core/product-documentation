---
title: integrate-cdn-resource-with-aws-s3
displayName: AWS S3
published: true
order: 10
toc:
pageTitle: Integrate CDN with AWS S3 Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with AWS S3 to enhance your site's speed and user experience.
---
# Integrate CDN resource with AWS S3

Before you start, please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to the <a href="https://console.aws.amazon.com" target="_blank">AWS Console</a> and navigate to S3.

Create an S3 bucket (define the Bucket Name and the Region you want)

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-aws-s3/create-s3.png" alt="Create an S3 bucket" width="50%">

Upload content to your S3 bucket.

<media-gallery>
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-aws-s3/upload-content-s33.png" alt="Upload content to your S3 bucket" width="50%">
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-aws-s3/upload-content-s3-2-1024x546.png" alt="Upload content to your S3 bucket" width="80%">
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-aws-s3/upload-complete.png" alt="Upload content to your S3 bucket" width="50%">
</media-gallery>

Enable Website Hosting and define the Index Document (does not need to exist e.g., index.html) for your S3 bucket under Properties > Static Website Hosting.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-aws-s3/s3-enable-hosting1.png" alt="Enable Website Hosting">

Use the following example to set a Bucket Policy (replace "example-bucket" with your S3 bucket name):

```
{

 "Version":"2012-10-17",  
 "Statement":[{  
   "Sid":"PublicReadGetObject",  
       "Effect":"Allow",  
     "Principal": "*",  
     "Action":["s3:GetObject"],  
     "Resource":["arn:aws:s3:::example-bucket/*"  
     ]  
   }  
 ]  
}  
```  

Add the bucket policy in the Permissions drop-down menu.

<media-gallery>
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-aws-s3/add-s3-bucket-policy.png" alt="Permissions drop-down menu">
<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-aws-s3/s3-bucket-policy-example.png" alt="Permissions drop-down menu">
</media-gallery>

Check accessibility of the file at the URL link in the browser. For example, the link for the file from this guide is bucket.s3-website.eu-central-1.amazonaws.com/logo.png

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-aws-s3/s3-endpoint-url.png" alt="Check accessibility " width="80%">

Log in your Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a> and <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">create a CDN resource</a>. Use S3 Endpoint as an origin source. For example, bucket.s3-website.eu-central-1.amazonaws.com

As soon as you create a Resource check accessibility of the content through the CDN by opening the URL link in the browser. For example, CNAME: awss3.site.com/logo.png. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> properly before using it for integration.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.