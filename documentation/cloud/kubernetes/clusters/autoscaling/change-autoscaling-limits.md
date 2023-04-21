---
title: change-autoscaling-limits
displayName: Change limits
published: true
order: 20
toc:
---
# Change autoscaling limits

1\. In the Cloud menu, go to **Kubernetes**, find the required cluster and click its name.

<img src="https://support.gcore.com/hc/article_attachments/13348527052433" alt="Screenshot_2023-02-27_at_13.37_2.png">

2\. Go to the **Pools** section, click ⋯ next to the pool and select **Change autoscaling limits**.  

<img src="https://support.gcore.com/hc/article_attachments/13348601064977" alt="Screenshot_2023-02-27_at_20.42_1-2.jpg">

3. In the new window, for **Minimum** and **Maximum number of nodes,** enter the number of nodes you want to maintain and click **Save**.

*   If you have specified more nodes than are in the cluster now, the system will deploy new ones.   
*   If you have specified fewer nodes, the system will remove redundant ones.