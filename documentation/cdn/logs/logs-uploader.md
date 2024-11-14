---
title: logs-uploader
displayName: Logs uploader (near-realtime)
published: true
order: 20
toc:
   --1--Logs uploader settings: "logs-uploader-settings"
   --2--Logs uploader statuses: "logs-uploader-statuses"
   --2--Log format: "log-format"
   --2--Log fields: "log-fields"
   --1--Configure logs for export: "configure-logs-for-export"
   --2--Step 1. Enable origin shielding: "step-1-optional-enable-origin-shielding"
   --2--Step 2. Include empty logs: "step-2-optional-include-empty-logs"
   --2--Step 3. Select log fields: "step-3-select-log-fields"
   --2--Step 4. Configure a storage provider: "step-4-configure-a-storage-provider"
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

### Log format

```
"$remote_addr" "-" "$remote_user" "[$time_local]" "$request" "$status"  
"$body_bytes_sent" "$http_referer" "$http_user_agent" "$bytes_sent"  
"$edgename" "$scheme" "$host" "$request_time"  
"$upstream_response_time" "$request_length" "$http_range" "[$responding_node]"  
"$upstream_cache_status" "$upstream_response_length" "$upstream_addr"  
"$gcdn_api_client_id" "$gcdn_api_resource_id" "$uid_got" "$uid_set"  
"$geoip_country_code" "$geoip_city" "$shield_type" "$server_addr" "$server_port"  
"$upstream_status" "-" "$upstream_connect_time" "$upstream_header_time"  
"$shard_addr" "$geoip2_data_asnumber" "$connection" "$connection_requests"  
"$http_traceparent" "$http_x_forwarded_proto" "$gcdn_internal_status_code" "$ssl_cipher"  
"$ssl_session_id" "$ssl_session_reused" "$sent_http_content_type" "$tcpinfo_rtt" 
"$server_country_code" "$gcdn_tcpinfo_snd_cwnd" "$gcdn_tcpinfo_total_retrans" "$gcdn_rule_id" 
```

It’s OK if you find a field that’s not listed in the example. We occasionally add new fields to the end of the line. If some fields are added to logs, you’ll receive an email about the update. 

### Log fields

The following table contains a complete list of available log fields. Fields formatted in italics relate to our internal CDN system, so you can ignore them.  

You can check other fields—they can be helpful for traffic analysis or statistics. 

