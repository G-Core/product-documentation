---
title: 4xx-errors-how-to-solve-storage-issues
displayName: Troubleshooting
published: true
order: 90
toc:
   --1--HTTP 404 error: "http-404"
   --1--HTTP 403 error: "http-403"
pageTitle: Fix 403 and 404 errors for your storage | Gcore
pageDescription: How to solve storage issues connected with 403 and 404 errors.
---

# 4xx errors: how to solve Storage issues

If you request content from S3 or SFTP storage and receive an error in return, check if there are open incidents or maintenance connected with Storage on Status Page. 

## HTTP 404 

1\.  Make sure that a file was uploaded to storage. You may use any applications that support S3 or SFTP for that purpose
 
2\.  Make sure you use the correct URL form for the request. The scheme for direct storage requests is described in the article. Notice that the Global 2 location includes three regions: use the host of the region, where the file was uploaded. The region’s URL is described in the <a href="https://gcore.com/docs/storage/request-content-directly-from-the-storage" target="_blank">article</a>. 

## HTTP 403 

By default, buckets and files in S3 storage are private and respond with 403 code on external requests. You can set up ACL rules for bucket or file with your S3-application documentation. 

- To add a rule for public reading via AWS CLI:

```
aws s3api put-object-acl --bucket my_bucket --key file.jpg --acl public-read --endpoint-url=https://s3-ed1.cloud.gcore.lu
```

Where ```my_bucket``` is the name of the bucket, ```file.jpg``` is the name of the file, and ```s-ed1.cloud.gcore.lu``` is the service URL.

- To add a rule for public reading via s3cmd: 


```
s3cmd setacl --acl-public s3://my_bucket/file.jpg
```

Where ```my_bucket``` is the name of the bucket and ```file.jpg``` is the name of the file.