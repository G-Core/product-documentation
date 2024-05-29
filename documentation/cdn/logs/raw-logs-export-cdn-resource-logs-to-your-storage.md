---
title: raw-logs-export-cdn-resource-logs-to-your-storage
displayName: Raw Logs (paid)
published: true
order: 10
toc:
   --1--Raw Logs settings: "raw-logs-settings"
   --2--Add logs from Origin Shielding: "add-logs-from-origin-shielding"
   --2--Raw Logs statuses: "raw-logs-statuses"
   --2--Export time intervals: "export-time-intervals"
   --2--Log traffic calculation: "log-traffic-calculation" 
   --2--Log path example: "log-path-example"
   --2--Log example: "log-example"
   --2--Log format: "log-format"
   --2--Log fields: "log-fields"
   --1--Export logs to S3 storage: "export-logs-to-s3-storage"
   --2--Amazon storage: "amazon-storage"
   --2--Non-Amazon storage: "non-amazon-storage"
   --1--Export logs to FTP or SFTP storage: "export-logs-to-ftp-or-sftp-storage"

pageTitle: Guide on Using the CDN Raw Logs Feature | Gcore
pageDescription: A comprehensive guide on using the CDN Raw Logs feature for exporting logs to your storage, understanding traffic calculation in log reports.
---
# Raw Logs: export CDN resource logs to your storage

Raw Logs is an option that enables an automatic export of CDN resource logs to your storage. Logs contain information about user requests sent to cache servers and pre-cache servers (if the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> is enabled).

<alert-element type="info" title="Info">

This is a paid feature. To activate Raw Logs, [contact the Gcore support team](mailto:support@gcore.com). 

After activation, enable Raw Logs in the Gcore Customer Portal and configure export to S3, FTP, or SFTP storage.

</alert-element>

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/raw-logs-page.png" alt="Raw Logs page in Customer Portal">

## Raw Logs settings  

In this section, you can find general information about log settings, overview of log statuses, and details on how Raw Logs are exported and calculated. 

### Add logs from Origin Shielding 

If you are using the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> feature, you’ll see the **Add logs from origin shielding** checkbox when configuring logs. We recommend that you select this option as it ensures that the logs report will include both requests to cache services and requests to the pre-cache server. Thus, you’ll receive more detailed information on resource usage. 

When setting up Raw Logs, select the checkbox to enable **Add logs from origin shielding**.

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/add-logs-from-origin-shielding.png" alt="Raw Logs page with the checkbox highlighted">

<alert-element type="tip" title="Tip">
 
If you don’t see the Origin Shielding option on the Raw Logs page, this feature is not activated for your account. For details on how to activate Origin Shielding, check our<a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">dedicated guide</a>. 
 
</alert-element>

### Raw Logs statuses 

You can check the status of the Raw Logs in the Gcore Customer Portal: 

* **Pending**: A status for the time interval between the connection to storage and the first log export. 

* **OK**: Logs are exported from at least one CDN server. 

* **Failed**: An error occurred while connecting to a storage, or the service failed to export logs within 24 hours. 

* **Pause**: The Raw Logs feature is paused. 

### Export time intervals 

Logs are exported at the end of each hour. If you activate Raw Logs at 00:30, the first logs will be exported between 00:45 and 01:00 and the next ones—between 01:45 and 02:00. 

If CDN servers are not requested and you didn’t select the **Do not send empty logs** checkbox when configuring Raw Logs, an empty log file (± 20 bytes) will be sent to your storage. 

### Log traffic calculation 

Logs can generate various types of analytics, such as delivered traffic. To understand what the totals mean, we recommend that you familiarize yourself with the formulas for calculating logs. For details about CDN reports, check out the <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource" target="_blank">View statistics on CDN resources</a> guide.  

The formula for calculating traffic depends on whether you’ve selected the **Add logs from origin shielding** option for Raw Logs. 

<expandable-element title="If Origin Shielding is disabled">
If this feature is disabled, the formula will look like this: 

```
total_bytes = upstream_bytes + sent_bytes 
```

Where:

- ```upstream_bytes``` are equal to the ```$upstream_response_length``` log field and refer to the response length from an origin in bytes
- ```sent_bytes``` are equal to the ```$bytes_sent``` log field and refer to the number of bytes sent to a user from the edge (cache) servers

For example, if ```$upstream_response_length``` is 10485760 (bytes) and ```$bytes_sent``` is 1514848 (bytes), the final value in the Raw logs report will be 12,000,608 (bytes).
 
</expandable-element>

<expandable-element title="If Origin Shielding is enabled">
If this feature is enabled, the formula will look like this: 

```
total_bytes = upstream_bytes + sent_bytes + shield_bytes
```

Where:

- ```upstream_bytes``` are equal to the ```$upstream_response_length``` log field and refer to the response length from an origin in bytes
- ```sent_bytes``` are equal to the ```$bytes_sent``` log field and refer to the number of bytes sent to a user from the edge (cache) servers
- ```shield_bytes``` are equal to the ```$bytes_sent``` log field and refer to the number of bytes sent to a user from the pre-cache server
 
