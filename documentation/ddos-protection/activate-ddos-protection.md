---
title: activate-ddos-protection
order: 20
displayName: Activate
published: true
toc:
   --1--Activate protection for a Gcore server: "activate-protection-for-a-Gcore-server"
   --2--DDoS questionnaire: "ddos-questionnaire"
   --1--Activate protection for a third-party server: "activate-protection-for-a-third-party-server"
   --1--Rent a dedicated server with DDoS protection: "rent-a-new-dedicated-server-with-ddos-protection"
   --1--Deactivate DDoS protection: "deactivate-ddos-protection"
pageTitle: Activate DDoS Protection | Gcore
pageDescription: Easily activate DDoS protection for you Bare Metal servers in cloud, Dedicated Servers, and third-party equipment.
---
# Activate DDoS protection

We provide DDoS protection for <a href="https://gcore.com/cloud/bare-metal-servers" target="_blank">Bare Metal</a> and <a href="https://gcore.com/hosting/dedicated" target="_blank">Dedicated Servers</a>. You can also get DDoS protection for equipment that’s not hosted by Gcore.

<alert-element type="info" title="Info">
 
After we set up the DDoS protection, the main IP of your server will be changed for Hosting. It will stay the same for Bare Metal.
 
</alert-element>

## Activate protection for a Gcore server

There are two options for setting up DDoS protection services: 

* Apply predefined protection profiles. 
* Request custom configuration. This is the only option available for the <a href="https://gcore.com/hosting" target="_blank">Hosting</a> platform. 

The predefined profiles are available on the **Network** tab in your server settings. For example, the following screenshot depicts the profile settings for Bare Metal: 


If no predefined protection profile aligns with your requirements, contact the <a href="mailto:support@gcore.com" target="_blank">Gcore support team</a> to request a custom configuration.

In your request, include the following information: 

* Server ID 
* Filled DDoS questionnaire 

### DDoS questionnaire

Complete the following questionnaire according to your infrastructure setup and DDoS protection requirements. 

<alert-element type="tip" title="Tip">
 
All fields in the questionnaire are optional, but we recommend providing as much information as possible to help us configure DDoS protection settings that are best optimized for your infrastructure. 

</alert-element>

**1. Destination data and protection of additional services**

For each destination that you want to protect, list the IP, port, and protocol.  

<table>
<thead>
<tr>
<td style="text-align: left"><b>Question</b></td>
<td style="text-align: left"><b>Your information</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">Specify IP addresses that should be added to the allowlist</td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left">Do you want to configure the access control list?</td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left">Do you want to set up game protection?</td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left">Do you need to configure the GEO filter?</td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left">Do you want to configure DNS protection?</td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left">Do you want to configure RegEx-based filtering?</td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left">Is your traffic encrypted by TLS protocol?</td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left">Do you want to configure rate limiting for incoming traffic from your own IP range?</td>
<td style="text-align: left"></td>
</tr>
</tbody>
</table>

**2. Bandwidth**

<table>
<thead>
<tr>
<td style="text-align: left"><b>Question</b></td>
<td style="text-align: left"><b>Your information</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">Clean traffic bandwidth in Mbps</td>
<td style="text-align: left"></td>
</tr>
</tbody>
</table>

**3. BGP information**

<table>
<thead>
<tr>
<td style="text-align: left"><b>Question</b></td>
<td style="text-align: left"><b>Your information</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left">What is your autonomous system number (ASN)?</td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left">What IP prefixes do you want to announce /24?</td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left">What’s your GRE tunnel endpoint?</td>
<td style="text-align: left"></td>
</tr>
</tbody>
</table>

**4. Protected Services**

<table>
<thead>
<tr>
<td style="text-align: left"><b>Protocol</b></td>
<td style="text-align: left"><b>Destination IP</b></td>
<td style="text-align: left"><b>Destination port</b></td>
<td style="text-align: left"><b>Service</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
</tr>
</tbody>
</table>

**5. Allowlisted services**

Specify services whose traffic should always be approved and never blocked. 

<table>
<thead>
<tr>
<td style="text-align: left"><b>Protocol</b></td>
<td style="text-align: left"><b>Source IP</b></td>
<td style="text-align: left"><b>Source port</b></td>
<td style="text-align: left"><b>Destination IP</b></td>
<td style="text-align: left"><b>Destination port</b></td>
<td style="text-align: left"><b>Service</b></td>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
</tr>
<tr>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
<td style="text-align: left"></td>
</tr>
</tbody>
</table>

## Activate protection for a third-party server 

For detailed configuration instructions, refer to the <a href="https://gcore.com/docs/ddos-protection/secure-transit/configure-secure-transit" target="_blank">Configure your infrastructure for Secure Transit</a> guide. 

## Rent a new dedicated server with DDoS protection

The configuration for a rented dedicated server is almost identical to the activation of a DDoS protection for an existing server.

The key difference is that you first need to select and order the preferred configuration in the <a href="https://gcore.com/hosting/dedicated" target="_blank">Dedicated Servers</a> section of our website. After that, proceed with the same configuration steps that are outlined in the <a href="https://gcore.com/docs/ddos-protection/activate-ddos-protection#activate-protection-for-a-Gcore-server" target="_blank">Activate protection for a Gcore server</a> section. 

## Deactivate DDoS protection

To deactivate your server's protection, contact the <a href="mailto:support@gcore.com" target="_blank">Gcore support team</a>. We will stop the service. Note that the main IP of your server will be changed after deactivation.