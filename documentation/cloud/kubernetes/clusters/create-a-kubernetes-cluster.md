---
title: create-a-kubernetes-cluster
displayName: Create
order: 10
published: true
toc:
   --1--1. Initiate: "step-1-initiate-the-process"
   --1--2. Select region: "step-2-select-the-region"
   --1--3. Select version: "step-3-select-the-version"
   --1--4. Configure pool: "step-4-configure-pools"
   --2--Vurtual Instance: "virtual-instance"
   --2--Bare Metal: "bare-metal-instances"
   --1--5. Select the CNI Provider: "step-5-select-the-cni-provider" 
   --1--6. Configure Network: "step-6-configure-network-settings"
   --1--7. Add SSH key: "step-7-add-a-ssh-key"
   --1--8. Specify cluster name : "step-8-specify-a-cluster-name"
   --1--(Optional) 9. Configure logging: "step-9-optional-configure-logging"
   --1--10. Finalize: "step-10-finalize"
pageTitle: Create a Kubernetes cluster | Gcore
pageDescription: Learn how to create a Kubernetes cluster on a Virtual Machine or a Bare Metal server.
---
# Create a Kubernetes cluster

## Step 1. Initiate the process

Open the “Kubernetes” tab and click **Create Cluster**.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/create-cluster.png" alt="Start Kubernetes container creation" width="80%">

A new page will open. Perform the remaining steps there. 

## Step 2. Select the region

Select a **region**—the location of the data center where your cluster will be deployed. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/region-k8s.png" alt="Kubernetes region" width="75%">

## Step 3. Select the version

Select your **Kubernetes cluster version**.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/version-k8s.png" alt="Kubernetes cluster version" width="60%">

## Step 4. Configure pools

Under the **Pools** block, configure a pool—a set of cluster nodes with the same specifications. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/pool-k8s.png" alt="Pools" width="80%">

- Enter the **Pool name** .
- Set the **minimum nodes** and **maximum nodes** for <a href="https://gcore.com/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling" target="_blank">autoscaling</a>.
- Select the type of a worker node: a **Virtual Instance** or a **Bare Metal instance**. 

<tabset-element>

### Virtual Instance

Select its flavor, disk size in GiB, and disk type.

Available Virtual Instance flavors:

- **Standard**. The amount of memory in GB is 2–4 times higher than that of vCPUs
- **vCPU**. The amount of vCPUs equals the amount of memory in GB
- **Memory**. The amount of memory in GB is much higher (up to 8 times) than that of vCPUs
- **High Frequency**. High CPU clock speed (3.7 GHz in the basic configuration)
- **SGX**. Supports Intel SGX technology

Available disk types:

- **High IOPS SSD**. A high-performance SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB.) The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.
- **Standard**. This is a network SSD disk that provides stable and high random I/O performance, as well as high data reliability (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB.) The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.
- **Cold**. This is a network HDD disk, suitable for less frequently accessed workloads. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s. Please note that this option is unavailable in Manassas.
- **Ultra**. This is the network block storage option, recommended for non-critical data and workloads that are accessed less frequently. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.
- **SSD low latency**. This is an SSD block storage, designed for applications that require low-latency storage and real-time data processing. It can achieve IOPS performance of up to 5000, with an average latency of 300 µs.

### Bare Metal instances

Select a flavor:

- **High-frequency**. Single-socket servers equipped with 2288G/2388 CPUs, suitable for hosting applications that require high processor frequency.
- **Infrastructure**. Multi-core, multi-socket configurations designed for hosting applications that demand a high number of cores. These servers are optimized for multithreading.

</tabset-element>

- Ensure the **Autohealing nodes** toggle is on to enable automatic recovery of failed nodes. When toggled on, this feature monitors node statuses. When it detects a non-working node, the autohealer initiates replacement. If one of the machines fails, the application will not stand idle: The node(s) will be replaced on a working machine, and the app will keep working.

- (Optional) Enable the **Public IPv4 address** option to assign public IPv4 addresses to cluster nodes.   

Add as many pools as you need using the **Add pool** button.

## Step 5. Select the CNI Provider 

Choose the network stack of either *Cilium* or *Calico*—networking and network security solutions for containers: 

- Cilium uses eBPF to inject functionality into the kernel and provides a broader range of additional features (load balancing, advanced security, failure detection, etc.) than Calico. Additionally, you can add necessary functions by checking the following boxes: DSR, tunneling, load balancer acceleration, and encryption. 
- Calico uses a more conservative stack based on iptables.  

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/cni-provider.png" alt="Network stack" width="65%">

## Step 6. Configure Network settings

Select an existing network and subnet or create new ones according to the instructions in our <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-network" target="_blank">dedicated guide</a>.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/network-k8s.png" alt="Network settings for Cluster" width="70%">

<expandable-element title="Advanced DDoS Protection"> 

You can enable **Advanced DDoS Protection** for your private network. To do so, activate the **Enable Advanced DDoS Protection** toggle, open the drop-down menu, and select the desired template from the list. We currently support the following templates: CS:GO, Rust, ARK, Basic L3/L4, or TCP protection. 

Depending on the selected template, the settings will be different. For example, for the Basic L3/L4 specify the uppermost threshold of attack that our DDoS Protection can mitigate in the “Mitigation capacity” field.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/ddos-k8s.png" alt="Configure profile template">

</expandable-element> 

## Step 7. Add an SSH key

Configure an SSH key for a remote SSH connection to all nodes. Select an existing key or create a new one. For details, consult our article on <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">how to connect to your instance via SSH</a>.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/ssh-cluster.png" alt="SSH settings for Cluster" width="50%">

## Step 8. Specify a cluster name

Enter the cluster's name in the field.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/name-cluster.png" alt="Name for Cluster" width="50%">

## Step 9. (Optional) Configure logging 

This is a paid option that allows you to collect and store Kubernetes logs. For more details on Managed Logging, read our <a href="https://gcore.com/docs/cloud/logging-as-a-service/configure-logging-and-view-your-logs" target="_blank">dedicated guide</a>. To configure Managed Logging in the customer portal, choose one of two options:

- **Select an existing topic**. If you already use Managed Logging, select this option.  
- **Create new topic**. If you don't have existing topics with a specified log retention time, choose this option and specify the required information.    

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/logging-cluster.png" alt="Logging for Cluster" width="70%">

## Step 10. Finalize

Check the cluster settings on the right side of the screen. If everything is correct, click **Create cluster**. 

The cluster will be created in just a few minutes! 