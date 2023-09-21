---
title: gcore-error-status-codes
displayName: Error status codes
published: true
order: 5
toc:
   --1--Check codes: "how-to-check-status-codes"
   --1--Errors: "error-status-codes"
   --2--403 errors: "403-errors"
   --2--404 errors: "404-errors"
   --2--Other errors (402, 458, 504, 508, 556, 557): "other-errors-402-458-504-508-556-557"
pageTitle: Explore Gcore Error Status Codes | Gcore
pageDescription: A comprehensive guide on how to troubleshoot special errors with the codes 402, 403, 404, 458, 504, 508, 556, 557.
---
# Resolve errors by status code for Gcore CDN

This article reviews errors caused by misconfigurations in Gcore services or option settings, their corresponding status codes, and solutions for each case.

## How to check status codes

Use the <a href="https://cdn.gcore.com/logs/log-viewer" target="_blankk">Log viewer</a> to check the delivery status codes of your content. Refer to the <a href="https://gcore.com/docs/cdn/logs/log-viewer-view-and-download-cdn-resource-logs" target="_blank">article about our Log viewer</a> for the information on configuring time and filters.

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/gcore-error-status-codes/error-codes.png" alt="How to check status codes" width="">

## Error status codes

Status codes 403 and 404 have multiple meanings. Explanations of each scenario that can lead to these status codes are presented in the table.

### 403 errors

<table>
<thead>
<tr>
<td><b>Cause</b></td>
<td><b>Details</b></td>
<td><b>Solution</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">The CDN resource is currently disabled.</td>
<td style="text-align: left">CDN resources have two states: “Enabled” and “Disabled.” <br>Disabled resources are inactive from your end and will not function.</td>
<td style="text-align: left">Navigate to the CDN resource settings and <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/suspend-a-cdn-resource-automatically-or-manually" target="_blank">turn on the resource</a>.</td>
</tr>
<tr>
<td style="text-align: left">The current resource security settings limit access for a user.</td>
<td style="text-align: left">You may have restricted access to content delivered via CDN to some users.</td>
<td style="text-align: left">Determine which parameter (Referrer, Country, IP, User agent) is causing the user receiving error 403 to be blocked, and disable it according to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/control-access-to-the-content-with-country-referrer-ip-and-user-agents-policies" target="_blank">guide</a>.<br><br><b>Example</b>: If you set the Country restriction to Angola and the user with error 403 is located there, you should remove this setting.</td>
</tr>
</tbody>
</table>

### 404 errors

<table>
<thead>
<tr>
<td><b>Cause</b></td>
<td><b>Details</b></td>
<td><b>Solution</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">You provided a link to a missing file on the origin.</td>
<td style="text-align: left">In your web page’s HTML file, you provide links to a content item on your origin via the CDN.<br> The link causing this error leads to a content item that does not exist on the origin. 
<br><br>
<b>Example</b>: If the link is <i>website.example.cdn/files/image.png</i>, then the file <i>image.png</i> is not found in the files directory.</td>
<td style="text-align: left">You need to place the content item on your origin.<br> The name and path to the item must match the link in your webpage HTML file.<br> If necessary, you can edit the link in the HTML file to specify a different content item name or path.<br><br>Alternatively, if you don’t want to deliver this content item via the CDN, remove the link to this content from the HTML file of the webpage.</td>
</tr>
<tr>
<td style="text-align: left">WebP compression and WebSockets options conflict.</td>
<td style="text-align: left">Due to internal limitations, the <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif" target="_blank">WebP compression</a> and <a href="https://gcore.com/docs/cdn/cdn-resource-options/websockets-allow-permanent-connections-with-the-origin" target="_blank">WebSockets</a> options cannot be enabled simultaneously.</td>
<td style="text-align: left">Disable one of the options.</td>
</tr>
<tr>
<td style="text-align: left">The “Host header” is incorrect.</td>
<td style="text-align: left">The “Host header” option informs the CDN where to address to receive the content.<br><br><b>Example</b>: You specified <i>website.com</i> as the origin, but the content is hosted on another server <i>mycontent.com</i>.<br> By default, the CDN uses the origin domain name as the value for the “Host header” and will contact the <i>mycontent.com</i> server with an incorrect Host header, and this will cause an error. 
</td>
<td style="text-align: left">Use the <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header" target="_blank">Host header option</a> in the CDN settings to provide the accurate Host header.<br> You can verify the validity of the new Host header using <a href="https://gcore.com/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue#2-check-the-host-header-option" target="_blank">this instruction</a>.</td>
</tr>
<tr>
<td style="text-align: left">Access to an origin is restricted for the CDN.</td>
<td style="text-align: left">The CDN can’t reach the origin if the access is restricted, and can’t deliver content to users.
<br><br>
<b>Note</b>: This case may also result in the 504 status code.</td>
<td style="text-align: left">Whitelist the IP addresses of Gcore servers using this <a href="https://gcore.com/docs/cdn/getting-started/configure-an-origin/add-cdn-servers-to-the-origin-acl-whitelist" target="_blank">guide</a>.<br> If the IP addresses are already whitelisted, Gcore subnets may be excluded from the ACL.<br> In such a case, configure the ACL using an HTTP header instead of an IP list using the <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/specify-http-headers-that-cdn-adds-to-requests-to-the-origin" target="_blank">Request headers option</a> in the CDN resource settings.</td>
</tr>
</tbody>
</table>

