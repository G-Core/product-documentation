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
   --2--Virtual Machine: "virtual-machine"
   --2--Bare Metal: "bare-metal"
   --1--5. Select the CNI Provider: "step-5-select-the-cni-provider" 
   --1--6. Configure Network: "step-6-configure-network-settings"
   --1--7. Add SSH key: "step-7-add-a-ssh-key"
   --1--8. Specify cluster name: "step-8-specify-a-cluster-name"
   --1--9. Configure logging: "step-9-optional-configure-logging"
   --1--10. Configure advanced settings: "step-10-optional-configure-advanced-settings"
   --1--11. Finalize: "step-10-finalize"   
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

Select your Kubernetes cluster version from the dropdown menu.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/version-k8s.png" alt="Kubernetes cluster version" width="60%">

## Step 4. Configure pools

Under the **Pools** block, configure a pool. A pool is a set of cluster nodes with the same specifications. 

- Enter the Pool name.
- Set the minimum nodes and maximum nodes for <a href="https://gcore.com/docs/cloud/kubernetes/clusters/autoscaling/about-autoscaling" target="_blank">autoscaling</a>.
- Select the type of a worker node: Virtual Machine or Bare Metal.  
- (Optional) Configure advanced pool settings. For an overview of advanced settings, check out the <a herf="https://gcore.com/docs/cloud/kubernetes/clusters/autoscaling/create-a-new-pool-in-cluster" target="_blank">Create and configure a pool</a> guide. 

<tabset-element>

### Virtual Machine

Select the flavor, disk size in GiB, and disk type.

The following Virtual Machine flavors are available:

- **Standard.** 2–4 times the memory of vCPUs
- **vCPU.** The number of vCPUs equals the amount of memory in GB
- **Memory.** Much higher memory than that of vCPUs-up to 8x more
- **High Frequency.** High CPU clock speed starting at 3.7 GHz in the basic configuration
- **SGX.** Supports Intel SGX technology

The following disk types are available:

- **High IOPS SSD.** A high-performance SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB.) The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.
- **Standard.** A network SSD disk that provides stable and high random I/O performance and high data reliability (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB.) The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.
- **Cold.** A network HDD disk suitable for less frequently accessed workloads. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s. Please note that this option is unavailable in Manassas.
- **Ultra.** The recommended network block storage option for non-critical data and workloads that are accessed less frequently. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.
- **SSD low latency.** An SSD block storage designed for applications that require low-latency storage and real-time data processing. The IOPS performance limit is 50,00, with an average latency of 300 µs.

### Bare Metal

The following Bare Metal flavors are available:

- **High-frequency.** Single-socket servers equipped with 2288G/2388 CPUs, suitable for hosting applications requiring high processor frequency.
- **Infrastructure.** Multi-core, multi-socket configurations designed for hosting applications that demand a high number of cores. These servers are optimized for multithreading.

</tabset-element>

- Ensure the **Autohealing nodes** toggle is on to enable automatic recovery of failed nodes. When toggled on, this feature monitors node statuses. Upon detecting a non-working node, the autohealer initiates its replacement. If one of the machines fails, the application will not stand idle: The node(s) will be replaced on a working machine, and the app will keep working.

- (Optional) Enable the **Public IPv4 address** option to assign public IPv4 addresses to cluster nodes.   

<alert-element type="info" title="Info">

