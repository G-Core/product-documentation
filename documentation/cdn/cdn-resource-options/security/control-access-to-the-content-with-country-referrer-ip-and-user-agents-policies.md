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
  
## Referrer Access Policy

Referer Access Policy is a restriction to publish the links to content on your site on other sites. To enable the option navigate to CDN Resources, click Settings of the Resource, choose the Advanced Settings tab, in the Access (Security) click Add Policy and find Referer Access Policy. 

By default, there are no restrictions by referer to your CDN Resource. You can set up Allow or Block Policy.

### Allow Referrer Policy

<img src="https://support.gcore.com/hc/article_attachments/13340190513425" alt="mceclip0.png">

Specify domains to which you would like to block access.

*   www.domain.com if you want to block access to the specific domain
*   \*.domain.com  if you want to block access to all subdomains of domain.com

When users request data from specified domains, they will get the denial of access.

### Block Referrer Policy

<img src="https://support.gcore.com/hc/article_attachments/13340191722129" alt="mceclip1.png">

Specify the domains which you would like to allow access to.

*   www.domain.com if you want to allow access to the specific domain
*   \*.domain.com  if you want to allow access to all subdomains of domain.com

When a user requests data from other domains, they will get the denial of access.

You can specify domains only one by one via Control Panel. To add the list of the domains use [API](https://apidocs.gcore.com/).

## Country Access Policy

You can limit access to your content for listed countries. To enable the option navigate to CDN Resources, click Settings, open the Advanced Settings, in the Access (Security) click Add Policy and find Country Access Policy. 

By default, there are no restrictions by country to your CDN Resource. You can set up Allow or Block policy.  
**Important!** You can specify countries only one by one via Control Panel. To add the list of the countries, use [API](https://apidocs.gcore.com/cdn).  
  
### Allow Country Access Policy

Access to the Resource is allowed for all the countries except for the specified in the field.

<img src="https://support.gcore.com/hc/article_attachments/115011428285/Screenshot-2018-1-3_G-Core_Labs_Resources_Settings_1_.png" alt="Screenshot-2018-1-3_G-Core_Labs_Resources_Settings_1_.png">

### Block Country Access Policy

Access to the Resource is denied for all the countries except for the specified in the field.

<img src="https://support.gcore.com/hc/article_attachments/115011428325/Screenshot-2018-1-3_G-Core_Labs_Resources_Settings_2_.png" alt="Screenshot-2018-1-3_G-Core_Labs_Resources_Settings_2_.png">

## IP Access Policy

You can limit access to your content to IP ranges.

In CDN Resource settings choose Show Advanced Settings, in the Access (Security) click Add Policy and find IP Access Policy. 

By default, there are no restrictions by IP to your CDN Resource. You can set up Allow or Block policy.

The option supports IPv4 and IPv6 addresses.

You can specify IPs only one by one via Control Panel. To add the list of the IPs use [API](https://apidocs.gcore.com/cdn).

  
### Allow IP Policy

Access to the resource is allowed for all the IPs except for the specified in the field.

<img src="https://support.gcore.com/hc/article_attachments/360016099617/____________eng.png" alt="____________eng.png">

### Block IP Policy

Access to the resource is denied for all the IPs except for the specified in the field.

<img src="https://support.gcore.com/hc/article_attachments/360016172698/____________eng.png" alt="____________eng.png">

## User Agent Access Policy

You can limit access to your CDN content for User Agents, for example, for certain browsers, consoles or some other devices.

In CDN Resource settings choose Show Advanced Settings, find Access (Security), click Add Policy and find User Agents Policy. 

By default access to the Resource is allowed for all the kinds of User Agents. You can set up the Allow or Block policy.  
  

### Set via the control panel

To set the user agents using the control panel:

1. Go to **CDN** and select the CDN resource you want to configure.

<img src="https://support.gcore.com/hc/article_attachments/11759524174225" alt="image1.png">

2. In the navigation panel, under the **Access** section, select **User agents policy**.

<img src="https://support.gcore.com/hc/article_attachments/11759524173201" alt="image2.png">

3. Toggle **Enable user agents policy** and choose either the **Allow by default** or **Block by default** option:

*   Selecting **Allow by default** allows access for all user agents except those specified.
*   Choosing **Block by default** blocks access for all user agents except those specified.

<img src="https://support.gcore.com/hc/article_attachments/11759511525777" alt="image3.png">

4. Set one or more user agents in the **User-Agent** select box. Accepted values are:

*   **Empty value.** This appears as an option in the select box. Select this value to allow or block incoming requests that do not have a User-Agent header.

<img src="https://support.gcore.com/hc/article_attachments/11759524278033" alt="" width="555" height="231">

*   **User agent string.** Enter one or more unique user agents. The maximum length of each string is 255 characters. If you need to increase this limit, you can contact our [support team](mailto:support@gcore.com).

<img src="https://support.gcore.com/hc/article_attachments/11759524358289" alt="" width="556" height="270">

**Note:** **User-Agent** text box cannot be left blank.

5. Click **Save changes**. Allow at least 15 minutes for the changes to take effect.

<img src="https://support.gcore.com/hc/article_attachments/11759524347409" alt="" width="661" height="60">

### Set via the API

To set the user agents using the API, the request must include the _user\_agent\_acl_ object. The following is a sample code for the object:

"options": {  
    "user\_agent\_acl": {  
       "enabled": true,  
       "policy\_type": "allow",  
       "excepted\_values": \[  
          "",  
          "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"  
      \]  
   }  
}

#### Request properties

The _user\_agent\_acl_ object passes the following information:

| Property        | Description                                                                                                                                                                                                                                                                                                                                                             |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| enabled         | This property indicates whether to enable the User Agents Policy.<br/>Possible values:<br/>true enables the option<br/>false disables the option<br/>                                                                                                                                                                                                                      |
| policy_type     | This property indicates the action to apply to the matching request.<br/>Possible values:<br/>nallow allows the request<br/>deny blocks the request<br/>                                                                                                                                                                                                                       |
| excepted_values | This property is an array of user agents to allow or block. The array must contain at least 1 item.<br/>Possible values:<br/>two double quotation marks without a space in-between (\"\") represents the empty value\n\na string that represents the user agent, with a maximum length of 255 characters; if you need to increase this limit, you can contact our support team |


Possible values:

*   _allow_ allows the request
*   _deny_ blocks the request

_excepted\_values_

This property is an array of user agents to allow or block. The array must contain at least 1 item.

Possible values:

*   two double quotation marks without a space in-between (_""_) represents the _empty value_
*   a string that represents the user agent, with a maximum length of 255 characters; if you need to increase this limit, you can contact our [support team](mailto:support@gcore.com)

#### Example

This example shows a [CDN update](https://apidocs.gcore.com/cdn) request that activates the User Agents Policy and blocks the requests without a User-Agent header.

<img src="https://support.gcore.com/hc/article_attachments/11759524427921" alt="image7.png">
