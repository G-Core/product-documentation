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

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, open the **GPU cloud** page. You'll be taken to the page for AI cluster creation.

<img src="https://assets.gcore.pro/docs/gpu-cloud/gpu-cloud-page.png" alt="Create an AI Cluster" width="80%">

2\. Select the region, a physical location of the data center. For example, if you choose Amsterdam-2, your cluster will be deployed on servers located in Amsterdam.

3\. Choose the flavor with relevant cluster configuration and allocated resources. The number in vPOD means the number of IPU-processors in your cluster. For instance, one Graphcore server consists of four IPU-processors.

4\. Select the OS image on which your model will be running.

5\. Configure volumes and set the size of your cluster. Note that you can't change the cluster size after its creation.  

6\. Set up a network interface. You can choose a public or private one.

If you are planning to use the GPU Cloud with servers hosted outside of Gcore Cloud, attach a public network interface. So, your cluster will be accessible from external networks.

If you want to use the service with Gcore servers only, assign a private network. Your cluster will be available only for internal networks. Select one of the existing networks or create a new one to attach it to your server.  
  
7\. (Optional) If you want to assign a reserved IP address to your server, turn on the **Use reserved IP** toggle and select one. For more details, see the article <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">Create and configure a reserved IP address</a>.   
  
8\. Turn on the **Use floating IP** toggle if you want to use a floating IP address. It’ll make your server accessible from outside networks even if they have only a private interface. Create a new IP address or choose an existing one. For more details, see the article <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">Create and configure a floating IP address</a>.  
  
9\. (Optional) If you need several network interfaces, click **Add Interface** and repeat the instructions from to Step 6.

10\. Select one of your SSH keys from the list, add a new key, or generate a key pair. You'll use this SSH key to connect to your cluster.  
  
11\. Name your cluster and click **Create Cluster**.

Congrats! The cluster is created! Use the IP address of your AI Cluster and the SSH key from Step 10 and connect to your server.

User login: ```ubuntu```

Connection port: ```22```