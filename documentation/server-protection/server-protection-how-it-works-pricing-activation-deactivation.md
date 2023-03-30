---
title: server-protection-how-it-works-pricing-activation-deactivation
displayName: Server Protection. How it works, pricing, activation, deactivation
published: true
toc:
   --1--How it works: "how-it-works"
   --1--Advanced protection modes: "advanced-protection-modes-advanced-protection"
   --1--Pricing: "pricing"
   --1--Order service: "how-to-activate-service"
   --1--Deactivate service: "how-to-deactivate-service"
---
Server Protection is a service that protects your servers and instances from DDoS attacks.

  
  
  
  

How it works
------------

Server Protection (free) is provided for all our equipment by default. In case of an attack, our system blocks the server's IP. So, an attacker cannot continue the attack. The server is not affected, but it becomes unavailable for several hours.

You can order advanced (paid) Server Protection. During an attack, it redirects traffic to the threat mitigation system (TMS), that helps to filter traffic and detect threats. This system recognizes an attack, removes attack traffic, and enables only legitimate traffic that won't impact the server's operation. You can configure the ACL (access control list) for TMS by yourself. The main advantage is that a server's IP is not blocked during an attack, and the server remains available.

Advanced protection can operate in one of two modes: always-on or on-demand.

Advanced protection modes
-------------------------

With on-demand mode, traffic passes through the TMS only during an attack. The system needs about a minute to identify a threat and redirect traffic to the TMS. During this first minute, a targeted server will receive attack traffic, and then filtered one.

With always-on mode, your traffic passes through the TMS all the time, even when there is no attack. This protection provides immediate response to an attack and guarantees that only legitimate traffic will be sent to your server.

 

 **Advanced protection**
------------------------

|                                         | \n Advanced protection\n                                                                                                                                         | Basic protection                                                                                                                                                                                  |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \nOn-demand\n                           | Always-on                                                                                                                                                        |
| \nPricing\n                             | \nPaid\n                                                                                                                                                         | Paid                                                                                                                                                                                              | Free                                                                                                       |
| \nAttack detection time(maximum)\n      | \n2 minutes\n \n                                                                                                                                                 | \n5 seconds\n \n                                                                                                                                                                                  | \n3 minutes \n \n                                                                                          |
| \nTypes of attacks to be prevented \n\n | \n• Common amplification attacks\n• IP spoofing attacks\n• Attacks using flows or volumetric attacks (L3)\n• Attacks to establish connection (L4)\n\n            | \n• Common amplification attacks\n• IP spoofing attacks\n• Attacks using flows or volumetric attacks (L3)\n• Attacks to establish a connection (L4)\n• Attacks at the application layer (L5-L7)\n | \n• Common amplification attacks\n• IP spoofing attacks\n                                                  |
| \nProtection technology\n               | \n1. Attack is detected.\n2. Traffic is redirected to TMS.\n3. TMS filters the traffic.\n4. TMS sends legitimate traffic to the server.\n                        | \n1. All traffic passes through TMS.\n2. In case of attack, TMS immediately filters the traffic.\n3. TMS sends legitimate traffic to the server.\n \n                                             | \n1. Attack is detected.\n2. The attacked IP is blocked for a while.\n\n \n                                |
| \nWhen it is suitable for you \n\n      | \n• Your server is rarely attacked\n• Your server is not attacked at the application layer (L7)\n• Your server doesn't host any critical business applications\n | \n• Your server is attacked more than 2-3 times a day\n• Your server is attacked at the application layer (L7)\n• Your server hosts a critical business application\n \n                          | \n• Your server is hardly ever attacked\n• Your server doesn't host any critical business applications\n\n |

  
  
  
  

Pricing
-------

 The price of a Server Protection depends on three things:

*   OSI layers to be protected**.** Two options are available: L3-L4 and L3-L7. The first option is cheaper.
*   Bandwidth used by the TMS to send traffic to a server**.** Several options are available: 1 Mbit/s, 10 Mbit/s, 100 Mbit/s, 200 Mbit/s, 500 Mbit/s, 1 Gbit/s, 2 Gbit/s,10 Gbit/s. The lower the bandwidth, the cheaper the price. 
*   Server location. Prices vary from location to location. Please send a request, and we will advise you the price for Server Protection in a particular data center. 

The price does not depend on a mode you choose. But note that always-on mode is available at L3-L7 layers, and on-demand mode is available only at L3-L4.

We can also offer you a plan with custom terms. Tell us what protection parameters you are interested in, and we will be happy to negotiate a custom proposal for you.

How to activate service
-----------------------

Server Protection is provided for [virtual servers](https://gcorelabs.com/cloud/compute-resources/), [Cloud baremetals](https://gcorelabs.com/cloud/bare-metal-servers/), and [dedicated servers](https://gcorelabs.com/hosting/dedicated/). We can also protect your equipment that is not hosted by us.

**To order protection for a Gcore server**, send a request to technical support via chat in the bottom-right corner of the screen. Please note that the main IP of your server will be changed after we set up the protection. In your request, specify the following details:

*   server ID, 
*   OSI levels to be protected (L3-L4 or L3-L7), 
*   protection mode (on-demand or always-on), 
*   bandwidth, 
*   IP whitelist and IP blacklist (optionally, you can specify it later). 

**To order protection for a third-party server**, fill out the application at the bottom of the [Server Protection](https://gcore.com/ddos-protection) section of our website. In the application, specify the following:

*   your contact info, 
*   location of your equipment, 
*   subnet of your equipment, 
*   IP whitelist and IP blacklist (optionally, you can specify it later).

**To rent a new dedicated server with Server Protection**, select its configuration in the [Dedicated servers](https://gcorelabs.com/hosting/dedicated/) section of our website and fill out an application at the bottom of the page. In the application, specify the following:

*   server configuration, 
*   OSI levels to be protected (L3-L4 or L3-L7), 
*   protection mode (on-demand or always-on), 
*   bandwidth, 
*   IP whitelist and IP blacklist (optionally, you can specify it later). 

**To rent a new instance or a baremetal server with Server Protection**, send a request to technical support via chat in the bottom-right corner of the screen. In your request, specify that you need Server protected equipment.

How to deactivate service
-------------------------

To deactivate protection of your server, contact our technical support. We will stop the service. Please note that the main IP of your server will be changed after deactivation.
