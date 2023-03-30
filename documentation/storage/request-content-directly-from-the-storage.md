---
title: request-content-directly-from-the-storage
displayName: Request files from storage
published: true
order: 70
toc:
   --1--S3: "request-content-directly-from-the-s3-storage"
   --1--SFTP: "request-content-directly-from-the-sftp-storage"
---
  

Request content directly from the S3 storage
--------------------------------------------

Use the following schema to request uploaded files:

http(s)://<bucket-name>.<location>.cloud.gcore.lu

You can find the hostname on the [Storages](https://storage.gcore.com/storage/list) tab in the Details section.

<img src="https://support.gcore.com/hc/article_attachments/10275919634193" alt="mceclip0.png">For example, your storage is in the Global-1 location. You've created a bucket _mybucket_ and uploaded _picture.png_ there:

/mybucket/picture.png

Global-1 location hostname:

s-ed1.cloud.gcore.lu

URL to request the file from the storage:

http://mybucket.s-ed1.cloud.gcore.lu/picture.png

S3 storages support both HTTP and HTTPS protocols.

Request content directly from the SFTP storage
----------------------------------------------

Upload your files to the _htdocs_ directory but don't specify the directory when requesting the content.

Use the following schema to form the URLs:

http://<storage name>.<hostname>/<file name>

You can find the storage name and hostname on the [Storages](https://storage.gcore.com/storage/list) tab in the Details section.

Path to the uploaded file in the storage: 

sftp://12345-test@ams.origin.gcdn.co:2200/export/home/12345-test/htdocs/picture.png

Where: 

*   _12345-test_ is a storage name;
*   _ams.origin.gcdn.co_ is a hostname.

URL to request the file from the storage:

http://12345-test.ams.origin.gcdn.co/picture.png

SFTP storage works only via HTTP protocol.