</expandable-element>

<alert-element type="info" title="Info">
 
The final value of log data may differ slightly from the billing statistics as there may be cases where not all logs are received, such as: 

* You are using the <a herf="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding"> target="_blank">Origin Shielding</a> feature but didn’t select the **Add logs from origin shieldin**g option. 

* You have a rate limit set on your storage side, and when CDN started generating logs, some logs weren’t downloaded because of the rate limitation. 
 
</alert-element>

## Log path example

```
s3://log-bucket-name/2019/08/20/15/nodename_primarycname.domain.ru_access.log.gz
```

## Log example

```
"0.0.0.0" "-" "-" "[26/Apr/2019:09:47:40 +0000]" "GET /ContentCommon/images/image.png HTTP/1.1"  
"200" "1514283" "https://example.com/videos/10" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1)  
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 YaBrowser/16.10.0.2309 Safari/537.36"  
"1514848" "[dh-up-gc18]" "https" "origin.cdn.com" "1.500" "0.445" "157" "bytes=0-1901653" "[dh]"  
"MISS" "10485760" "0.0.0.0:80" "2510" "7399" "-" "-" "KZ" "-" "shield_no" "0.0.0.0" "80" "206" "-" "0.000"  
"0.200" "0.0.0.0" "asnumber" "106980391" "1" "00-d5fe1dc9035165ce36952daf29686b6c-14330be33197dd1a-01" "-" "-"  
"ECDHE-RSA-AES256-GCM-SHA384" "28a4184139cb43cdc79006cf2d1a4ac93bdc****" "r"  
"application/json" "21" "PL" "45" "10" "100700"
```

## Log format

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

## Log fields

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
    <td   >The filed shows whether a session was reused (“r” ) or not (“.”)</td>
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

## Export logs to S3 storage

### Amazon storage

1\. In the Gcore Customer Portal, navigate to **CDN** > **Logs**. 

2\. Enable the **Receive Raw Logs** toggle to open log settings.

3\. Keep the **Do not send empty logs** option selected if you don't want to receive empty logs. Otherwise, uncheck it. 

4\. If you use our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> feature, you’ll see a checkbox **Add logs from origin shielding**. Select the checkbox to receive logs from both edge servers and pre-cache shielding servers. 

5\. Select to receive logs using S3.

6\. Choose Amazon as the storage type. 

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/export-logs-from-amazon-1.png" alt="Raw logs settings for Amazon S3" width="80%">

7\. Specify your access key ID. In your Amazon personal account, it's called "AWS access key ID". For details on how to find your key ID, check the <a href="https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html" target="_blank">official Amazon guide</a>. An access key ID and secret access key are required to configure log export to your storage.

8\. Specify your secret access key. In your Amazon account, it's called "AWS secret access key". For details on how to find your access key, check the <a href="https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html" target="_blank">official Amazon guide</a>. 

9\. (Optional) Enter your AWS region—the location of a server where your storage is hosted. For most storage types, the region is determined automatically, so you might leave the field empty. However, we recommend specifying the region to ensure that your logs are exported successfully. 

10\. Choose how to organize your storage: put logs of all CDN resources into one bucket or use separate buckets for each CDN resource.

11\. Specify buckets for log export. Make sure to indicate an existing bucket. Otherwise, your logs won’t be exported.  
Enter a folder name if you want to export logs to a specific folder within a bucket.

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/export-logs-from-amazon-2.png" alt="Raw logs settings for Amazon S3" width="80%">

12\. Click **Save changes**.

You've successfully configured Raw Logs export to Amazon S3.

### Non-Amazon storage

1\. In the Gcore Customer Portal, navigate to **CDN** > **Logs**. 

2\. Enable the **Receive Raw Logs** toggle to open log settings.  

3\. Keep the **Do not send empty logs** option selected if you don't want to receive empty logs. Otherwise, uncheck it. 

4\. If you use our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> feature, you’ll see a checkbox **Add logs from origin shielding**. Select the checkbox to receive logs from both edge servers and pre-cache shielding servers. 

5\. Select to receive logs using S3.

6\. Select Other as the storage type. 

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/export-logs-from-s3-other-1.png" alt="Raw logs settings for 3-rd party S3 storage" width="80%">

7\. Specify a hostname—a name that's assigned to a storage server within a network and is used instead of an IP address. If you use <a href="https://gcore.com/storage" target="_blank">Gcore Object Storage</a>, you can find its access key ID in your personal account in the <a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">Hostname</a> field.

8\. Specify your access key ID. Along with a secret access key, it's required to configure log export to your storage. If you use <a href="https://gcore.com/storage" target="_blank">Gcore Object Storage</a>, you can find its access key ID in your personal account in the <a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">Access key</a> field.

