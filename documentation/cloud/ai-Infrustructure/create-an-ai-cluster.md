---
title: create-an-ai-cluster
displayName: Create an AI Cluster
order: 20
published: true
toc:
pageTitle: Create an AI Cluster | Gcore
pageDescription: Learn how to create an AI cluster using Gcore's AI Infrastructure. Follow the step-by-step guide to set up your cluster and start using it.
---
# Create an AI Cluster

1\. Open the "AI Infrastructure" tab and click **Create Cluster**.

<img src="https://assets.gcore.pro/docs/cloud/ai-Infrustructure/create-an-ai-cluster/Screenshot_2022-08-10_at_18.11_1-2.png" alt="Create an AI Cluster" width="80%">

You'll be taken to the page for AI cluster creation. Do Steps 2, 3 and 4 in it. The screenshot below highlights the fields that you need to interact with at these steps.

<img src="https://assets.gcore.pro/docs/cloud/ai-Infrustructure/create-an-ai-cluster/gc_1-2.png" alt="Create an AI Cluster" width="80%">

2\. Select the region — this is a city of the data center. For example, if you choose Amsterdam-2, your cluster will be deployed on servers located in Amsterdam.

There are two available regions:

- Amsterdam-2 with new Graphcore Bow-2000 servers,
- Luxembourg-2 with standard Graphcore M2000 servers.

3\. Select the size of your cluster.

The number in vPOD means the number of IPU-processors in your cluster. One Graphcore server consists of four IPU-processors.

The cluster size cannot be changed after creation.  
  
4\. Select the OS image for the Poplar server.

Please note: Ubuntu 18.04 is available only for Amsterdam-2.

Do Steps 5, 6, 7, 8, 9, and 10. The screenshot below highlights the fields that you need to interact with at these steps.

<img src="https://assets.gcore.pro/docs/cloud/ai-Infrustructure/create-an-ai-cluster/gcccc_1-4.png" alt="Create an AI Cluster">

5\. Click the expand arrow to set up a network interface.  
  
6\. Select a public or private network interface.

If you are planning to use the AI Infrastructure with servers hosted outside of Gcore Cloud, attach a public network interface. So, your cluster will be accessible from external networks.

If you want to use the service with Gcore servers only, assign a private network. Your cluster will be available only for internal networks. Select one of the existing networks or create a new one to attach it to your Poplar server.  
  
7\. If you want to assign a reserved IP address to your Poplar server, turn on the **Use reserved IP** toggle and select one. For more details, see the article <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">Create and configure a reserved IP address</a>.   
  
8\. Turn on the **Use floating IP** toggle if you want to use a floating IP address. It’ll make your Poplar server accessible from outside networks even if they have only a private interface. Create a new IP address or choose an existing one. For more details, see the article <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">Create and configure a floating IP address</a>.  
  
9\. If you need several network interfaces, click **Add Interface** and go back to Step 6. If you don’t, skip this step.10\. Select one of your SSH keys from the list, or add a new one, or generate it. You'll use this SSH key to connect to your cluster.  
  
11\. Name your cluster and click **Create Cluster**.

<img src="https://assets.gcore.pro/docs/cloud/ai-Infrustructure/create-an-ai-cluster/Screenshot_2022-08-10_at_17.59_1-3.png" alt="Create Cluster">

Congrats! The cluster is created! Use the IP address of your AI Cluster and the SSH key from Step 10 and connect to your Poplar server.

User login: ```ubuntu```

Connection port: ```22```

<img src="https://assets.gcore.pro/docs/cloud/ai-Infrustructure/create-an-ai-cluster/Screenshot_2022-08-10_at_16.00_1-5.png" alt="cluster is created">
