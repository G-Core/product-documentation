---
title: create-a-VM
displayName: Create
order: 10
published: true
toc:
   --1--Step 1. Select a region: "step-1-select-a-region"
   --1--Step 2. Configure the image: "step-2-configure-the-image"
   --1--Step 3. Choose the VM type: "step-3-choose-the-vm-type"
   --1--Step 4. Set up volumes: "step-4-set-up-volumes"
   --1--Step 5. Add network interfaces: "step-5-add-network-interfaces"
   --1--Step 6. Configure firewall settings: "step-6-configure-firewall-settings"
   --1--Step 7. Set up authentication: "step-7-set-up-authentication"
   --1--Step 8 (Optional). Configure additional options: "step-8-optional-configure-additional-options"
   --1--Step 9. Specify the number of VMs: "step-9-specify-the-number-of-vms"
   --1--Step 10. Create a VM: "step-10-create-a-vm" 
pageTitle: Create a VM | Gcore
pageDescription: Learn how to create a Linux or Windows Virtual Machine in Gcore Edge Cloud. Start using your Virtual Machine in minutes with ease.
---
# Create a Virtual Machine

Create Linux or Windows Virtual Machines in Gcore Cloud.

## Step 1. Select a region

1\. In the <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Gcore Customer Portal</a>, open **Instances** tab and click **Create Instance**.

![The Create VM button](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/1-create-instancebutton.png)

2\. Choose the region where you want to deploy your Virtual Machine (VM).

![Region selection](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/2-region-selection.png)

Notice that regions are labeled either Core or Edge. This represents the region's equipment specifications.

|                                          | Core                        | Edge*                               |
|------------------------------------------|-----------------------------|-------------------------------------|
| Equipment generation                     | The latest                  | Different                           |
| Designed for high scalability on the fly | Yes                         | Not                                 |
| Available resources                      | 1000 cores and 30 TB of RAM | Up to 300 cores and 1 TB of RAM     |
| Ports for user traffic and storage       | Separate                    | Shared                              |
| Price                                    | Higher                      | Lower                               |


\* Edge regions can be transformed into Core regions. Just [send us a request](mailto:support@gcore.com).

## Step 2. Configure the image

Select the type of hardware architecture on which your VM will be running:

- **x86-64**: This architecture is known for its broad compatibility with Linux operating systems and Windows distributions. It is commonly used in general purpose computing applications.

- **ARM**: ARM architecture is designed for energy efficiency and low power consumption, which also supports strong performance, making it ideal for high-performance computing tasks. However, ARM Virtual Machines are compatible with fewer OS distributions.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/configure-image.png" alt="Choose x86-64 or ARM architecture" width="80%">

Your choice of hardware architecture will affect the available OS options and VM flavors. Choose an OS distribution, a volume, a snapshot, a custom image, or a template from the marketplace.

## Step 3. Choose the VM type

Select the appropriate CPU generation:

- **Intel® Xeon® Scalable, 3rd Gen or 2nd Gen** if you’ve selected x-86-64 architecture at the previous step.

- **ARM Ampere® Altra® Max Family** if you selected ARM architecture in the previous step.

Choose one of the available flavors.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/vm-type.png" alt="VM types and flavors" width="80%">

<expandable-element title="Description of flavors">

*   **Shared**. VMs that share the core of a physical machine with other VMs. They are designed for workloads that don't require high performance.  
    Availability: Luxembourg

<alert-element type="info" title="Info">

 The bandwidth limit for the **Shared** flavor is up 100 Mbps. For other configurations it's up 1 Gbps.

</alert-element>

*   **Standard**. VMs best suited for a wide range of workloads that require predictable computing performance.  
    Availability: all regions.
*   **vCPU**. CPU-optimized VMs. Ideal for CPU-intensive tasks that require predictable computing performance, such as batch processing of large data sets and video encoding.  
    Availability: all Core regions.
*   **Memory**. Memory-optimized VMs. Suitable for memory-intensive tasks such as databases, SRM/ERP or data warehouses.  
    Availability: all Core regions.
*   **High Frequency**. VMs with a high CPU clock rate (3.7 GHz in the basic configuration). Ideal for applications requiring single-threaded performance, financial and probabilistic analytics, and automation of computational processes.  
    Availability: Luxembourg, Manassas, Frankfurt.
*   **SGX**. VMs that support Intel SGX (Security Guard Extension) that helps to protect data from disclosure or modification by isolating private parts of code and data (enclaves). The best option for storing critical or sensitive data in the cloud.  
    Availability: Luxembourg, Manassas, Singapore.
*   **GPU**. VMs with a graphics card. Suitable for working with graphic information, deep and machine learning applications, and high-performance computing.  
    Availability: Luxembourg.
*   **GPU-HF**. VMs with a high clock rate of the CPU and with a graphics card, suitable for complex calculations that require graphics accelerator resources, high performance, and speed.  
    Availability: Luxembourg.

</expandable-element>

## Step 4. Set up volumes