If you want to [enable an IPv6 dual-stack](https://gcore.com/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster#enable-ipv6) for your cluster, at least one of the pools must have a public IPv4 address. 

</alert-element>

- Add as many pools as you need using the **Add pool** button.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/pool-k8s.png" alt="Pools" width="80%">

## Step 5. Select the CNI Provider 

Choose either the Cilium or Calico network stack. These provide networking and network security solutions for containers.

- Cilium uses eBPF to inject functionality into the kernel and provides a broader range of additional features (load balancing, advanced security, failure detection, etc.) than Calico. You can add additional functions as required by checking the relevant box for DSR, tunneling, Load Balancer acceleration, and encryption.

- Calico uses a more conservative stack based on iptables.

You can also enable <a href="https://github.com/cilium/hubble-ui" target="_blank">Hubble UI</a> for the Cilium and use the graphical interface to check your cluster's network traffic. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/cni-provider.png" alt="Enable CNI provider section" width="80%">

(Optional) Set up the CIDR range for pods in a cluster. The default ranges are: 

Calico:

* For pods: 172.16.0.0/18  

* For services: 172.24.0.0/18  

Cilium:

* For pods: 172.16.0.0/17  

* For services: 172.24.0.0/17 

Your CIRD range can't overlap with the following ranges: 10.255.255.0/24, 192.168.128.0/17. These ranges are reserved for internal usage.   

<alert-element type="warning" title="Warning">

You cannot change the network stack after the cluster has been created.

</alert-element>

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/cni-provider.png" alt="Network stack" width="70%">

## Step 6. Configure network settings

<tabset-element>

### Configure a network 

Add one or multiple network interfaces to your cluster. 

If you have previously <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-network" target="_blank">created networks</a>, select the correct network from the dropdown. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/network-kubernetes.png" alt="Network settings for Cluster" alt="Network settings available for the Kubernetes cluster" width="80%">

To add a new network, click **Add a new network** radio button and configure the network as follows: 

1\. Enter the network name. 

2\. (optional) Turn on the **Bare Metal network** toggle to connect Bare Metal servers to the network. 

3\. (optional) Turn on the **Add tags** toggle to add metadata to the network. 

4\. Click **Create network**. 

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/create-network-dialog.png" alt="create network dialog" alt="Network settings available for the Kubernetes cluster" width="80%">

<p id="enable-ipv6"> 5. (Optional) Enable IPv6 dual-stack to assign both IPv4 and IPv6 addresses for network interfaces of worker nodes and pods. If the <b>Enable IPv6 dual-stack</b> toggle is not available, make sure that at least one pool from your cluster is in a public network. If your Kubernetes cluster is only connected to a private network, you also need to configure and add an IPv6 subnetwork. </p>

### Configure a subnetwork 

If you have previously  <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork" target="_blank">created subnetworks</a>, select the correct subnetwork from the dropdown.  

To add a new subnetwork, click **Add a new subnetwork** and configure it according to the following instructions: <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork#create-a-subnetwork" target="_blank">Create a subnetwork</a>. 

</tabset-element>

By default, your container is under Basic DDoS Protection. It can prevent certain attacks by blocking IP addresses used by malicious actors. For a higher level of protection, we recommend enabling Advanced DDoS Protection.   

<expandable-element title="Advanced DDoS Protection"> 

You can enable **Advanced DDoS Protection** for your private network. To do so, activate the **Enable Advanced DDoS Protection** toggle, open the drop-down menu, and select the desired template from the list. We currently support the following templates: CS:GO, Rust, ARK, Basic L3/L4, or TCP protection. 

The settings offered depend on the selected template. For example, for the Basic L3/L4 specify the uppermost threshold of attack in Gbps that our DDoS Protection can mitigate in the “Mitigation capacity” field.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/ddos-k8s.png" alt="Configure profile template">

</expandable-element>

## Step 7. Add an SSH key

Configure an SSH key to enable a remote SSH connection to all nodes. Select an existing key or create a new one. For details, consult our article on <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">how to connect to your VM via SSH</a>.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/ssh-cluster.png" alt="SSH settings for Cluster" width="70%">

## Step 8. Specify a cluster name

Name the cluster in the field as shown below.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/name-cluster.png" alt="Name for Cluster" width="70%">

## Step 9. (Optional) Configure logging 

Managed Logging is a paid feature that allows you to collect and store Kubernetes logs. For more details on Managed Logging, read our <a href="https://gcore.com/docs/cloud/logging-as-a-service/configure-logging-and-view-your-logs" target="_blank">dedicated guide</a>. To configure Managed Logging in the Gcore Customer Portal, choose one of two options:

- **Select an existing topic.** If you already use Managed Logging, select this option.  
- **Create new topic.** If you haven't used Managed Logging before, choose this option and specify the required information.

<img src="https://assets.gcore.pro/docs/cloud/kubernetes/clusters/create-a-kubernetes-cluster/logging-cluster.png" alt="Logging for Cluster" width="70%">

## Step 10. (Optional) Configure advanced settings  

Enable OIDC authentication for your cluster. Follow instructions from the <a href="https://gcore.com/docs/cloud/kubernetes/clusters/secure-cluster-with-oidc" target="_blank">Secure Kubernetes cluster with OIDC authentication</a> guide. 

You can also configure cluster autoscaler settings that will apply to the entire Kubernetes cluster and affect all nodes. For detailed overview of each configuration, check out <a href="https://gcore.com/docs/cloud/kubernetes/clusters/autoscaling/advanced-cluster-autoscaler-settings" target="_blank">Advanced Cluster Autoscaler settings</a>. 

## Step 11. Finalize

Check the cluster settings on the right side of the screen. If everything is correct, click **Create cluster**. 

The cluster will be created in just a few minutes! 
