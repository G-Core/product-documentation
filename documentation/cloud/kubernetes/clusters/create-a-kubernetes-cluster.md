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

The new page will open. Do the remaining steps there. 

2\. Select a **region**—the location of the data center where your cluster will be deployed. 

3\. Select your **Kubernetes cluster version.** 

4\. Under the **Pools** block, configure a pool — a set of cluster nodes with the same specifications. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/pool-setup.png" alt="Pools" width="65%">

- Enter the **Pool name** 
- Set the **Minimum nodes** and **Maximum nodes** for <a href="https://gcore.com/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling" target="_blank">autoscaling</a>.
- Select the type of a worker node: a **Virtual instance** or a **Bare metal instance**. 

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

For **Bare metal instances**, also select a flavor:

<expandable-element title="Available flavors of bare metal servers">

**High-frequency**. These servers are single-socket servers equipped with 2288G/2388 CPUs, suitable for hosting applications that require high processor frequency.

**Infrastructure**. These servers are multi-core, multi-socket configurations designed for hosting applications that demand a high number of cores and are optimized for multithreading.

</expandable-element>

- Ensure the **Autohealing nodes** toggle is on to enable automatic recovery of failed nodes. The option monitors node statuses. When it detects a non-working node, the autohealer initiates replacement. If one of the machines fails, the application will not stand idle: the node will be replaced, and the app will keep working.

- (Optional) Enable the **Public IPv4 address** option to assign public IPv4 addresses to cluster nodes.   

Add as many pools as you need using the **Add pool** button.

5\. Under the **Network settings** block, select a network and subnet from existing ones or create a new one, according to the <a href="" target="_blank">separate guide</a>.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/network-settings-cluster.png" alt="Network settings for Cluster" width="70%">

6\. Under **SSH key**, configure an SSH key for a remote SSH connection to all nodes. You can select the key from existing ones or create a new one. For details, see the article: <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">Connect to your instance via SSH</a>. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/ssh-cluster.png" alt="SSH settings for Cluster" width="70%">

7\. Enter the cluster name in the field.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/name-cluster.png" alt="Name for Cluster" width="70%">

8\. (Optional) Enable **Logging**. It’s a paid option that allows you to collect and store Kubernetes logs. For more details on Managed Logging, read the <a href="https://gcore.com/docs/cloud/logging-as-a-service/configure-logging-and-view-your-logs" target="_blank">separate guide</a>. To configure logging in the customer portal, you can choose one of two options: 

- **Select an existing topic**. If you already used logging, select the existing topic.  
- **Create new topic**. Specify the needed information if you have no existing topics where the logs retention time before deletion is set.   

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/logging-cluster.png" alt="Logging for Cluster" width="70%">

9\. Double-check the cluster settings on the right side of the screen. If everything is correct, click **Create cluster**. 

The cluster will be created in a few minutes! 