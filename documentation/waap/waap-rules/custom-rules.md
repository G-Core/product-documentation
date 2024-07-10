---
title: custom-rules
displayName: Custom rules
published: true
order:
pageTitle: Learn about Gcore custom rules | Gcore
pageDescription: Learn about Gcore custom rules and how to use them for filtering incoming traffic and blocking malicious requests.
---
# Custom rules

Using custom rules is a great way to ensure a thorough assessment and filtering of web requests. You can control access to specific URLs, limit access to your application, allow or block countries or organizations, and adjust WAAP behavior to a variety use cases.  

<alert-element type="tip" title="Tip">
 
If you only want to create Access control lists (ACL), check our <a href="https://gcore.com/docs/waap/ip-security/allow-and-block-ip-addresses" target="_blank">Allow and block IP addresses</a> guide. 

</alert-element>

You can create the following types of custom rules:  

*  WAF rules. Consist of two key elements: rule type that defines the conditions for matching a rule and an action that will be enforced when the rule is triggered.   

*  Rate limit rules. Allow you to set the limit for the number of requests allowed within a particular time range.  

*  Tag rules. Tags are added to existing rules and function as identifiers for monitoring and analytics purposes. You can also create custom rules based on tags. 

## Actions in custom rules 

Rule actions are triggered based on the conditions you specify. If you create multiple rules with the same conditions, then only the action with the highest priority level will take place. 

For example, you’ve created a rule that allows all requests from 1.1.1.1 to access your application, and then you added another rule to present a CAPTCHA screen to 1.1.1.1. In this situation, only the **Allow** action will be triggered because it has a higher priority level than the CAPTCHA action.  

The following table features all rule actions along with their priority levels. 

<table>
<thead>
  <tr>
    <th style="width:30%"><strong>Action</strong></th>
    <th style="width:55%"><strong>Description</strong></th>
    <th style="width:15%"><strong>Priority level</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>Monitor</td>
   <td>Logs any request that meets the condition of the rule. This action type doesn’t present any challenge to the user.</td>
   <td>First</td>
    </tr>
    <tr>
   <td>Allow</td>
   <td>Allows specified traffic to view the application's content and exclude the user from any security checks.</td>
   <td>Second</td>
    </tr>
    <tr>
   <td>Block</td>
   <td>Blocks specified traffic from accessing the application's content.</td>
   <td>Third</td>
    </tr>
    <tr>
   <td>Captcha</td>
   <td>Displays a CAPTCHA challenge before the user can view the application's content.</td>
   <td>Fourth</td>
    </tr>
    <tr>
   <td>JavaScript validation</td>
   <td>Displays a JavaScript validation challenge before the user can view the application's content.</td>
   <td>Fifth</td>
    </tr>
    <tr>
   <td>Tag</td>
   <td>Tags a request with the custom user-defined tag you specify. This action type doesn’t send any challenge to the user and only adds information to a request.<br><br>
All tag action rules run first before any other action type. They don’t stop the rule engine even after the condition has been met and the tag has been applied.<br>
Thus, the user-defined tags that are generated in this run can be used in the "user-defined tag" condition of the same run (during the same request processing).</td>
   <td>N/A<br> 
   Tags work in parallel—if a request is blocked, it can still be tagged.</td>
    </tr>                                
</tbody>
</table> 

<alert-element type="tip" title="Tip">
 
The **Tag** action doesn’t challenge requests. Thus, it has no assigned priority level.
 
</alert-element>

## Rule conditions 

When <a href="https://gcore.com/docs/waap/waap-rules/custom-rules/create-amd-manage-rules" target="_blank">creating a rule</a>, it’s important to choose a proper type of condition that defines when the rule will be triggered. The following types of custom rule conditions are available:  

<table>
<thead>
  <tr>
    <th style="width:20%"><strong>Condition type</strong></th>
    <th style="width:80%"><strong>Description</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
   <td>IP</td>
   <td>Challenge requests based on a specified IP address. You can also enter multiple IP addresses, separated with commas.<br> 
   You cannot enter a subnet.</td>
    </tr>
    <tr>
   <td>IP range</td>
   <td>Challenge requests based on a specified IP address range.<br>
   For example, if you enter 8.8.8.8 and 10.10.10.10, then every address higher than 8.8.8.8 and every address lower than 10.10.10.10 will trigger the rule.</td>
    </tr>
    <tr>
   <td>URL</td>
   <td>Challenge requests based on a specified URL.<br>
   The expression may start with a slash (/) to represent the path following the hostname in the URL.<br>
   You can create the rule to trigger for:<br><br>
   An exact match, such as "/index.html". In this case, you must start with a slash (/)<br>
   A partial match, such as "index". In this case, any request that contains an "index", such as /index.html, /index.htm, /index.php, will activate the rule.  
   </td>
    </tr>
    <tr>
   <td>User agent</td>
   <td>Challenge requests based on a specified user agent.<br>
   You can create the rule to trigger for:<br><br>
   An exact match that will include a specific user agent. For example, Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko). Chrome/44.0.2403.157 Safari/537.36.<br>
   A partial match that will include a more general user agent type, such as AppleWebKit. In this case, any user agent with AppleWebKit will trigger the rule. 
   </td>
    </tr>
    <tr>
   <td>Header</td>
   <td>Challenge requests based on a specified header.</td>
    </tr>
    <tr>
   <td>Header exists</td>
   <td>Challenge requests depending on whether a specific header NAME is present in the request. For example, if a request doesn't include the 'User-Agent' header name, then such request should be blocked or challenged.</td>
    </tr>
    <tr>
   <td>HTTP method</td> 
   <td>Challenge requests based on a specified HTTP method, such as GET, POST, and others.</td>
    </tr>      
    <tr>
   <td>File extension</td>
   <td>Challenge requests based on a specified file type, such as pdf, jpeg, jfif, and exe.</td>
    </tr>
    <tr>
   <td>Content type</td>
   <td>Challenge requests based on a specified content type, such as application/pdf.</td>
    </tr>
    <tr>
   <td>Country</td>
   <td>Challenge requests based on the country associated with the requesting IP address. This challenge is based on public IP address databases.</td>
    </tr>
    <tr>
   <td>Organization</td>
   <td>Challenge requests based on the organization associated with the requesting IP address. This challenge is based on a public database that contains known ranges relating to organizations.</td>
    </tr>
    <tr>
   <td>Owner types</td>
   <td>Challenge requests based on the category associated with a related IP range. For example, an IP range can be categorized as Commercial, CDN, or related to Hosting Services.</td>
    </tr>
    <tr>
   <td>Session request count</td>
   <td>Challenge requests based on the number of requests made within a session (per session ID).</td>
    </tr>
    <tr>
   <td>Tag</td>
   <td>Sanction requests based on specific pre-defined tags provided by Gcore. View the full list of tags, their API slugs, and their descriptions in our <a href="" target="_blank">dedicated guide</a>.</td>
    </tr>
    <tr>
   <td>User-defined tag</td>
   <td>Sanction requests based on custom-generated tags named "user-defined tags".<br>
   You can create these tags in the Customer Portal or via API. For more details, check out the <a href="" target="_blank">Tag generating rules</a> guide.</td>
    </tr>                                                          
</tbody>
</table>
