---
title: configure-an-allowed-address-pair
displayName: Allowed address pair
published: true
order: 50
toc:
   --1--What is an allowed address pair?: "what-is-an-allowed-address-pair"
   --1--Configure: "assign-an-allowed-address-pair"
pageTitle: Allowed address pair | Gcore
pageDescription: Learn how to assign an additional IP address to your VM's interface using an allowed address.
---
# Configure an allowed address pair

## What is an allowed address pair?

An allowed address pair is a feature that allows you to add an extra IP address to the interface of a virtual machine.

By default, a virtual machine has a MAC-IP binding. It means all the traffic that comes to a given IP address will be sent to the machine that has that particular MAC address. If you want to allow traffic for another IP address, you need to add it to the allowed address pair. As such, your machine will become accessible for both IP addresses.

In Gcore, you can add an allowed address pair via an API request.

## Assign an allowed address pair

1. Generate an authorization token or use a <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">permanent API token</a>.

2. Make sure you know the project ID, region ID, instance ID, instance port ID, network ID, and MAC address. Otherwise, send API requests to get the project ID, region ID, instance ID, port ID, network ID, and then find your MAC address from the command line.

3. Send the following API request:


**Method:** PUT  
**Endpoint:** ```https://api.gcore.com/cloud/v1/ports/{**project_id}**/**{region_id}**/**{port_id}**/allow_address_pairs:```  
**Request body:**

<code-block>
{   
  "port_id": <span style="color: orange">"1f0ca628-a73b-42c0-bdac-7b10d023e097"</span>,   
  "instance_id": <span style="color: orange">"bc688791-f1b0-44eb-97d4-07697294b1e1"</span>,   
  "network_id": <span style="color: orange">"351b0dd7-ca09-431c-be53-935db3785067"</span>,   
  "allowed_address_pairs": \[   
    {   
      "ip_address": <span style="color: orange">"192.168.123.20"</span>,   
      "mac_address": <span style="color: orange">"00:16:3e:f2:87:16"</span>  
    },	   
    {   
      "ip_address": <span style="color: orange">"192.168.0.2/32"</span>,   
      "mac_address": <span style="color: orange">"00:16:3e:f2:87:89"</span>  
    }   
  \]   
} 
</code-block> 

Enter your custom values instead of the highlighted ones. For more details, refer to the <a href="https://api.gcore.com/docs/cloud" target="_blank">Gcore API documentation</a>.

Now your machine is available through the IP addresses you specified in the request.
