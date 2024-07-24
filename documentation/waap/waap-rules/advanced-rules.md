---
title: advanced-rules
displayName: Advanced rules
published: true
order: 20
toc:
   --1--Create advanced rules: "create-advanced-rules"
   --1--Advanced rule properties: "advanced-rule-properties"
pageTitle: Learn about Gcore advanced rules | Gcore
pageDescription: Learn about Gcore advanced rules and how to use them for filtering incoming traffic and blocking malicious requests.
---
# Advanced rules

<alert-element type="info" title="Info">

This feature is available for the Enterprise package. 

</alert-element>

Similarly to WAAP custom rules, you can create, edit, and manage advanced custom rules. These rules also contain “If/Then” statements, but they also support more complex conditions created with the <a href="https://github.com/google/cel-spec" target="_blank">Common Expression Language (CEL)</a> syntax. 

## Create advanced rules

Due to the highly technical aspect of the advanced rules functionality, the ability to create and manage these rules is currently only available through our API.  

Check out the following guides for details on how to create advanced rules and their key components:  

* API docs: learn how to construct and manage advanced rules. 

* Advanced rules - objects, attributes, and types: get the list of all available objects you can use in rule expressions along with their respective attributes and types. 

* Advanced rules - source field objects: check the available source field objects you can use in your expressions along with their respective attributes and types. 

## Advanced rule properties

The advanced rule object contains the following properties: 

```
{ 
"name": "string", 
"source": "string", 
"enabled": true, 
"description": "string", 
"phase": "EXECUTION_PHASE_UNSPECIFIED", 
"ruleAction": { 
"allow": {}, 
"block": { 
"statusCode": "STATUS_CODE_UNSPECIFIED", 
"actionDuration": "string" 
}, 
"captcha": {}, 
"handshake": {}, 
"monitor": {}, 
"tag": { 
"tags": [ 
"string" 
] 
} 
} 
}
```

<expandable-element title="Description of the properties">

<table>
<thead>
  <tr>
    <th style="text-align: left"><b>Field</b></th>
    <th style="text-align: left"><b>Description</b></th>
    <th style="text-align: left"><b>Values</b></th>
    <th style="text-align: left"><b>Details</b></th>
  </tr>
</thead>
<tbody>
<tr>
    <td style="text-align: left"><code>name</code></td>
    <td style="text-align: left">Rule name</td>
    <td style="text-align: left">Can contain only ASCII letters, numbers, spaces, periods, and colons.</td>
    <td style="text-align: left"></td>
</tr>
<tr>
    <td style="text-align: left"><code>ruleAction</code></td>
    <td style="text-align: left">The action to execute when a condition is true.</td>
    <td style="text-align: left">ACTION_UNSPECIFIED: The action is undetermined.<br> 
    BLOCK: WAAP blocked the request.<br>
    ALLOW: WAAP allowed the request.<br>
    CAPTCHA: WAAP presented the user with a CAPTCHA<br>
    HANDSHAKE: WAAP. performed automatic browser validation.<br>
    MONITOR: WAAP monitored and allowed the request.<br>
    TAG: WAAP will generate tag with no action. </td>
    <td style="text-align: left">On tag <a href="https://gcore.com/docs/waap/waap-rules/custom-rules#actions-in-custom-rules" target="_blank">action</a>, the tag field should be provided.<br>
    On block <a href="https://gcore.com/docs/waap/waap-rules/custom-rules#actions-in-custom-rules" target="_blank">action</a>, setting up the <code>statusCode</code> and <code>actionDuration</code> is optional. The default value will be 403 and 0s (seconds). </td>
</tr>
<tr>
    <td style="text-align: left"><code>source</code></td>
    <td style="text-align: left">The condition part of the rule.</td>
    <td style="text-align: left">Can reference namespace objects: request, whois, session, response, tags, user_agent, client_data, as well as use data and functions.<br> 
    Supported Python operand syntax: and, or, in, not, ==, !=, >, <, etc.<br>
    Supported CEL operand syntax: ||, && <br></td>
    <td style="text-align: left">Every string value should be enclosed in single quotation marks <code>'</code> and <strong>not<strong> in double quotation marks <code>"</code>.</td>
