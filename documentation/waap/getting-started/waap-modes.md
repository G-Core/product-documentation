---
title: waap-modes
displayName: WAAP modes
published: true
order: 20
toc:
   --1--Monitor mode: "monitor-mode"
   --1--Protect mode: "protect-mode"
   --1--How requests are processed in each mode: "how-requests-are-processed-in-each-waap-mode"
   --1--Enable a WAAP mode for your domain: "enable-a-waap-mode-for-your-domain" 
pageTitle: Learn about WAAP monitor and protect modes | Gcore
pageDescription: Learn how to enable monitor and protect modes for your domain.
---
# WAAP modes

In Gcore WAAP, you can use two modes: monitor and protect.  

Each mode defines how the system will manage incoming traffic to your domain: log information about every request without taking action or challenge and block all malicious requests. 

## Monitor mode

<alert-element type="info" title="Info">
 
L7 DDoS protection is always active even when the WAAP is in monitor mode.

</alert-element>

In monitor mode, WAAP analyzes incoming traffic and logs any security violations or suspicious activity without blocking or modifying requests. Basically, WAAP works exactly like in protection mode, but it doesn't enforce any actions on requests.  

Monitor mode is useful for observing, fine-tuning, and assessing your WAAP’s configuration before you switch to the protect mode.  

<alert-element type="tip" title="Tip">
 
We recommend using monitor mode before switching to protection to verify that WAAP is set correctly and doesn't block legitimate traffic.
When you first add your domain to WAAP, it’s best to use the monitor mode for several days to make sure that all security settings work as expected. 

</alert-element>

## Protect mode 

In this mode, WAAP actively enforces all security settings, including <a href="https://gcore.com/docs/waap/waap-policies" target="_blank">WAAP policies</a> and <a href="https://gcore.com/docs/waap/waap-rules" target="_blank">rules</a>, and challenges or blocks incoming requests that violate these rules or pose a security risk.  

Protect mode ensures real-time defense against web-based attacks like SQL injection, cross-site scripting (XSS), and other common vulnerabilities. 

## How requests are processed in each WAAP mode

To demonstrate the difference between the monitor and protect modes, let’s consider an example of a cURL request with no header modification flags, which triggers the "Invalid user agent" policy. 

If WAAP is in monitor mode, then the request will receive the “200 OK” status code: 

```

curl -I https://c8k3p3x4.cdn.gcore.com 

 HTTP/2 200 

 date: Mon, 25 Mar 2019 20:40:37 GMT 
``` 

If WAAP is in protect mode, the request will receive the “403 Forbidden” status code: 

```
curl -I https://c8k3p3x4.cdn.gcore.com 

 HTTP/2 403  

 date: Mon, 25 Mar 2019 20:38:48 GMT 
```

You can also see the difference on the **Analytics** page in the **Requests** table:  

* In monitor mode, the cURL request will be marked as **Suppressed**. All requests with this result would have been blocked in protect mode. 

* In protect mode, the cURL request will be marked as **Blocked**. 

<img src="https://assets.gcore.pro/docs/waap/getting-started/waf-requests.png" alt="WAF graph on the Analytics page in the Customer Portal">

## Enable a WAAP mode for your domain 

You can switch between monitor and protect modes depending on your security requirements and the level of risk tolerance for your web applications. 

Here’s an example of how to enable protect mode for your domain:  

1\. In the Gcore Customer Portal, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/getting-started/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain for which you want to enable a WAAP mode and click the domain name to open it.

3\. Open the **WAAP** page.

4\. In the upper-right corner of the screen, next to the WAAP mode, select **Protect** from the dropdown.

<img src="https://assets.gcore.pro/docs/waap/getting-started/protect-mode.png" alt="Domains page in the Customer Portal">