### Other errors (402, 458, 504, 508, 556, 557)

<table>
<thead>
<tr>
<td><b>Status code</b></td>
<td><b>Cause</b></td>
<td><b>Details</b></td>
<td><b>Solution</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">402</td>
<td style="text-align: left">You are trying to deliver streaming content while the <a href="https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs#conditions-for-streams-and-videos-delivery-via-cdn" target="_blank">Streaming via CDN</a> feature is disabled.</td>
<td style="text-align: left">Streaming content (<i>.ts</i> and <i>.m3u8</i> files) can only be delivered via the CDN when the Streaming feature is enabled, which is available for paid tariffs.</td>
<td style="text-align: left">Enable <a href="https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs#conditions-for-streams-and-videos-delivery-via-cdn" target="_blank">Streaming via CDN</a>.</td>
</tr>
<tr>
<td style="text-align: left">458</td>
<td style="text-align: left">The maximum number of requests from the client's IP address has been exceeded.</td>
<td style="text-align: left">This restriction is set with the Rate Limiter option, designed to restrict a maximum number of requests from a single IP.</td>
<td style="text-align: left">Increase the permitted requests from a single IP within the <a href="https://gcore.com/docs/web-security/configure-rate-limiter-to-limit-the-number-of-requests#configure-rate-limiter" target="_blank">Rate Limiter settings</a>. 
<br><br>
<b>Note</b>: Rate limiter settings always apply to every user viewing your content.</td>
</tr>
<tr>
<td style="text-align: left">504</td>
<td style="text-align: left">Access to an origin is restricted for the CDN.</td>
<td style="text-align: left">The CDN can’t reach the origin if the access is restricted, and can’t deliver content to users.
<br><br>
<b>Note</b>: This case may also result in the 404 status code.</td>
<td style="text-align: left">Whitelist the IP addresses of Gcore servers using this <a href="https://gcore.com/docs/cdn/getting-started/configure-an-origin/add-cdn-servers-to-the-origin-acl-whitelist" target="_blank">guide</a>.<br> If the IP addresses are already whitelisted, Gcore subnets may be excluded from the ACL.<br> In such a case, configure the ACL using an HTTP header instead of an IP list using the <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/specify-http-headers-that-cdn-adds-to-requests-to-the-origin" target="_blank">Request headers option</a> in the CDN resource settings.</td>
</tr>
<tr>
<td style="text-align: left">508</td>
<td style="text-align: left">The domain of the CDN resource (CNAME) and the origin are messed up.</td>
<td style="text-align: left">Your origin and the domain name of your CDN resource lead to requests being directed back to each other, resulting in a loop. 
<br><br>
<b>Example</b>: You've set up a CNAME record using your origin domain name value instead of the custom value specified in your account and mentioned in the <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">setup instructions</a>.</td>
<td style="text-align: left"><a href="https://gcore.com/docs/cdn/troubleshooting/content-is-unavailable-after-a-cdn-resource-creation-how-to-solve-the-issue#1-check-the-configuration-of-the-personal-domain" target="_blank">Adjust the settings</a> by configuring the path to files on your origin to go through the CDN resource domain name. <br><br> Ensure that the CDN resource domain name is correctly directed to the subdomain displayed in your personal account within the DNS settings, as described in the <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">setup instructions</a>.</td>
</tr>
<tr>
<td style="text-align: left">556</td>
<td style="text-align: left">The number of connections to an origin has been exceeded.</td>
<td style="text-align: left">This occurs when requests to an origin time out, increasing the number of connections.</td>
<td style="text-align: left">Ensure that your origin’s response time is within 5 seconds.</td>
</tr>
<tr>
<td style="text-align: left">557</td>
<td style="text-align: left">The number of requests to the server has exceeded the limit of 5,000 requests per server.</td>
<td style="text-align: left">If you have only one server in a specific location and there has been a high volume of requests from that location, the server will reject some requests with a 557 response code.</td>
<td style="text-align: left"><a href="https://gcore.com/docs/cdn/add-an-origin-group" target="_blank">Add more origins</a> from the relevant location to the origins group.</td>
</tr>
</tbody>
</table>
