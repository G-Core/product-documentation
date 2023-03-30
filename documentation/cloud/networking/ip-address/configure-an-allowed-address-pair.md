---
title: configure-an-allowed-address-pair
displayName: Allowed address pair
published: true
order: 50
toc:
   --1--What is an allowed address pair?: "what-is-an-allowed-address-pair"
   --1--Configure: "assign-an-allowed-address-pair"
---
  

What is an allowed address pair?
--------------------------------

An allowed address pair is a feature that allows you to add an extra IP address to the interface of a virtual machine.

By default, a virtual machine has a MAC-IP binding. It means all the traffic that comes to a given IP address will be sent to the machine that has that particular MAC address. If you want to allow traffic for another IP address, you need to add it to the allowed address pair. As such, your machine will become accessible for both IP addresses.

In Gcore, you can add an allowed address pair via an API request.

Assign an allowed address pair
------------------------------

1. Generate an authorization token or use a [permanent token](https://gcore.com/support/articles/360018625617/).

2. Make sure you know the project ID, region ID, instance ID, instance port ID, network ID, and MAC address. Otherwise, send API requests to get the [project ID](https://apidocs.gcore.com/cloud), [region ID](https://apidocs.gcore.com/cloud), [instance ID](https://apidocs.gcore.com/cloud), [port ID](https://apidocs.gcore.com/cloud), and [network ID,](https://apidocs.gcore.com/cloud) then find your MAC address from the command line.

3. Send the following API request:

**Method:** PUT  
**Endpoint:** https://api.gcore.com/cloud/v1/ports/{**project\_id}**/**{region\_id}**/**{port\_id}**/allow\_address\_pairs:  
**Request body:**

{{   
  "port\_id": "**1f0ca628-a73b-42c0-bdac-7b10d023e097**",   
  "instance\_id": "**bc688791-f1b0-44eb-97d4-07697294b1e1**",   
  "network\_id": "**351b0dd7-ca09-431c-be53-935db3785067**",   
  "allowed\_address\_pairs": \[   
    {   
      "ip\_address": "**192.168.123.20**",   
      "mac\_address": "**00:16:3e:f2:87:16**"   
    },	   
    {   
      "ip\_address": "**192.168.0.2/32**",   
      "mac\_address": "**00:16:3e:f2:87:89**"   
    }   
  \]   
} 

Enter your custom values instead of the highlighted ones. For more details, refer to the [Gcore API documentation](https://apidocs.gcore.com/cloud).

Now your machine is available through the IP addresses you specified in the request.