---
title: 4xx-errors-how-to-solve-storage-issues
displayName: Troubleshooting
published: true
order: 90
toc:
   --1--HTTP 404 error: "http-404"
   --1--HTTP 403 error: "http-403"
---
  

If you request content from S3 or SFTP storage and receive an error in return, check if there are open incidents or maintenance connected with Storage on Status Page. 

HTTP 404 
---------

1.  Make sure that a file was uploaded to storage. You may use any applications that support S3 or SFTP for that purpose. 
2.  Make sure you use the correct URL form for the request. The scheme for direct storage requests is described in the article. Notice that the Global 2 location includes three regions: use the host of the region, where the file was uploaded. The region’s URL is described in the article. 

HTTP 403 
---------

By default, buckets and files in S3 storage are private and respond with 403 code on external requests. You can set up ACL rules for bucket or file with your S3-application documentation. 

*   To add a rule for public reading via AWS CLI:

_aws s3api put-object-acl --bucket my\_bucket --key file.jpg -**\-acl public-read -**\-endpoint-url=https://s3.us-east.gcore.com_ 

Where:

My\_bucket – the name of the bucket.

File.jpg - the name of the file.

s3.us-east.gcore.com - the region URL.

*   To add a rule for public reading via s3cmd: 

_s3cmd setacl --acl-public s3://my\_bucket/file.jpg_ 

Where:

my\_bucket – the name of the bucket.

file.jpg - the name of the file.