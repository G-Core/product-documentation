---
title: logs-uploader
displayName: Logs uploader (near-realtime)
published: true
order: 
toc:
   --1--Configure Logs uploader: "configure-logs-uploader"
   --2--For Amazon: "amazon"
   --2--For Object Storage Service: "oss"
   --2--For Gcore or other storage: "gcore-other"
pageTitle: Guide on Using the CDN Logs Uploader Feature | Gcore
pageDescription: A comprehensive guide on using the CDN Logs Uploader feature for exporting logs to your storage in near-realtime.
---
# Logs uploader (near-realtime)

Logs Uploader is a feature that enables an automatic export of CDN resource logs to your storage in near-realtime. 

Exported logs contain information about user requests sent to cache servers and pre-cache servers (if you have the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin shielding</a> feature enabled).

<alert-element type="info" title="Info">

This is a paid feature. To activate Logs Uploader, [contact the Gcore support team](mailto:support@gcore.com). 

</alert-element>

## Logs uploader settings

In this section, you can find general information about log settings, statuses, and how to configure logs exporting for different storage types.

### Logs uploader statuses 

You can check the status of the Logs uploader in the Gcore Customer Portal: 

* **Pending**: A status for the time interval between the connection to storage and the first log export. 

* **OK**: Logs are exported from at least one CDN server. 

* **Failed**: An error occurred while connecting to a storage, or the service failed to export logs within 24 hours. 

* **Pause**: The Logs uploader feature is paused. 

### Add logs from Origin Shielding 

If you are using the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> feature, you’ll see the **Add logs from origin shielding** checkbox when configuring Logs uploader. 

We recommend that you select this option as it ensures that the logs report will include both requests to cache services and requests to the pre-cache server. Thus, you’ll receive more detailed information on resource usage. 

When configuring Logs uploader, select the checkbox to enable **Add logs from origin shielding**.

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/.png" alt="Logs uploader page with the checkbox highlighted" width="80%">

<alert-element type="tip" title="Tip">
 
If you don’t see the Origin Shielding option on the **Logs uploader** page, this feature is not activated for your account. For details on how to activate Origin Shielding, check our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">dedicated guide</a>. 
 
</alert-element>

## Export logs with Logs uploader

<tabset-element>

### Amazon

Follow these instructions to export logs to AWS storage: 

1\. Open the <a href="https://gcore.com/cdn" target="_blank">Gcore CDN page</a> and navigate to **Logs** > **Logs uploader**. 

2\. Enable the feature and configure its settings as described above in the <a href="https://gcore.com/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage#logs-uploader-configuration" target="_blank">Logs uploader configuration</a> section. 

3\. In the **Storage provider**, select **Amazon**. 

4\. Provide your access key ID and secret access key, which together form <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html" target="_blank">long-term AWS credentials</a>. 

5\. (Optional). Choose a storage region. While the region is often determined automatically, we recommend specifying it to ensure that your logs are exported successfully. 

6\. Specify the name of a bucket where you want to export CDN logs. 

7\. (Optional). Enter a folder name if you want to export logs to a specific folder within a bucket. 

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/logs-uploader-aws.png" alt="Receive logs to AWS" width="80%">

### OSS

Follow these instructions to export logs to configure logs for Alibaba Cloud <a href="https://www.alibabacloud.com/en/product/object-storage-service?_p_lc=1" target="_blank">Object Storage Service</a> (OSS): 

1\. Open the <a href="https://gcore.com/cdn" target="_blank">Gcore CDN page</a> and navigate to **Logs** > **Logs uploader**. 

2\. Enable the feature and configure its settings as described above in the <a href="https://gcore.com/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage#logs-uploader-configuration" target="_blank">Logs uploader configuration</a> section. 

3\. In the **Storage provider**, select **OSS**. 

4\. Provide your access key ID and secret access key. Check the <a href="https://www.alibabacloud.com/help/en/oss/developer-reference/access-control/?spm=a2c63.p38356.0.0.439d43celIzLks" target="_blank">official OSS documentation</a> for details. 

5\. (Optional). Choose a storage region. While the region is often determined automatically, we recommend specifying it to ensure that your logs are exported successfully. 

6\. Specify the name of a bucket where you want to export CDN logs. 

7\. (Optional). Enter a folder name if you want to export logs to a specific folder within a bucket. 

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/logs-uploader-oss.png" alt="Receive logs to AWS" width="80%">

### Gcore\Other

Follow these instructions to export logs to <a href="https://gcore.com/storage" target="_blank">Gcore Object Storage</a> or any S3 storage of your choice: 

1\. Open the <a href="https://gcore.com/cdn" target="_blank">Gcore CDN page</a> and navigate to **Logs** > **Logs uploader**. 

2\. Enable the feature and configure its settings as described above in the <a href="https://gcore.com/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage#logs-uploader-configuration" target="_blank">Logs uploader configuration</a> section. 

3\. In the **Storage provider**, select **Gcore** or **Other**. 

4\. Specify a hostname—a name that’s assigned to a storage server within a network and is used instead of an IP address. In you’re using Gcore Storage, you can find your hostname in the <a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#object-storage" target="_blank">storage details section</a>. 

5\. Provide your access key ID and secret access key. You can find this information in the <a href="https://gcore.com/docs/storage/request-content-directly-from-the-storage" target="_blank">Details of the storage</a>. 

6\. Specify the name of a bucket where you want to export CDN logs. 

7\. (Optional). Enter a folder name if you want to export logs to a specific folder within a bucket. 

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/logs-uploader-gcore-other.png" alt="Receive logs to AWS" width="80%">

</tabset-element>