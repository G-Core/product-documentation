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

This feature is available for the <a href="https://gcore.com/docs/waap/billing#enterprise" target="_blank">Enterprise</a> package. 

</alert-element>

Similarly to WAAP <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">custom rules</a>, you can create, edit, and manage advanced custom rules. These rules also contain “If/Then” statements, but they support more complex conditions created with the <a href="https://github.com/google/cel-spec" target="_blank">Common Expression Language (CEL)</a> syntax. 

## Create advanced rules

Due to the highly technical aspect of the advanced rules functionality, the ability to create and manage these rules is currently only available through our API.  

Check out the following guides for details on how to create advanced rules and their key components:  

* <a href="https://api.gcore.com/docs/waap" target="_blank">API docs</a>: Learn how to construct and manage advanced rules. 

* <a href="https://gcore.com/docs/waap/waap-rules/advanced-rules/advanced-rule-objects" target="_blank">Advanced rule objects and attributes</a>: Get the list of all available objects you can use in rule expressions along with their respective attributes and types. 

* <a href="https://gcore.com/docs/waap/waap-rules/advanced-rules/source-field-objects" target="_blank">Source field objects</a>: Check the available source field objects you can use in your expressions along with their respective attributes and types. 

## Advanced rule properties

The advanced rule object contains the following properties: 

```
{
  "name": "string",
  "description": "",
  "enabled": true,
  "action": {
    "allow": {},
    "block": {
      "status_code": 403,
      "action_duration": "string"
    },
    "captcha": {},
    "handshake": {},
    "monitor": {},
    "tag": {
      "tags": [
        "string"
      ]
    }
  },
  "source": "string",
  "phase": "access"
}
```

<alert-element type="info" title="Info">
 
Each rule can contain only one action—`block`, `allow`, `captcha`, `handshake`, `monitor`, or `tag`. If you use multiple actions in a single rule, the API will return an error.
 
</alert-element>

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
    <td style="text-align: left"><code>action</code></td>
    <td style="text-align: left">The action to execute when a condition is true.</td>
    <td style="text-align: left"><ul>
    <li><code>block</code>: WAAP blocked the request.</li>
    <li><code>allow</code>: WAAP allowed the request.</li>
    <li><code>captcha</code>: WAAP presented the user with a CAPTCHA</li>
    <li><code>handshake</code>: WAAP. performed automatic browser validation.</li>
    <li><code>monitor</code>: WAAP monitored and allowed the request.</li>
    <li><code>tag</code>: WAAP will generate a tag with no action.</li>
    </ul>
    <td style="text-align: left">On tag <a href="https://gcore.com/docs/waap/waap-rules/custom-rules#actions-in-custom-rules" target="_blank">action</a>, the tag field should be provided.<br><br>
    For the block <a href="https://gcore.com/docs/waap/waap-rules/custom-rules#actions-in-custom-rules" target="_blank">action</a>, setting up the <code>status_code</code> (integer) and <code>action_duration</code> (time in seconds) is optional. By default, the status is set to <code>"status_code": 403</code>, and duration equals to <code>0s</code>.</td>
</tr>
<tr>
    <td style="text-align: left"><code>source</code></td>
    <td style="text-align: left">The condition part of the rule.</td>
    <td style="text-align: left">Can reference namespace objects: request, whois, session, response, tags, user_agent, client_data, as well as use data and functions.<br><br>
    Supported Python operand syntax: and, or, in, not, ==, !=, >, <, etc.<br>
    Supported CEL operand syntax: ||, && <br></td>
    <td style="text-align: left">Every string value should be enclosed in single quotation marks <code>'</code> and <strong>not</strong> in double quotation marks <code>"</code>.</td>
</tr>
<tr>
    <td style="text-align: left"><code>enabled</code></td>
    <td style="text-align: left">Whether or not the rule is enabled.</td>
    <td style="text-align: left">Boolean: <code>true</code> or <code>false</code></td>
    <td style="text-align: left">Default value: <code>false</code></td>
</tr>
<tr>
    <td style="text-align: left"><code>description</code></td>
    <td style="text-align: left">A string to describe the purpose of the rule.</td>
    <td style="text-align: left">Any string.<br>
    The character limit for the description field is 100 characters.</td>
    <td style="text-align: left">Default value: <code>false</code></td>
</tr>
<tr>
    <td style="text-align: left"><code>phase</code></td>
    <td style="text-align: left">The request processing phase.</td>
    <td style="text-align: left">
    <ul>
    <li><code>access</code>: The advanced rule applies to the request phase (request headers and body available).</li>
    <li><code>header_filter</code>: The advanced rule applies to the response headers phase.</li>
    <li><code>body_filter</code>: The advanced rule applies to the response body phase.</li>
    </ul></td>
    <td style="text-align: left">Default value: <code>access</code></td>
</tr>
</tbody>
</table> 
</expandable-element>

## Best practices 

