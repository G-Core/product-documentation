---
title: response-pages
displayName: Response pages
published: true
order: 
pageTitle: A guide on Response pages | Gcore
pageDescription: Learn more about Gcore Response pages.
---
# Response pages

When WAAP detects suspicious or malicious traffic to your domain, it presents clients with a challenge or block page. Challenge pages are displayed as a response to suspicious activity, while block pages are presented as a response to detected malicious activity. 

Both page types can be triggered by <a href="https://gcore.com/docs/waap/waap-policies" target="_blank">WAAP policies</a> or by <a href="https://gcore.com/docs/waap/waap-rules" target="_blank">custom rules</a>. For example, when the system suspects that the traffic is coming from an automated bot rather than a human user, it will present the client with a browser validation or captcha page.  

If WAAP detects an SQL injection attempt, it will present a client with a block page. 

## Types of response pages 

The following pages can be displayed to users who demonstrate suspicious activity: 

* Browser validation 
* Enable cookies 
* Enable JavaScript  
* Captcha 
* Block 
* Block CSRF 

You can customize these pages by adding extra information or applying your corporate branding. To do so, follow the instructions for <a href="" target="_blank">creating and updating response pages</a>. 

<alert-element type="tip" title="Tip">
 
To learn about the security challenges that may cause your visitors to see response pages, see Troubleshoot Blocked Users.
 
</alert-element>

## Order of displaying WAAP response pages 

WAAP serves the relevant challenge or block pages according to their priority—a page with the highest priority always takes precedence. This ensures that the most restrictive actions are enforced first. 

<table>
<thead>
<tr>
    <th style="text-align: left;">Page</th>
    <th style="text-align: left;">Priority</th>
    <th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr style="text-align: left;"> 
    <td>Block</td>
    <td>First</td>
    <td>It has the highest priority due to the high risk associated with a request.<br><br>When a block rule is triggered, the request is immediately blocked, and a block page is displayed. 
    </td>
</tr>
<tr style="text-align: left;"> 
    <td>Block CSRF</td>
    <td>First</td>
    <td>This page has the same priority as the block page. The only difference is that it’s tailored specifically to Cross-Site Request Forgery (CSRF) attacks.</td>
</tr>
<tr style="text-align: left;"> 
    <td>Captcha</td>
    <td>Second</td>
    <td>If the system suspects that the traffic comes from an automated user, it presents a CAPTCHA challenge. If the user passes the challenge, they are allowed to access the domain.<br><br>
    Typically, the system does browser validation before presenting users with the captcha page.</td>
</tr>
<tr style="text-align: left;"> 
    <td>Browser validation</td>
    <td>Third</td>
    <td>Typically, this page is not visible to users and appears for less than a second. It is used to validate browser JavaScript and cookies support.</td>
</tr>
<tr style="text-align: left;"> 
    <td>Enable Cookies<br><br>Enable JavaScript</td>
    <td>N/A</td>
    <td>These pages appear as part of the browser validation mechanism.<br><br>
    If cookies or JavaScript are disabled in a user’s browser, the corresponding page will appear to inform the user how to enable the required functionality.</td>
</tr>
</tbody>
</table>

Each response page, regardless of its type, contains the following information displayed to users:  

* **Reference ID**: This ID is unique to each chain of requests that triggered a particular policy or custom rule.  

* **IP address**: IP address of the client that made the request. 

* **Date and time**: A date and time when the request was made. 

<alert-element type="tip" title="Tip">
 
This information can be useful for diagnostic purposes and troubleshooting. If you encounter issues with a specific page and require assistance from our support team, we recommend providing these details in your support request. 
 
</alert-element>

## Browser validation page 

Browser validation mechanism is used to detect if a request is made by a browser that can run JavaScript and support cookies. 

When a request is subject to browser validation, a user will be presented with the browser validation page. They don’t need to  erform any action, and the page will be displayed for less than a second.  

If the challenge is failed, either the “enable cookies” or “enable JavaScript” page will be displayed to the client. A similar page may also appear when the domain is under a DDoS attack. 

## Enable Cookies page 

This page is displayed when a user has disabled cookies in their browser. The user will need to enable cookies to access the domain. 

Here is an example of the enable cookies page: 

<img src="https://assets.gcore.pro/docs/waap/response-pages/enable-cookies.png" alt="Enable cookies response page" width="80%">

## Enable JavaScript page 

This page is displayed when a user has disabled JavaScript support in their browser. They will need to enable JavaScript to access the domain. 

Here is an example of the enable JavaScript page: 

<img src="https://assets.gcore.pro/docs/waap/response-pages/enable-js.png" alt="Enable JavaScript response page" width="80%">

## Captcha challenge 

This page is shown to validate that a real person wants to access your site, and it’s not an automated request. A user will need to enter the displayed characters. 

Here’s what the captcha page looks like: 

<img src="https://assets.gcore.pro/docs/waap/response-pages/captcha.png" alt="Captcha response page" width="80%">

Before challenging a client with CAPTCHA, WAAP does the initial browser validation. 

<alert-element type="info" title="Info">
 
On rare occasions, when inspecting traffic on the <a href="https://gcore.com/docs/waap/analytics" target="_blank">Analytics</a> pages, you might see two consecutive CAPTCHA log lines. This happens when CAPTCHA is served without a prior successful browser validation challenge. 

In this case, the Captcha page will generate a browser validation challenge before serving CAPTCHA itself, and both browser validation and captcha will be logged as a captcha event. 
 
</alert-element>

## Block page 

This page appears when the client has received a hard block because the request violates custom rules and policies configured in WAAP. Block pages are used to inform users that their access to the protected domain has been denied. 

Here’s what the Block page looks like: 

<img src="https://assets.gcore.pro/docs/waap/response-pages/block-page.png" alt="Block response page" width="80%">

You can customize this default page to add your branding elements or provide more information about the reason for a block. 

## Block CSRF page 

This page is shown when the system suspects a Cross-site request forgery (CSRF) attack. This type of attack tricks a browser into executing an unwanted action in an application where a user is logged in. A user will be blocked from accessing your domain. 

Here’s what the Block CSRF page looks like: 

<img src="https://assets.gcore.pro/docs/waap/response-pages/block-csrf.png" alt="Block CSRF response page" width="80%">

## DDoS page 

This page is built with minimal resources to keep it lightweight and quick to load. It is displayed when WAAP is mitigating automated traffic during an application layer (L7) DDoS attack on your domain. 

This page has functionality similar to the browser validation page. 