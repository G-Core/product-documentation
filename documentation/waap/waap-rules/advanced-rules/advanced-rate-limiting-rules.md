---
title: advanced-rate-limiting-rules
displayName: Advanced rate limiting rules
published: true
order: 20
toc:
   --1--Rate limiting method: "rate-limiting-method"
   --1--Implementation: "implementation-methods"
   --2--Advanced rules via API: "advanced-rules-via-api"
   --2--Best practices: "best-practices"
   --3--Block IPs that exceed request limit: "block-ips-that-exceed-request-limit-for-any-url"
   --3--Embed additional conditions: "embed-additional-conditions"
   --3--Rate limit complex URL regex: "rate-limit-complex-url-regex"
   --3--Embed IP range to the condition: "embed-ip-range-to-the-condition"
   --3--Cluster (PoP) granularity: "cluster-pop-granularity"
   --3--Rate limit by tag filter: "rate-limit-by-tag-filter"               
pageTitle: Learn about Gcore advanced rules | Gcore
pageDescription: Learn about Gcore advanced rules and how to use them for filtering incoming traffic and blocking malicious requests.
---
# Advanced rate limiting rules

The rate limiting feature allows you to limit the number of specific web requests to your domain within a particular period.  

We have a unique implementation of rate limiting: it’s set as a conditioning segment within a rule and can be embedded within any other condition segment. This is an advanced functionality that’s only available in the advanced rules. 

## Rate limiting method 

Use the `request.rate_limit()` method to implement rate limiting: 

```
request.rate_limit(
    ip = [<string>, ...],
    url = <string>,
    time = <int>,
    requests = <int>,
    method = [<string>, ...],
    status_code = [<int>, ...],
    content_type = <string>,
    scope = <string>
)
```

For <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules#tag-based-rules" target="_blank">tag-based</a> rate limiting rules, use `request.limit_rate` instead: 

```
request.limit_rate(
    ip = [<string>, ...],
    url = <string>,
    time = <int>,
    requests = <int>,
    method = [<string>, ...],
    status_code = [<int>, ...],
    content_type = <string>,
    scope = <string>,
    tag = <string>
)

```

The method returns `true` if the count of requests (4) under the granularity (8) with the filters (1, 2, 5, 6, 7, 9) exceeds the limit for a given time (3). 

<table>
<thead>
<tr>
    <th></th>
    <th style="text-align: left;">Parameter name</th>
    <th style="text-align: left;">Required</th>
    <th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr style="text-align: left;">
    <td>1</td>
    <td><code>ip</code></td>
    <td>False</td>
    <td>List of IP addresses that the rule applies to. If there are no IPs in the list, counting will be done for all IPs.</td>
</tr>
<tr style="text-align: left;">
    <td>2</td>
    <td>url</td>
    <td>True</td>
    <td>A regex pattern used to match the request's URI (URL + query_params).</td>
</tr>
<tr style="text-align: left;">
    <td>3</td>
    <td><code>time</code></td>
    <td>True</td>
    <td>The time limit, in seconds, within which we only allow <b>n</b> number of requests to URI matching the pattern.</td>
</tr>
<tr style="text-align: left;">
    <td>4</td>
    <td><code>requests</code></td>
    <td>True</td>
    <td>The maximum number of requests <b>accepted</b> within the given period before an action is taken (minimum value is 20 requests).</td>
</tr>
<tr style="text-align: left;">
    <td>5</td>
    <td><code>method</code></td>
    <td>False</td>
    <td>List of method types the request aggregation will be applied to.</td>
</tr>
<tr style="text-align: left;">
    <td>6</td>
    <td><code>status_code</code></td>
    <td>False</td>
    <td>List of status codes the request aggregation will be applied to.</td>
</tr>
<tr style="text-align: left;">
    <td>7</td>
    <td><code>content_type</code></td>
    <td>False</td>
    <td>Regex pattern to match request content_types against.</td>
</tr>
<tr style="text-align: left;">
    <td>8</td>
    <td><code>scope</code> (granularity)</td>
    <td>False<br>
    If the granularity isn’t set to <code>cluster</code>, the default aggregation will be set to <code>cluster</code>.</td>
    <td>The <code>cluster</code> scope counts all the traffic of a POP:
   <ul>
   <li>Interval counting is made on each POP separately.This can cause unsynchronized counting.</li>
  <li>IP counting can be counted separately on different POPs (each request individually, not overlapped).</li>
  <li>POPs could be related to certain locations, which means that some clients may never be addressed to certain POPs</li>
  <li>The <code>cluster</code> scope counts traffic per given IP.</li>
</ul>
   </td>
