---
title: ip-reputation
displayName: IP reputation
published: true
order: 30
toc:
   --1--Configure policy rules: "configure-policy-rules"
   --2--Traffic via TOR network: "traffic-via-tor-network"
   --2--Traffic via proxy networks: "traffic-via-proxy-networks"
   --2--Traffic from hosting services: "traffic-from-hosting-services"
   --2--Traffic via VPNs: "traffic-via-vpns"
   --2--Bot traffic: "bot-traffic"
   --2--Traffic from suspicious NAT ranges: "traffic-from-suspicious-nat-ranges"
   --2--External reputation block list: "external-reputation-block-list"
   --2--Traffic via CDNs: "traffic-via-cdns"     
pageTitle: Set up IP reputation WAF policy for your domain | Gcore
pageDescription: Learn how to enable and customize IP reputation policy.
---
# IP reputation

Gcore WAAP protects your web application by blocking traffic that comes from well-known malicious IP addresses.  

We constantly collect, update, and validate these IP addresses. The malicious IPs are added to the blocklist. With this information, you can block, challenge, or allow traffic from highly suspected entities.  

## Configure policy rules 

You can review the IP reputation policy and enable or disable its rules in the Gcore Customer Portal: 

1\. Navigate to **WAAP** > **Domains**. 

<img src="https://assets.gcore.pro/docs/waap/waap-policies/ip-reputation/domains-page.png" alt="Domains page in the Customer Portal">

2\. Find the domain where you want to configure the policy and click the domain name to open it.  

3\. In the sidebar menu, click **WAF**. 

4\. On the **Policies** page that opens, click **IP reputation** to expand the section and adjust the policy rules. 

<img src="https://assets.gcore.pro/docs/waap/waap-policies/ip-reputation/ip-reputation.png" alt="WAF policies page with the highlighted Ip reputation policy">

<alert-element type="info" title="Info">

All IP reputation rules are enabled by default. To disable a rule, turn on the toggle near that rule. 

</alert-element>

### Traffic via TOR network 

TOR nodes are commonly used for web anonymity. They can also be used by hackers, scrapers, and spammers to crawl and hack web applications. 

Use JavaScript validation to verify traffic originating from the TOR network. This helps to prevent potential anonymity and security risks associated with TOR usage within web applications. 

### Traffic via proxy networks 

Proxy networks are commonly used for web anonymity. They can also be used by hackers, scrapers, and spammers to crawl and hack web applications. 

Use JavaScript validation to verify traffic from known proxy networks. This proves enhanced visibility and security against potential risks associated with proxy usage within web applications. 

### Traffic from hosting services 

Organic human traffic is unlikely to come from IP spaces that belong to hosting providers. Instead, this traffic typically comes from infected servers controlled by hackers. 

Use JavaScript validation to verify traffic from hosting services and commercial cloud providers. This enhances your application security by mitigating potential risks associated with such services within web applications. 

### Traffic via VPNs 

Virtual Private Networks (VPNs) are commonly used for web anonymity. They can also be used by hackers, scrapers, and spammers to crawl and hack web applications. 

Validate traffic originating from VPNs using JavaScript. This provides increased visibility and security against potential risks associated with VPN usage within web applications. 

### Bot traffic 

Use JavaScript validation to verify traffic coming from IP addresses that have been associated with malicious automated agents (bots). 

### Traffic from suspicious NAT ranges 

Validate traffic coming from high-risk NAT ranges using JavaScript. These ranges are calculated based on historical web behavior detected by a machine learning classifier. 

### External reputation block list 

The IPs on this list are known to be malicious or spam. When an IP with a negative reputation is detected, validate the incoming traffic via JavaScript. 

### Traffic via CDNs 

Organic human traffic is unlikely to originate from IP spaces that belong to CDN companies. When such traffic is detected, validate it via JavaScript. 