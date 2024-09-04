---
title: waap-modes
displayName: WAAP modes
published: true
order: 20
toc:
   --1--Monitor mode: "monitor-mode"
   --1--Protect mode: "protect-mode"
   --1--How requests are processed in each mode: "how-requests-are-processed-in-each-mode"
   --1--Enable a WAAP mode for your domain: "enable-a-waap-mode-for-your-domain" 
pageTitle: Learn about WAAP monitor and protect modes | Gcore
pageDescription: Learn how to enable monitor and protect modes for your domain.
---
# WAAP modes

In Gcore WAAP, you can use two modes: monitor and protect.  

Each mode defines how the system will manage incoming traffic to your domain: log information about every request without taking action or challenge and block all malicious requests. 

## Monitor mode

<alert-element type="info" title="Info">
 
<a href="https://gcore.com/docs/waap/ddos-protection" target="_blank">L7 DDoS protection</a> is always active even when WAAP is in monitor mode.

</alert-element>

In monitor mode, WAAP analyzes incoming traffic and logs any security violations or suspicious activity without blocking or modifying requests. Basically, WAAP works exactly like in protection mode, but it doesn't enforce any actions on requests.  

Monitor mode is useful for observing, fine-tuning, and assessing your WAAP’s configuration before you switch to the protect mode. While the system only monitors incoming requests, you can observe WAAP’s behavior, understand traffic patterns, and check for any false positives, opmitizing your security settings accordingly.  

This gives you confidence that WAAP will work correctly and efficiently in the protect mode.  

<alert-element type="tip" title="Tip">
 
We recommend using monitor mode before switching to protect to verify that WAAP is set correctly and doesn't block legitimate traffic.
When you first add your domain to WAAP, it’s best to use the monitor mode for several days to make sure that all security settings work as expected. 

</alert-element>

## Protect mode 

In this mode, WAAP actively enforces all security settings, including <a href="https://gcore.com/docs/waap/waap-policies" target="_blank">WAAP policies</a> and <a href="https://gcore.com/docs/waap/waap-rules" target="_blank">rules</a>. It challenges or blocks incoming requests that violate these rules or pose a security risk.  

Protect mode ensures real-time defense against web-based attacks like SQL injection, cross-site scripting (XSS), and other common vulnerabilities. 

## How requests are processed in each mode

To demonstrate the difference between the monitor and protect modes, let’s consider an example of a cURL request with no header modification flags, which triggers the <a href="https://gcore.com/docs/waap/waap-policies/protocol-validation#invalid-user-agent-and-unknown-user-agent" target="_blank">Invalid user agent</a> policy. 

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

You can also see the difference on the **Analytics** page in the <a href="https://gcore.com/docs/waap/analytics#requests-table" target="_blank">Requests table</a>:  

* In monitor mode, the cURL request will be marked as **Suppressed**. All requests with this result would have been blocked in protect mode. 

* In protect mode, the cURL request will be marked as **Blocked**. 

<img src="https://assets.gcore.pro/docs/waap/getting-started/waap-requests-blocked.png" alt="WAAP graph on the Analytics page in the Customer Portal">

## Enable a WAAP mode for your domain 

You can switch between monitor and protect modes depending on your security requirements and the level of risk tolerance for your web applications. 

<alert-element type="warning" title="Warning">

If your domain is in monitor mode, all traffic is allowed to your domain, regardless of configured security rules and policy groups. This mode is only recommended for testing WAAP settings. 

</alert-element>

Here’s an example of how to enable protect mode for your domain:  

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/getting-started/domains-waap-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain for which you want to enable a WAAP mode and click the domain name to open it. You'll be directed to the **Policies** page.

3\. In the upper-right corner of the screen, next to the WAAP mode, select **Protect** from the dropdown.

<img src="https://assets.gcore.pro/docs/waap/getting-started/protect-mode.png" alt="Domains page in the Customer Portal">
