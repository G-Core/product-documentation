---
title: create-a-new-pool-in-cluster
displayName: Create a pool
order: 30
published: true
toc:
---
# Create a new pool in a cluster

1\. In the Cloud menu, go to **Kubernetes**, find the required cluster and click its name.

<img src="https://support.gcore.com/hc/article_attachments/13344056819601" alt="Screenshot_2023-02-27_at_13.37_2.png">

2\. Go to the **Pools** section and click **Add pool**.

<img src="https://support.gcore.com/hc/article_attachments/13344082420369" alt="Screenshot_2023-02-27_at_18.50_1-2.jpg" width="497" height="308">

3\. The new window will expand.  
In the **General** section, give the pool a name, specify the maximum and minimum number of nodes. Autoscaling will regulate the number of nodes within the specified limits by removing unnecessary nodes during low load and deploying new ones during high loads.

<img src="https://support.gcore.com/hc/article_attachments/13344100888849" alt="Screenshot_2023-02-28_at_12.41.04.png" width="452" height="280">

4\. For the **Type** section, select a machine configuration for the nodes in the pool. There are five configurations available:

*   Standard — machines with 2 to 4 times more GB of memory than vCPUs.
*   vCPU — machines with an equal number of vCPUs and GB of memory.
*   Memory— machines with significantly more GB of memory (up to 8 times) than vCPUs.
*   High Frequency — machines with a high CPU clock rate (3.7 GHz in the basic configuration).
*   GX — machines that support Intel SGX technology

5\. For **Volume settings**, select the size and type of a disk to store the pool data. There are four types available:

*   High IOPS SSD — network SSD block storage optimized for low latency transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB). The IOPS performance limit is 9000. The bandwidth limit is 500 MB/s.     
*   Standard — high-performance network SSD block storage (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB). The IOPS performance limit is 4500. The bandwidth limit is 300 MB/s. 
*   Cold — network HDD block storage. The maximum number of IOPS is 1000. The bandwidth limit is 100 MB/s.     
*   Ultra — network HDD block storage, equivalent to the Cold disk. The maximum number of IOPS is 1000. The bandwidth limit is 100 MB/s.     

7.  Click **Save**. 

The pool has been created.