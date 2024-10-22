---
title: source-field-objects
displayName: Source field objects
published: true
order: 20               
pageTitle: View the list of source field objects available in advanced rule expressions | Gcore
pageDescription: Learn about Gcore advanced rules and the supported source field objects that you can use in advanced rule expressions.
---
# Source field objects in advanced rule expressions

<alert-element type="info" title="Info">
 
For the `request`, `Whois`, `session`, and `user-agent` objects, every string value should be enclosed in a single-quotes `'` and **not** in double-quotes `"`. 
 
</alert-element>

## request

<table>
<thead>
<tr>
    <th style="text-align: left; width:15%">Attribute</th>
    <th style="text-align: left; width:15%">Type</th>
    <th style="text-align: left; width:25%">Description</th>
    <th style="text-align: left; width:35%">Compiled <code>source</code> field</th>
    
  </tr>
  </thead>
<tbody>
<tr style="text-align: left;">
    <td>headers</td>
    <td>dict</td>
    <td>Request headers</td>
    <td></td>
  </tr>
<tr style="text-align: left;">
    <td>ip</td>
    <td>string</td>
    <td>Client IP</td>
    <td>request.ip<br>
    request.ip == '117.20.32.5' ||<br>
    request.ip == '117.20.32.4'</td>
  </tr>
<tr style="text-align: left;">
    <td>uri</td>
    <td>string</td>
    <td>Domain's URI (URL path + arguments)</td>
    <td>request.uri<br>
    ('/prehistoric/monotony/monotony.phtml' or '/amfphp/services') in request.uri</td>
  </tr>
<tr style="text-align: left;">
    <td>path</td>
    <td>string</td>
    <td>Domain’s URL path</td>
    <td>request.path<br>
    request.path in ['/process_neopet_desc.phtml', '/modify_neomessages.phtml']</td>
  </tr>
<tr style="text-align: left;">
    <td>method</td>
    <td>string</td>
    <td>HTTP method (uppercase).</td>
    <td>request.method<br>
    request.method == 'OPTION'</td>
  </tr>
<tr style="text-align: left;">
    <td>origin_ip</td>
    <td>string</td>
    <td>Web application server IP</td>
    <td>request.origin_ip<br>
    request.origin_ip == '120.36.54.1'</td>
  </tr>
<tr style="text-align: left;">
    <td>ja3</td>
    <td>string</td>
    <td>TLS fingerprint.</td>
    <td>request.ja3<br>
    request.ja3 == 'e2925c27149b0d0dc34373d55040dde1' or request.ja3 == '3e9b20610098b6c9bff953856e58016a' or request.ja3 == '7d671906ed4a1edac3262a54676dacfa'</td>
  </tr>
<tr style="text-align: left;">
    <td>http_version</td>
    <td>string</td>
    <td>Represents HTTP version</td>
    <td>request.http_version<br>
    request.http_version in ['1.1']</td>
  </tr>
<tr style="text-align: left;">
    <td>is_api()</td>
    <td>function</td>
    <td>Returns true if the request is API</td>
    <td>request.is_api()</td>
  </tr>
<tr style="text-align: left;">
    <td>is_ajax()</td>
    <td>function</td>
    <td>Returns true if the request is AJAX</td>
    <td>request.is_ajax()</td>
  </tr>
<tr style="text-align: left;">
    <td>is_static()</td>
    <td>function</td>
    <td>Returns <code>true</code> if the request is static</td>
    <td>request.is_static()</td>
  </tr>
<tr style="text-align: left;">
    <td>ip_in_range</td>
    <td>function</td>
    <td>Returns <code>true</code> if client ip is within the specified range</td>
    <td>request.ip_in_range(<string>, <string>)<br>
    request.ip_in_range('72.21.217.0', '72.21.217.255')  
or request.ip_in_range('2409:4072:6c8c:e228:ecaf:ce2c:fd7d:0000', '2409:4072:6c8c:e228:ecaf:ce2c:fd7d:4780')</td>
  </tr>
<tr style="text-align: left;">
    <td>rate_limit</td>
    <td>function</td>
    <td>Returns true if the rate limit exceeded for these parameters (the scope is 'ip'/'cluster').<br>For parameter descriptions, check out the <a href="https://gcore.com/docs/waap/waap-rules/advanced-rules/advanced-rate-limiting-rules" target="_blank">Rate limiting</a> guide.</td>
    <td>rate_limit(<br>
[ip <string>, ...],<br>
url <string>,<br>
interval <int>,<br>
requests <int>,<br>
[method <string>,...],<br>
[status_code <int>,...],<br>  
content_type <string>,<br>  
scope <string><br> 
)<br>
example:<br>
request.rate_limit([], '/', 5, 200, ['GET', 'HEAD'], [], 'text/html; charset=', 'ip')</td>
  </tr>
  </tbody>
</table>

## whois

<table>
<thead>
  <tr>
    <th style="text-align: left;">Attribute</th>
    <th style="text-align: left;">Type</th>
    <th style="text-align: left;">Description</th>
    <th style="text-align: left;">Compiled <code>source</code> field</th>
  </tr>
  </thead>
