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
   --1--Override CORS: "override-cors-for-a-bucket"
   --1--Add a folder: "add-a-folder-to-a-bucket"
   --1--Manage files: "manage-files"
   --1--Delete buckets: "delete-buckets"
---
  
  
  
  
  
  
  

Create buckets
--------------

1. Go to the [Storage](https://storage.gcore.com/storage/list) section.

2. Click the **···** icon opposite the storage that you want to use for the bucket’s creations and select **Buckets**.

<img src="https://support.gcore.com/hc/article_attachments/9583826509201" alt="" width="480" height="179">

2. Click the **Add new bucket** button.

<img src="https://support.gcore.com/hc/article_attachments/9583820047249" alt="" width="399" height="144">

3. Enter the name of the bucket and click **Create**.

**Note.** The name must be unique. Our system checks the names of buckets of all users. If the name matches the name of the bucket of another user, you will see the error _create bucket: bucket already exist: bad params_.

<img src="https://support.gcore.com/hc/article_attachments/9583820068497" alt="" width="231" height="101">

The bucket’s creation is complete.

Add Lifecycle policy (available for S3 in Luxembourg only)
----------------------------------------------------------

You can configure the lifecycle policy for a bucket via the _aws cli_ client according to the [‎“Lifecycle policy. Delete objects from the bucket automatically”](https://gcore.com/support/articles/360003952457/)‎ guide. If you use S3 storage in Luxembourg, it is possible to assign Lifecycle policy for buckets in the control panel:

1. Open the bucket page, click the **···** icon and select **Lifecycle Management**.

<img src="https://support.gcore.com/hc/article_attachments/9583826542353" alt="" width="400" height="166">

**Note:** If your S3 storage is in different locations OTHER THAN Luxembourg (e.g., Chicago, Singapore, and so on), the Lifecycle Management menu item will be absent.

2. Enter the number of days. After this time, files will be deleted from the bucket. Click **Save changes**.

<img src="https://support.gcore.com/hc/article_attachments/9583826570129" alt="" width="225" height="221">

If you want to discard the expiration time, click the **Cancel policy** button.

Configure HTTP access
---------------------

If you want to use [S3 storage as the origin for a CDN resource](https://gcore.com/support/articles/360002237078/), you must share access to a bucket. In this case, all files from the bucket will be available via the HTTP protocol.

1. Open the bucket page, click the **···** icon and select **HTTP access to all files**.

<img src="https://support.gcore.com/hc/article_attachments/9583826576913" alt="" width="400" height="166">

2. Press **Apply**.

<img src="https://support.gcore.com/hc/article_attachments/9583826600849" alt="" width="248" height="83">

Use File manager
----------------

File manager makes it possible to create folders and upload and delete files. You can also get S3 and HTTP/HTTPS links to files.

Override CORS for a bucket
--------------------------

To use File manager, you must first configure the CORS. The CORS technology makes it possible to handle requests from our domain _storage.gcorelabs.com_.

**Note:** CORS should be configured for each bucket separately.

You can configure CORS in three ways:

*   Via s3cmd according to the [“Set CORS policy on a bucket via s3cmd”](https://gcore.com/support/articles/4408830003345/) guide.
*   Via API according to the [API docs](https://apidocs.gcore.com/storage)—this way makes it possible to override CORS not only for _storage.gcorelabs.com_ and other domains.
*   In the control panel.

To configure CORS in the control panel:

1. Open the bucket page, click the **···** icon, and select **File manager**.

<img src="https://support.gcore.com/hc/article_attachments/9583826602385" alt="" width="400" height="166">

2. Click the **Override CORS** button.

<img src="https://support.gcore.com/hc/article_attachments/9583820172049" alt="" width="264" height="217">

That’s it. After this action, you should enter the Access and Secret key to log in to the File Manager. Access and Secret keys are the credentials that are generated after storage creation. We don’t keep them in our system because it’s private and secure information. If you’ve forgotten keys, generate a new one in the Storage section by pressing the **···** icon and selecting **Generate new keys**.

<img src="https://support.gcore.com/hc/article_attachments/9583820180753" alt="" width="480" height="154">

Add a folder to a bucket
------------------------

1. Open File manager.

2. Click **Add folder**. Enter the name of the folder and click **Create**.

<img src="https://support.gcore.com/hc/article_attachments/9583826672017" alt="" width="400" height="218">

The folder is created. After this, you can work with files.

Manage files
------------

1. Open File manager and go to the folder where you want to upload files. You can also upload files to the bucket root.

2. Click **Select files**, select them from your PC, and click **Upload**.

<img src="https://support.gcore.com/hc/article_attachments/9583826673425" alt="" width="400" height="223">

Files will be loaded to a folder or a bucket. Then, you can copy links to files from the bucket in different formats: in S3 to manage them via the console or terminal, and conventional HTTP/HTTPS links to view files in the browser.

To get links, check the boxes on the left of files and click **Copy S3 URL** or **Copy URL**.

<img src="https://support.gcore.com/hc/article_attachments/9583820224913" alt="" width="480" height="126">

For example, for the file _sample.txt_, the links look as follows:

*   s3://s-ed1.cloud.gcore.lu/example/folder1/sample.txt
*   https://s-ed1.cloud.gcore.lu/example/folder1/sample.txt

where

*   _s3_ or _https_ is a protocol (format)
*   _s-ed1.cloud.gcore.lu_ is a hostname
*   _example_ is a bucket
*   _folder1_ is a folder
*   _sample.txt_ is a file name.

You can also delete files. To do this, click **Delete** opposite those files that you want to remove from the folder or bucket.

Delete buckets
--------------

Deletion time depends on the overall size of the files that are in the bucket.

To delete a bucket, click the **···** icon on the bucket’s page, select **Delete** and confirm.

<img src="https://support.gcore.com/hc/article_attachments/9583820228497" alt="" width="400" height="166">