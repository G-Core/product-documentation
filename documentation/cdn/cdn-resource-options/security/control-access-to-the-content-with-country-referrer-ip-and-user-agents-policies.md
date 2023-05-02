---
title: control-access-to-the-content-with-country-referrer-ip-and-user-agents-policies
displayName: Manage access policies
published: true
order: 10
toc:
   --1--Referrer Access Policy: "referrer-access-policy"
   --2--Allow Policy: "allow-referrer-policy"
   --2--Block Policy: "block-referrer-policy"
   --1--Country Access Policy: "country-access-policy"
   --2--Country Allow Policy: "allow-country-access-policy"
   --2--Country Block Policy: "block-country-access-policy"
   --1--IP Access Policy: "ip-access-policy"
   --2--IP Allow Policy: "allow-ip-policy"
   --2--IP Block Policy: "block-ip-policy"
   --1--User Agent Access Policy: "user-agent-access-policy"
   --2--Set via the control panel: "set-via-the-control-panel"
   --2--Set via the API: "set-via-the-api"
   --3--Request properties: "request-properties"
   --3--Example: "example"
---
# Control access to the content with Country, Referrer, IP, and User agents policies
  
## Referrer Access Policy

Referer Access Policy is a restriction to publish the links to content on your site on other sites. To enable the option navigate to CDN Resources, click Settings of the Resource, choose the Advanced Settings tab, in the Access (Security) click Add Policy and find Referer Access Policy. 

By default, there are no restrictions by referer to your CDN Resource. You can set up Allow or Block Policy.

### Allow Referrer Policy

<img src="https://support.gcore.com/hc/article_attachments/13340190513425" alt="" width="70%">

Specify domains to which you would like to block access.

- ```www.domain.com``` if you want to block access to the specific domain
- ```*.domain.com```  if you want to block access to all subdomains of domain.com

When users request data from specified domains, they will get the denial of access.

### Block Referrer Policy

<img src="https://support.gcore.com/hc/article_attachments/13340191722129" alt="" width="70%">

Specify the domains which you would like to allow access to.

- ```www.domain.com``` if you want to allow access to the specific domain
- ```*.domain.com``` if you want to allow access to all subdomains of domain.com

When a user requests data from other domains, they will get the denial of access.

You can specify domains only one by one via Control Panel. To add the list of the domains use <a href="https://apidocs.gcore.com/cdn" target="_blank">API</a>.

## Country Access Policy

You can limit access to your content for listed countries. To enable the option navigate to CDN Resources, click Settings, open the Advanced Settings, in the Access (Security) click Add Policy and find Country Access Policy. 

By default, there are no restrictions by country to your CDN Resource. You can set up Allow or Block policy.  

**Note**: You can specify countries only one by one via Control Panel. To add the list of the countries, use <a href="https://apidocs.gcore.com/cdn" target="_blank">API</a>.  
  
### Allow Country Access Policy

Access to the Resource is allowed for all the countries except for the specified in the field.

<img src="https://support.gcore.com/hc/article_attachments/115011428285/Screenshot-2018-1-3_G-Core_Labs_Resources_Settings_1_.png" alt="" width="70%">

### Block Country Access Policy

Access to the Resource is denied for all the countries except for the specified in the field.

<img src="https://support.gcore.com/hc/article_attachments/115011428325/Screenshot-2018-1-3_G-Core_Labs_Resources_Settings_2_.png" alt="" width="70%">

## IP Access Policy

You can limit access to your content to IP ranges.

In CDN Resource settings choose Show Advanced Settings, in the Access (Security) click Add Policy and find IP Access Policy. 

By default, there are no restrictions by IP to your CDN Resource. You can set up Allow or Block policy.

The option supports IPv4 and IPv6 addresses.

You can specify IPs only one by one via Control Panel. To add the list of the IPs use <a href="https://apidocs.gcore.com/cdn" target="_blank">API</a>.

### Allow IP Policy