<tbody>
<tr style="text-align: left;">
    <td>country</td>
    <td>string</td>
    <td style="text-align: left;">Two-letter country code (uppercase).</td>
    <td style="text-align: left;">whois.country<br>
    whois.country in ['BR', 'VN', 'ID']</td>
  </tr>
  <tr style="text-align: left;">
    <td>org</td>
    <td>string</td>
    <td style="text-align: left;">Organization name from the WHOIS database.</td>
    <td style="text-align: left;">whois.org<br>
    whois.org in ['Google Inc', 'Google Inc.', 'Google LLC', 'Google Incorporated']</td>
  </tr>
    <tr style="text-align: left;">
    <td>owner_type</td>
    <td>string</td>
    <td style="text-align: left;">Owner type of the range.</td>
    <td style="text-align: left;">whois.owner_type<br>
    whois.owner_type != 'hosting services'</td>
  </tr>
  </tbody>
</table>

## session

<table>
<thead>
  <tr>
    <th style="text-align: left; width:15%">Attribute</th>
    <th style="text-align: left; width:10%">Type</th>
    <th style="text-align: left; width:35%">Description</th>
    <th style="text-align: left; width:30%">Compiled <code>source</code> field</th>
  </tr>
  </thead>
<tbody>
<tr style="text-align: left;">
    <td>request_counter</td>
    <td>int</td>
    <td style="text-align: left;">Sequential number of the request within the session.</td>
    <td style="text-align: left;">session.session_request_counter<br>
    session.request_counter > 1000</td>
  </tr>
  <tr style="text-align: left;">
    <td>profiling_status</td>
    <td>string</td>
    <td style="text-align: left;">Client’s fingerprint profiling status.<br><br>
    Values:
    <ul style="text-align: left;">
    <li><strong>Initiated</strong>: JavaScript was injected in the response and sent to the client for execution.</li>
    <li><strong>Executed once</strong>: JavaScript was executed, and WAAP received preliminary results.</li>
    <li><strong>Profiling error</strong>: An error occurred during profiling.</li>
    <li><strong>Profiling completed</strong>: Profiling completed without error.</li>
   <li><strong>Idle</strong>: All JavaScript tests and fingerprinting process completed.</li>
   </ul>
    <td style="text-align: left;">session.profiling_status<br>
    session.profiling_status == 'idle'</td>
  </tr>
  </tbody>
</table>

## response

<table>
<thead>
  <tr>
    <th style="text-align: left;">Attribute</th>
    <th style="text-align: left;">Type</th>
    <th style="text-align: left;">Description</th>
    <th style="text-align: left;">Compiled <code>source</code> field</th>
  </tr>
  </thead>
<tbody>
<tr style="text-align: left;">
    <td>status</td>
    <td>int</td>
    <td style="text-align: left;">HTTP status code</td>
    <td style="text-align: left;">response.status</td>
  </tr>
  <tr style="text-align: left;">
    <td>headers</td>
    <td>dict</td>
    <td style="text-align: left;">Response headers</td>
    <td style="text-align: left;">response.headers['Access-Control-Allow-Credentials'] == 'true'</td>
  </tr>
  </tbody>
</table>

## tags

<table>
<thead>
  <tr>
    <th style="text-align: left;">Attribute</th>
    <th style="text-align: left;">Type</th>
    <th style="text-align: left;">Description</th>
    <th style="text-align: left;">Compiled <code>source</code> field</th>
  </tr>
  </thead>
<tbody>
<tr style="text-align: left;">
    <td>exists(tag <string>)</td>
    <td>function</td>
    <td style="text-align: left;">Returns <code>true</code> if the tag exists.</td>
    <td style="text-align: left;">tags.exists(<string>)<br>
    tags.any([<string>, <string>…., <string>]) up to 10 tags<br>
    tags.all([<string>, <string>…., <string>]) up to 10 tags<br>
    tags.any(['proxynetwork','hostingservices'])<br>
    tags.exists('penalty')</td>
  </tr>
  <tr style="text-align: left;">
    <td>any([tag <string>, ...])</td>
    <td>function</td>
    <td style="text-align: left;">Returns <code>true</code> if any of the tags exists.</td>
    <td></td>
  </tr>
    <tr style="text-align: left;">
    <td>all([tag <string>, ...])</td>
    <td>function</td>
    <td style="text-align: left;">Returns <code>true</code> if all tags exist.</td>
    <td></td>
  </tr>
  </tbody>
</table>

## user-agent  

The **ua_parsed** table contains user agent information collected by WAAP from the source of the logged request. 

<table>
<thead>
  <tr>
    <th style="text-align: left; width:20%">Attribute</th>
    <th style="text-align: left; width:15%">Type</th>
    <th style="text-align: left; width:30%">Description</th>
    <th style="text-align: left; width:25%">Compiled <code>source</code> field</th>
  </tr>
  </thead>
  <tbody>
