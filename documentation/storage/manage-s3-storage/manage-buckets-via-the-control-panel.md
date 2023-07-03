---
title: manage-buckets-via-the-control-panel
displayName: Manage buckets
published: true
order: 10
toc:
   --1--Create buckets: "create-buckets"
   --1--Add Lifecycle policy (S3 Luxembourg): "add-lifecycle-policy-available-for-s3-in-luxembourg-only"
   --1--Configure HTTP access: "configure-http-access"
   --1--Use File manager: "use-file-manager"
   --2--Override CORS: "override-cors-for-a-bucket"
   --2--Add a folder: "add-a-folder-to-a-bucket"
   --2--Manage files: "manage-files"
   --1--Delete buckets: "delete-buckets"
---

# Manage buckets via the Control panel

## Create buckets

1. Go to the <a href="https://storage.gcore.com/storage/list" target="_blank">Storage</a> section.

2. Click the **···** icon opposite the storage that you want to use for the bucket’s creations and select **Buckets**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/bucket-main-menu-10.png" alt="" width="80%">

2. Click the **Add new bucket** button.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/add-bucket-20.png" alt="" width="50%">

3. Enter the name of the bucket and click **Create**.

**Note**: The name must be unique. Our system checks the names of buckets of all users. If the name matches the name of the bucket of another user, you will see the error: ```create bucket: bucket already exist: bad params```.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/confirm-creation-30.png" alt="" width="50%">

The bucket’s creation is complete.

## Add Lifecycle policy (available for S3 in Luxembourg only)

You can configure the lifecycle policy for a bucket via the *aws cli* client according to the "<a href="https://gcore.com/docs/storage/manage-s3-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/remove-objects-from-a-bucket-automatically-with-aws-cli" target="_blank">Remove objects from a bucket automatically with AWS CLI</a>" guide. If you use S3 storage in Luxembourg, it is possible to assign Lifecycle policy for buckets in the Control panel:

1. Open the bucket page, click the **···** icon and select **Lifecycle Management**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/lifecycle-management-40.png" alt="" width="80%">

**Note**: If your S3 storage is in different locations OTHER THAN Luxembourg (e.g., Chicago, Singapore, and so on), the Lifecycle Management menu item will be absent.

2. Enter the number of days. After this time, files will be deleted from the bucket. Click **Save changes**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/change-lifecycle-50.png" alt="" width="80%">

If you want to discard the expiration time, click the **Cancel policy** button.

## Configure HTTP access

If you want to use <a href="https://gcore.com/docs/storage/use-storage-as-the-origin-for-your-cdn-resource" target="_blank">S3 storage as the origin for a CDN resource</a>, you must share access to a bucket. In this case, all files from the bucket will be available via the HTTP protocol.

1. Open the bucket page, click the **···** icon and select **HTTP access to all files**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/http-access-60.png" alt="" width="80%">

2. Press **Apply**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/apply-http-access-70.png" alt="" width="50%">

## Use File manager

File manager makes it possible to create folders and upload and delete files. You can also get S3 and HTTP/HTTPS links to files.

### Override CORS for a bucket

To use File manager, you must first configure the CORS. The CORS technology makes it possible to handle requests from our domain *storage.gcorelabs.com*.

**Note**: CORS should be configured for each bucket separately.

You can configure CORS in three ways:

- Via s3cmd according to the "<a href="https://gcore.com/docs/storage/manage-s3-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/remove-objects-from-a-bucket-automatically-with-aws-cli#manage-a-lifecycle-policy-with-aws-cli" target="_blank">Set CORS policy on a bucket via s3cmd</a>" guide.
- Via API according to the <a href="https://apidocs.gcore.com/storage" target="_blank">API docs</a>—this way makes it possible to override CORS not only for *storage.gcorelabs.com* and other domains.
- In the Control panel.

To configure CORS in the control panel:

1. Open the bucket page, click the **···** icon, and select **File manager**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/file-manager-80.png" alt="" width="80%">

2. Click the **Override CORS** button.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/override-cors-90.png" alt="" width="80%">

That’s it. After this action, you should enter the Access and Secret key to log in to the File Manager. Access and Secret keys are the credentials that are generated after storage creation. We don’t keep them in our system because it’s private and secure information. If you’ve forgotten keys, generate a new one in the Storage section by pressing the **···** icon and selecting **Generate new keys**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/generate-key-100.png" alt="">

### Add a folder to a bucket

1. Open File manager.

2. Click **Add folder**. Enter the name of the folder and click **Create**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/add-folder-110.png" alt="" width="80%">

The folder is created. After this, you can work with files.

### Manage files

1. Open File manager and go to the folder where you want to upload files. You can also upload files to the bucket root.

2. Click **Select files**, select them from your PC, and click **Upload**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/manage-files-120.png" alt="" width="80%">

Files will be loaded to a folder or a bucket. Then, you can copy links to files from the bucket in different formats: in S3 to manage them via the console or terminal, and conventional HTTP/HTTPS links to view files in the browser.

To get links, check the boxes on the left of files and click **Copy S3 URL** or **Copy URL**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/copy-url-130.png" alt="" width="80%">

For example, for the file *sample.txt*, the links look as follows:

- s3://s-ed1.cloud.gcore.lu/example/folder1/sample.txt
- https://s-ed1.cloud.gcore.lu/example/folder1/sample.txt

where

- *s* or *https* is a protocol (format)
- *s-ed1.cloud.gcore.lu* is a hostname
- *example* is a bucket
- *folder1* is a folder
- *sample.txt* is a file name.

You can also delete files. To do this, click **Delete** opposite those files that you want to remove from the folder or bucket.

## Delete buckets

Deletion time depends on the overall size of the files that are in the bucket.

To delete a bucket, click the **···** icon on the bucket’s page, select **Delete** and confirm.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets/delete-bucket-140.png" alt="" width="80%">