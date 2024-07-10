---
title: waap-rules
displayName: WAAP rules
published: true
order:
pageTitle: Learn about Gcore predefined, advanced, and custom rules  | Gcore
pageDescription: Learn about Gcore WAAP rules and how to use them for filtering incoming traffic and blocking malicious requests.
---
# WAAP rules

WAAP rules allow you to specify how to inspect web requests to your domain and what actions to take when a request matches certain criteria. This helps protect your applications from common threats such as SQL injection, cross-site scripting (XSS), and other malicious activities.  

For example, you can create a rule to block any request with common SQL injection patterns or require CAPTCHA validation to prevent spam.  

## What rules can you create?  

Depending on your package level, you can create the following rules: 

* <a href="https://gcore.com/docs/waap/ip-security/allow-and-block-ip-addresses" target="_blank">Allow/Block IP rules</a>: Easy to configure and designed for use cases when you need a straightforward, simple tool to manage IP access to your domain. These rules form access control lists (ACLs) and are free for any plan that includes our WAAP product.  

* <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">Custom rules</a>: These rules compose of “if/then” statements and cover more complicated scenarios, such as filtering requests from specified countries or organizations. We offer several predefined custom rules tailored for different plans. 

* <a href="https://gcore.com/docs/waap/waap-rules/advanced-rules" target="_blank">Advanced rules</a>: Designed for technical users who need even more control over rule creation. Can be configured via API and are available within the WAAP Enterprise plan. 

<alert-element type="info" title="Info">
 
In addition to the above-described rules that you can configure, WAAP also contains a set of  <a href="https://gcore.com/docs/waap/waap-rules/predefined-rules" target="_blank">predefined WAAP rules</a> that you can either enable or disable on the rules page. 
 
</alert-element>

## Rule criteria 

For any WAAP rule, it’s important to define the criteria that will put that rule into action. You can create WAAP rules based on a variety of conditions: 

* Origin of the IP or IP range.  

* Country or geographical location of the request. 

* Length of a specified part of the request, such as query string. 

* Strings that appear in the request. For example, values that appear in the user-agent header or text strings from the query string. 

* Specific <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/tag-rules/predefined-tags" target="_blank">tags</a>.  

* SQL code that’s likely to be malicious and used to extract data from your database, also known as SQL injection. 

* Requests with potentially malicious scripts that can exploit vulnerabilities in web applications. This is known as cross-site scripting (XSS). 

* Some rule types take sets of criteria. For example, you can specify up to 10,000 IP addresses or IP address ranges in an IP address rule.