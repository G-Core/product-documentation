---
title: change-autoscaling-limits
displayName: Change limits
published: true
order: 20
toc:
pageTitle: Change autoscaling limits | Gcore
pageDescription: Learn how to change autoscaling limits in a Kubernetes cluster. 
---
# Change autoscaling limits

1\. In the Cloud menu, go to **Kubernetes**, find the required cluster and click its name.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/change-autoscaling-limits/13348527052433.png" alt="Screenshot_2023-02-27_at_13.37_2.png">

2\. Go to the **Pools** section, click ⋯ next to the pool and select **Change autoscaling limits**.  

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/change-autoscaling-limits/13348601064977.png" alt="Screenshot_2023-02-27_at_20.42_1-2.jpg">

3. In the new window, for **Minimum** and **Maximum number of nodes,** enter the number of nodes you want to maintain and click **Save**.

*   If you have specified more nodes than are in the cluster now, the system will deploy new ones.   
*   If you have specified fewer nodes, the system will remove redundant ones.