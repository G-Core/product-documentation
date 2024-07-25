---
title: advanced-rule-objects
displayName: Advanced rule objects and attributes
published: true
order: 20               
pageTitle: View the list of advanced rules objects, attributes, and their types | Gcore
pageDescription: Learn about Gcore advanced rules and supported rule objects, attributes, and their types.
---
# Advanced rule objects and attributes

The following table contains all available objects and attributes you can use in your advanced rules.  

<table>
<thead>
<tr>
    <th style="text-align: left;">Object</th>
    <th style="text-align: left;">Attribute</th>
    <th style="text-align: left;">Arguments</th>
    <th style="text-align: left;">Type</th>
    <th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr style="text-align: left;">
<td>client_data</td>
    <td></td>
    <td></td>
    <td>Container</td>
    <td></td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>fingerprint</td>
    <td></td>
    <td>Dict</td>
    <td>Client fingerprint object</td>
</tr>
<tr style="text-align: left;">
    <td>response</td>
    <td></td>
    <td></td>
    <td>Container</td>
    <td>Container for response context</td>
</tr>
<tr>
    <td></td>
    <td>headers</td>
    <td></td>
    <td>Dict</td>
    <td>A dictionary of the response headers</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>status</td>
    <td></td>
    <td>Var</td>
    <td>Status code from the origin (integer)</td>
</tr>
<tr style="text-align: left;">
    <td>request</td>
    <td></td>
    <td></td>
    <td>Container</td>
    <td>Container for request context</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>rate_limit</td>
    <td></td>
    <td>Function</td>
    <td>Returns <code>true</code> if the rate limit is exceeded</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>content_type </td>
    <td>String</td>
    <td>A string with a maximum of 30 characters (optional)</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>interval</td>
    <td>Integer</td>
    <td>An integer between 1 and +inf</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>ip_list</td>
    <td>List</td>
    <td>A list of 0-10 items: a string representing an UP address (IPv4 or IPv6)</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>method_list</td>
    <td>List</td>
    <td>A list of 0-9 items of: an HTTP method</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>requests</td>
    <td>Integer</td>
    <td>An integer between 20 and +inf</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>scope</td>
    <td>Choice</td>
    <td>One of the following values: IP or cluster</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>status_list</td>
    <td>List</td>
    <td>A list of 0-20 items: an integer between 100 and 999</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>url</td>
    <td>URL</td>
    <td>A valid URL</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>ip_in_range</td>
    <td></td>
    <td>Function</td>
    <td>Returns true if the client IP is contained within the given range</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>from_ip</td>
    <td>IP</td>
    <td>A string representing an IP address (IPv4 or IPv6)</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td></td>
    <td>to_ip</td>
    <td>IP</td>
    <td>A string representing an IP address (IPv4 or IPv6)</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>headers</td>
    <td></td>
    <td>Dict</td>
    <td>A dictionary of the request headers</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>ip</td>
    <td></td>
    <td>Var</td>
    <td>A string representing the client IP</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>is_ajax</td>
    <td></td>
    <td>Function</td>
    <td>Returns true if the request type is AJAX</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>is_api</td>
    <td></td>
    <td>Function</td>
    <td>Returns true if the request is an API call</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>is_static</td>
    <td></td>
    <td>Function</td>
    <td>Returns true if the request type is STATIC</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>method</td>
    <td></td>
    <td>Var</td>
    <td>HTTP method (uppercase)</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>origin_ip</td>
    <td></td>
    <td>Var</td>
    <td>A string representing the client origin IP</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>path</td>
    <td></td>
    <td>Var</td>
    <td>Path of the URL</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>query_params</td>
    <td></td>
    <td>Var</td>
    <td>Query params</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>upload_file_content_type</td>
    <td></td>
    <td>Var</td>
    <td>Content type of the uploaded file (e.g., image/PNG)</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>upload_file_extension</td>
    <td></td>
    <td>Var</td>
    <td>File extension of the uploaded file (e.g., PNG)</td>
</tr>
<tr style="text-align: left;">
<td></td>
    <td>uri</td>
    <td></td>
    <td>Var</td>
    <td>A full URI string</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>url</td>
    <td></td>
    <td>Var</td>
    <td>A full URL string</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>all</td>
    <td></td>
    <td>Function</td>
    <td>Returns true if all the given tags exist</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>any</td>
    <td></td>
    <td>Function</td>
    <td>Returns true if one or more of the given tags exist</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>exists</td>
    <td></td>
    <td>Function</td>
    <td>Returns true if the given tag exists</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>tag</td>
    <td></td>
    <td>String</td>
    <td>A string with a maximum of 30 characters</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>tag_list</td>
    <td></td>
    <td>List</td>
    <td>A list of 1-10 items of a string with max 30 characters</td>
</tr>
<tr style="text-align: left;">
    <td>user_agent</td>
    <td></td>
    <td></td>
    <td>Container</td>
    <td>The User-agent header segments in lowercase</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>client</td>
    <td></td>
    <td>Var</td>
    <td>Client name. For example, Chrome, Firefox.</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>client_type</td>
    <td></td>
    <td>Var</td>
    <td>Client type. For example, major, lib.</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>client_version</td>
    <td></td>
    <td>Var</td>
    <td>Client version. For example, 47.1.23.</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>client_version_float</td>
    <td></td>
    <td>Var</td>
    <td>Client version, major.minor part. For example, 47.1.</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>cpu</td>
    <td></td>
    <td>Var</td>
    <td>CPU brand. For example, Intel.</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>device</td>
    <td></td>
    <td>Var</td>
    <td>Device brand. For example, iPhone, PlayStation.</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>device_type</td>
    <td></td>
    <td>Var</td>
    <td>Device type. For example, mobile, console.</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>engine</td>
    <td></td>
    <td>Var</td>
    <td>Engine type. For example, Gecko, AppleWebKit.</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>os</td>
    <td></td>
    <td>Var</td>
    <td>Client's OS. For example, Linux, Windows 8.</td>
</tr>
<tr style="text-align: left;">
    <td>whois</td>
    <td></td>
    <td></td>
    <td>Container</td>
    <td>Container for WHOIS data of the client IP</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>country</td>
    <td></td>
    <td>Var</td>
    <td>Country code (uppercase)</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>org</td>
    <td></td>
    <td>Var</td>
    <td>Organization name</td>
</tr>
<tr style="text-align: left;">
    <td></td>
    <td>owner_type</td>
    <td></td>
    <td>Var</td>
    <td>Owner type</td>
</tr>
</tbody>
</table>