You can use our API documentation as a guide in constructing your own advanced rules. The following sections demonstrate a few examples of advanced rules created via our API using cURL. 

### Rate limiting

Block IPs that hit more than 200 requests per 5 seconds (changeable) when the following cookies don't exist. You can find more examples in our <a href="https://gcore.com/docs/waap/waap-rules/advanced-rules/advanced-rate-limiting-rules" target="_blank">Rate limiting</a> guide.

```
curl --request POST \
--url https://api.gcore.com/waap/v1/domains/{domain_id}/advanced-rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "action": {
        "block": {
            "status_code": 403
        }
    },
    "phase": "access",
    "name": "Block Scrappers",
    "description": "Block IPs that hit more than 200 requests per 5 seconds for any `events` paths",
    "enabled": false,
    "source": "request.rate_limit([], '.*events', 5, 200, [], [], '', 'ip') and not ('mb-web-ui' in request.headers['Cookie'] or 'mb-mobile-ios' in request.headers['Cookie'] or 'mobile-android' in request.headers['Cookie'] or 'mb-mobile-android' in request.headers['Cookie'] or 'session-token' in request.headers['Cookie']) and not request.headers['session']"
}'
```
### Penalty rule 

Block the IPs that were detected with certain TLS fingerprint for the next 5 minutes (chained rule): 

```
curl --request POST \ 
--url https://api.gcore.com/waap/v1/domains/{domain_id}/advanced-rules \ 
--header 'accept: application/json' \ 
--header 'content-type: application/json' \ 
--data ' 
{ 
"action": {"block": {"status_code": 403,   "action_duration": "5m"}}, 
"phase": "access", 
"name": "Penalty TLS fingerprint", 
"description": "Block and tag IPs that are detected with certain TLS fingerprint for the next 5 minutes", 
"enabled": false, 
"source": "request.ja3 == 'e2925c27149b0d0dc34373d55040dde1'"
} 
'
```

```
curl --request POST \
--url https://api.gcore.com/waap/v1/domains/{domain_id}/advanced-rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "action": {
        "block": {}
    },
    "phase": "access",
    "name": "Block Penalty",
    "description": "Block requests that are detected with `penalty` tag",
    "enabled": false,
    "source": "tags.exists('penalty')"
}'
```

### Validate a set of countries 

Use JavaScript validation to challenge IPs that are coming from countries without certain cookies: 

```
curl --request POST \
--url https://api.gcore.com/waap/v1/domains/{domain_id}/advanced-rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "action": {
        "handshake": {}
    },
    "phase": "access",
    "name": "Validate set of countries",
    "description": "Validate with JavaScript challenge IPs that are coming from the following countries",
    "enabled": false,
    "source": "whois.country in ['BR', 'VN', 'ID', 'TH', 'ME', 'XK', 'LK'] and not ('mb-web-ui' in request.headers['Cookie'] or 'mb-mobile-ios' in request.headers['Cookie'] or 'mobile-android' in request.headers['Cookie'] or 'mb-mobile-android' in request.headers['Cookie'])
}'
```

### Add clients to allow list 

```
curl --request POST \
--url https://api.gcore.com/waap/v1/domains/{domain_id}/advanced-rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "action": {
        "allow": {}
    },
    "name": "Whitelist known IPs",
    "enabled": false,
    "source": "request.ip == '117.20.32.5' or request.ip == '117.20.32.4' or request.ip_in_range('72.21.217.0', '72.21.217.255')"
}'
```

### Tag and allow registered clients 

Make sure that the tag value is enclosed in the double-quotes character ". 

```
curl --request POST \
--url https://api.gcore.com/waap/v1/domains/{domain_id}/advanced-rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "name": "Tag registered clients",
    "description": "Detect and tag registered clients by cookie",
    "source": "'mb-mobile-android' in request.headers['Cookie']",
    "action": {
        "tag": {
            "tags": ["registered"]
        }
    }
}'
```

```
curl --request POST \
--url https://api.gcore.com/waap/v1/domains/{domain_id}/advanced-rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "name": "Allow registered clients",
    "description": "Allow registered clients",
    "source": "tags.exists('registered')",
    "action": {
        "allow": {}
    }
}'
```

### Define login pages 

```
curl --request POST \
--url https://api.gcore.com/waap/v1/domains/{domain_id}/advanced-rules \
--header 'accept: application/json' \
--header 'content-type: application/json' \
--data '{
    "name": "Detect and Tag Login Pages",
    "source": "['url1/login','url2/signup'] in request.uri",
    "action": {
        "tag": {
            "tags": ["login page"]
        }
    }
}'
```

## Review existing rules 

After you create advanced rules, they will appear on the **WAAP rules** page in the Gcore Customer Portal. You can enable or disable the rules by clicking the relevant toggles.

<img src="https://assets.gcore.pro/docs/waap/waap-rules/advanced-rules/advanced-rules-section-empty.png" alt="Advanced rules section with empty table in the Customer Portal" width="80%">