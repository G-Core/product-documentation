---
title: manage-buckets-via-the-control-panel
displayName: Manage buckets
published: true
order: 10
toc:
   --1--Create a bucket: "create-a-bucket"
   --1--File manager: "file-manager"
   --2--Access (Override CORS): "access-override-cors"
   --2--Authorize: "authorization"
   --2--Add folders: "adding-folders"
   --2--Upload files: "uploading-files"
   --2--Delet folders and files: "deleting-folders-and-files"
   --2--Copy URL or S3 URL: "copying-url-or-s3-url"
   --1--Configure HTTP access: "configuring-http-access"
   --1--Add lifecycle policy (for Luxembourg S3): "adding-lifecycle-policy-for-s3-in-luxembourg-only"
pageTitle: A Comprehensive Guide on How to Manage Gcore Buckets | Gcore
pageDescription: Creating and configuring Gcore storage buckets, adding lifecycle policies, managing files, and setting CORS in the Customer Portal.
---
# Managing buckets through the Customer Portal

## Create a bucket

1\. Navigate to the <a href="https://storage.gcore.com/storage/list" target="_blank">Storage</a> section and click the storage name to open the bucket managing interface.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-10.png" alt="Open the Buckets interface" width="80%">

You can access the bucket interface by clicking the three dots on the right side and selecting **Buckets**.

2\. Click **Add new bucket**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-20.png" alt="Add new bucket" width="80%">

3\. A pop-up window will appear. Here, you'll need to input a name for your bucket that meets the following criteria and then click **Create**:

- The length should be between 3 to 63 characters
- The name should be in lowercase only
- Avoid using underscores, trailing dashes, consecutive dots, or a mix of dots and dashes as they conflict with DNS notation rules
- The bucket name must be unique within the entire Gcore S3 system, not just your account. If a name is already used, you'll receive a ```This bucket name already exists. Please use a different name``` error message

**Note**: Refrain from including sensitive information in the bucket name as it will be visible in the object's URL, potentially posing a security risk.

Once you've completed these steps, your bucket will be created and prepared for the following functions:

- <a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#file-manager" target="_blank">File management</a> (this includes uploading and other related tasks)
- <a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#configuring-http-access" target="_blank">Providing HTTP access to all files within the bucket</a>
- <a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#adding-lifecycle-policy-for-s3-in-luxembourg-only" target="_blank">Setting a lifecycle policy</a> (this feature is only available for the S3 Luxembourg location)

## File manager

### Access (Override CORS)

To access the file manager (Override CORS), you must add ```https://storage.gcore.com``` to your list of approved origins. This is a one-time action.

To access the file manager, click the bucket name you created. A pop-up will appear where you can select **Override CORS**.

**Note**: CORS must be set up individually for each bucket.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-30.gif" alt="Override CORS" width="85%">

You also have the option to set the CORS policy through the <a href="https://api.gcore.com/docs/storage#tag/Storage/operation/storageBucketCORSCreateHttp" target="_blank">API</a>. This method allows you to override CORS for not just ```https://storage.gcore.com``` but also for other domains.

### Authorization

To authorize, click on the bucket name, enter the Access and Secret keys, then click **Auth**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-40.gif" alt="Authorize to file manager" width="80%">

You can access the file manager by clicking the three dots on the right side and selecting **File manager**.

<expandable-element title="Access and Secret keys features">

**Note**: If you have entered keys, they will be saved and will not need to be re-entered within the session. Keys will be requested for each new session.

To avoid manually inputting, save the Access and Secret keys with the browser functionality. 

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-50.png" alt="Manage passwords browser functionality" width="70%">

The Access and Secret keys are generated during storage creation. We don't store them in our system for security and privacy reasons. If you've forgotten the values, click **Generate new keys** in the <a href="https://storage.gcore.com/storage/list" target="_blank">Storages</a> tab.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-60.png" alt="Generate new keys" width="80%">

</expandable-element>

### Adding folders

Once you're <a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#authorization" target="_blank">authorized in the file manager</a>, click **Add folder**. Enter the desired name in the field provided and click **Create**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-70.gif" alt="Creation of folders" width="80%">

In the interface, you can view the last modification date. To open the folder, simply click its name.

### Uploading files

To upload files, <a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#authorization" target="_blank">authorize access to your bucket</a> and click **Select and upload file(s)** either in the bucket root or within a specific folder. Then, follow the standard upload process.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-80.png" alt="Uploading of files" width="80%">

### Deleting folders and files

To delete folders or files, <a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#authorization" target="_blank">authorize access to your bucket</a> and click **Delete** next to the desired object, or select the checkboxes next to the object names and click **Delete selected**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-90.png" alt="Deletion of files" width="80%">

**Note**: Deleting a folder will also delete any nested files within it.

### Copying URL or S3 URL

To copy the links of certain files, <a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#authorization" target="_blank">authorize access to your bucket</a>, select objects and click the relevant buttons: **Copy S3 URL** or **Copy URL**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-100.png" alt="Copy S3 URL and Copy URL" width="80%">

For instance, the links for the file ```image 3972.png``` will look like this:

- ```s3://s-ed1.cloud.gcore.lu/000-sample-for-articles/test/image%3972.png```
- ```https://s-ed1.cloud.gcore.lu/000-sample-for-articles/test/image%3972.png```

**Note**: If <a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#configuring-http-access" target="_blank">HTTP access to all files</a> is not enabled, you'll encounter a 403 error when opening the file.

## Configuring HTTP access

If you wish to <a href="https://gcore.com/docs/storage/use-storage-as-the-origin-for-your-cdn-resource" target="_blank">use S3 storage as the origin for a CDN resource</a> or to make files accessible via an S3 URL, you'll need to allow HTTP access to your bucket. To do this, go to the bucket interface, click on the three dots on the right, and select **HTTP access to all files**. Then, click **Apply**.


<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-110.gif" alt="Configure HTTP access to all files" width="80%">

## Adding lifecycle policy (for S3 in Luxembourg only)

To add a lifecycle policy, navigate to the bucket interface, click the three dots to the right, and select **Lifecycle management**. Set the period after which files will be deleted and click **Save changes**.

<img src="https://assets.gcore.pro/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel/manage-buckets-cp-120.gif" alt="Set lifecycle policy" width="80%">

If you decide to remove the expiry time, click **Cancel policy**.

You can still set a lifecycle policy if your storage is outside the S3 Luxembourg location. You can do this with the AWS CLI tool, as outlined in the <a href="https://gcore.com/docs/storage/manage-s3-storage/configure-aws-sli-s3cmd-and-aws-javascript-sdk/remove-objects-from-a-bucket-automatically-with-aws-cli" target="_blank">separate guide</a>.