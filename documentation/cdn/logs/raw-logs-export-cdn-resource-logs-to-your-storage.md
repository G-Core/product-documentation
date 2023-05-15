---
title: raw-logs-export-cdn-resource-logs-to-your-storage
displayName: Raw Logs (paid)
published: true
order: 10
toc:
   --1--What is a Raw Logs feature?: "what-is-a-raw-logs-feature"
   --1--Export to an S3 storage: "export-logs-to-an-s3-storage"
   --2--Amazon storage: "amazon-storage"
   --2--Non-Amazon storage: "non-amazon-storage"
   --1--Export to an FTP/SFTP storage: "export-logs-to-an-ftp-sftp-storage"
   --1--Export time intervals: "export-time-intervals"
   --1--Log path example: "log-path-example"
   --1--Log format: "log-format"
   --1--Log example: "log-example"
   --1--Log fields: "log-fields"
---
# Raw Logs: export CDN resource logs to your storage

## What is a Raw Logs feature?

Raw Logs is an option that enables an automatic export of CDN resource logs to your storage. Logs contain information about user requests sent to cache servers and pre-cache servers (if <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">origin shielding</a> is enabled).

**Note**: The feature is paid. To activate, contact us via [support@gcore.com](mailto:support@gcore.com). After activation, enable "Raw Logs" in your control panel and configure export to S3, FTP, or SFTP storage.

<img src="https://support.gcore.com/hc/article_attachments/13202181890193" alt="">

## Export logs to an S3 storage
----------------------------

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

<img src="https://support.gcore.com/hc/article_attachments/12745153936913" alt="" width="70%">

### Non-Amazon storage

1\. Leave the box "Do not send empty logs" checked if you don't want to receive empty logs. If you want to receive empty logs, uncheck it.

2\. If you use our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">origin shielding</a> option, you can see a checkbox "Add logs from origin shielding". Check the box if you want to receive logs from both edge servers and pre-cache shielding servers.

3\. For storage type, select "Other".

4\. Specify a hostname — a name that is assigned to a storage server within a network and is used instead of an IP address. If you use <a href="https://gcore.com/storage" target="_blank">Gcore S3 storage</a>, you can find its access key ID in your personal account in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">Hostname</a>" field.

5\. Specify your access key ID. Along with a secret access key, it is required to configure log export to your storage. If you use <a href="https://gcore.com/storage" target="_blank">Gcore S3 storage</a>, you can find its access key ID in your personal account in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">Access key</a>" field.

6\. Specify your secret access key. If you use <a href="https://gcore.com/storage" target="_blank">Gcore S3 storage</a>, you can find its secret access key in your personal account in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#s3" target="_blank">Secret key</a>" field.

7\. Specify a bucket hostname — a bucket ID that is used by your S3 storage system in the ```{bucket_name}.{hostname}``` format. It is required to ensure that logs are exported to a correct bucket within a storage. This field is optional: for some storages, a bucket hostname is determined automatically. If you use Gcore or Yandex.Cloud storage, a bucket hostname is required. A bucket hostname of the Gcore storage looks as follows: ```{bucket name}.{hostname from step 3}```. For example: ```examplename.s-ed1.cloud.gcore.lu```. A bucket hostname of Yandex.Cloud storage looks as follows: ```{bucket name}.{Yandex.Cloud hostname}```. For example: ```examplename.storage.yandexcloud.net```.

8\. Specify a region — location ID of a server where your storage is hosted. This is optional: for some storages, the region is determined automatically. You can leave the field empty. If you use <a href="https://gcore.com/storage" target="_blank">Gcore S3 storage</a>, a location ID is required. You can find it in the "Details" of the storage. Your location ID is a part of your hostname to the first dot.

<img src="https://support.gcore.com/hc/article_attachments/5620116388497/image_1377.png" alt="" width="50%">  

9\. Choose how to organize storage: put logs of all CDN resources into one bucket or to use separate buckets for each CDN resource.

10\. Specify bucket(s) for log export. Make sure you indicate an existing bucket. Otherwise, your logs cannot be exported. If you want to export logs to a specific folder within a bucket, specify a folder name.

11\. Click **Save changes**.

<img src="https://support.gcore.com/hc/article_attachments/12745252125201" alt="" width="70%">

## Export logs to an FTP/SFTP storage

1\. Leave the box "Do not send empty logs" checked if you don't want to receive empty logs. If you want to receive empty logs, uncheck it.

2\. If you use our <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">origin shielding</a> option, you can see a checkbox "Add logs from origin shielding". Check the box if you want to receive logs from both edge servers and pre-cache shielding servers.

3\. Specify a hostname — a name that is assigned to a storage server within a network and is used instead of an IP address. If you use <a href="https://gcore.com/storage" target="_blank">Gcore SFTP storage</a>, you can find its hostname in the "Details" of the storage in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#sftp" target="_blank">Hostname</a>" field. It looks as follows: ```ams.origin.gcdn.co```. Additionally, you can specify an FTP or SFTP storage port by adding a colon after the hostname. For example: ```ams.origin.gcore.co:2200```.

4\. Specify a storage username. If you use <a href="https://gcore.com/storage" target="_blank">Gcore SFTP storage</a>, you can find its username in the "Details" of your storage in the "<a href="https://gcore.com/docs/storage/create-an-s3-or-sftp-storage#sftp" target="_blank">Storage/User name</a>" field.

5\. Enter your storage password.

6\. Specify a folder for export. If you use <a href="https://gcore.com/storage" target="_blank">Gcore SFTP storage</a>, specify the root (home) folder where other folders originate from. You can find its name in the "Details" of your SFTP storage at the end of the "Upload path" field.

<img src="https://support.gcore.com/hc/article_attachments/5620132659217/image_1379.png" alt="" width="50%">

If you use an SFTP storage from another provider, clarify whether a root folder that includes other folders is created by default. If not, leave the field empty. If yes, specify a folder name.

7\. Choose how to organize storage: put logs of all CDN resources into one folder or to use separate folders for each CDN resource. Then specify a folder name. If you specify a non-existent folder, logs will be exported to a root folder.

8\. Click **Save changes**.


<img src="https://support.gcore.com/hc/article_attachments/12745350391697" alt="" width="70%">

## Export time intervals


Logs are exported at the end of each hour. If you activate Raw Logs at 00:30, the first logs will be exported between 00:45 and 01:00, and the next ones — between 01:45 and 02:00.

If CDN servers are not requested and the box "Do not send empty logs" is unchecked, an empty log file (± 20 bytes) will be sent to your storage.

You can see the status of the Raw Logs option in your control panel:

- "Pending" is a status for the time interval between the connection to a storage and the very first log export
- "OK" is a status showing that logs are exported from at least one CDN server
- "Failed" is a status indicating that an error occurred while connecting to a storage or that the service failed to export logs within 24 hours
- "Pause" is a status showing that the option is paused

<img src="https://support.gcore.com/hc/article_attachments/5620114453777/image_1381.png" alt="" width="50%">

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
"$request_id" "$http_x_forwarded_proto" "$http_x_forwarded_request_id" "$ssl_cipher"  
"$ssl_session_id" "$ssl_session_reused"  
"$sent_http_content_type" "$tcpinfo_rtt" 
```

Please don’t be surprised if you see a field that is not listed above. We occasionally add new fields. If some fields are added to logs, you will receive an email about it. New fields are added to the end of the line.

## Log example

```
"0.0.0.0" "-" "-" "[26/Apr/2019:09:47:40 +0000]" "GET /ContentCommon/images/image.png HTTP/1.1"  
"200" "1514283" "https://example.com/videos/10" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1)  
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 YaBrowser/16.10.0.2309 Safari/537.36"  
"1514848" "[dh-up-gc18]" "https" "origin.cdn.com" "1.500" "0.445" "157" "bytes=0-1901653" "[dh]"  
"MISS" "10485760" "0.0.0.0:80" "2510" "7399" "-" "-" "KZ" "-" "shield_no" "0.0.0.0" "80" "206" "-" "0.000"  
"0.200" "0.0.0.0" "asnumber" "106980391" "1" "c1c0f12ab35b7cccccd5dc0a454879c5" "-" "-"  
"ECDHE-RSA-AES256-GCM-SHA384" "28a4184139cb43cdc79006cf2d1a4ac93bdc****" "r"  
"application/json" "21"
```

Log fields
----------

Not all fields are important. Some of them relate to our internal CDN system and are not meaningful for you. In the table below, we have highlighted such system fields in italics. Other fields can be helpful for traffic analysis or statistics.

<table class="tg">
<thead>
  <tr>
    <th class="tg-fr2s">Field</th>
    <th class="tg-fr2s">Log value example</th>
    <th class="tg-j0cj">Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-fr2s">$remote_addr</td>
    <td class="tg-1onv">0.0.0.0</td>
    <td class="tg-7zkw">User's IP address</td>
  </tr>
  <tr>
    <td class="tg-4jnw">$remote_user<br>(internal system variable)</td>
    <td class="tg-4jnw">-</td>
    <td class="tg-4oen">Username used in Basic authentication </td>
  </tr>
  <tr>
    <td class="tg-1onv">[$time_local]</td>
    <td class="tg-1onv">[26/Apr/2019<br>:09:47:40 +0000]</td>
    <td class="tg-7zkw">Local time in Common Log Format</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$request</td>
    <td class="tg-7zkw">GET /ContentCommon/<br>images/image.png<br>HTTP/1.1</td>
    <td class="tg-7zkw">HTTP method, requested file path, HTTP version</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$status</td>
    <td class="tg-7zkw">200</td>
    <td class="tg-7zkw">Response status code from a CDN server</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$body_bytes_sent</td>
    <td class="tg-7zkw">1514283</td>
    <td class="tg-7zkw">Number of bytes sent to a user, excluding the response header size</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$http_referer</td>
    <td class="tg-7zkw">https://example.com<br>/videos/10</td>
    <td class="tg-7zkw">Referrer - a URL requested by a user</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$http_user_agent</td>
    <td class="tg-7zkw">Mozilla/5.0<br>(Macintosh; Intel<br>Mac OS X 10_12_1)<br>AppleWebKit/537.36<br>(KHTML, like Gecko)<br>Chrome/53.0.2785.116<br>YaBrowser/16.10.0.2309<br>Safari/537.36</td>
    <td class="tg-7zkw">User agent that was used to send a request (browser or other application)</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$bytes_sent</td>
    <td class="tg-7zkw">1514848</td>
    <td class="tg-7zkw">Number of bytes sent to a user</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$edgename</td>
    <td class="tg-7zkw">[dh-up-gc18]</td>
    <td class="tg-7zkw">CDN server that forwarded a requested file</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$scheme</td>
    <td class="tg-7zkw">https</td>
    <td class="tg-7zkw">Protocol (HTTP or HTTPS) of a request</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$host</td>
    <td class="tg-7zkw">cdn.example.com</td>
    <td class="tg-7zkw">Requested hostname of a CDN resource</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$request_time</td>
    <td class="tg-7zkw">1.500</td>
    <td class="tg-7zkw">Request processing time in seconds (accurate to milliseconds); time elapsed between the first bytes of a request were processed and logging after the last bytes were sent to a user</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$upstream_response_time</td>
    <td class="tg-7zkw">0.445</td>
    <td class="tg-7zkw">Number of seconds (accurate to milliseconds) it took to receive a response from an origin. In case of multiple responses, commas and colons are used </td>
  </tr>
  <tr>
    <td class="tg-7zkw">$request_length</td>
    <td class="tg-7zkw">157</td>
    <td class="tg-7zkw">Request length (including request line, header, and request body)</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$http_range</td>
    <td class="tg-7zkw">bytes=0-1901653</td>
    <td class="tg-7zkw">File fragment size in a Range request</td>
  </tr>
  <tr>
    <td class="tg-7zkw">[$responding_node]</td>
    <td class="tg-7zkw">dh</td>
    <td class="tg-7zkw">Responding data center</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$upstream_cache_status</td>
    <td class="tg-7zkw">MISS</td>
    <td class="tg-7zkw">Status of a requested file in CDN cache:<br>- HIT is a status of a response served from CDN cache.<br>- STALE is a status of an outdated response that failed to update because an origin was not responding or responding incorrectly.<br>- UPDATING is a status of an outdated response that is still updating since a previous request.<br>- REVALIDATED is a status of a response that is identical to the one on an origin based on the proxy_cache_revalidate directive.<br>- EXPIRED is a status of a response that has expired in cache, but still matches the one on an origin. A request has been sent to an origin for re-caching.<br>- MISS is a status of a response that has been served directly from an origin, rather than from cache.<br>- BYPASS is a status of a response for the first file request after clearing the cache.<br>Note: this status appears when the file is requested by each CDN server.<br>When one CDN server requests a file for the first time, it will have the BYPASS status.<br>When the same server requests the file again, the status will be changed to HIT.<br>When another CDN server requests the file, it will again have the BYPASS status.<br></td>
  </tr>
  <tr>
    <td class="tg-7zkw">$upstream_response_length</td>
    <td class="tg-7zkw"> 10485760</td>
    <td class="tg-7zkw">Response length from an origin in bytes. In case of multiple responses, commas and colons are used</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$upstream_addr</td>
    <td class="tg-7zkw">0.0.0.0:80</td>
    <td class="tg-7zkw">Origin's IP address and port</td>
  </tr>
  <tr>
    <td class="tg-4oen">$gcdn_api_client_id<br>(internal system variable)</td>
    <td class="tg-4oen">123</td>
    <td class="tg-4oen">Your ID in our system</td>
  </tr>
  <tr>
    <td class="tg-4oen">$gcdn_api_resource_id<br>(internal system variable)</td>
    <td class="tg-4oen">01</td>
    <td class="tg-4oen">Your CDN-resource ID in our system</td>
  </tr>
  <tr>
    <td class="tg-4oen">$uid_got<br>(internal system variable)</td>
    <td class="tg-4oen">-</td>
    <td class="tg-4oen">Cookie name and received user ID</td>
  </tr>
  <tr>
    <td class="tg-4oen">$uid_set<br>(internal system variable)</td>
    <td class="tg-4oen">-</td>
    <td class="tg-4oen">Cookie name and provided user ID</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$geoip_country_code</td>
    <td class="tg-7zkw">KZ</td>
    <td class="tg-7zkw">User’s country code according to the <a href="https://www.iso.org/obp/ui/#search/code/"><span style="text-decoration:underline;color:#FF5700">ISO 3166 standard</span></a> (Alpha-2 code).</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$geoip_city</td>
    <td class="tg-7zkw">-</td>
    <td class="tg-7zkw">User’s city code</td>
  </tr>
  <tr>
    <td class="tg-4oen">$shield_type<br>(internal system variable)</td>
    <td class="tg-4oen">shield_no</td>
    <td class="tg-4oen">This field shows whether the <a href="https://gcorelabs.com/support/articles/214080309/"><span style="text-decoration:underline;color:#FF5700">shielding option</span></a> is enabled:<br>shield_old - enabled<br>shield_no - disabled</td>
  </tr>
  <tr>
    <td class="tg-4oen">$server_addr<br>(internal system variable)</td>
    <td class="tg-4oen">0.0.0.0</td>
    <td class="tg-4oen">IP address of an Anycast zone or CDN server</td>
  </tr>
  <tr>
    <td class="tg-4oen">$server_port<br>(internal system variable)</td>
    <td class="tg-4oen">80</td>
    <td class="tg-4oen">Requested port</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$upstream_status</td>
    <td class="tg-7zkw">206</td>
    <td class="tg-7zkw">Origin response code</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$upstream_connect_time</td>
    <td class="tg-7zkw">0.000</td>
    <td class="tg-7zkw">Number of seconds (accurate to milliseconds) it took to access an origin server</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$upstream_header_time</td>
    <td class="tg-7zkw">0.200</td>
    <td class="tg-7zkw">Number of seconds (accurate to milliseconds) it took to receive a response header from an origin server</td>
  </tr>
  <tr>
    <td class="tg-4oen">$shard_addr<br>(internal system variable)</td>
    <td class="tg-4oen">0.0.0.0</td>
    <td class="tg-4oen">IP address of a CDN server that was first to accept a request if the Cache Sharding feature is enabled</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$geoip2_data_asnumber</td>
    <td class="tg-7zkw">asnumber</td>
    <td class="tg-7zkw">Number of an autonomous system that sent a request</td>
  </tr>
  <tr>
    <td class="tg-4oen">$connection<br>(internal system variable)</td>
    <td class="tg-4oen">2897494295</td>
    <td class="tg-4oen">Connection serial number</td>
  </tr>
  <tr>
    <td class="tg-4oen">$connection_requests<br>(internal system variable)</td>
    <td class="tg-4oen">1</td>
    <td class="tg-4oen">Current number of requests made through a connection</td>
  </tr>
  <tr>
    <td class="tg-4oen">$request_id<br>(internal system variable)</td>
    <td class="tg-4oen">c1c0f12ab35b7<br>cccccd5dc0a<br>454879c5</td>
    <td class="tg-4oen">Unique request identifier generated from 16 random bytes, in hexadecimal form</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$http_x_forwarded_proto</td>
    <td class="tg-7zkw">-</td>
    <td class="tg-7zkw">Initial protocol of an incoming request (HTTP or HTTPS)</td>
  </tr>
  <tr>
    <td class="tg-4oen">$http_x_forwarded_request_id<br>(internal system variable)</td>
    <td class="tg-4oen">-</td>
    <td class="tg-4oen">Initial ID of an incoming request</td>
  </tr>
  <tr>
    <td class="tg-4oen">$ssl_cipher<br>(internal system variable)</td>
    <td class="tg-4oen">ECDHE-RSA-AES256<br>-GCM-SHA384</td>
    <td class="tg-4oen">Cipher name used for an established SSL connection</td>
  </tr>
  <tr>
    <td class="tg-4oen">$ssl_session_id<br>(internal system variable)</td>
    <td class="tg-4oen">28a4184139cb43<br>cdc79006cf2d1<br>a4ac93bdc****</td>
    <td class="tg-4oen">Session ID of an established SSL connection</td>
  </tr>
  <tr>
    <td class="tg-4oen">$ssl_session_reused<br>(internal system variable)</td>
    <td class="tg-4oen"> r</td>
    <td class="tg-4oen">The filed shows whether a session was reused (“r” ) or not (“.”)</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$sent_http_content_type</td>
    <td class="tg-7zkw">application/json</td>
    <td class="tg-7zkw">Value of the Content-Type HTTP header, indicating the MIME type of a transmitted file</td>
  </tr>
  <tr>
    <td class="tg-7zkw">$tcpinfo_rtt</td>
    <td class="tg-7zkw">  21</td>
    <td class="tg-7zkw">Average time (latency) it takes to transfer a packet to/from a server. The unit of time is microseconds.</td>
  </tr>
</tbody>
</table>
