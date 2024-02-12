---
title: getting-started-with-dnssec
displayName: DNSSEC
published: true
order: 60
toc:
   --1--Overview: "dnssec-overview"
   --1--Enable via API: "enable-dnssec-via-dns-api"
   --1--View in Customer Portal: "view-values-for-dnssec-in-the-customer-portal"
   --1--Disable: "disable-dnssec"
pageTitle: DNSSEC—Security Extensions Overview & Configuration Guide | Gcore 
pageDescription: Learn about DNSSEC, its benefits, and how to enable or disable it using API requests in the Gcore Customer Portal.
---
# Getting started with DNSSEC 

## DNSSEC overview

DNSSEC (DNS Security Extensions) is a set of security extensions for DNS, functioning as an additional layer of authentication. DNSSEC guards against attacks such as DNS cache poisoning, where scammers attempt to redirect users to a harmful site even when users input a valid web address.

At its core, DNSSEC validates digital signatures in a sequential manner across a chain of trust, extending from the DNS root to the specific DNS record being requested. DNSSEC permits authoritative DNS servers to respond with a signature. Recursive DNS resolvers (recursors) then use these signatures to authenticate the DNS responses.

<alert-element type="warning" title="Warning">

DNSSEC does not encrypt the data between the end user and the recursor. To ensure confidentiality and integrity between clients and recursors, use technologies such as DNS over HTTPS (DoH) and DNS over TLS (DoT). We plan to implement DNS over TLS/HTTPS secure protocols on our public servers to reduce the risk of query interceptions.

</alert-element>

## Enable DNSSEC via DNS API

<alert-element type="info" title="Info"> 

Remember to replace the placeholders in the API request samples in double curly brackets with your own values.

</alert-element>

1\. <a href="https://api.gcore.com/docs/dns#tag/Zones/operation/CreateZone" target="_blank">Create a domain zone</a> for which you want to use DNSSEC using the following API request:

```
POST https://api.gcore.com/dns/v2/zones 
Content-Type: application/json 
Authorization: APIKey {{apikey}} 
{ 
	"contact": "support@gcore.com", 
	"enabled": true, 
	"expiry": 3600, 
	"name": "{{zone_name}}", 
	"nx_ttl": 60, 
	"primary_server": "ns1.gcorelabs.net", 
	"refresh": 3600, 
	"retry": 3600, 
	"serial": 1 
} 
```

<alert-element type="warning" title="Warning">

If you're transferring your DNS zone from one DNS provider to another, disable DNSSEC in advance and wait for the DS record TTL time before taking further actions.

</alert-element>

2\. <a href="https://api.gcore.com/docs/dns#tag/RRsets/operation/CreateRRSet" target="_blank">Create an RRSet</a> using the following API request:

```
POST https://api.gcore.com/dns/v2/zones/{{zone_name}}/{{rrset_name}}/A 
Content-Type: application/json 
Authorization: APIKey {{apikey}} 
{ 
	"resource_records": [ 
    	    { 
        	        "content": [ 
            	            "{{ip_address}}" 
        	        ], 
        	        "enabled": true 
    	    } 
	] 
} 
```
3\. Enable DNSSEC for the domain using the following API request:

```
PATCH https://api.gcore.com/dns/v2/zones/{{zone_name}}/dnssec 
Content-Type: application/json 
Authorization: APIKey {{apikey}}  
{"enabled":true}
```

4\. Obtain Delegation Signer record data for your registrar control panel using the following API request:

```
GET https://api.gcore.com/dns/v2/zones/{{zone_name}}/dnssec 
Content-Type: application/json 
Authorization: APIKey {{apikey}}
```

Here's an example output. 

```
{
  "algorithm": "13",
  "digest": "87071836FA02797589CBA87E1F808CE1CADF6D32F1FCD375D9EEE1914720521B",
  "digest_algorithm": "SHA256",
  "digest_type": "2",
  "ds": "example.com. 3600 IN DS 7888 13 2 87071836FA02797589CBA87E1F808CE1CADF6D32F1FCD375D9EEE1914720521B",
  "flags": 257,
  "key_tag": 7888,
  "key_type": "ECDSAP256SHA256",
  "public_key": "1Aobr0AwVzIefTveXVrjk06w9iMVHUOzdSiW3V9Vr9l6A3D+8tuf9Hv6CBGgVAbx0GYFQicOLn5jV30C1o20QQ=="
}
```

<alert-element type="warning" title="Warning"

The DS value of the record is represented in the “ds” field, not “digest.”

</alert-element>

5\. Input the Delegation Signer record in your registrar’s control panel.

<alert-element type="caution" title="Caution">

Once you've added a Delegation Signer record in your domain registrar's control panel, the changes may take up to 24 hours to take effect, though usually, it takes about an hour.

</alert-element>

That's it. You have completed the configuration on your end.

## View values for DNSSEC in the Customer Portal

To enable the DNSSEC feature in the Gcore Customer Portal, contact [technical support](mailto:support@gcore.com). This step is only necessary during closed beta testing.

Open the added domain zone in the Customer Portal. If DNSSEC was successfully enabled for your Gcore account, you will see the activated toggle in the advanced mode.

<img src="https://assets.gcore.pro/docs/dns/getting-started-with-dnssec/dnssec-is-enabled-10.png" alt="How to know that DNSSEC is enabled" width="80%">

Click the info icon to open the popup with keys and other signing information.

<img src="https://assets.gcore.pro/docs/dns/getting-started-with-dnssec/dnssec-configuration-20.png" alt="DNSSEC configuration page" width="80%">

## Disable DNSSEC

<alert-element type="info" title="Info"> 

Remember to replace the placeholders in the API request samples in double curly brackets with your own values.

</alert-element>

To disable DNSSEC:

1\. Remove the DS record in the registrar control panel. The DNS record in the upper-level zone informs the recursors that they must validate authoritative servers responses for your zone. If DNSSEC is disabled in Gcore but not in the upper-level domain, recursors will attempt to validate a record signature that is already disabled. This scenario will cause an outage for your domain.

2\. Disable DNSSEC in Gcore using the following API request:

```
PATCH https://api.gcore.com/dns/v2/zones/{{zone_name}}/dnssec 
Content-Type: application/json 
Authorization: APIKey {{apikey}} 
{"enabled":false}
```

3\. After disabling DNSSEC, wait for the TTL of the DS record to expire so the cached record will expire.