9\. Specify your secret access key. If you use <a href="https://gcore.com/storage" target="_blank">Gcore Object Storage</a>, you can find its secret access key in your personal account in the <a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">Secret key</a> field.

10\. Specify a bucket hostname—a bucket ID that's used by your Object storage system in the ```{bucket_name}.{hostname}``` format. It's required to ensure that logs are exported to the correct bucket within a storage. A bucket hostname of the Gcore storage looks as follows: ```{bucket name}.{hostname from step 3}```. 
For example: ```examplename.s-ed1.cloud.gcore.lu```. 

11\. (Optional) Specify a regio—location ID of a server where your storage is hosted. For some storage types, the region is determined automatically, so you can leave the field empty. 

<alert-element type="info" title="Info">
 
If you use <a href="https://gcore.com/storage" target="_blank">Gcore Object Storage</a>, a location ID is required. You can find it in the <a href="https://gcore.com/docs/storage/request-content-directly-from-the-storage" target="_blank>Details of the storage</a. Your location ID is a part of your hostname to the first dot.  
 
</alert-element>

12\. Choose how to organize storage: put logs of all CDN resources into one bucket or use separate buckets for each CDN resource. 

13\. Specify buckets for log export. Make sure to indicate an existing bucket. Otherwise, your logs won’t be exported. If you want to export logs to a specific folder within a bucket, specify the folder name. 

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/export-logs-from-s3-other-2.png" alt="Raw logs settings for 3-rd party S3 storage" width="80%">

14\. Click **Save changes**. 

You've successfully configured Raw Logs export to S3 storage.

## Export logs to FTP or SFTP storage

1\. In the Gcore Customer Portal, navigate to **CDN** > **Logs**. 

2\. Enable the **Receive Raw Logs** toggle to open log settings.  

3\. Keep the **Do not send empty logs** option selected if you don't want to receive empty logs. Otherwise, uncheck it. 

4\. If you use our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> feature, you’ll see a checkbox **Add logs from origin shielding**. Select the checkbox to receive logs from both edge servers and pre-cache shielding servers. 

5\. Select to receive logs via SFTP. 

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/export-logs-from-sftp-1.png" alt="Raw logs settings for SFTP storage" width="80%">

6\. Specify a hostname—a name that’s assigned to a storage server within a network and is used instead of an IP address. If you use <a href="https://gcore.com/storage" target="_blank">Gcore SFTP Storage</a>, you can find its hostname in the <a href="https://gcore.com/docs/storage/request-content-directly-from-the-storage" target="_blank">Details of the storage</a> in the <a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#sftp" target="_blank">Hostname field</a>. It looks as follows: ```ams.origin.gcdn.co```.

<alert-element type="warning" title="Warning">
 
You need to specify an FTP or SFTP storage port after the hostname. For example: ```ams.origin.gcore.co:2200```. Otherwise, you’ll get the “Wrong connection settings error” and won’t be able to connect to the storage. 
 
</alert-element>

7\. Specify a username you use to log in to the storage. If you use <a href="https://gcore.com/storage" target="_blank">Gcore SFTP storage</a>, you can find the username in the <a href="https://gcore.com/docs/storage/request-content-directly-from-the-storage" target="_blank">Details of your storage</a> in the <a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#sftp" target="_blank">Storage/User name</a> field.

8\. Enter the password you use to authenticate to the storage. 

9\. Specify a folder for export. If you use <a href="https://gcore.com/storage" target="_blank">Gcore SFTP storage</a>, specify the root (home) folder where other folders originate from. You can find its name in the <a href="https://gcore.com/docs/storage/request-content-directly-from-the-storage" target="_blank">Details of your storage</a> at the end of the **Upload path** field.

If you use an SFTP storage from another provider, clarify whether a root folder that includes other folders is created by default. If not, leave the field empty. If yes, specify a folder name.

<alert-element type="info" title="Info">
 
If you’re using the Gcore SFTP storage, you won’t be able to write to the home folder. It only receives logs and can’t be manually modified. 
 
</alert-element>

10\. Choose how to organize the storage: put logs of all CDN resources into one folder or use separate folders for each CDN resource. Then, specify a folder name. If you specify a non-existent folder, logs will be exported to a root folder.

11\. (Optional) Specify the folder name where logs will be stored. If you specify a non-existent folder, logs will be exported to a root folder. For Gcore SFTP storage, you can only specify the default **htdocs** folder.  

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/export-logs-from-sftp-2.png" alt="Raw logs settings for SFTP storage" width="80%">

12\. Click **Save changes**.

You've successfully configured Raw Logs export to FTP or SFTP storage.

## Deactivate Raw Logs 

To stop Raw Logs delivery, disable the **Receive Raw Logs** toggle.  

If you disable the logs, your settings will be saved. You can always activate the same configuration by enabling the Receive Raw Logs toggle again.  

If you made any changes to the configuration, click Discard changes to cancel any changes made during the editing process.

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/deactivate-logs.png" alt="Raw logs settings for SFTP storage" width="80%">