---
title: set-the-hostname-passed-in-sni-requests-to-the-origin-server
displayName: Set SNI hostname
published: true
order: 50
toc:
pageTitle: Setting SNI Hostname in CDN Requests | Gcore
pageDescription: Understand how to set the hostname for SNI requests in CDN to ensure accurate SSL certificate retrieval and enhanced security.
---
# Set the hostname passed in SNI requests to the origin

Server Name Indication (SNI) is an extension of the TLS protocol, which adds the domain name to the handshake process so that the TLS process reaches the right domain name (if there are several hostnames at the same IP address) and receives the correct SSL certificate.  

The Change SNI Hostname option allows specifying the hostname that is added to SNI requests from  CDN servers to the origin server via HTTPS. 

**Note**: The option works only if CDN servers use the HTTPS protocol to pull content from an origin server. 

There are two modes: 

1\. Dynamic SNI hostname matches the value of the "Change Host Header" option.  
  
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/set-the-hostname-passed-in-sni-requests-to-the-origin-server/sni_eng_dyn.png" alt="Change Host Header" width="80%">

2.Custom SNI hostname where you should specify a SNI hostname. The value cannot be empty or contain an IP address.  
  
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/set-the-hostname-passed-in-sni-requests-to-the-origin-server/sni_eng_custom.png" alt="The value" width="80%">

**Note**: After a CDN resource creation, the option will be automatically activated with the default value - Dynamic SNI hostname.