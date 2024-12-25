---
title: about-waap
displayName: About WAAP
published: true
order: 10
toc:
   --1--Getting started: "getting-started"
   --1--Difference between WAF and WAAP: "whats-the-difference-between-waf-and-waap"
   --1--How WAAP works: "how-waap-works"
   --2--WAF edge nodes: "waf-edge-nodes"
   --2--Behavioral component: "behavioral-component"
pageTitle: About WAAP | Gcore
pageDescription: Discover Gcore WAAP (Web Application and API Protection) and learn how it works.
---
# About Gcore WAAP

Gcore WAAP (web application and API protection) protects your websites, web applications, and APIs from known vulnerabilities and common exploits by applying predefined security policies, built-in rules, and behavioral analysis to incoming requests. 

WAAP is designed to work out of the box, but it’s also highly customizable: You can create and set up your own rules, adjust policies, and customize WAAP behavior as needed. Our built-in reporting system empowers you to analyze traffic, which helps you better understand how to fine-tune WAAP's protection and adjust custom rules. 

WAAP offers the following key features: 

* Next-gen WAF
* API discovery and protection 
* L7 DDoS protection
* Bot protection and auti-automation
* AI intelligence
* OWASP Top 10 protection
* Robust security policies  
* Security insights 
* Real-time analytics

## Getting started 

For instructions on how to protect your domain with our WAAP, refer to our guide on <a href="https://gcore.com/docs/waap/getting-started/configure-waap-for-a-domain" target="_blank">how to configure WAAP for a domain</a>. 

## What’s the difference between WAF and WAAP? 

Web application firewalls (WAFs) filter HTTP traffic to shield web applications from common threats like SQL injection and cross-site scripting. However, as applications increasingly depend on APIs and face sophisticated threats like bot attacks and Layer 7 DDoS, traditional WAFs fall short in providing comprehensive protection. Read more about why WAF isn't enough for today's security landscape in [our dedicated article](https://gcore.com/blog/cybersecurity-beyond-waf/).


A web application and API protection (WAAP) solution expands on WAF functionality, integrating advanced defenses such as API-specific security, behavioral analysis, and Layer 7 mitigation to safeguard modern applications and APIs against evolving cyber threats.

A **WAF** sits between the client and the origin server, meaning that any request a client makes passes through the WAF for an "inspection" before arriving at its destination, the website's origin server. 

A **WAAP** (Web Application and API Protection) is a security tool that offers WAF protection along with more advanced measures to protect web applications and APIs from cyberattacks. 

## How WAAP works 

Our cloud-based, next-generation WAF uses a two-part system to inspect incoming traffic: 

* **WAF edge nodes** that perform actions against requests. 

* **Behavioral component** that runs heuristics and ML models and performs behavioral analytics. 

WAF edge nodes and behavioral components work together to provide protection against common vulnerabilities such as L7 DDoS attacks, OWASP Top 10 threats, bots, and more. 

### WAF edge nodes 

These nodes are responsible for running <a href="https://gcore.com/docs/waap/waap-policies" target="_blank">WAAP policies</a> against requests. They also enforce actions on requests (block, allow, Captcha, JavaScript validation, or tag) based on the recommendation provided by the second part, the behavioral component.  

The existence of nodes that run policies against traffic is what essentially defines a typical first-gen WAF.  

<alert-element type="tip" title="Tip">
 
The <a href="https://gcore.com/docs/waap/waap-policies" target="_blank">WAAP policies</a> section covers existing policy groups in detail. 

You can also create your own <a href="https://gcore.com/docs/waap/waap-rules/custom-rules" target="_blank">custom rules</a> to filter traffic as you see fit. 
 
</alert-element>

### Behavioral component 

The behavioral component is responsible for asynchronously analyzing traffic from WAF Edge nodes. It is centralized and built on a scalable cloud environment, ensuring that WAF always has sufficient resources for deep analysis without memory or processing limitations.   

The component analyzes and detects malicious behavioral patterns and, based on this information, indicates what actions should be enforced by WAF edge nodes: block, challenge, or allow requests. As the behavioral component processes requests, it generates information tags for each request entity. These tags are sent together with instructions (actions to be enforced) to WAF Edge nodes. 

This system's advanced analytical capabilities, combined with the independent yet collaborative operation of its two components, transform our WAF into a next-generation solution.
