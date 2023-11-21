---
title: create-a-kubernetes-cluster
displayName: Create
order: 10
published: true
toc:
pageTitle: Create a Kubernetes cluster | Gcore
pageDescription: Learn how to create a Kubernetes cluster on a virtual machine or a bare metal server.
---
# Create a Kubernetes cluster

1\. Open the **Kubernetes** tab and click **Create Cluster**.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/10611849724433.png" alt="Kubernetes tab " width="80%">

2\. Select a region — the location of the data center where your cluster will be deployed. 

3\. Select your **Kubernetes cluster version.** 

4\. Under **Pools**, configure a pool — a set of cluster nodes with the same specifications. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/pool-setup.png" alt="Pools" width="65%">

- Enter the **pool name** 
- Set the **minimum nodes** and **maximum nodes** for <a href="https://gcore.com/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling" target="_blank">autoscaling</a>.
- Select the type of a worker node: a virtual instance or a bare metal server. 

For **Virtual instances**, select its flavor, disk size in GiB and the disk type.

<expandable-element title="Available flavors of virtual instances">

**Standard**. These are machines on which the amount of memory in GB is 2–4 times higher than that of vCPUs.

**vCPU**. These are machines on which the amount of vCPUs equals the amount of memory in GB.

**Memory**. These are machines on which the amount of memory in GB is much higher (up to 8 times) than that of vCPUs.

**High Frequency**. These are machines with a high CPU clock speed (3.7 GHz in the basic configuration).

**SGX**. These are machines that support Intel SGX technology.

</expandable-element>

<expandable-element title="Available disk types">

* **High IOPS SSD**. This is a high-performance SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB). The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.

* **Standard**. This is a network SSD disk, which provides stable and high random I/O performance, as well as high data reliability (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB). The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.

* **Cold**. This is a network HDD disk, suitable for less frequently accessed workloads. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s. Please note that this option is unavailable in Manassas.

* **Ultra**. This is the network block storage option, recommended for non-critical data and workloads that are accessed less frequently. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

* **SSD Low-Latency**. This is an SSD block storage, designed for applications that require low-latency storage and real-time data processing. It can achieve IOPS performance of up to 5000, with an average latency of 300 µs.

</expandable-element>

For **Baremetal instances**, also select a flavor:

<expandable-element title="Available flavors of bare metal servers">

**High-frequency**. These servers are single-socket servers equipped with 2288G/2388 CPUs, suitable for hosting applications that require high processor frequency.

**Infrastructure**. These servers are multi-core, multi-socket configurations designed for hosting applications that demand a high number of cores and are optimized for multithreading.

</expandable-element>

- Make sure the **Autohealing nodes** toggle is on to enable automatic recovery of failed nodes. The option monitors node statuses. When it detects a non-working node, the autohealer initiates replacement. If one of the machines fails, the application will not stand idle: the node will be replaced, and the app will keep working.

- (Optional) Enable the **Public IPv4 address** option to set a public network with external IPs.   

Add as many pools as you need using the **Add pool** button.

5\. Under **Network settings**, select a network and subnet from existing ones or create a new one.

6\. Under **SSH key**, specify the key that will be added to all nodes for connection.

You can select the key from existing ones or create a new one.

7\. Enter the cluster name.

8\. On the right side of the screen, double-check the cluster settings. If everything is correct, click **Create cluster**.

The cluster will be created in a few minutes!