---
title: create-a-new-pool-in-cluster
displayName: Create a pool
order: 30
published: true
pageTitle: Create a new pool | Gcore
pageDescription: Learn how to create a new pool in a Kubernetes cluster. 
---
# Create a new pool in a cluster

1\. In the Cloud menu, go to **Kubernetes**, find the required cluster and click its name.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/create-a-new-pool-in-cluster/13344056819601.png" alt="Screenshot_2023-02-27_at_13.37_2.png">

2\. Go to the **Pools** section and click **Add pool**.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/create-a-new-pool-in-cluster/13344082420369.png" alt="Screenshot_2023-02-27_at_18.50_1-2.jpg" width="497" height="308">

3\. The new window will expand. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/autoscaling/create-a-new-pool-in-cluster/15416891909265.png" alt="Expanded window">

Enter the **pool name**, set the **minimum nodes** and **maximum nodes** for <a href="https://gcore.com/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling" target="_blank">autoscaling</a>. Autoscaling will regulate the number of nodes within the specified limits by removing unnecessary nodes during low load and deploying new ones during high loads.

For **Type**, select the type of a worker node: a virtual instance or a bare metal server. 

For virtual instances, you should select its flavor, disk size in GiB and the disk type.

<expandable-element title="Available flavors of virtual instances">

**Standard**. These are machines on which the amount of memory in GB is 2–4 times higher than that of vCPUs.

**vCPU**. These are machines on which the amount of vCPUs equals the amount of memory in GB.

**Memory**. These are machines on which the amount of memory in GB is much higher (up to 8 times) than that of vCPUs.

**High Frequency**. These are machines with a high CPU clock speed (3.7 GHz in the basic configuration).

**SGX**. These are machines that support Intel SGX technology.

</expandable-element>

<expandable-element title="Available disk types">

**High IOPS SSD**. Network SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB). The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.

**Standard**. High-performance network SSD block storage (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB). The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.

**Cold**. Network HDD block storage. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

**Ultra**. Network HDD block storage, similar to Cold disks. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

</expandable-element>

For bare metal servers, you also should select a flavor:

<expandable-element title="Available flavors of bare metal servers">

**High-frequency**. These servers are single-socket servers equipped with 2288G/2388 CPUs, suitable for hosting applications that require high processor frequency.

**Infrastructure**. These servers are multi-core, multi-socket configurations designed for hosting applications that demand a high number of cores and are optimized for multithreading.

</expandable-element>

Make sure the **Autohealing nodes** toggle is on to enable automatic recovery of failed nodes. The option monitors node statuses. When it detects a non-working node, the autohealer initiates replacement. If one of the machines fails, the application will not stand idle: the node will be replaced, and the app will keep working.

4.  Click **Save**. 

The pool has been created.
