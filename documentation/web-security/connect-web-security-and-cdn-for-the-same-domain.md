---
title: connect-web-security-and-cdn-for-the-same-domain
displayName: Use Web Application Security and CDN
published: true
order: 31
toc:
   --1--What's the challenge?: "what-is-the-challenge-in-using-web-application-security-and-cdn-together"
   --1--How we solved It: "how-we-solved-the-challenge"
   --1--Configure: "configure-web-secure-and-cdn-for-your-application"
pageTitle: Web Security and CDN | Gcore  
pageDescription: A step-by-step guide on how to connect protection for a CDN resource.
---
# Connect Web Security and CDN for the same domain

## What is the challenge in using Web Application Security and CDN together?

Previously, it was challenging to connect Web Application Security and CDN services for the same domain. The issue was that when using a CDN, the edge servers that cache content sent numerous requests to your application from a few IP addresses of our internal subnets. This made it difficult for Web Application Security to effectively apply the Bot protection mechanism since it couldn't distinguish between requests from legitimate users from an internal network IP and malicious requests from bots.

To avoid blocking legitimate requests, we recommended connecting CDNs and Web Protection to separate subdomains. However, it was not convenient for customers.

## How we solved the challenge

We changed the bot-identifying process, thereby resolving the connectivity conflict between Web Application Security and CDN. Now, our security system analyzes web request characteristics to block robotic activity rather than relying on specific identifying information. This allows you to connect Web Security and CDN services for the main domain without subdomains.

## Configure Web Secure and CDN for your application

1\. Create a resource under the protection according to the Create and configure a protected resource guide.


2\. Go to the Resources tab and copy the IP address from the "Protected IP" column.

**Note**: The IP from the example (*5.188.189.82*) will be different from yours.

<img src="https://assets.gcore.pro/docs/web-security/connect-web-security-and-cdn-for-the-same-domain/13997686949649.png" alt="Web protection">


3\. Go to the CDN resources tab and create a CDN resource according to the appropriate guide: Create a CDN resource for only static files or an entire site.

**3.1.** If you want to use Web Application Security with the CDN resource **for only static files**, specify the following values during creation:


- The IP address copied at step #2 in the "Origin" field (e.g., *5.188.189.82*).
- The custom domain based on your application domain in the "Custom domain" field (e.g., *cdn.test-domain.com*).

<img src="https://assets.gcore.pro/docs/web-security/connect-web-security-and-cdn-for-the-same-domain/13997787631505.png" alt="Set up initial configuration" width="80%">

Complete the creation of the CDN resource by making all the necessary settings.

**3.2.** If you want to use Web Application Security with the CDN resource **for an entire site**, specify the following values during creation:

- The domain of your application in the "Enter site name" step (e.g., *test-domain.com*).
- The IP address copied at step #2 in the "IPv4 address" field (e.g., *5.188.189.82*).

<img src="https://assets.gcore.pro/docs/web-security/connect-web-security-and-cdn-for-the-same-domain/13997781806353.png" alt="Add DNS record" width="80%">

Complete the creation of the CDN resource by making all the necessary settings.

That's it! This is how you connect Web Application Security and CDN for the same domain.