---
title: create-a-kubernetes-cluster
displayName: Create
order: 10
published: true
toc:
---
1. Open the **Kubernetes** tab and click **Create Cluster**.

<img src="https://support.gcore.com/hc/article_attachments/10611849724433" alt="" width="666" height="312">

2.Select a region — the location of the data center where your cluster will be deployed. 

3\. Select your **Kubernetes cluster version.** 

4\. Under **Pools**, configure a pool — a set of cluster nodes with the same specifications. 

<img src="https://support.gcore.com/hc/article_attachments/13351075707153" alt="Screenshot_2023-02-28_at_15.45.09.png">

Enter the pool name.

For **Minimum number of nodes,** set the limit of nodes to be deployed when [Autoscaling](https://gcore.com/support/articles/4407814896401/) is on and workload decreases**.**

For **Maximum number of nodes,** set the limit of nodes to be deployed when [Autoscaling](https://gcore.com/support/articles/4407814896401/) is on and workload increases.

For **Type**, select a configuration of VMs for your pool. Five groups of configurations are available:

*   **Standard.** These are machines on which the amount of memory in GB is 2-4 times higher than that of vCPUs.
*   **vCPU.** These are machines on which the amount of vCPUs equals the amount of memory in GB.
*   **Memory**. These are machines on which the amount of memory in GB is much higher (up to 8 times) than that of vCPUs.
*   **High Frequency.** These are machines with a high CPU clock speed (3.7 GHz in the basic configuration).
*   **SGX**. These are machines that support Intel SGX technology.

For **Volume settings**, specify the disk size in GiB and select one of four disk types:

*   **High IOPS SSD**. Network SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB). The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.
*   **Standard**. High-performance network SSD block storage (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB). The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.
*   **Cold**. Network HDD block storage. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.
*   **Ultra**. Network HDD block storage, similar to Cold disks. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

Add as many pools as you need using the **Add pool** button.

5. Under **Network settings**, select a network and subnet from existing ones or create a new one.

6. Under **SSH key**, specify the key that will be added to all nodes for connection.

You can select the key from existing ones or create a new one.

7. Enter the cluster name.

8. In **Advanced options**, turn on **Autohealing nodes** to enable automatic recovery of failed nodes. 

The option monitors node statuses. When it detects a non-working node, the autohealer initiates replacement. If one of the machines fails, the application will not stand idle: the node will be replaced, and the app will keep working.

9. On the right side of the screen, double-check the cluster settings. If everything is correct, click **Create cluster**.

The cluster will be created in a few minutes!