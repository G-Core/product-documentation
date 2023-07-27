---
title: bare-metal-kubernetes
displayName: Bare Metal support
published: true
order: 20
toc:
   --1--How does it work: "how-does-it-work"
   --1--Advantages: "advantages"
   --1--Configurations: "available-configurations"
   --1--Create a cluster: "create-a-bare-metal-kuberenetes-cluster"
pageTitle: Bare Metal Kubernetes | Gcore
pageDescription: Unlock the power of Bare Metal Kubernetes and deploy nodes directly on physical servers for better performance, security, and direct internet access.
---
# Bare Metal Kubernetes

With Managed Kubernetes, users can deploy worker nodes of their Kubernetes cluster directly on bare metal servers. This empowers users to leverage the full potential of Kubernetes while enjoying the substantial benefits of dedicated hardware resources.

## How does it work?

Traditionally, applications are deployed on virtual instances, with Kubernetes and containers added on top. This setup involves multiple layers: instances, hypervisors, and operating systems. However, Kubernetes on bare metal simplified this. With bare metal, Kubernetes works directly on the host server's operating system (OS). This means that containers in such a cluster have direct access to the underlying hardware, bringing a number of benefits to users.

## Advantages

1. **Improved performance**. Bare metal support unleashes the full potential of the hardware by eliminating the virtualization layer. 
2. **Enhanced security and isolation**. With bare metal, applications operate in a completely isolated environment without any shared resources or "noisy neighbors." This means that you don't have to worry about other workloads affecting performance or security.
3. **Higher network performance**. Applications running on bare metal servers can handle higher traffic due to their dedicated access to the network card, using 100% of the network card’s bandwidth.
4. **Faster disk response time**. In a bare metal setup, applications have direct access to the underlying hardware, including disks. This direct access leads to lower latency as there are no additional layers involved.
5. **Direct internet access**. Users can assign a public interface to their bare metal servers, enabling direct internet access without intermediary layers. This minimizes the latency from the server to end users.

## Available configurations

We offer two types of in-stock configurations:

1. **High frequency**. These servers are single-socket servers equipped with 2288G/2388 CPU, suitable for hosting applications that require high processor frequency.
2. **Infrastructure**. These servers are multi-core, multi-socket configurations designed for hosting applications that require a high number of cores and are optimized for multithreading.

## Create a bare metal Kubernetes cluster

To create a cluster that would run on bare metal nodes, take a look at our article: <a href="https://gcore.com/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster" target="_blank">Create a Kubernetes cluster</a>. Just select the **Bare metal instances** option in the **Pools** section at Step 4.


