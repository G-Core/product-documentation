---
title: secure-transit
displayName: Secure Transit
published: true
order: 40
toc:
pageTitle: About Secure Transit | Gcore
pageDescription: Learn about the Secure Transit feature that provides DDoS protection and helps to optimize your data flow.
---
# Secure Transit

Secure Transit is a network traffic management and security solution designed to optimize data flow while providing DDoS protection. It goes beyond just protecting against DDoS attacks—it also ensures the efficient routing of legitimate traffic, improving network performance by reducing latency. 

## Key features

* **DDoS Protection**. It detects, mitigates, and filters DDoS attacks before they reach your network. This ensures that malicious traffic doesn’t disrupt your services. 
* **Traffic optimization**. Secure Transit enhances network performance by efficiently routing legitimate traffic through our Gcore network, reducing latency and improving the speed of data delivery. This is crucial for latency-sensitive applications like gaming, real-time communications, and streaming. 

## How it works 

We route traffic through Gcore’s global network by anycasting protected network to Internet. It inspects the traffic to filter out malicious activity and ensures that legitimate traffic is delivered with minimal latency, improving performance for users across the globe. 

As we receive your original data packets, we process these packets, encapsulate them with extra headers, and then send the packets back to your origin. Secure Transit uses anycast tunnels to transmit packets from the Gcore’s network to your origin network. 

## Getting started 

Check the <a href="https://gcore.com/docs/ddos-protection/activate-ddos-protection/configure-secure-transit" target="_blank">Configure your infrastructure for Secure Transit</a> guide for details instructions on how to use the feature. 