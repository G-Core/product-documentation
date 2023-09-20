---
title: request-content-directly-from-the-storage
displayName: Request files from storage
published: true
order: 70
toc:
   --1--S3: "request-content-directly-from-the-s3-storage"
   --1--SFTP: "request-content-directly-from-the-sftp-storage"
pageTitle: Schemes for requesting files in S3 and SFTP storages | Gcore
pageDescription: Instructions on how to request content directly from the S3 and SFTP storage.
---
# Request content directly from the storage

## Request content directly from the S3 storage

Use the following schema to request uploaded files:

```
http(s)://<bucket-name>.<location>.cloud.gcore.lu
```

You can find the hostname on the <a href="https://storage.gcore.com/storage/list" target="_blank">Storages</a> tab in the "Details" section.

<img src="https://assets.gcore.pro/docs/storage/request-content-directly-from-the-storage/10275919634193.png" alt="Details section">

For example, your storage is in the Luxembourg location. You've created a bucket *mybucket* and uploaded *picture.png* there:

```
/mybucket/picture.png
```

The Luxembourg location hostname is:

```
s-ed1.cloud.gcore.lu
```

URL to request the file from the storage is:

```
http://mybucket.s-ed1.cloud.gcore.lu/picture.png
```

S3 storages support both HTTP and HTTPS protocols.

## Request content directly from the SFTP storage

Upload your files to the *htdocs* directory but don't specify the directory when requesting the content.

Use the following schema to form the URLs:

```
http://<storage name>.<hostname>/<file name>
```

You can find the storage name and hostname on the <a href="https://storage.gcore.com/storage/list" target="_blank">Storages</a> tab in the "Details" section.

Path to the uploaded file in the storage: 

```
sftp://12345-test@ams.origin.gcdn.co:2200/export/home/12345-test/htdocs/picture.png
```

Where: 
- *12345-test* is a storage name;
- *ams.origin.gcdn.co* is a hostname.

URL to request the file from the storage:

```
http://12345-test.ams.origin.gcdn.co/picture.png
```

SFTP storage works only via HTTP protocol.