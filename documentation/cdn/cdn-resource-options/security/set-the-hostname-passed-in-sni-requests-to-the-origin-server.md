---
title: set-the-hostname-passed-in-sni-requests-to-the-origin-server
displayName: Set SNI hostname
published: true
order: 50
toc:
---
# Set the hostname passed in SNI requests to the origin

Server Name Indication (SNI) is an extension of the TLS protocol, which adds the domain name to the handshake process so that the TLS process reaches the right domain name (if there are several hostnames at the same IP address) and receives the correct SSL certificate.  

The Change SNI Hostname option allows specifying the hostname that is added to SNI requests from  CDN servers to the origin server via HTTPS. 

**Note**: The option works only if CDN servers use the HTTPS protocol to pull content from an origin server. 

There are two modes: 

1\. Dynamic SNI hostname matches the value of the "Change Host Header" option.  
  
<img src="https://support.gcore.com/hc/article_attachments/360016827078/sni_eng_dyn.png" alt="" width="70%">

2.Custom SNI hostname where you should specify a SNI hostname. The value cannot be empty or contain an IP address.  
  
<img src="https://support.gcore.com/hc/article_attachments/360016751237/sni_eng_custom.png" alt="" width="70%">

**Note**: After a CDN resource creation, the option will be automatically activated with the default value - Dynamic SNI hostname.