</tr>
<tr>
    <td style="text-align: left"><code>enabled</code></td>
    <td style="text-align: left">Whether or not the rule is enabled.</td>
    <td style="text-align: left">Boolean: true or false</td>
    <td style="text-align: left">Default value: false.</td>
</tr>
<tr>
    <td style="text-align: left"><code>description</code></td>
    <td style="text-align: left">A string to describe the purpose of the rule.</td>
    <td style="text-align: left">Any string.<br>
    The character limit for the description field is 100 characters.</td>
    <td style="text-align: left">Default value: false.</td>
</tr>
<tr>
    <td style="text-align: left"><code>phase</code></td>
    <td style="text-align: left">The request processing phase.</td>
    <td style="text-align: left">EXECUTION_PHASE_UNSPECIFIED: The phase for applying the advanced rule is not specified.<br>
    ACCESS: The advanced rule applies to the request phase (request headers and body available).<br>
    HEADER_FILTER: The advanced rule applies to the response headers phase.<br>
    BODY_FILTER: The advanced rule applies to the response body phase.</td>
    <td style="text-align: left">Default value: ACCESS.</td>
</tr>
<tr>
    <td style="text-align: left"><code>statusCode</code></td>
    <td style="text-align: left">A custom HTTP status code returned by WAAP if a rule blocks a request.</td>
    <td style="text-align: left">None (default: 403), 405, 403, 429, 418</td>
    <td style="text-align: left">Status code can be defined only when the ruleAction is set to BLOCK.</td>
</tr>
<tr>
    <td style="text-align: left"><code>actionDuration</code></td>
    <td style="text-align: left">The duration of an action.</td>
    <td style="text-align: left">A string with a number followed by:<br>
    m - minutes<br>
    s - seconds<br>
    h - hours<br>
    d - days<br>
    For instance, 5m will generate an action with a life span of 5 minutes.</td>
    <td style="text-align: left">actionDuration can be defined only when the ruleAction is set to BLOCK.<br>
    When setting actionDuration, the tag name penalty will be produced on the client IP for the period duration that been set.</td>
</tr>
<tr>
    <td style="text-align: left"><code>tag</code></td>
    <td style="text-align: left">A user-defined tag that will be attached to the request.</td>
    <td style="text-align: left">String<br>
    Tags with spaces will be converted to underscore line _ and will be presented in lowercase. For instance, Ignore Automation will become ignore_automation.</td>
    <td style="text-align: left">Tag-based rules are informative rules.<br>
    Tag value should be enclosed in double quotation marks <code>'</code> and <strong>not<strong> in single quotation marks <code>"</code>.</td>
</tr>
</tbody>
</table> 
</expandable-element>

## Best practices 

You can use our API documentation as a guide in constructing your own advanced rules. The following sections demonstrate a few examples of advanced rules created via our API using cURL. 

### Rate limiting

Block IPs that hit more than 200 requests per 5 seconds (changeable) when the following cookies don't exist. You can find more examples in our Rate limiting guide.

```
curl --request POST \ 
--url https://api.gcore.com/waap/v1alpha/stacks/test_stack_id/sites/test_site_id/advanced_rules \ 
--header 'accept: application/json' \ 
--header 'content-type: application/json' \ 
--data ' 
{ 
"ruleAction": {"block": {"statusCode": "FORBIDDEN_403"}}, 
"phase": "ACCESS", 
"name": "Block Scrappers", 
"description": "Block IPs that hit more than 200 requests per 5 seconds for any `events` paths", 
"enabled": false, 
"source": "request.rate_limit([], '.*events', 5, 200, [], [], '', 'ip') and not ('mb-web-ui' in request.headers['Cookie'] or 'mb-mobile-ios' in request.headers['Cookie'] or 'mobile-android' in request.headers['Cookie'] or 'mb-mobile-android' in request.headers['Cookie'] or 'session-token' in request.headers['Cookie']) and not request.headers['session']" 
} 
' 
```

### Penalty rule 

Will block the IPs that were detected with certain TLS fingerprint for the next 5 minutes (chained rule): 

