---
title: create-an-instance
displayName: Create
order: 10
published: true
toc:
pageTitle: Create a VM | Gcore
pageDescription: Learn how to create a Linux or Windows machine in Cloud. Start using your virtual machine in minutes with ease.
---
# Create an instance

1. Open **Instances** tab and click **Create Instance**.

![The Create Instance button](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/1-create-instancebutton.png)

2. Select the region where you want to deploy the instance.

![Region selection](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/2-region-selection.png)

Regions can be of two types: Core and Edge. A region determines the equipment specifications.

 

|                                          | Core                        | Edge*                               |
|------------------------------------------|-----------------------------|-------------------------------------|
| Equipment generation                     | The latest                  | Different                           |
| Designed for high scalability on the fly | Yes                         | Not                                 |
| Available resources                      | 1000 cores and 30 TB of RAM | Up to 300 cores and 1 TB of RAM     |
| Ports for user traffic and storage       | Separate                    | Shared                              |
| Price                                    | Higher                      | Lower                               |


\* We can always transform an edge region to core upon your request.

3. Configure the image.

Select the type of hardware architecture on which your instance will be running:

- **x86-64**: This architecture is known for its broad compatibility with Linux operating systems and Windows distributions. It is commonly used in general purpose computing applications.
- **ARM**: ARM architecture is designed for energy efficiency and low power consumption, which also supports strong performance, making it ideal for high-performance computing tasks. However, ARM instances are compatible with fewer OS distributions.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/17.png" alt="Choose x86-64 or ARM architecture">

Your choice of hardware architecture will affect the available OS options and instance flavors. Choose an OS distribution, a volume, a snapshot, a custom image, or a template from the marketplace.

4. Configure the instance type.

Select the appropriate CPU generation:

- **Intel® Xeon® Scalable, 3rd Gen or 2nd Gen** if you’ve selected x-86-64 architecture at the previous step.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/18.png" alt="VM based on Intel® Xeon® Scalable, 3rd Gen or 2nd Gen">

- **ARM Ampere® Altra® Max Family** if you’ve selected ARM architecture at the previous step.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/19.png" alt="VM based on Ampere® Altra® Max Family">

Choose one of the available flavors.

<expandable-element title="Description of flavors">

*   **Shared**. VMs that share a core of a physical machine with other VMs, designed for workloads that do not require high performance.  
    Availability: Luxembourg
**Note:** The bandwidth limit for the **Shared** flavor is up 100 Mbps, for other configurations it is up 1 Gbps.
*   **Standard**. VMs best suited for a wide range of workloads that require predictable computing performance.  
    Availability: all regions.
*   **vCPU**. CPU Optimized VMs, best suited for CPU-intensive tasks that require predictable computing performance such as batch processing of large data sets and video encoding.  
    Availability: all CORE regions.
*   **Memory**. Memory Optimized VMs, suitable for memory-intensive tasks such as databases, SRM/ERP or data warehouses.  
    Availability: all CORE regions.
*   **High Frequency**. VMs with the high CPU clock rate (3.7 GHz in the basic configuration). It is perfect for applications requiring single-threaded performance, financial and probabilistic analytics, and automation of computational processes.  
    Availability: Luxembourg, Manassas, Frankfurt.
*   **SGX**. VMs that support Intel SGX (Security Guard Extension) that helps to protect data from disclosure or modification by isolating private parts of code and data (enclaves). This configuration is the best for those who store critical, sensitive data in the cloud.  
    Availability: Luxembourg, Manassas, Singapore.
*   **GPU**. VMs with a graphics card, suitable for working with graphic information, deep and machine learning applications, and high-performance computing.  
    Availability: Luxembourg.
*   **GPU-HF**. VMs with the high clock rate of the CPU and with a graphics card, suitable for complex calculations that require graphics accelerator resources, high performance and speed.  
    Availability: Luxembourg.

</expandable-element>

5. Configure **Volumes**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/5-volume-selection.png" alt="Configure Volumes" width=80%>

Enter a volume name, choose its type and set its size in GiB

<expandable-element title="Available volume types">

* **High IOPS SSD**. This is a high-performance SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB). The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.

Availability: Amsterdam, Frankfurt, London, Luxembourg, Luxembourg-2, Manassas, Paris-2, Singapore

* **Standard**. This is a network SSD disk, which provides stable and high random I/O performance, as well as high data reliability (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB). The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.

Availability: all regions

* **Cold**. This is a network HDD disk, suitable for less frequently accessed workloads. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

Availability: Luxembourg

* **Ultra**. This is the network block storage option, recommended for non-critical data and workloads that are accessed less frequently. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

Availability: Luxembourg

* **SSD Low-Latency**. This is an SSD block storage, designed for applications that require low-latency storage and real-time data processing. It can achieve IOPS performance of up to 5000, with an average latency of 300 µs.

Availability: Amsterdam-2, Frankfurt, Hong Kong, Luxembourg-2, Manassas, Tokyo

</expandable-element>

(optional) Add an **Attachment Tag**.

6. Add one or multiple interfaces in Network settings.

If you select a **public** interface, you can turn on the **Use Reserved IP** toggle and assign a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">reserved IP address</a> to your instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/6-public-network-selected.png" alt="Reserved IP toggle" width=80%>

If you select a **private** interface, configure a network and a subnetwork according to the steps below. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/7-private-network-selected.jpg" alt="private interface" width=80%>

