---
title: raw-logs-export-cdn-resource-logs-to-your-storage
displayName: Raw Logs (paid)
published: true
order: 10
toc:
   --1--What is a Raw Logs feature?: "what-is-a-raw-logs-feature"
   --1--What is "Add logs from origin shielding"?: "what-is-the-add-logs-from-origin-shielding-option"
   --1--How is traffic calculated?: "how-is-traffic-calculated-in-log-reports" 
   --1--Export to an S3 storage: "export-logs-to-an-s3-storage"
   --2--Amazon storage: "amazon-storage"
   --2--Non-Amazon storage: "non-amazon-storage"
   --1--Export to an FTP/SFTP storage: "export-logs-to-an-ftp-sftp-storage"
   --1--Export time intervals: "export-time-intervals"
   --1--Log path example: "log-path-example"
   --1--Log format: "log-format"
   --1--Log example: "log-example"
   --1--Log fields: "log-fields"
pageTitle: Mastering CDN Raw Logs | Gcore
pageDescription: A comprehensive guide on using the CDN Raw Logs feature for exporting logs to your storage, understanding traffic calculation in log reports.
---
# Raw Logs: export CDN resource logs to your storage

## What is a Raw Logs feature?

Raw Logs is an option that enables an automatic export of CDN resource logs to your storage. Logs contain information about user requests sent to cache servers and pre-cache servers (if <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">origin shielding</a> is enabled).

**Note**: The feature is paid. To activate, contact us via [support@gcore.com](mailto:support@gcore.com). After activation, enable "Raw Logs" in your control panel and configure export to S3, FTP, or SFTP storage.

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/13202181890193.png" alt="What is a Raw Logs feature">

## What is the "Add logs from origin shielding" option? 

If you are using the <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin Shielding</a> feature, we recommend that you enable the "Add logs from origin shielding" option. This means that the report will include not only requests to cache services, but also those to the pre-cache server. As a result, you will receive more detailed information on resource usage.

**Note**: If your account does not have "Origin Shielding" switched on, this option will not be available when setting up Raw logs.  

To enable "Add logs from origin shielding", tick the appropriate box when setting up Raw Logs (step #2 in the [guide below](https://gcore.com/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage#export-logs-to-an-s3-storage)).

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/15499340205969.png" alt="Add logs from origin shielding" width="50%">

## How is traffic calculated in log reports?

Logs can generate various types of analytics, such as traffic delivered. To understand what the totals mean, we recommend that you familiarize yourself with the formulas for calculating the logs.

The formula for calculating traffic depends on whether you use the "Add logs from origin shielding" option.

1. If this option is disabled, the formula will look like this:

```
total_bytes = upstream_bytes + sent_bytes 
```

Where:
- ```upstream_bytes``` are equal to the ```$upstream_response_length``` log field and refer to the response length from an origin in bytes
- ```sent_bytes``` are equal to the ```$bytes_sent``` log field and refer to the number of bytes sent to a user from the edge (cache) servers

For example, if ```$upstream_response_length``` is 10485760 (bytes) and ```$bytes_sent``` is 1514848 (bytes), the final value in the Raw logs report will be 12,000,608 (bytes).

2. If the "Add logs from origin shielding" option is enabled, the formula will look like this:

```
total_bytes = upstream_bytes + sent_bytes + shield_bytes
```
Where:

- ```upstream_bytes``` are equal to the ```$upstream_response_length``` log field and refer to the response length from an origin in bytes
- ```sent_bytes``` are equal to the ```$bytes_sent``` log field and refer to the number of bytes sent to a user from the edge (cache) servers
- ```shield_bytes``` are equal to the ```$bytes_sent``` log field and refer to the number of bytes sent to a user from the pre-cache server

**Note**: The final value of log data may differ slightly from the billing statistics, as there may be cases where not all logs are received, such as:

- You are using the "Origin Shielding" feature but did not check the "Add logs from origin shielding" box
- You have a rate limit set on your storage side, and when CDN started generating logs, some logs were not downloaded because of the rate limitation

## Export logs to an S3 storage

### Amazon storage

1\. Leave the box "Do not send empty logs" checked if you don't want to receive empty logs. If you want to receive empty logs, uncheck it.

2\. If you use our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">origin shielding</a> option, you can see a checkbox "Add logs from origin shielding". Check the box if you want to receive logs from both edge servers and pre-cache shielding servers.

3\. For storage type, select "Amazon".

4\. Specify your access key ID. In your Amazon personal account, it is called "AWS access Key ID". You can find it using the <a href="https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html" target="_blank">instruction</a>. An access key ID and secret access key are required to configure log export to your storage.

5\. Specify your secret access key. In your Amazon personal account, it is called "AWS secret access Key". You can find it using the <a href="https://docs.aws.amazon.com/powershell/latest/userguide/pstools-appendix-sign-up.html" target="_blank">instruction</a>.

6\. Specify your AWS region — the location of a server where your storage is hosted. This is optional: for most storages, the region is determined automatically. You can leave the field empty. But we recommend filling it out to ensure that your logs are exported successfully.

7\. Choose how to organize storage: put logs of all CDN resources into one bucket or use separate buckets for each CDN resource.

8\. Specify bucket(s) for log export. Make sure you indicate an existing bucket. Otherwise, your logs cannot be exported. Specify a folder name if you want to export logs to a specific folder within a bucket.

9\. Click **Save changes**.

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/12745153936913.png" alt="Raw logs" width="80%">

### Non-Amazon storage

1\. Leave the box "Do not send empty logs" checked if you don't want to receive empty logs. If you want to receive empty logs, uncheck it.

2\. If you use our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">origin shielding</a> option, you can see a checkbox "Add logs from origin shielding". Check the box if you want to receive logs from both edge servers and pre-cache shielding servers.

3\. For storage type, select "Other".

4\. Specify a hostname — a name that is assigned to a storage server within a network and is used instead of an IP address. If you use <a href="https://gcore.com/storage" target="_blank">Gcore S3 storage</a>, you can find its access key ID in your personal account in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">Hostname</a>" field.

5\. Specify your access key ID. Along with a secret access key, it is required to configure log export to your storage. If you use <a href="https://gcore.com/storage" target="_blank">Gcore S3 storage</a>, you can find its access key ID in your personal account in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">Access key</a>" field.

6\. Specify your secret access key. If you use <a href="https://gcore.com/storage" target="_blank">Gcore S3 storage</a>, you can find its secret access key in your personal account in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">Secret key</a>" field.

7\. Specify a bucket hostname — a bucket ID that is used by your S3 storage system in the ```{bucket_name}.{hostname}``` format. It is required to ensure that logs are exported to a correct bucket within a storage. A bucket hostname of the Gcore storage looks as follows: ```{bucket name}.{hostname from step 3}```. For example: ```examplename.s-ed1.cloud.gcore.lu```. 

8\. Specify a region — location ID of a server where your storage is hosted. This is optional: for some storages, the region is determined automatically. You can leave the field empty. If you use <a href="https://gcore.com/storage" target="_blank">Gcore S3 storage</a>, a location ID is required. You can find it in the "Details" of the storage. Your location ID is a part of your hostname to the first dot.

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/image_1377.png" alt="Specify a region " width="50%">  

9\. Choose how to organize storage: put logs of all CDN resources into one bucket or to use separate buckets for each CDN resource.

10\. Specify bucket(s) for log export. Make sure you indicate an existing bucket. Otherwise, your logs cannot be exported. If you want to export logs to a specific folder within a bucket, specify a folder name.

11\. Click **Save changes**.

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/export-logs-to-s3-storage.png" alt="Specify a region " width="80%">

## Export logs to an FTP/SFTP storage

1\. Leave the box "Do not send empty logs" checked if you don't want to receive empty logs. If you want to receive empty logs, uncheck it.

2\. If you use our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">origin shielding</a> option, you can see a checkbox "Add logs from origin shielding". Check the box if you want to receive logs from both edge servers and pre-cache shielding servers.

3\. Specify a hostname — a name that is assigned to a storage server within a network and is used instead of an IP address. If you use <a href="https://gcore.com/storage" target="_blank">Gcore SFTP storage</a>, you can find its hostname in the "Details" of the storage in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#sftp" target="_blank">Hostname</a>" field. It looks as follows: ```ams.origin.gcdn.co```. Additionally, you can specify an FTP or SFTP storage port by adding a colon after the hostname. For example: ```ams.origin.gcore.co:2200```.

4\. Specify a storage username. If you use <a href="https://gcore.com/storage" target="_blank">Gcore SFTP storage</a>, you can find its username in the "Details" of your storage in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#sftp" target="_blank">Storage/User name</a>" field.

5\. Enter your storage password.

6\. Specify a folder for export. If you use <a href="https://gcore.com/storage" target="_blank">Gcore SFTP storage</a>, specify the root (home) folder where other folders originate from. You can find its name in the "Details" of your SFTP storage at the end of the "Upload path" field.

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/image_1379.png" alt="Raw logs" width="50%">

If you use an SFTP storage from another provider, clarify whether a root folder that includes other folders is created by default. If not, leave the field empty. If yes, specify a folder name.

7\. Choose how to organize storage: put logs of all CDN resources into one folder or to use separate folders for each CDN resource. Then specify a folder name. If you specify a non-existent folder, logs will be exported to a root folder.

8\. Click **Save changes**.


<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/12745350391697.png" alt="Specify a folder for export" width="80%">

## Export time intervals


Logs are exported at the end of each hour. If you activate Raw Logs at 00:30, the first logs will be exported between 00:45 and 01:00, and the next ones — between 01:45 and 02:00.

If CDN servers are not requested and the box "Do not send empty logs" is unchecked, an empty log file (± 20 bytes) will be sent to your storage.

You can see the status of the Raw Logs option in your control panel:

- "Pending" is a status for the time interval between the connection to a storage and the very first log export
- "OK" is a status showing that logs are exported from at least one CDN server
- "Failed" is a status indicating that an error occurred while connecting to a storage or that the service failed to export logs within 24 hours
- "Pause" is a status showing that the option is paused

<img src="https://assets.gcore.pro/docs/cdn/logs/raw-logs-export-cdn-resource-logs-to-your-storage/image_1381.png" alt="Raw logs" width="50%">

## Log path example

```
s3://log-bucket-name/2019/08/20/15/nodename_primarycname.domain.ru_access.log.gz
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

Please don’t be surprised if you see a field that is not listed above. We occasionally add new fields. If some fields are added to logs, you will receive an email about it. New fields are added to the end of the line.

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

## Log fields

Not all fields are important. Some of them relate to our internal CDN system and are not meaningful for you. In the table below, we have highlighted such system fields in italics. Other fields can be helpful for traffic analysis or statistics.

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
    <td>Status of a requested file in CDN cache:<br>- HIT is a status of a response served from CDN cache.<br>- STALE is a status of an outdated response that failed to update because an origin was not responding or responding incorrectly.<br>- UPDATING is a status of an outdated response that is still updating since a previous request.<br>- REVALIDATED is a status of a response that is identical to the one on an origin based on the proxy_cache_revalidate directive.<br>- EXPIRED is a status of a response that has expired in cache, but still matches the one on an origin. A request has been sent to an origin for re-caching.<br>- MISS is a status of a response that has been served directly from an origin, rather than from cache.<br>- BYPASS is a status of a response for the first file request after clearing the cache.<br>Note: this status appears when the file is requested by each CDN server.<br>When one CDN server requests a file for the first time, it will have the BYPASS status.<br>When the same server requests the file again, the status will be changed to HIT.<br>When another CDN server requests the file, it will again have the BYPASS status.<br></td>
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
    <td>Unique request identifier generated from 16 random bytes, in hexadecimal form</td>
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
    <td>Size of the TCP Congestion window, i.e. the maximum number of TCP segments that the connection can send before an acknowledgement is required.</td>
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