```
curl --request POST \ 
--url https://api.gcore.com/waap/v1alpha/stacks/test_stack_id/sites/test_site_id/advanced_rules \ 
--header 'accept: application/json' \ 
--header 'content-type: application/json' \ 
--data ' 
{ 
"ruleAction": {"block": {"statusCode": "FORBIDDEN_403", "actionDuration": "5m"}}, 
"phase": "ACCESS", 
"name": "Penalty TLS fingerprint", 
"description": "Block and tag IPs that are detected with certain TLS fingerprint for the next 5 minutes", 
"enabled": false, 
"source": "request.ja3 == 'e2925c27149b0d0dc34373d55040dde1'" 
} 
'
```

```
curl --request POST \ 
--url https://api.gcore.com/waap/v1alpha/stacks/test_stack_id/sites/test_site_id/advanced_rules \ 
--header 'accept: application/json' \ 
--header 'content-type: application/json' \ 
--data ' 
{ 
"ruleAction": {"block": {}}, 
"phase": "ACCESS", 
"name": "Block Penalty", 
"description": "Block requests that are detected with `penalty` tag", 
"enabled": false, 
"source": "tags.exists('penalty')" 
} 
' 
```

### Validate a set of countries 

Use JavaScript validation to challenge IPs that are coming from countries without certain cookies: 

```
curl --request POST \ 
--url https://api.gcore.com/waap/v1alpha/stacks/test_stack_id/sites/test_site_id/advanced_rules \ 
--header 'accept: application/json' \ 
--header 'content-type: application/json' \ 
--data ' 
{ 
"ruleAction": {"handshake": {}}, 
"phase": "ACCESS", 
"name": "Validate set of countries", 
"description": "Validate with JavaScript challenge IPs that are coming from the following countries", 
"enabled": false, 
"source": "whois.country in ['BR', 'VN', 'ID', 'TH', 'ME', 'XK', 'LK'] and not ('mb-web-ui' in request.headers['Cookie'] or 'mb-mobile-ios' in request.headers['Cookie'] or 'mobile-android' in request.headers['Cookie'] or 'mb-mobile-android' in request.headers['Cookie'])" 
} 
' 
```

### Add clients to allow list 

```
curl --request POST \ 
--url https://api.gcore.com/waap/v1alpha/stacks/test_stack_id/sites/test_site_id/advanced_rules \ 
--header 'accept: application/json' \ 
--header 'content-type: application/json' \ 
--data ' 
{ 
"ruleAction": {"allow": {}}, 
"name": "Whitlist knowen IPs", 
"enabled": false, 
"source": "request.ip == '117.20.32.5' or request.ip == '117.20.32.4' or request.ip_in_range('72.21.217.0', '72.21.217.255')" 
} 
' 
```

### Tag and allow registered clients 

Make sure that the tag value is enclosed in the double-quotes character ". 

```
curl --request POST \ 
--url https://api.gcore.com/waap/v1alpha/stacks/test_stack_id/sites/test_site_id/advanced_rules \ 
--header 'accept: application/json' \ 
--header 'content-type: application/json' \ 
--data ' 
{ 
"name": "Tag registered clients", 
"description": "Detect and tag registered clients by cookie", 
"source": "'mb-mobile-android' in request.headers['Cookie']", 
"ruleAction": {"tag": {"tags": ["registered"]}} 
} 
' 
curl --request POST \ 
--url https://api.gcore.com/waap/v1alpha/stacks/test_stack_id/sites/test_site_id/advanced_rules \ 
--header 'accept: application/json' \ 
--header 'content-type: application/json' \ 
--data ' 
{ 
"name": "Allow registered clients", 
"description": "Allow registered clients", 
"source": "tags.exists('registered')", 
"ruleAction": {"allow": {}} 
} 
' 
```

### Define login pages 

```
curl --request POST \ 
--url https://api.gcore.com/waap/v1alpha/stacks/test_stack_id/sites/test_site_id/advanced_rules \ 
--header 'accept: application/json' \ 
--header 'content-type: application/json' \ 
--data ' 
{ 
"name": "Detect and Tag Login Pages", 
"source": "['url1/login','url2/signup'] in request.uri", 
"ruleAction": {"tag": {"tags": ["login page"]}} 
} 
' 
```

## Review existing rules 

After you create advanced rules, they will appear in the Gcore Customer Portal, on the WAAP rules page. You can enable or disable the rules by clicking the relevant toggles.

<img src="https://assets.gcore.pro/docs/waap/waap-rules/advanced-rules/advanced-rules-section-empty.png" alt="Advanced rules section with empty table in the Customer Portal" width="80%">