<expandable-element title="View log fields">
<table>
<thead>
  <tr>
    <th>Field</th>
    <th>Log value example</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$remote_addr</td>
    <td>0.0.0.0</td>
    <td>User's IP address</td>
  </tr>
  <tr>
    <td>$remote_user<br>(internal system variable)</td>
    <td>-</td>
    <td>Username used in Basic authentication </td>
  </tr>
  <tr>
    <td>[$time_local]</td>
    <td>[26/Apr/2019<br>:09:47:40 +0000]</td>
    <td>Local time in Common Log Format</td>
  </tr>
  <tr>
    <td>$request</td>
    <td>GET /ContentCommon/<br>images/image.png<br>HTTP/1.1</td>
    <td>HTTP method, requested file path, HTTP version</td>
  </tr>
  <tr>
    <td>$status</td>
    <td>200</td>
    <td>Response status code from a CDN server</td>
  </tr>
  <tr>
    <td>$body_bytes_sent</td>
    <td>1514283</td>
    <td>Number of bytes sent to a user, excluding the response header size</td>
  </tr>
  <tr>
    <td>$http_referer</td>
    <td>https://example.com<br>/videos/10</td>
    <td>Referrer - a URL requested by a user</td>
  </tr>
  <tr>
    <td>$http_user_agent</td>
    <td>Mozilla/5.0<br>(Macintosh; Intel<br>Mac OS X 10_12_1)<br>AppleWebKit/537.36<br>(KHTML, like Gecko)<br>Chrome/53.0.2785.116<br>YaBrowser/16.10.0.2309<br>Safari/537.36</td>
    <td>User agent that was used to send a request (browser or other application)</td>
  </tr>
  <tr>
    <td>$bytes_sent</td>
    <td>1514848</td>
    <td>Number of bytes sent to a user</td>
  </tr>
  <tr>
    <td>$edgename</td>
    <td>[dh-up-gc18]</td>
    <td>CDN server that forwarded a requested file</td>
  </tr>
  <tr>
    <td>$scheme</td>
    <td>https</td>
    <td>Protocol (HTTP or HTTPS) of a request</td>
  </tr>
  <tr>
    <td>$host</td>
    <td>cdn.example.com</td>
    <td>Requested hostname of a CDN resource</td>
  </tr>
  <tr>
    <td>$request_time</td>
    <td>1.500</td>
    <td>Request processing time in seconds (accurate to milliseconds); time elapsed between the first bytes of a request were processed and logging after the last bytes were sent to a user</td>
  </tr>
  <tr>
    <td>$upstream_response_time</td>
    <td>0.445</td>
    <td>Number of seconds (accurate to milliseconds) it took to receive a response from an origin. In case of multiple responses, commas and colons are used </td>
  </tr>
  <tr>
    <td>$request_length</td>
    <td>157</td>
    <td>Request length (including request line, header, and request body)</td>
  </tr>
  <tr>
    <td>$http_range</td>
    <td>bytes=0-1901653</td>
    <td>File fragment size in a Range request</td>
  </tr>
  <tr>
    <td>[$responding_node]</td>
    <td>dh</td>
    <td>Responding data center</td>
  </tr>
  <tr>
    <td>$upstream_cache_status</td>
    <td>MISS</td>
    <td>Status of a requested file in CDN cache:
    <br> HIT is the status of a response served from the CDN cache.
    <br> STALE is the status of an outdated response that failed to update because an origin was not responding or responding incorrectly.
    <br>UPDATING is the status of an outdated response that is still updating since a previous request.
    <br>REVALIDATED is the status of a response that is identical to the one on an origin based on the proxy_cache_revalidate directive.
    <br>EXPIRED is the status of a response that has expired in cache but still matches the one on an origin. A request has been sent to an origin for re-caching.
    <br>MISS is the status of a response that has been served directly from an origin rather than from a cache.
    <br>BYPASS is the status of a response for the first file request after clearing the cache. This status appears when the file is requested by each CDN server.
    <br>When one CDN server requests a file for the first time, it will have the BYPASS status.
    <br>When the same server requests the file again, the status will be changed to HIT.<br>When another CDN server requests the file, it will again have the BYPASS status.<br></td>
  </tr>
  <tr>
    <td>$upstream_response_length</td>
    <td> 10485760</td>
    <td>Response length from an origin in bytes. In case of multiple responses, commas and colons are used</td>
  </tr>
  <tr>
    <td>$upstream_addr</td>
    <td>0.0.0.0:80</td>
    <td>Origin's IP address and port</td>
  </tr>
  <tr>
    <td>$gcdn_api_client_id<br>(internal system variable)</td>
    <td>123</td>
    <td>Your ID in our system</td>
  </tr>
  <tr>
    <td>$gcdn_api_resource_id<br>(internal system variable)</td>
    <td>01</td>
    <td>Your CDN-resource ID in our system</td>
  </tr>
  <tr>
    <td>$uid_got<br>(internal system variable)</td>
    <td>-</td>
    <td>Cookie name and received user ID</td>
  </tr>
  <tr>
    <td>$uid_set<br>(internal system variable)</td>
    <td>-</td>
    <td>Cookie name and provided user ID</td>
  </tr>
  <tr>
    <td>$geoip_country_code</td>
    <td>KZ</td>
    <td>User’s country code according to the <a href="https://iso.org/obp/ui/#search/code"><span style="text-decoration:underline;color:#FF5700">ISO 3166 standard</span></a> (Alpha-2 code).</td>
  </tr>
  <tr>
    <td>$geoip_city</td>
    <td>-</td>
    <td>User’s city code</td>
  </tr>
  <tr>
    <td>$shield_type<br>(internal system variable)</td>
    <td>shield_no</td>
    <td>This field shows whether the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding"><span style="text-decoration:underline;color:#FF5700">shielding option</span></a> is enabled:<br>shield_old - enabled<br>shield_no - disabled</td>
  </tr>
  <tr>
    <td>$server_addr<br>(internal system variable)</td>
    <td>0.0.0.0</td>
    <td>IP address of an Anycast zone or CDN server</td>
  </tr>
  <tr>
    <td   >$server_port<br>(internal system variable)</td>
    <td   >80</td>
    <td   >Requested port</td>
  </tr>
  <tr>
    <td  >$upstream_status</td>
    <td  >206</td>
    <td  >Origin response code</td>
  </tr>
  <tr>
    <td  >$upstream_connect_time</td>
    <td  >0.000</td>
    <td  >Number of seconds (accurate to milliseconds) it took to access an origin server</td>
  </tr>
  <tr>
    <td  >$upstream_header_time</td>
    <td  >0.200</td>
    <td  >Number of seconds (accurate to milliseconds) it took to receive a response header from an origin server</td>
  </tr>
  <tr>
    <td   >$shard_addr<br>(internal system variable)</td>
    <td   >0.0.0.0</td>
    <td   >IP address of a CDN server that was first to accept a request if the Cache Sharding feature is enabled</td>
  </tr>
  <tr>
    <td  >$geoip2_data_asnumber</td>
    <td  >asnumber</td>
    <td  >Number of an autonomous system that sent a request</td>
  </tr>
  <tr>
    <td   >$connection<br>(internal system variable)</td>
    <td   >2897494295</td>
    <td   >Connection serial number</td>
  </tr>
  <tr>
    <td   >$connection_requests<br>(internal system variable)</td>
    <td   >1</td>
    <td   >Current number of requests made through a connection</td>
  </tr>
  <tr>
    <td>$http_traceparent<br>(internal system variable)</td>
    <td   >00-d5fe1dc903<br>5165ce36952da<br>f29686b6c-143<br>30be33197dd1a<br>-01</td>
    <td>Unique request identifier, more info in the <a href="https://gcore.com/docs/cdn/troubleshooting/traceparent-header-for-troubleshooting" target="_blank">Traceparent guide</a></td>
  </tr>
  <tr>
    <td>$http_x_forwarded_proto</td>
    <td  >-</td>
    <td>Initial protocol of an incoming request (HTTP or HTTPS)</td>
  </tr>
  <tr>
    <td>$gcdn_internal_status_code,<br>(internal system variables)</td>
    <td>-</td>
    <td>Initial status code. Possible values are: <code>-</code>, or <code>100700</code></td>
  </tr>
  <tr>
    <td   >$ssl_cipher<br>(internal system variable)</td>
    <td   >ECDHE-RSA-AES256<br>-GCM-SHA384</td>
    <td   >Cipher name used for an established SSL connection</td>
  </tr>
  <tr>
    <td   >$ssl_session_id<br>(internal system variable)</td>
    <td   >28a4184139cb43<br>cdc79006cf2d1<br>a4ac93bdc****</td>
    <td   >Session ID of an established SSL connection</td>
  </tr>
  <tr>
    <td   >$ssl_session_reused<br>(internal system variable)</td>
    <td   > r</td>
    <td   >The field shows whether a session was reused (“r” ) or not (“.”)</td>
  </tr>
  <tr>
    <td  >$sent_http_content_type</td>
    <td  >application/json</td>
    <td  >Value of the Content-Type HTTP header, indicating the MIME type of a transmitted file</td>
  </tr>
  <tr>
    <td  >$tcpinfo_rtt</td>
    <td  >  21</td>
    <td  >Average time (latency) it takes to transfer a packet to/from a server. The unit of time is microseconds.</td>
  </tr>
  <tr>
  <td>$server_country_code</td>
  <td>PL</td>
  <td>Server’s country code according to the <a href="https://iso.org/obp/ui/#search/code"><span style="text-decoration:underline;color:#FF5700">ISO 3166 standard</span></a> (Alpha-2 code).</td>
  </tr>
  <tr>
    <td>$gcdn_tcpinfo_snd_cwnd</td>
    <td>45</td>
    <td>Size of the TCP Congestion window, i.e., the maximum number of TCP segments that the connection can send before an acknowledgment is required.</td>
  </tr>
  <tr>
    <td>$tcpi_total_retrans</td>
    <td>10</td>
    <td>Total number of retransmitted packets over the life of the connection.</td>
  </tr>
  <tr>
  <td>$gcdn_rule_id</td>
  <td>100700</td>
  <td>Initial rule ID (beta). Possible values are: <code>-</code>, or <code>100700</code></td>
  </tr>