To configure a network, select an existing network from the drop-down list or create a new one by clicking **Add a new network**. If you choose the latter, the new window will open:

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/8-create-network-window.png" alt="Add a new network" width=80%>

 * Enter the network name.

 * (optional) Turn on the <b>Bare Metal Network</b> toggle to connect bare metal servers to the network

 * (optional) Turn on the <b>Add tags</b> toggle to add metadata to the network.

 * Click <b>Create network</b>.

To create a subnet, select an existing subnet from the drop-down list or create a new one by clicking **Add a new subnetwork**. If you choose the latter, the new window will open:

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/9-create-subnetwork-window.png" alt="Add a new subnetwork" width=50%>

 * Enter the subnet name.

 * Set CIDR between ranges: 10.0.0.0 - 10.255.255.255, 172.16.0.0—172.31.255.255, 192.168.0.0—192.168.255.255. Set the mask between 16 and 24.

 * (optional) Turn on the <b>Enable DHCP</b> toggle to automatically assign IP addresses to machines in the subnet.

 * (optional) Turn on the <b>Non-routable subnetwork</b> toggle to block access to the subnet from external networks and other subnets. If you keep the network routable, you can specify the **Gateway IP** address. Otherwise, a random IP address will be assigned.

 * (optional) Enter <b>Custom DNS servers</b> to add specific DNS servers**.**

 * optional) Turn on <b>Add tags</b> to add metadata to the subnetwork.

 * Click <b>Create subnetwork</b>.

Optionally, you can turn on the **Use Reserved IP** toggle to assign a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">reserved IP address</a> to your instance and/or turn on the **Use Floating IP** toggle to assign a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">floating IP address</a> to your instance.

7. For **Firewall settings**, select the default firewall or create a new one by clicking **Add firewall**.

![The Firewall settings](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/10-firewall-settings.png)

If you keep the default firewall, the incoming traffic will be allowed over ICMP, TCP (SSH) and RDP protocols.

If you want to create a new firewall, refer to the article: <a href="https://gcore.com/docs/cloud/networking/add-and-configure-a-firewall" target="_blank">Add and configure a firewall</a>.

8. (for a Linux instance) Configure an **SSH key** for a remote SSH connection.

![The SSH key field](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/11-ssh-key.png)

You can add an existing SSH key or generate a new one. You enter a public key and use a private key for connection. For details, see the article: <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">Connect to your instance via SSH</a>.

9. (for a Windows instance) Configure **Access** by setting a password for the Admin user.

![the field for credentials to access a Windows instance](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/12-access-for-windows-instance.png)

Your password must contain between 8 and 16 characters and at least one lowercase letter (a-z), one uppercase letter (A-Z), one number (0-9) and one special character (!#$%&’()\*+,-./:;<=>?@\[\]^_{|}~).

You can connect to a Windows instance <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">from your Control Panel</a> or from your computer over RDP protocol.

10. (optional) Configure **Additional options**.

*   Turn on **User data** to customize your VM during the initial boot by a cloud-init agent.

![The field to add user data](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/13-add-user-data.png)

You can configure your password to connect to your Linux instance <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">from your Control Panel</a> or via SSH. To do it, insert the code below to the **User data** field and enter your password:

```
#cloud-config  
password: **your password**  
chpasswd: { expire: False }  
ssh_pwauth: True
```

**Note:** If an instance is only in a private subnet, DHCP must be enabled in the settings of this subnet, so you can log in with a password.

You can configure the password hash—a machine-readable set of symbols. It’ll protect your real password from being compromised. To generate a hash, use the Python script:

```
#!/usr/bin/env python3  
\# based on [https://stackoverflow.com/a/17992126/117471](https://stackoverflow.com/a/17992126/117471)\# pip3 install passlib  
import sys  
from getpass import getpass  
from passlib.hash import sha512_crypt  
passwd = input() if not sys.stdin.isatty() else getpass()  
print(sha512_crypt.hash(passwd , rounds = 5000 ))
```

*   Turn on **Add tags** to add a key-value pair that form the metadata of the virtual machine description.

![The field to add tags](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/14-add-tags.png)

*   Turn on **Add to placement group** to determine how to place multiple instances.

![The field to add the instance to a placement group](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/15-add-placement-group.png)

<expandable-element title="Types of placement groups">

You can place your virtual machine in one of three types of groups:

- **Affinity** groups assemble virtual machines on the same hardware. Machines launched in one affinity group will exchange data faster because they are located on the same server.

- **Anti-affinity** groups work the opposite way: All virtual machines in this group will be separated across different physical hardware. This increases fault tolerance of a cluster: Even if something happens to one server, machines on the other(s) will remain available.

- **Soft anti-affinity** groups encourage, but don't strictly enforce, the separation of virtual machines. Unlike a strict anti-affinity policy, where machines may never be placed together, soft anti-affinity allows placement on the same hardware when it is necessary due to factors like resource constraints or high demand. It is suitable for users who want to use the anti-affinity policy by default while also avoiding machine creation failures if an unused host was not found.

</expandable-element>

You can add the instance to an existing placement group or create a new one by clicking **Add placement group**.

11. Specify the number of machines with the same configuration you need and give them names.

![The field to set the number of instances](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/16-number-of-instances.png)

The maximum number is limited by your quotas.

For names, use Latin characters, underscores, spaces, and dots.

12. Click **Create virtual machine**.

Your server will be transitioned to the **Building** status. The system will allocate resources for your virtual machine.

After that, the server will be automatically moved to the **Power on** status. Your machine is ready to run!
