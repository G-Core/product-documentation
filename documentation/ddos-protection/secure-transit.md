---
title: secure-transit
displayName: Super Transit
published: true
order: 40
toc:
pageTitle: About Super Transit | Gcore
pageDescription: Learn about Super Transit, a feature that provides advanced DDoS protection and optimizes data flow for improved network performance.
---
# Super Transit

Super Transit is an advanced network traffic management and security solution that optimizes data flow while delivering robust DDoS protection. It goes beyond just defending against DDoS attacks—it intelligently routes legitimate traffic to enhance network performance, minimize latency, and provide seamless data transmission.

## Key benefits

Super Transit has two key benefits:
* **Enhances DDoS Protection:** The feature proactively detects, mitigates, and filters DDoS attacks before they can impact your network. This ensures that malicious traffic is blocked, allowing your services to remain uninterrupted. 
* **Optimizes traffic routing:** Super Transit intelligently enhances network performance by efficiently routing legitimate traffic through the Gcore network, reducing latency and accelerating data delivery. This is crucial for latency-sensitive applications such as online gaming, real-time communications, and high-quality streaming.

## How it works 

Super Transit uses anycast routing and tunneling technologies to filter out malicious traffic while accelerating legitimate requests. Your traffic is processed as follows:
- **Traffic diversion:** Incoming traffic is automatically routed through Gcore’s global anycast network, where it is analyzed in real time.
- **Threat detection and mitigation:** Super Transit identifies and filters DDoS attacks and other malicious activity, blocking threats before they reach your infrastructure.
- **Performance optimization:** Legitimate traffic is intelligently routed through the optimal path within Gcore’s high-performance backbone, reducing latency and ensuring seamless data transmission.
- **Secure tunneling to your network:** Once filtered and optimized, traffic is securely forwarded to your origin using GRE (Generic Routing Encapsulation) or other tunneling protocols, ensuring a smooth, uninterrupted connection.

## Getting started 

Check out our guide on <a href="https://gcore.com/docs/ddos-protection/secure-transit/configure-secure-transit" target="_blank">configuring your infrastructure for Super Transit</a> guide for detailed instructions on how to use this feature. 
