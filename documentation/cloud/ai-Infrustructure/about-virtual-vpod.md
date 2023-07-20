---
title: about-virtual-vpod
displayName: Virtual vPOD
order: 30
published: true
toc:
   --1--What is a virtual vPOD?: "what-is-a-virtual-vpod"
   --1--Features: "features-of-virtual-vpods"
   --1--Benefits: "benefits-of-virtual-vpods"
   --1--Configurations: "configurations"
pageTitle: Virtual vPOD | Gcore
pageDescription: Discover virtual vPODs. AI clusters with Poplar servers on virtual machines, offering cost savings, faster deployment, and flexible configurations.
---
# About Virtual vPOD

## What is a virtual vPOD?

A virtual vPOD is a flavor of an AI cluster in which a Poplar server is deployed on a virtual machine, as opposed to a dedicated vPOD, which deploys a Poplar server on a dedicated bare metal server.

With virtual vPODs, you can directly access the host machines and can easily set up your own development environment on each IPU instance, install and run any code in an ultrafast connection with IPU accelerators, have better experience with deploying and developing such frameworks like TensorFlow and PyTorch on Cloud IPUs, use ephemeral storage, execute custom code in input pipelines, and integrate Cloud IPUs into research and production workflows.

## Features of virtual vPODs

Virtual vPODs offer two main features.

1. **External volumes**. With virtual vPODs, you can connect external block storage for system and data volumes and easily attach new data volumes. 
2. **Suspension mode**. Virtual vPODs have the Suspension mode, which allows you to avoid any charges when your cluster is stopped. This feature is particularly useful when you have temporary or unpredictable workloads or when you want to make changes to your cluster. When a cluster is suspended, its state is saved on external storage. You can resume the cluster within a few minutes, and it’ll be restored to its previous state. This feature allows for better control over costs and resource optimization.

## Benefits of virtual vPODs

1.  **Cost savings**. With the suspension mode, users can save money by temporary pausing their resources when they are not in use.
2.  **Faster deployment time**. Virtual vPODs are deployed in just 5 minutes, compared to 15 minutes required for physical vPODs.
3.  **Greater storage options**. With Virtual vPODs, users can easily attach external data volumes.
4.  **Flexibility**. Virtual vPODs can be easily modified or reconfigured as needed to meet changing requirements.

## Configurations

Each flavor of virtual vPOD comes with:

- 1 virtual machine. The configuration of a virtual machine depends on the capacity of vCPU, RAM and ephemeral storage.
- Host server(s) with 4 IPU-processors on each. The exact number of host servers depends on the flavor you choose.

For up-to-date prices and availability, refer to <a href="https://gcore.com/cloud/ai-platform" target="_blank">our website</a> or your <a href="https://cloud.gcore.com/cloud/projects/list" target="_blank">Control panel</a>.