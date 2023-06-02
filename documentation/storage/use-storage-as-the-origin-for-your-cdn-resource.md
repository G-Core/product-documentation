---
title: use-storage-as-the-origin-for-your-cdn-resource
displayName: Use storage with CDN
published: true
order: 40
toc:
   --1--Use as an origin: "use-as-an-origin"
   --2--S3 storage: "use-s3-storage"
   --2--SFTP storage: "use-sftp-storage"
   --1--Request content from CDN: "request-content-from-cdn"
   --2--S3 storage is the origin: "s3-storage-is-the-origin"
   --2--SFTP storage is the origin: "sftp-storage-is-the-origin"
---
# Use storage as the origin for your CDN resource

## Use as an origin

### Use S3 storage

Go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN</a> tab and press **Create CDN resource**.

<img src="https://assets.gcore.pro/docs/storage/use-storage-with-cdn/create-cdn-resource-10.png" alt="">

Specify values in the fields:

- Path to your bucket in following format
    
```http(s)://<bucket-name>.<location>.cloud.gcore.lu```
    
More details in the "<a href="#request-content-from-cdn">Request content directly from the S3 storage</a>" section below. 

- Custom domain, e.g., _cdn.example.com_. Read more about the personal domain setup in the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">Create and set a custom domain for the content delivery via CDN</a>" guide.

<img src="https://assets.gcore.pro/docs/storage/use-storage-with-cdn/use-as-origin-20.png" alt="" width="70%">

### Use SFTP storage

Go to the <a href="https://cdn.gcore.com/resources/list" target="_blank">CDN</a> tab and press **Create CDN resource**.

<img src="https://assets.gcore.pro/docs/storage/use-storage-with-cdn/create-cdn-resource-10.png" alt="">


To specify the Origin Source, use the following schema: 

```<storage name>.<hostname>```

Both name and hostname can be found on the Storage tab > Storages > Details.

<img src="https://assets.gcore.pro/docs/storage/use-storage-with-cdn/use-sftp-as-origin-40.png" alt="" width="70%">

If your storage name is 12345-test and your hostname is *ams.origin.gcdn.co*, you should specify *12345-test.ams.origin.gcdn.co* as the Origin Source. Read more about personal domain setup in the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">Create and set a custom domain for the content delivery via CDN</a>" guide.

## Request content from CDN

### S3 storage is the origin

An addressing scheme where you specify the bucket at the beginning ```<bucket-name>.<location>.cloud.gcore.lu``` allows you to increase the security of your CDN usage because you hide the Hostname of your repository.

Use the following schema to request uploaded files:

```http(s)://<Custom domain>/<folder*>/<file>```

*If the folder was created in the bucket. If files were added to the root of the bucket - specify file names.  

For example, you've: 

- used a bucket *mybucket*, S3 storage in the Luxembourg location *s-ed1.cloud.gcore.lu*
- created a CDN resource for the storage with the Custom domain with *cdn.example.com*. 

To request file *picture.png*, which was uploaded into the bucket, from CDN use the following URL:

http://cdn.example.com/picture.png

**Note**: By default, created buckets and all the stored files in buckets are private. To make a file public, read <a href="https://gcore.com/docs/storage/manage-s3-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/configure-access-control-on-s3-storage-with-aws-cli-and-s3cmd" target="_blank">the article on ACL and policy</a> or <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl" target="_blank">official documentation</a>.

### SFTP storage is the origin

Upload your files to the htdocs directory, but don't specify the directory when requesting the content.

Path to the uploaded file in the storage: 

```sftp://12345-test@ams.origin.gcdn.co:2200/export/home/12345-test/htdocs/picture.png```

If the CDN Custom domain is *cdn.example.com*, the URL to request the file from CDN will be:

http://cdn.example.com/picture.png