Enter a volume name, choose its type, and set its size in GiB.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/add-volume.png" alt="Configure Volumes" width="80%">

<expandable-element title="Available volume types">

* **High IOPS SSD**. High-performance SSD block storage designed for latency-sensitive transactional workloads (60 IOPS per 1 GiB; 2.5 MB/s per 1 GiB). The IOPS performance limit is 9,000. The bandwidth limit is 500 MB/s.

Availability: Amsterdam, Frankfurt, London, Luxembourg, Luxembourg-2, Manassas, Paris-2, Singapore

* **Standard**. Network SSD disk, which provides stable and high random I/O performance, as well as high data reliability (6 IOPS per 1 GiB; 0.4 MB/s per 1 GiB). The IOPS performance limit is 4,500. The bandwidth limit is 300 MB/s.

Availability: all regions

* **Cold**. Network HDD disk, suitable for less frequently accessed workloads. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

Availability: Luxembourg

* **Ultra**. Network block storage option, recommended for non-critical data and workloads that are accessed less frequently. The maximum number of IOPS is 1,000. The bandwidth limit is 100 MB/s.

Availability: Luxembourg

* **SSD Low-Latency**. SSD block storage, designed for applications that require low-latency storage and real-time data processing. It can achieve IOPS performance of up to 5000, with an average latency of 300 µs.

Availability: Amsterdam-2, Frankfurt, Hong Kong, Luxembourg-2, Manassas, Tokyo

</expandable-element>

(optional) Add an **Attachment Tag**.

## Step 5. Add network interfaces

If you select a **public** interface, you can turn on the **Use reserved IP** toggle and assign a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">reserved IP address</a> to your VM. Enable the **IPv6 dual-stack** toggle to use IPv6 addresses. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/use-reserved-ip.png" alt="Network settings with highlighted Reserved IP toggle" width="60%">

If you select a **private** interface, configure a network and a subnetwork according to the following steps. 

<alert-element type="info" title="Info">
 
If you need both a public and private interface, disable the default gateway on the private network's subnetwork and assign a floating IP to the private interface.

</alert-element>

<tabset-element>

### Configure a network

Select an existing network from the dropdown list or create a new one by clicking **Add a new network**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/add-new-network.png" alt="Private interface with highlighted Add a new network link" width="60%">

If you choose to add a new network, a new window will open where you'll configure the network settings:

1\. Enter the network name.

2\. (optional) Turn on the <b>Use reserved IP</b> toggle if you want to assign a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">reserved IP address</a> to the Virtual Machine. Select the desired IP from the list.

3\. (optional) Turn on the <b>Use floating IP</b> toggle if you want to assign a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">floating IP address</a> and receive incoming connections to the VM.

4\. (optional) Turn on the <b>Enable IPv6 dual-stack</b> toggle to use IPv6 addresses. 

5\. Click <b>Create network</b>.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/create-network.png" alt="Add a new network" width="60%">

### Configure a subnetwork

<alert-element type="info" title="Info">
 
If your VM has several subnetworks, <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork#set-up-the-default-gateway" target="_blank"> ensure that only one subnetwork is routable</a>. Otherwise, there will be a conflict with the default gateway on the server, and you might not be able to connect to the VM. 

</alert-element>

Select an existing subnetwork from the dropdown list or create a new one by clicking **Add a new subnetwork**. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/add-new-subnetwork.png" alt="Add a new subnetwork" width="60%">

If you choose to add a new subnetwork,  a new window will open where you'll configure the subnetwork settings:

1\. Enter the subnetwork name.

2\. Set CIDR between ranges: 10.0.0.0 - 10.255.255.255, 172.16.0.0—172.31.255.255, 192.168.0.0—192.168.255.255. Set the mask between 16 and 29.

<p id="enable-DHCP"> 3. (optional) Turn on the <b>Enable DHCP</b> toggle to assign IP addresses to machines in the subnet automatically.</p>

4\. (optional) Turn on the **Non-routable subnetwork** toggle to block access to the subnet from external networks and other subnets. If you keep the network routable, you can specify the **Gateway IP** address. Otherwise, a random IP address will be assigned.

5\. (optional) Enter **Custom DNS servers** to add specific DNS servers.

6\. (optional) Turn on **Add tags** to add metadata to the subnetwork.

7\. Click **Create subnetwork**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create/create-subnetwork-annotated.png" alt="Add a new subnetwork dialog" width="60%">

<alert-element type="tip" title="Tip">

Optionally, you can turn on the **Use Reserved IP** toggle to assign a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">reserved IP address</a> to your VM and turn on the **Use Floating IP** toggle to assign a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">floating IP address</a>.

</alert-element>

</tabset-element>

## Step 6. Configure firewall settings

For **Firewall settings**, select the default firewall or create a new one by clicking **Add firewall**.

![The Firewall settings](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/10-firewall-settings.png)

If you keep the default firewall, the incoming traffic will be allowed over ICMP, TCP (SSH), and RDP protocols.

