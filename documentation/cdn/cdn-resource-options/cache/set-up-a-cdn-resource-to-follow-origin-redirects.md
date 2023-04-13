---
title: set-up-a-cdn-resource-to-follow-origin-redirects
displayName: Set a redirect from an origin
published: true
order: 20
toc:
   --1--About Redirection from Origin: "about-redirection-from-origin"
   --1--Configuration: "configuration"
   --2--via the control panel: "via-the-control-panel"
   --2--via the API: "via-the-api"
---
  
  
  

About Redirection from Origin
-----------------------------

The Redirection from Origin option controls whether the CDN follows redirects returned by the origin. By default, this option is disabled, which means that when the origin returns an HTTP 3xx status code, the CDN simply caches and serves this response to the user. If you enable this option, the CDN automatically retrieves the target content from the new location, which is then cached and returned to the user.

**Important:** Setting redirects may cause users to receive an outdated version of the content, so it is recommended that you [purge the CDN cache](https://www.gcore.com/support/articles/214532065/) when changes are made.

Configuration
-------------

### Via the control panel

To configure origin redirection using the control panel:

1. Go to **CDN** and select the CDN resource you want to configure.

<img src="https://support.gcore.com/hc/article_attachments/11761445358353" alt="image1.png">

2. In the navigation panel, under the **Cache** section, select **Redirection from origin**.

<img src="https://support.gcore.com/hc/article_attachments/11761431909649" alt="image2.png">

3. Toggle **Follow redirect from origin** on.

<img src="https://support.gcore.com/hc/article_attachments/11761431981585" alt="image3.png">

4. Select one or more status codes in the **Redirect status codes** select box. The options are:

*   301—to follow redirect for status code HTTP 301
*   302—selected by default; follows redirect for status code HTTP 302
*   303—to follow redirect for status code HTTP 303
*   307—to follow redirect for status code HTTP 307
*   308—to follow redirect for status code HTTP 308

<img src="https://support.gcore.com/hc/article_attachments/11761445403921" alt="image4.png">

5. Click **Save changes**. Allow at least 15 minutes for the changes to take effect.

<img src="https://support.gcore.com/hc/article_attachments/11761432025745" alt="image5.png" width="669" height="65">

**Important:** Once saved, we recommend <a>purging the CDN cache](https://www.gcore.com/support/articles/214532065/) to ensure that users receive an updated version of your content.

### Via the API

To configure origin redirection using the API, the request must include the follow\_origin\_redirect object. The following is a sample code for the object:

"options": {  
    "follow\_origin\_redirect": {  
       "enabled": _true_,  
       "codes": \[  
          _302_,  
          _308_  
        \]  
     }  
  }

#### Request properties

The _follow\_origin\_redirect_ object passes the following information:

| Property | Description                                                                                                                                                                                             |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| enabled | This property indicates whether to enable Redirection from Origin.<br/>Possible values:<br/>true enables the option<br/>false disables the option<br/>                                                       |
| codes | This property is an array of HTTP status codes that will cause the CDN to follow a redirect. The array must contain a minimum of 1 and a maximum of 5 items.<br/>Possible values:<br/>301<br/>302<br/>303<br/>307<br/>308 |


#### Example

This example shows a [CDN update](https://apidocs.gcore.com/cdn#tag/Resources/operation/change_cdn_resource) request that activates the Redirection from Origin and instructs the CDN to follow redirects for status codes 301, 302, and 303.

<img src="https://support.gcore.com/hc/article_attachments/11761432040465" alt="image6.png">
