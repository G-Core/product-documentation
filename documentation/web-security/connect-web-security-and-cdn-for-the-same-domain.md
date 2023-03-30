---
title: connect-web-security-and-cdn-for-the-same-domain
displayName: Use Web Security and CDN
published: true
order: 120
toc:
    --1--What's the challenge?: "what-is-the-challenge-in-using-web-security-and-cdn-together"
    --1--How we solved It: "how-we-solved-the-challenge"
    --1--Configure: "configure-web-secure-and-cdn-for-your-application"
---

What is the challenge in using Web Security and CDN together?
-------------------------------------------------------------


Previously, it was challenging to connect [Web Security](\"https://gcore.com/web-security\") and [CDN](\"https://gcore.com/dcdn\") services for the same domain. The issue was that when using a CDN, the edge servers that cache content sent numerous requests to your application from a few IP addresses of our internal subnets. This made it difficult for Web Security to effectively apply the Bot protection mechanism since it couldn't distinguish between requests from legitimate users from an internal network IP and malicious requests from bots.


To avoid blocking legitimate requests, we recommended connecting CDNs and Web Protection to separate subdomains. However, it was not convenient for customers.


How we solved the challenge
---------------------------


We changed the bot-identifying process, thereby resolving the connectivity conflict between Web Security and CDN. Now, our security system analyzes web request characteristics to block robotic activity rather than relying on specific identifying information. This allows you to connect Web Security and CDN services for the main domain without subdomains.


Configure Web Secure and CDN for your application
-------------------------------------------------


1. Create a resource under the protection according to the \\"[Create and configure resource](\"https://gcore.com/support/articles/360000578457/\")\\" guide.


2. Go to the [Resources](\"https://control.gcore.com/resources/all\") tab and copy the IP address from the \\"Protected IP\\" column.


**Note**: The IP from the example (_5.188.189.82_) will be different from yours.


![\"image_3292.png\"](\"https://support.gcore.com/hc/article_attachments/13997686949649\")


3. Go to the [CDN resources](\"https://cdn.gcore.com/resources/list\") tab and create a CDN resource according to the appropriate guide: Create a CDN resource [for only static files](\"https://gcore.com/support/articles/213969429/\") or [an entire site](\"https://gcore.com/support/articles/4410067902737/\").


**3.1.** If you want to use Web Secure with the CDN resource **for only static files**, specify the following values during creation:


*   The IP address copied at step #2 in the "Origin" field (e.g., _5.188.189.82_).
*   The custom domain based on your application domain in the \\"Custom domain\\" field (e.g., _cdn.test-domain.com_).


![\"image_3293.png\"](\"https://support.gcore.com/hc/article_attachments/13997787631505\")


Complete the creation of the CDN resource by making all the necessary settings.


**3.2.** If you want to use Web Secure with the CDN resource **for an entire site**, specify the following values during creation:


*   The domain of your application in the \\"Enter site name\\" step (e.g., _test-domain.com_).
*   The IP address copied at step #2 in the \\"IPv4 address\\" field (e.g., _5.188.189.82_).


![\"image_3296.png\"](\"https://support.gcore.com/hc/article_attachments/13997781806353\")


Complete the creation of the CDN resource by making all the necessary settings.


That's it! This is how you connect Web Secure and CDN for the same domain.
