---
title: cache-percentage-is-low-how-to-solve-the-issue
displayName: Low cache hit ratio
published: true
order: 20
toc:
   --1--Cache hit ratio: "what-is-the-cache-hit-ratio"
   --1--Issues: "issues-with-the-low-cache-hit-ratio"
   --1--Check: "check-if-slow-content-delivery-is-related-to-low-cache-hit-ratio"
   --1--Causes and solutions: "causes-and-solutions-for-low-cache-hit-ratio"
pageTitle: Boost CDN Cache Hit Ratio | Gcore
pageDescription: Learn how to improve your CDN Cache Hit Ratio. Get tips on CDN integration, cache settings, and leverage Large Files Delivery Optimization.
---
# Cache hit ratio is low: How to solve the issue

## What is the cache hit ratio?

The cache hit ratio is the percentage of traffic delivered from the CDN edge cache without requesting the origin server. You can check it in the <a href="https://cdn.gcore.com/reports/statistics" target="_blank">Statistics</a> section within the control panel.  

<img src="https://assets.gcore.pro/docs/cdn/troubleshooting/cache-percentage-is-low-how-to-solve-the-issue/statistics-low-cache-hit-ratio.png" alt="" width="80%">

A high cache hit ratio shows the efficiency and practicality of using CDNs. The higher it is, the better. By reducing the number of times CDN edge servers request a file from the source, you improve performance, reduce the load on the source, and reduce outbound traffic costs.

## Issues with the low cache hit ratio

A low cache hit ratio is a sign of something going awry, and shows that many requests are proxied to the origin instead of files being delivered from the cache. 

A low cache hit ratio can be accompanied by low content delivery speed Compare the request scheme for cached file ```User → CDN edge → User``` with uncached—```User → CDN edge → Origin → CDNedge → User```. In the second case, more requests go to the origin, which causes longer response time simply due to a higher distance and more hops in the sequence.

## Check if slow content delivery is related to low cache hit ratio

1\. Check Statistics for “Cache hit ratio.” If it is low (less than 80% in most cases), also check “Traffic” and “Requests” to avoid misconceptions in determining the cause. You can learn more about where and how to view reports in the guide about <a href="https://gcore.com/docs/cdn/view-statistics-of-a-cdn-resource#statistics" target="_blank">viewing statistics of CDN resources</a>.

**Note**: 80% is an approximate number, used for descriptive purposes, the accurate number highly depends on the use-case.

2\. Check the response headers using the ```curl -I``` command; for instance:

```
curl -I cdn.example.com/assets/sample-image.png
```

**Note**: Request content from one specific CDN edge server. 

<expandable-element title="How to request content from the same server">
**Note**: Requesting content from the same server several times is very important. Normally, your request will hit multiple servers in your location, returning an unrepresentative result because one server may have cached the file and another may not. 

To request the file from the same server:

1\. Request the file that appears not to be distributed from the CDN, and check the **“X-id”** header. This header shows the server that received the request. Copy that value.

2\. Run the following command to get its IP:

```
nslookup/dig {x-id server}.fe.gc.onl
```
3\. Request the file from the IP address which you got in step 2: 

```
curl -Ik -H "Host: {cdn.domain}" "http{s}://{ip-address}/file"
```

Compare the file headers with the values listed in the table below.

</expandable-element>

The response will contain different headers. You should focus on the inappropriate values of caching headers “Cache-control” and “Cache”:

<table>
<thead>
<tr>
<td><b>Value</b></td>
<td><b>Meaning</b></td>
</tr>
</thead>
<tbody>
<tr>
<td>Cache-Control: <i>max-age=0</i></td>
<td rowspan="3" style="text-align: left">This value prohibits content caching.<br> It may cause an issue with the Cache hit ratio<br> and reduce performance.<br> However, in some cases, this value is ok.</td>
</tr>
<tr>
<td>Cache-Control: <i>no-cache</i></td>
</tr>
<tr>
<td>Cache-Control: <i>no-store</i></td>
</tr>
<tr>
<td>Cache-Control: <i>private</i></td>
<td style="text-align: left">This value caches content only in users’ browsers,<br> not the edge servers’ cache.
<br><br>
<b>Note</b>: If the request contains custom headers<br> starting with X (e.g., “X-custom-header”),<br> the CDN will treat the request as a new request<br> and forward it to the origin (as with cookies.)</td>
</tr>
<tr>
<td>Cache: <i>MISS</i></td>
<td style="text-align: left">This value specifies that the response is received<br> from the origin, bypassing the cache.<br> Our CDN caches files on the first request.<br> This means that the first request for a file<br> will result in MISS (CDN had to reach the origin<br> to pull the resource and cache it locally)<br> and every following request for the same file will result in HIT(served from a local CDN cache.)</td>
</tr>
</tbody>
</table>

3\. Check the <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin" target="_blank">CDN resource caching settings</a>. The feature must be enabled and configured to support CDN caching. 

4\. Check <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers" target="_blank">Ignore Query String and Ignore Set-Cookie options</a>. If it’s disabled, content with different query strings and Set-Cookie headers caches separately.

**Note**: If content delivery speed is not related to low cache hit ratio, check <a href="https://gcore.com/docs/cdn/troubleshooting/content-delivery-speed-is-low-how-to-solve-the-issue" target="_blank">our guide</a> to help with other causes.

## Causes and solutions for low cache hit ratio

<table>
<thead>
<tr>
<td><b>Cause</b></td>
<td><b>Solution</b></td>
</tr>
</thead>
<tbody>
<tr>
<td>Traffic started less than two days ago, and more cache needs to be collected.</td>
<td style="text-align: left">Traffic patterns and amounts dictate how long you should wait to populate the cache.<br> Usually, waiting for around 48 hours after the CDN integration is enough to cache most resources, but the exact time is individual.<br> You can also deliver more content through CDN.</td>
</tr>
<tr>
<td>Content is not requested enough, and the cache per server is low.</td>
<td style="text-align: left">Increase the traffic to your content or use the paid <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin shielding</a> option to accumulate requests.</td>
</tr>
<tr>
<td>A “Cache-Control” value prohibits the CDN from caching content.</td>
<td style="text-align: left">Ensure that the <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/specify-cache-lifetime-on-a-cdn-resource-or-origin" target="_blank">CDN Caching</a> option is enabled and configured in the following way.
<ul>
<li>For CDN controlled: <b>Don’t</b> set 0 in the “Cache expiry” field.</li>
<li>For Origin controlled: <b>Don’t</b> set values from the step above (<i>max-age=0, no-cache, no-store, private</i>.)</li>
</ul>
</td>
</tr>
<tr>
<td>Responses contain query strings or a Set-Cookie header, so the files are cached as different.</td>
<td style="text-align: left">Enable <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers" target="_blank">Ignore Query String and Ignore Set Cookie options</a>. Then, a single file will be delivered from the cache, regardless of the request parameters and the Set Cookie header.</td>
</tr>
<tr>
<td>The Vary header is set on origins so that content is cached suboptimally.</td>
<td style="text-align: left">Change the Vary header settings on your origin or use the <a href="https://gcore.com/docs/cdn/cdn-resource-options/http-headers/add-or-hide-response-headers#hide-response-headers" target="_blank">Hide response headers</a> feature in the customer portal.<br>Set “Hide only,” select the Vary header and other that are necessary and save changes.
<br><img src="https://assets.gcore.pro/docs/cdn/troubleshooting/cache-percentage-is-low-how-to-solve-the-issue/low-cache-hit-ratio-20.png" alt="How to hide the Vary header" width="50%">
</td>
</tr>
</tbody>
</table>