<tr style="text-align: left;">
    <td>engine</td>
    <td>string</td>
    <td style="text-align: left;">The client engine. For example, Gecko.</td>
    <td style="text-align: left;">user_agent.engine</td>
  </tr>
<tr style="text-align: left;">
    <td>client</td>
    <td>string</td>
    <td style="text-align: left;">The name of the client. An example of client name is "Firefox".</td>
    <td style="text-align: left;">user_agent.client</td>
  </tr>
<tr style="text-align: left;">
    <td>client_type</td>
    <td>string</td>
    <td style="text-align: left;">The type of client. Optional values: Major browser, NA, Lib, Crawler, Custom browser, mobile app, Headless browser, Bot, Application, mail client, Site monitoring, RSS reader, Game console, Text browser, Network diagnostics, certificate authority, paying service.</td>
    <td style="text-align: left;">user_agent.client_type<br>
    'major browser' in user_agent.client_type</td>
  </tr>
<tr style="text-align: left;">
    <td>client_version</td>
    <td>string</td>
    <td style="text-align: left;">The client engine's version.</td>
    <td style="text-align: left;">user_agent.client_version</td>
  </tr>
<tr style="text-align: left;">
    <td>client_version_float</td>
    <td>string</td>
    <td style="text-align: left;">A possibly truncated version of the client browser engine's version.</td>
    <td style="text-align: left;">user_agent.client_version_float</td>
  </tr>
<tr style="text-align: left;">
    <td>os</td>
    <td>string</td>
    <td style="text-align: left;">The client computer's operating system. An example of os is "Mac OS X 10.14".</td>
    <td style="text-align: left;">user_agent.os</td>
  </tr>
<tr style="text-align: left;">
    <td>cpu</td>
    <td>string</td>
    <td style="text-align: left;">The client computer's CPU. An example of CPU is "Intel".</td>
    <td style="text-align: left;">user_agent.cpu</td>
  </tr>
<tr style="text-align: left;">
    <td>device</td>
    <td>string</td>
    <td style="text-align: left;">Information about the client device. An example of a device is "mac".</td>
    <td style="text-align: left;">user_agent.device</td>
  </tr>
<tr style="text-align: left;">
    <td>device_type</td>
    <td>string</td>
    <td style="text-align: left;">Additional information about the client device.<br><br> Optional values: <ul style="text-align: left;">
    <li>Web search engine bots</li>
    <li>mobile</li>
   <li> NA</li>
    <li>SEO</li>
   <li>Analytics or marketing bots</li>
   <li>Preview bot</li>
    <li>Media or entertainment search bots</li>
    <li>Social media or blog bots</li>
    <li>RSS seed reader bots</li>
    <li>Site monitoring and web development bots</li>
   <li> Web archiver bots</li>
    <li>console</li>
   <li>Job search engine bots</li>
   <li> Online advertising bots</li>
    <li>News aggregator bots</li>
   <li>Academic or research bots</li>
   <li>Desktop</li>
   <li>Business intelligence bots</li>
   <li>Automated shopping cart and sniper bots</li>
    <li>Enterprise data aggregator bots</li>
    <li>Media player</li></td>
    <td style="text-align: left;">user_agent.device_type<br>
    user_agent.device_type == 'na'</ul></td>
  </tr>
    </tbody>
</table>

## client_data

<table>
<thead>
  <tr>
    <th style="text-align: left;">Attribute</th>
    <th style="text-align: left;">Type</th>
    <th style="text-align: left;">Description</th>
    <th style="text-align: left;">Compiled <code>source</code> field</th>
  </tr>
  </thead>
<tbody>
<tr style="text-align: left;">
    <td>fingerprint['hash']</td>
    <td>dict</td>
      <td rowspan="4" style="text-align: left;">A table that contains fingerprint information about the request (the information is collected by WAAP with injected JavaScript):<br>
      <ul style="text-align: left;">
      <li>fp__hash of the client</li>
      <li>fp__js of the client</li>
      <li>fp__flash of the client</li>
      <li>fp__header of the client</li></ul><br>
       client_data.fingerprint == 'kvd8oxizrdl-41-37zpvwqrr-5tzoaavgfr7-v2osmr4iefe-noieo-90.3095389639745667'
      </td>
    <td style="text-align: left;">client_data.fingerprint['hash']client_data.fingerprint['hash'] == '9be394dca715eca8e42783397a507d2e'</td>
  </tr>
  <tr style="text-align: left;">
    <td>fingerprint['js']</td>
    <td>dict</td>
    <td style="text-align: left;">client_data.fingerprint['js']</td>
  </tr>
    <tr style="text-align: left;">
    <td>fingerprint['flash']</td>
    <td>dict</td>
    <td style="text-align: left;">client_data.fingerprint['flash'] </td>
  </tr>
    </tr>
    <tr style="text-align: left;">
    <td>fingerprint['header']</td>
    <td>dict</td>
    <td style="text-align: left;">client_data.fingerprint['header'] </td>
  </tr>
  </tbody>
</table>
