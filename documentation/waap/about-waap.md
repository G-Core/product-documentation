---
title: about-waap
displayName: About WAAP
published: true
order: 10
toc:
pageTitle: About WAAP | Gcore
pageDescription: Learn more about Gcore Web Application and API Protection and available security features.
---
# About Gcore WAAP

Gcore’s WAAP protects your websites, web applications, and APIs from known vulnerabilities and common exploits by applying predefined security policies, built-in rules, and behavioral analysis to incoming requests. 

WAAP is designed to work out of the box, but it’s also highly customizable: you can create and setup your own rules, adjust policies, and customize WAF behavior as needed. 

You can further analyze this traffic through our built-in reporting system, which helps you better understand how to fine-tune WAF's behavior and adjust rules. 

WAAP offers you such key features as: 

* Next-gen WAF 
* OWASP Top 10 protection and a set of robust security policies  
* Security insights 
* Real-time analytics 
* API discovery and protection 
* L7 DDoS protection 
* Bot protection 

## Getting started 

For instructions on how to protect your domain with our WAAP, check out our guide on <a href="https://gcore.com/docs/waap/getting-started-configure-waap-for-a-domain" target="_blank">setting up WAAP for a new domain</a>. 

## What’s the difference between WAF and WAAP? 

Traditional firewalls typically serve as the first line of defense against malicious visitors and focus on the layer 3 (Network) and layer 4 (Transport) in the <a href="https://osi-model.com/" target="_blank">OSI model</a>. This means that they can’t interpret and process HTTP and HTTPS traffic, which is the type of traffic making requests to your web applications. 

To protect your web applications and APIs, you need to use a web application firewall (WAF). It’s designed to filter out the "good" and "bad" HTTP and HTTPS traffic at the Application layer (Layer 7) in the OSI model. 

A **WAF** sits between the client and the origin server, meaning that any request a client makes passes through the WAF for an "inspection" before arriving at its destination, the website's origin server. 

A **WAAP** (Web Application and API Protection) is a security tool that offers basic WAF protection along with more advanced measures aimed to protect your web applications and APIs from cyberattacks. 

As the malicious web attacks continue to evolve and become more sophisticated, our WAAP will continue to undergo upgrades and maintenance needed to keep our platform up-to-date and effective against these attacks. 

## How WAAP works 

Our cloud-based next-generation WAF uses a two-part system to inspect incoming traffic: 

* **WAF Edge nodes** that perform actions against requests. 

* **Cloud intelligence component** that runs heuristics and ML models and performs behavioral analytics. 

WAF edge nodes and behavioral components work together to provide protection against common vulnerabilities such as L7 DDoS attacks, <a href="" target="_blank">OWASP Top 10 threats</a>, bots, and more. 

### WAF Edge nodes 

These nodes are responsible for running rule sets (also know as <a href="https://gcore.com/docs/waap/waf-policies" target="_blank">WAF policies</a>) against requests. They also enforce actions on requests (block, allow, or monitor) based on the recommendation provided by the second part, the behavioral component.  

The existence of nodes that run rule sets against traffic is what essentially defines a typical first-gen WAF.  

<alert-element type="tip" title="Tip">
 
The <a href="https://gcore.com/docs/waap/waf-policies" target="_blank">WAF policies</a> section covers existing rule sets in detail. You can also create your own <a href="https://gcore.com/docs/waap/waf-rules/custom-rules" target="_blank">custom rules</a> to filter traffic as you see fit. 
 
</alert-element>

### Behavioral component 

The behavioral component is centralized and responsible for asynchronously analyzing traffic from WAF Edge nodes. This component then instructs the nodes to either block, allow, or monitor a request.  

This analytical aspect of the system and independent functioning of both parts is what elevates our WAF to the next-generation level.
