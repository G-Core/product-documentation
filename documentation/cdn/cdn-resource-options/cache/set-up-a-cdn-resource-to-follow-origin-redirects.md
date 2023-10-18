---
title: set-up-a-cdn-resource-to-follow-origin-redirects
displayName: Set a redirect from an origin
published: true
order: 20
toc:
   --1--About Redirection from Origin: "about-redirection-from-origin"
   --1--Configuration: "configuration"
   --2--via the Control panel: "via-the-control-panel"
   --2--via the API: "via-the-api"
   --3--Request properties: "request-properties"
   --3--Example: "example"
pageTitle: Guide to Set Up CDN Origin Redirection | Gcore
pageDescription: Learn how to configure CDN resources to follow origin redirects in two ways—in the control panel and via API.
---
# Set up a CDN resource to follow origin redirects
  
## About Redirection from Origin

The Redirection from Origin option controls whether the CDN follows redirects returned by the origin. By default, this option is disabled, which means that when the origin returns an HTTP 3xx status code, the CDN simply caches and serves this response to the user. If you enable this option, the CDN automatically retrieves the target content from the new location, which is then cached and returned to the user.

**Important:** Setting redirects may cause users to receive an outdated version of the content, so it is recommended that you <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">purge the CDN cache</a> when changes are made.

## Configuration

### Via the Control panel

To configure origin redirection using the control panel:

1\. Go to **CDN** and select the CDN resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/set-up-a-cdn-resource-to-follow-origin-redirects/11761445358353.png" alt="CDN resource">

2\. In the navigation panel, under the **Cache** section, select **Redirection from origin**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/set-up-a-cdn-resource-to-follow-origin-redirects/11761431909649.png" alt="Cache section">

3\. Toggle **Follow redirect from origin** on.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/set-up-a-cdn-resource-to-follow-origin-redirects/11761431981585.png" alt="Follow redirect from origin">

4\. Select one or more status codes in the **Redirect status codes** select box. The options are:

- 301—to follow redirect for status code HTTP 301
- 302—selected by default; follows redirect for status code HTTP 302
- 303—to follow redirect for status code HTTP 303
- 307—to follow redirect for status code HTTP 307
- 308—to follow redirect for status code HTTP 308

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/set-up-a-cdn-resource-to-follow-origin-redirects/11761445403921.png" alt="Redirect status codes">

5\. Click **Save changes**. Allow at least 15 minutes for the changes to take effect.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/set-up-a-cdn-resource-to-follow-origin-redirects/11761432025745.png" alt="Save changes" width="50%">

**Note**: Once saved, we recommend <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">purging the CDN cache</a> to ensure that users receive an updated version of your content.

### Via the API

To configure origin redirection using the API, the request must include the ```follow_origin_redirect``` object. The following is a sample code for the object:

```
"options": {  
    "follow_origin_redirect": {  
       "enabled": true,  
       "codes": [  
          302,  
          308  
        ]  
     }  
  }
```

#### Request properties

The ```follow_origin_redirect``` object passes the following information:

<table>
	<tbody>
		<tr>
			<td style="text-align:center"><b>Property</b></td>
			<td style="text-align:center"><b>Description</b></td>
		</tr>
		<tr>
			<td>enabled</td>
			<td>This property indicates whether to enable Redirection from Origin. <br>Possible values:
<ul> 
<li>true enables the option</li>
<li>false disables the option</li>
</ul>
</td>
		</tr>
		<tr>
			<td>codes</td>
			<td>This property is an array of HTTP status codes that will cause the CDN to follow a redirect. The array must contain a minimum of 1 and a maximum of 5 items. <br>Possible values: 301, 302, 303, 307, 308</td>
		</tr>
	</tbody>
</table>

#### Example

This example shows a <a href="https://api.gcore.com/docs/cdn#tag/Resources/operation/change_cdn_resource" target="_blank">CDN update request</a> that activates the Redirection from Origin and instructs the CDN to follow redirects for status codes *301*, *302*, and *303*.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/set-up-a-cdn-resource-to-follow-origin-redirects/11761432040465.png" alt="CDN update request " width="80%">
