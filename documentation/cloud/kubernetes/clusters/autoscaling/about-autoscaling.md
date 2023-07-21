---
title: about-autoscaling
displayName: Overview
order: 10
published: true
toc:
   --1--What is autoscaling?: "what-is-autoscaling"
   --1--How does it work?: "how-does-autoscaling-work"
   --1--Change settings: ""
   --1--Disable: "disable-autoscaling"
pageTitle: About autoscaling | Gcore
pageDescription: Understand autoscaling in a cloud environment, where resources are adjusted based on demand to optimize performance.
---
# About autoscaling
  
## What is autoscaling?

Autoscaling is a system that adjusts the number of nodes in a pool based on changes in load. If the existing nodes cannot handle the load, a new one will be deployed. Conversely, if some nodes are idle without any load, they will be removed. 

## How does autoscaling work?

You set the minimum and maximum number of nodes, and autoscaling will ensure that the number of nodes remains within these limits. It will not create more nodes than the specified maximum, and it will not remove any nodes if the minimum has been reached. 

*   If a new pod (application container group) needs to run and the existing nodes don’t have enough resources to do it, autoscaling will deploy a new node. The amount of free resources is determined by "resources.requests".
*   If some nodes are running without any pods for 20 minutes straight, the system will remove them.     
*   If you manually delete nodes with running pods, reducing the current number of nodes below the level set by autoscaling, the system will reassess the load on the pool after 20 minutes. If the current nodes are unable to handle the required pods, more nodes will be added. If the nodes are sufficient, no additional nodes will be added.

## Change autoscaling settings

1\. In the Cloud menu, go to **Kubernetes**, find the required cluster and click its name.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling/13323994996881.png" alt="Screenshot_2023-02-27_at_13.37_2.png">

2\. Go to the **Pools** section, click ⋯ next to the pool and select **Change autoscaling limits**.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling/13328028097425.png" alt="Screenshot_2023-02-27_at_20.42_1.jpg">

3\. In the new window, specify the maximum and minimum number of nodes and click **Save**.

New autoscaling settings have been applied.

## Disable autoscaling

When you turn off autoscaling, the number of nodes in the pool will remain constant.

1\. In the Cloud menu, go to **Kubernetes**, find the required cluster and click its name.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling/13325419009809.png" alt="Screenshot_2023-02-27_at_13.37_2.png">

2\. Go to the **Pools** section, click ⋯ next to the pool and select **Change autoscaling limits**.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling/13328028097425.png" alt="Screenshot_2023-02-27_at_20.42_1.jpg">

3\. In the new window, enter the same number of nodes for minimum and maximum and click **Save**.

Autoscaling has been disabled. The pool will now maintain the specified number of nodes all the time, regardless of load.