If you want to create a new firewall, refer to our article on <a href="https://gcore.com/docs/cloud/networking/add-and-configure-a-firewall" target="_blank">adding and configuring a firewall</a>.

## Step 7. Set up authentication

<tabset-element>

### Linux Virtual Machine 

Configure an SSH key for a remote SSH connection. You can add an existing SSH key or generate a new one. For instructions on how to generate and configure the key, check out this guide: <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-via-ssh" target="_blank">Connect to a VM via SSH</a>.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/11-ssh-key.png" alt="SSH keys section with three options: select, generate, or add a new SSH key" width="80%"> 

In addition to SSH keys, you can also set up a password for your Virtual Machine, as described in [step 9](#configure-user-data). Setting a password is necessary if you want to connect to a Linux VM <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel#connect-to-a-linux-instance" target="_blank">from the Customer Portal</a>. 

### Windows Virtual Machine 

Configure **Access** by setting a password for the Admin user.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/12-access-for-windows-instance.png" alt="Access field with a password" width="80%"> 

<alert-element type="info" title="Info">

Your password must contain between 8 and 16 characters, including at least one lowercase letter (a-z), one uppercase letter (A-Z), one number (0-9), and one special character (!#$%&’()\*+,-./:;<=>?@\[\]^_{|}~).

</alert-element>

You can use the password to connect to a Windows VM from the <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">Gcore Customer Portal</a> or from your computer using RDP (Remote Desktop Protocol).

</tabset-element> 

## Step 8 (optional). Configure additional options

<p id="configure-user-data">Enable the <strong>User data</strong> toggle to customize your VM during the initial boot by a <code>cloud-init</code> agent.</p>

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/13-add-user-data.png" alt="User data field with password configuration" width="80%"> 

You can configure your password to connect to your Linux VM <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">from the Customer Portal</a> or <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-via-ssh" target="_blank">via SSH</a>. To do so, insert the following code to the field, replacing `**your password**` with your chosen password:

```
#cloud-config  
password: **your password**  
chpasswd: { expire: False }  
ssh_pwauth: True
```

<alert-element type="info" title="Info">

On Cloud VMs with Windows OS, you can't use the `password` parameter both in the “Access” and “User data” fields. Since the "Access" field is required, configuring user data on Windows Virtual Machines is not possible. 

Read more about the allowed VM parameters in our <a href="https://api.gcore.com/docs/cloud#tag/Instances/operation/InstanceCreateSetV2.post" target="_blank">API docs</a>.

</alert-element>

<expandable-element title="Configure a password hash">

You can configure the password hash, a machine-readable set of symbols. It’ll protect your real password from being compromised. To generate a hash, use the Python script:

```
#!/usr/bin/env python3  
\# based on [https://stackoverflow.com/a/17992126/117471](https://stackoverflow.com/a/17992126/117471)\# pip3 install passlib  
import sys  
from getpass import getpass  
from passlib.hash import sha512_crypt  
passwd = input() if not sys.stdin.isatty() else getpass()  
print(sha512_crypt.hash(passwd , rounds = 5000 ))
```

</expandable-element>

<alert-element type="warning" title="Warning">

If a VM is only in a private subnet, DHCP must be enabled in the settings of this subnet, so you can log in with a password.

</alert-element>

*   Turn on **Add tags** to add a key-value pair that forms the metadata of the Virtual Machine description.

![The field to add tags](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/14-add-tags.png)

*   Turn on **Add to placement group** to determine how to place multiple VMs.

![The field to add the VM to a placement group](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/15-add-placement-group.png)

<expandable-element title="Types of placement groups">

You can place your VM in one of three types of groups:

- **Affinity** groups assemble virtual machines on the same hardware. Machines launched in one affinity group will exchange data faster because they are located on the same server.

- **Anti-affinity** groups work the opposite way: All Virtual Machines in this group will be separated across different physical hardware. This increases fault tolerance of a cluster: Even if something goes wrong with one server, machines on the other servers will remain available.

- **Soft anti-affinity** groups encourage, but don't strictly enforce, the separation of Virtual Machines. Unlike a strict anti-affinity policy, where machines may never be placed together, soft anti-affinity allows placement on the same hardware when it is necessary due to factors like resource constraints or high demand. It is suitable for users who want to use the anti-affinity policy by default while also avoiding machine creation failures if an unused host is not found.

</expandable-element>

You can add the VM to an existing placement group or create a new one by clicking **Add placement group**.

## Step 9. Specify the number of VMs 

Indicate how many machines with the same configuration you need and name the VMs.

![The field to set the number of instances](https://assets.gcore.pro/docs/cloud/virtual-instances/create-an-instance/16-number-of-instances.png)

The maximum number is limited by your quotas.

For names, use Latin characters, underscores, spaces, and dots.

## Step 10. Create a VM 

Click **Create virtual machine**.

Your server will be transitioned to the **Building** status. The system will allocate resources for your Virtual Machine.

After that, the server will be automatically moved to the **Power on** status. Your machine is ready to run!