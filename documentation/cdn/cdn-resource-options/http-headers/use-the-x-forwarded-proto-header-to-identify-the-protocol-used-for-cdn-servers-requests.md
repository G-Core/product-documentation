---
title: use-the-x-forwarded-proto-header-to-identify-the-protocol-used-for-cdn-servers-requests
displayName: Identify a user's request protocol 
published: true
order: 50
toc:
---
The X-Forwarded-Proto header is a standard header for identifying the protocol (HTTP or HTTPS) that a client used to connect to a server.

Our СDN servers sent X-Forwarded-Proto header by default. The header shows which protocol an end-user used to connect to CDN server. 

You can use this header after adding the necessary settings from your side:

*   to set up redirects from HTTP to HTTPS;
*   to deliver different content to users based on the request protocol.