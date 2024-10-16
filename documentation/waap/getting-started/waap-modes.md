---
title: waap-modes
displayName: WAAP modes
published: true
order: 20
toc:
   --1--Monitor mode: "monitor-mode"
   --1--Protect mode: "protect-mode"
   --1--Inactive mode: "inactive-mode"
   --1--Stopped mode: "stopped-mode"
   --1--How requests are processed in monitor and protect modes: "how-requests-are-processed-in-monitor-and-protect-modes"
   --1--Enable monitor and protect modes: "enable-monitor-and-protect-modes-for-your-domain"
pageTitle: Learn about WAAP modes | Gcore
pageDescription: Learn how WAAP behaves in monitor, protect, inactive, and stopped modes. Enable monitor and protect modes for a domain.
---
# WAAP modes

Gcore WAAP has four modes: monitor, protect, inactive, and stopped. Each mode defines how the system will manage incoming traffic to your domain.

## Monitor mode

<alert-element type="info" title="Info">
 
<a href="https://gcore.com/docs/waap/ddos-protection" target="_blank">L7 DDoS protection</a> is always active even when WAAP is in monitor mode.

</alert-element>

In monitor mode, WAAP analyzes incoming traffic and logs any security violations or suspicious activity without blocking or modifying requests. Basically, WAAP works exactly like in protection mode, but it doesn't enforce any actions on requests.  

Monitor mode is useful for observing, fine-tuning, and assessing your WAAP’s configuration before you switch to the protect mode. While the system only monitors incoming requests, you can observe WAAP’s behavior, understand traffic patterns, and check for any false positives, optimizing your security settings accordingly.  

This gives you confidence that WAAP will work correctly and efficiently in the protect mode.  

<alert-element type="tip" title="Tip">
 
We recommend using monitor mode before switching to protect to verify that WAAP is set correctly and doesn't block legitimate traffic.
When you first add your domain to WAAP, it’s best to use the monitor mode for several days to make sure that all security settings work as expected. 

</alert-element>

## Protect mode 

In this mode, WAAP actively enforces all security settings, including <a href="https://gcore.com/docs/waap/waap-policies" target="_blank">WAAP policies</a> and <a href="https://gcore.com/docs/waap/waap-rules" target="_blank">rules</a>. It challenges or blocks incoming requests that violate these rules or pose a security risk.  

Protect mode ensures real-time defense against web-based attacks like SQL injection, cross-site scripting (XSS), and other common vulnerabilities. 

## Inactive mode 

In inactive mode, WAAP protection for the domain is disabled, and traffic is not inspected as in monitor mode. All web requests **bypass CDN and WAAP**, going directly to the origin. However, you can still update the domain configuration and security settings. 

<alert-element type="info" title="Info">
 
Inactive domains still incur charges as we retain all configured settings and data. If you want to discontinue billing for WAAP protection, delete a domain. 
 
</alert-element>

If you want to delete a domain, it has to be inactive. To change WAAP mode to inactive, <a href="https://gcore.com/docs/waap/getting-started/manage-domains#disable-waap-protection-for-a-domain" target="_blank">disable WAAP protection for a relevant CDN resource</a>. You can always <a href="https://gcore.com/docs/waap/getting-started/configure-waap-for-a-domain#step-2-enable-waap-in-cdn-resource-settings" target="_blank">enable WAAP</a> again in the resource settings. 

## Stopped mode 

In this mode, traffic is not inspected and WAAP protection for the domain is disabled. Domains in stopped mode aren’t billable. 

WAAP mode can change to **Stopped** for the following reasons: 

* The trial period has ended. 

* Payment for the product was unsuccessful. In this case, you cannot activate any other WAAP mode until payment is completed. 

When the product is in the stopped mode, you can’t create, modify, or edit any WAAP settings.

## How requests are processed in monitor and protect modes

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

## Enable monitor and protect modes for your domain 

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
