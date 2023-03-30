---
title: use-storage-as-the-origin-for-your-cdn-resource
displayName: Use storage with CDN
published: true
order: 40
toc:
   --1--Use as an origin: "use-the-storage-as-an-origin-for-your-cdn-resource"
   --2--S3 storage: "use-s3-storage"
   --2--SFTP storage: "use-sftp-storage"
   --1--Request content from CDN: "request-content-from-cdn"
   --2--S3 storage is the origin: "s3-storage-is-the-origin"
   --2--SFTP storage is the origin: "sftp-storage-is-the-origin"
---
:  
    •  
    •  
:  
    •  
    •

Use the storage as an origin for your CDN resource 
---------------------------------------------------

### Use S3 storage

Go to the [CDN](https://cdn.gcore.com/resources/list) tab and press **Create CDN resource**.

<img src="https://support.gcore.com/hc/article_attachments/10272561190417" alt="mceclip1.png">

Specify values in the fields:

*   Path to your bucket in following format
    
    http(s)://<bucket-name>.<location>.cloud.gcore.lu
    
    More details in the "[Request content directly from the S3 storage](https://support.gcore.com/hc/en-us/articles/360002252378)" guide. S3 storage supports both HTTP and HTTPS delivery. So choose any pull protocol you prefer.
*   Custom domain, e.g., _cdn.example.com_. Read more about the personal domain setup in the "[Create a domain name for content delivery through a CDN](https://gcore.com/support/articles/213969769/)" guide.

<img src="https://support.gcore.com/hc/article_attachments/10327746152465" alt="mceclip0.png" width="540" height="696">

### Use SFTP storage

Go to the [CDN](https://cdn.gcore.com/resources/list) tab and press **Create CDN resource**.

<img src="https://support.gcore.com/hc/article_attachments/10272561190417" alt="mceclip1.png">

SFTP storage supports only HTTP protocol.

To specify the Origin Source, use the following schema: **<storage name>.<hostname>**. Both name and hostname can be found on the Storage tab > Storages > Details.

<img src="https://support.gcore.com/hc/article_attachments/360003529538/sftp_cdn_resource_eng.png" alt="sftp_cdn_resource_eng.png">If your storage name is 12345-test and your hostname is _ams.origin.gcdn.co_, you should specify _12345-test.ams.origin.co_ as the Origin Source. Read more about personal domain setup in [this article](https://www.gcore.com/support/articles/213969769/). The Custom Host Header field is auto-filled. 

Request content from CDN
------------------------

### S3 storage is the origin

An addressing scheme where you specify the bucket at the beginning (<bucket-name>.<location>.cloud.gcore.lu) allows you to increase the security of your CDN usage because you hide the Hostname of your repository.

Use the following schema to request uploaded files:

http(s)://<Custom domain>/<folder\*>/<file>

\*If the folder was created in the bucket. If files were added to the root of the bucket - specify file names.  

For example, you've: 

*   used a bucket _mybucket,_ S3 storage in the Luxembourg location _s-ed1.cloud.gcore.lu_
*   created a CDN resource for the storage with the Custom domain with _cdn.example.com_. 

To request file _picture.png,_ which was uploaded into the bucket, from CDN use the following URL:

http://cdn.example.com/picture.png

**Note!** By default, created buckets and all the stored files in buckets are private. To make a file public, read [an article on ACL and policy](https://support.gcore.com/hc/en-us/articles/360002115857) or official [documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl).

### SFTP storage is the origin

Upload your files to the htdocs directory, but don't specify the directory when requesting the content.

Path to the uploaded file in the storage: 

sftp://12345-test@ams.origin.gcdn.co:2200/export/home/12345-test/htdocs/picture.png

CDN Custom Domain:

cdn.mycompany.com

URL to request the file from CDN:

http://cdn.mycompany.com/picture.png