Access to the resource is allowed for all the IPs except for the specified in the field.

<img src="https://support.gcore.com/hc/article_attachments/360016099617/____________eng.png" alt="" width="70%">

### Block IP Policy

Access to the resource is denied for all the IPs except for the specified in the field.

<img src="https://support.gcore.com/hc/article_attachments/360016172698/____________eng.png" alt="" width="70%">

## User Agent Access Policy

You can limit access to your CDN content for User Agents, for example, for certain browsers, consoles or some other devices.

In CDN Resource settings choose Show Advanced Settings, find Access (Security), click Add Policy and find User Agents Policy. 

By default access to the Resource is allowed for all the kinds of User Agents. You can set up the Allow or Block policy.   

### Set via the Control panel

To set the user agents using the control panel:

1\. Go to CDN and select the CDN resource you want to configure.

<img src="https://support.gcore.com/hc/article_attachments/11759524174225" alt="">

2\. In the navigation panel, under the "Access" section, select **User agents policy**.

<img src="https://support.gcore.com/hc/article_attachments/11759524173201" alt="">

3\. Toggle "Enable user agents policy" and choose either the **Allow by default** or **Block by default** option:

- Selecting **Allow by default** allows access for all user agents except those specified.
- Choosing **Block by default** blocks access for all user agents except those specified.

<img src="https://support.gcore.com/hc/article_attachments/11759511525777" alt="">

4\. Set one or more user agents in the **User-Agent** select box. Accepted values are:

- **Empty value.** This appears as an option in the select box. Select this value to allow or block incoming requests that do not have a User-Agent header.

<img src="https://support.gcore.com/hc/article_attachments/11759524278033" alt="" width="70%">

- **User agent string.** Enter one or more unique user agents. The maximum length of each string is 255 characters. If you need to increase this limit, you can contact our [support team](mailto:support@gcore.com).

<img src="https://support.gcore.com/hc/article_attachments/11759524358289" alt="" width="70%">

**Note**: **User-Agent** text box cannot be left blank.

5\. Click **Save changes**. Allow at least 15 minutes for the changes to take effect.

<img src="https://support.gcore.com/hc/article_attachments/11759524347409" alt="" width="50%">

### Set via the API

To set the user agents using the API, the request must include the ```user_agent_acl``` object. The following is a sample code for the object:

```
"options": {  
    "user_agent_acl": {  
       "enabled": true,  
       "policy_type": "allow",  
       "excepted_values": [  
          "",  
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"  
      ]  
   }  
}
```

#### Request properties

The ```user_agent_acl``` object passes the following information:

<table>
<tbody>
<tr>
<td><b>Property</b></td>
<td><b>Description</b></td>
</tr>
<tr>
<td><i>enabled</i></td>
<td>This property indicates whether to enable the User Agents Policy.
Possible values:
<ul>
<li>true enables the option</li>
<li>false disables the option</li>
</ul>
</td>
</tr>
<tr>
<td><i>policy_type</i></td>
<td>This property indicates the action to apply to the matching request. Possible values:
<ul>
<li>allow allows the request</li>
<li>deny blocks the request</li>
</ul>
</td>
</tr>
<tr>
<td><i>excepted_values</i></td>
<td>This property is an array of user agents to allow or block. The array must contain at least 1 item.
Possible values:
<ul>
<li>two double quotation marks without a space in-between ("") represents the <i>empty value</i></li>
<li>a string that represents the user agent, with a maximum length of 255 characters; if you need to increase this limit, you can contact our <a href="mailto:support@gcore.com">support team</a></li>
<ul>
</td>
</tr>
</tbody>
</table>

#### Example

This example shows a <a href="https://apidocs.gcore.com/cdn" target="_blank">CDN update</a> request that activates the User Agents Policy and blocks the requests without a User-Agent header.

<img src="https://support.gcore.com/hc/article_attachments/11759524427921" alt="" width="70%">