</tr>
<tr style="text-align: left;">
    <td>9</td>
    <td><code>tag</code></td>
    <td>False</td>
    <td>Aggregation of tagged (<a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules#tag-generating-rules" target="_blank">user-defined tags</a>) requests will be applied for each IP.</td>
</tr>
</tbody>
</table>

## Implementation 

### Advanced rules via API 

```
curl --request POST \
--url https://api.gcore.com/waap/v1alpha/stacks/STACK_ID/sites/SITE_ID/advanced_rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "ruleAction": {"block": {"statusCode": "FORBIDDEN_403"}},
    "phase": "ACCESS",
    "name": "Block Scrappers",
    "description": "Block IPs that hit more than 200 requests per 5 seconds for any `events` paths",
    "enabled": false,
    "source": "request.rate_limit([], '.*events', 5, 200, [], [], '', 'ip') and not ('mb-web-ui' in request.headers['Cookie'] or 'mb-mobile-ios' in request.headers['Cookie'] or 'mobile-android' in request.headers['Cookie'] or 'mb-mobile-android' in request.headers['Cookie'] or 'session-token' in request.headers['Cookie']) and not request.headers['session']" 
}'
```

### Best practices 

#### Block IPs that exceed request limit for any URL

Each request will be counted individually for each IP. For example, if the IP address 1.2.3.4 sends more than 200 requests within a 5-second timeframe, it will be blocked. 

Another IP address, such as 1.2.3.5, will only be blocked if it exceeds the allowed threshold of 200 requests in the same time interval.

```
curl --request POST \
--url https://api.gcore.com/waap/v1alpha/stacks/STACK_ID/sites/SITE_ID/advanced_rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "ruleAction": {"block": {"statusCode": "FORBIDDEN_403"}},
    "phase": "ACCESS",
    "name": "Limit Certain IPs",
    "description": "Limit Certain IPs",
    "enabled": false,
    "source": "request.rate_limit(['1.2.3.4', '1.2.3.5'], '.*events', 5, 200, [], [], '', 'ip')"
}'
```

#### Embed additional conditions

```
curl --request POST \
--url https://api.gcore.com/waap/v1alpha/stacks/STACK_ID/sites/SITE_ID/advanced_rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "ruleAction": {"block": {"statusCode": "FORBIDDEN_403"}},
    "phase": "ACCESS",
    "name": "Embedding additional condition to rate limit feature",
    "description": "Embedding additional condition to rate limit feature",
    "enabled": false,
    "source": "request.headers['User-Agent'] == 'Firefox' AND request.rate_limit(['1.2.3.4', '1.2.3.5'], '.*events', 5, 200, [], [], '', 'ip')"
}'
```
Note that using an additional condition, such as an IP, is considered a bad practice. For example, if you use `request.ip in ['1.2.3.4']` and `request.rate_limit([], '', 5, 200, [], [], '', 'ip')`, the rate limit will count requests per interval for every IP. However, it will set an action only when 1.2.3.4 exceeds the number of requests. 

This behavior is linked to the rule you are creating, not the rate limit condition. Thus, even with a blank IP list and an embedded IP condition, the rate limit will still count requests for all IPs.

#### Rate limit complex URL regex

```
curl --request POST \
--url https://api.gcore.com/waap/v1alpha/stacks/STACK_ID/sites/SITE_ID/advanced_rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "ruleAction": {"block": {"statusCode": "FORBIDDEN_403"}},
    "phase": "ACCESS",
    "name": "Rate limit complexed URL regex",
    "description": "Rate limit complexed URL regex",
    "enabled": false,
    "source": "request.rate_limit([], '.*(?<!aif|aiff|au|avi|bin|bmp|cab|carb|cct|cdf|class|css|doc|dor|dtd|exe|flv|gcf|gff|gif|grv hdmt hqx|ico|ini|jpeg|jpg|js|mov|mp3|nc|pct|pdf|png|ppc|pws|svg|swa|swf|txt|vbs|w32|wav|wbmp|wml|wmlc|wmls|wmlsc|xsd|zip|webp|jxr|hdp|wdp|webm|ogv|mp4|tif|woff|wot|woff)$', 120, 20, [], [], '', 'ip')"
}'
```

#### Embed IP range to the condition 

```
curl --request POST \
--url https://api.gcore.com/waap/v1alpha/stacks/STACK_ID/sites/SITE_ID/advanced_rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "ruleAction": {"block": {"statusCode": "FORBIDDEN_403"}},
    "phase": "ACCESS",
    "name": "Embedding IP range to the condition",
    "description": "Embedding IP range to the condition",
    "enabled": false,
    "source": "request.ip_in_range('10.0.0.0', '10.255.255.255') and request.rate_limit([], '.*[.]jpg', 120, 20, [], [], '', 'ip')"
}'
```

#### Cluster (PoP) granularity 

Rate limit all GET or HEAD redirected (302) requests with specific content type: 

```
curl --request POST \
--url https://api.gcore.com/waap/v1alpha/stacks/STACK_ID/sites/SITE_ID/advanced_rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "ruleAction": {"block": {"statusCode": "FORBIDDEN_403"}},
    "phase": "ACCESS",
    "name": "Embedding IP range to the condition",
    "description": "Embedding IP range to the condition",
    "enabled": false,
    "source": "request.rate_limit([], '.*url', 120, 20, ['GET', 'HEAD'], [302], 'text/html; charset=[uU][tT][fF]-8', 'cluster')"
}'
```

#### Rate limit by tag filter 

This functionality allows embedding <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules#tag-generating-rules" target="_blank">user-defined tags</a> into the rate limit condition so only tagged IPs requests will be aggregated into the rate limit mechanism. 

Note that my tag is a <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules#tag-generating-rules" target="_blank">user-defined tag</a> that should be defined in a separate rule. 

```
curl --request POST \
--url https://api.gcore.com/waap/v1alpha/stacks/STACK_ID/sites/SITE_ID/advanced_rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "ruleAction": {"block": {"statusCode": "FORBIDDEN_403"}},
    "phase": "ACCESS",
    "name": "Embedding tag to the condition",
    "enabled": false,
    "source": "request.limit_rate(tag="my tag",ips=["2.3.4.5"], url="/my_url/.*", time=10, requests=120, scope="ip")"
}'
```