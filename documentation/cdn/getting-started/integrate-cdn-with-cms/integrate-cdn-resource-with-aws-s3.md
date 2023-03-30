---
title: integrate-cdn-resource-with-aws-s3
displayName: AWS S3
published: true
order: 10
toc:
---
Before you start, please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to the [AWS Console](https://console.aws.amazon.com/) and navigate to S3.

Create an S3 bucket (define the Bucket Name and the Region you want)

<img src="https://support.gcore.com/hc/ru/article_attachments/115000082305/create-s3.png" alt="">

Upload content to your S3 bucket.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000082325/upload-content-s33.png" alt="">

<img src="https://support.gcore.com/hc/ru/article_attachments/115000082345/upload-content-s3-2-1024x546.png" alt="">

<img src="https://support.gcore.com/hc/ru/article_attachments/115000080709/upload-complete.png" alt="">

Enable Website Hosting and define the Index Document (does not need to exist e.g., index.html) for your S3 bucket under Properties > Static Website Hosting.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000082365/s3-enable-hosting1.png" alt="">

Use the following example to set a Bucket Policy (replace "example-bucket" with your S3 bucket name):

{

 "Version":"2012-10-17",  
 "Statement":\[{  
   "Sid":"PublicReadGetObject",  
       "Effect":"Allow",  
     "Principal": "\*",  
     "Action":\["s3:GetObject"\],  
     "Resource":\["arn:aws:s3:::example-bucket/\*"  
     \]  
   }  
 \]  
}  
  

Add the bucket policy in the Permissions drop-down menu.

<img src="https://support.gcore.com/hc/ru/article_attachments/115000082405/add-s3-bucket-policy.png" alt="">

<img src="https://support.gcore.com/hc/ru/article_attachments/115000080829/s3-bucket-policy-example.png" alt="">

Check accessibility of the file at the URL link in the browser. For example, the link for the file from this guide is bucket.s3-website.eu-central-1.amazonaws.com/logo.png

<img src="https://support.gcore.com/hc/ru/article_attachments/115000082585/s3-endpoint-url.png" alt="" width="2364" height="1147">

Log in your Gcore [control panel](https://control.gcdn.co/) and [create a CDN-Resource](https://support.gcore.com/hc/en-us/articles/213969429-How-to-set-up-a-CDN-service). Use S3 Endpoint as an origin source. For example, bucket.s3-website.eu-central-1.amazonaws.com

As soon as you create a Resource check accessibility of the content through the CDN by opening the URL link in the browser. For example, CNAME: awss3.site.com/logo.png. Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/ru/articles/213969769-%D0%9D%D0%B0%D1%81%D1%82%D1%80%D0%BE%D0%B9%D0%BA%D0%B0-CNAME-%D0%B7%D0%B0%D0%BF%D0%B8%D1%81%D0%B8-) properly before using it for integration.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.