</tbody>
</table>

</expandable-element>

## Configure logs for export

You can enable Logs uploader feature in the Gcore Customer Portal on the <a href="https://gcore.com/cdn" target="_blank">Gcore CDN page</a>. To open log settings, navigate to  **Logs** > **Logs uploader** and configure the feature as described above in the following steps.

### Step 1 (optional). Enable origin shielding

If you are using the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">origin shielding</a> feature, you’ll see the **Add logs from origin shielding** checkbox when configuring Logs uploader. 

We recommend that you select this option as it ensures that the logs report will include both requests to cache services and requests to the pre-cache server. Thus, you’ll receive more detailed information on resource usage. To include these logs, select the checkbox to enable **Include logs from origin shielding**.

<img src="https://assets.gcore.pro/docs/cdn/logs/logs-uploader/enable-origin-shielding.png" alt="Include logs from origin shielding checkbox highlighted" width="80%">

<alert-element type="tip" title="Tip">
 
If you don’t see the origin shielding option on the **Logs uploader** page, this feature is not activated for your account. For details on how to activate origin shielding, check our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">dedicated guide</a>. 
 
</alert-element>

### Step 2 (optional). Include empty logs

Keep the **Do not send empty logs** option selected if you don't want to receive empty logs. Otherwise, uncheck it. 

### Step 3. Select log fields

Choose which <a href="https://gcore.com/docs/cdn/logs/logs-uploader#log-fields" target="_blank">log fields</a> you want to include in the exported report. By default, all fields are selected. 

## Step 4. Configure a storage provider

<tabset-element>

### Amazon

Follow these instructions to export logs to AWS storage: 

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