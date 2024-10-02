---
title: configure-mtls-authentication
displayName: Configure mutual TLS authentication
published: true
order: 30
toc:
pageTitle: Configure mutual TLS certificates on a Load Balancer | Gcore
pageDescription: Learn how to configure Load Balancer with mutual TLS certificates authentication.
---
# Configure mutual TLS authentication  

Gcore Load Balancers support mutual TLS (mTLS) authentication that enables two-way authentication between the client and the server. This feature ensures that traffic is encrypted and both parties are verified before any data exchange. 

To configure mTLS, you need to set up: 

* A TLS certificate for client authentication. 

* An identifier of the certificate revocation list (if you maintain that list). 

* A bundle of trusted root and intermediate certificates (CA bundle) that will be used to verify client certificates.  

You can configure mTLS via API. Check <a href="https://api.gcore.com/docs/cloud#tag/Load-Balancers/operation/LoadBalancerPoolViewSet.post" target="_blank">Gcore API documentation</a> for more information about the required parameters and acceptable values for setting up mTLS. 