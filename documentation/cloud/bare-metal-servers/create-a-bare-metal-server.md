---
title: create-a-bare-metal-server
displayName: Create a Bare Metal server
published: true
order: 20
toc:
pageTitle: Create a Bare Metal Server | Gcore
pageDescription: Create a Bare Metal server in the Cloud for high-performance computing. Customize configurations and connect via SSH.
---
# Create a Bare Metal server

Bare Metal server in the cloud is a machine deployed on dedicated physical hardware for a single tenant.

Physical servers are being managed from the regular Cloud interface, but the virtualization software is not installed on the servers.

## What is the difference between a Virtual Server and a Bare Metal?

A Virtual Server in the cloud does not interact directly with a physical computer; it uses a software layer called a hypervisor. The hypervisor allocates physical computing resources such as CPU, RAM, and Storage for each Virtual Machine (VM). The computing resources for these VMs are allocated from the shared physical hardware on which the created Virtual Server data is deployed. The hypervisor acts as a traffic cop of sorts, directing and allocating the Bare Metal's resources to each of the various new virtual machines, ensuring they don't disrupt each other.

The disadvantage of a Virtual Server is limited performance, which can be critical for some applications.

**Bare Metal** is considered to be a more high-performance solution.

In this case, all physical server resources are allocated to a single user and can provide better performance than a comparable Virtual Server. Resources are not shared, as in the case of Virtual Machine, and the hypervisor level is not required, which allows the application to allocate more computing resources.

Please note that due to the features of the Bare Metal infrastructure, creating a compatible custom image requires a special program to build the image for a physical server and code from a dedicated repository.

We have prepared very detailed instructions with all the necessary files available via the  <a href="https://github.com/G-Core/baremetal-dib-elements" target="_blank">link</a>.

## Create a Bare Metal server

Physical machines are created inside the project. You can use the default project or create a new one (for more information, see the article "How to create and delete a project").

<alert-element type="info" title="Info">
 
**Note**! By default, physical servers are not available for ordering. To create a physical server, you need to request a <a href="https://gcore.com/docs/cloud/getting-started/request-a-quota-increase" target="_blank">quota increase</a>.
 
</alert-element>

Quotas of physical machines are carried out according to the server types: "Basic", "High-frequency", and "Infrastructure". For more information on managing quotas, read the article <a href="https://gcore.com/docs/cloud/getting-started/request-a-quota-increase" target="_blank">"Reqest a quota increase</a>.

To create a Bare Metal:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Bare Metal**.

2\. Click **Create Bare Metal**.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/bare-metal-page.png" alt="Bare metal page in Customer Portal" width="80%">

3\. Select the region.
    
4\.  Select the image to install. You can choose a system from the prepared templates or from custom images that you've previously uploaded. You can find more information about uploading the images in the article <a href="https://gcore.com/docs/cloud/images/upload-an-image-to-the-storage" target="_blank">"Upload an image to the storage"</a>. Consider that only prepared images can be used for Bare Metal servers.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/select-image.png" alt="A menu with available OS images" width="80%">

5\.  Select the server type. Currently, "High-Frequency" and "Infrastructure" servers are available.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/server-type.png" alt="A menu with available server types" width="80%">
    
6\.  Add network interfaces. You can create a public and private interface. 

Consider that after creating a Bare Metal server, you won’t be able to attach an external network to it. Additionally, you can’t attach more than 6 networks to the server. 

If you select a public interface, you can also enable the Use reserved IP toggle and assign a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-reserved-ip-address" target="_blank">reserved IP address</a> to your Bare Metal. 

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/network-section-reserved-ip-highlighted.png" alt="A menu with available network settings and highlighed reserved ip toggle" width="80%">

If you select a **private** interface, configure a network and a subnetwork according to the following steps. 

<alert-element type="info" title="Info">

If you need both a public and private interface, disable the default gateway on the private network's subnetwork and assign a floating IP to the private interface. 

</alert-element>

<tabset-element>

### Configure a network 

If you have created private <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-network" target="_blank">networks</a> before, select the needed network from the dropdown. To add a new network, click **Private network** radio button and configure the network as follows. 

1\. Enter the network name. 

2\. Make sure that the **Bare Metal network** toggle is enabled. This is required to connect Bare Metal servers to the network. 

3\. (optional) Turn on the **Add tags** toggle to add metadata to the network. 

4\. Click **Create network**. 

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/create-network-dialog.png" alt="A menu with available network settings and highlighed reserved ip toggle" width="80%">

5\. (Optional) Enable IPv6 dual-stack to assign both IPv4 and IPv6 addresses for network interfaces of worker nodes and pods. If the Enable IPv6 dual-stack toggle is not available, make sure that at least one pool from your cluster is in a public network. If your Kubernetes cluster is only connected to a private network, you also need to configure and add an IPv6 subnetwork. 

Consider that to activate IPv6 dual-stack, you only need to configure a network interface. Subnetwork will be automatically selected. 

### Configure a subnetwork 

<alert-element type="info" title="Info">

If your Bare Metal has several subnetworks, <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork#set-up-the-default-gateway" target="_blank">ensure that only one subnetwork is routable</a>. Otherwise, there will be a conflict with the default gateway on the server, and you might not be able to connect to the Bare Metal. 

</alert-element>

If you have created <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork" target="_blank">subnetworks</a> before, select the needed subnetwork from the dropdown. If you choose **Automatic**, the system will use one of the existing subnetworks, which has the highest amount of available resources.   

To add a new subnetwork, click **Add a new subnetwork** and configure according to the following instructions: <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork#create-a-subnetwork" target="_blank">Create a subnetwork</a>. 

</tabset-element>

7\. Add an SSH key or generate a new one for a remote connection to a server. For more information about adding a key, read the article <a href="https://gcore.com/docs/cloud/bare-metal-servers/connect-to-your-bare-metal-server-via-ssh" target="_blank">Connect to your Bare Metal via SSH</a>. You can connect via SSH to all machines except Windows servers.
    
<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/ssh-keys.png" alt="A menu with ssh keys settings settings" width="80%"> 

If you select Windows OS, you should set a password for the Admin user. It can contain Latin letters (a-zA-Z), numbers (0-9) and special characters (!#$%&'()*+,-./:;<=>?@[]^_{|}~). Valid length is from 8 to 16 characters. You can connect to the Windows server <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">from the Customer Portal</a> or from your computer using the RDP protocol.
    
<img style="font-size: 15px;" src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/access.png" alt="A menu with access settings" width="80%">

8\. In **Additional options**, you can add metadata for processing by a `cloud-init` agent running on a Virtual Machine. To do it insert your script in the **User data** field.

<img style="font-size: 15px;" src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/user-data.png" alt="A menu with user data settings" width="80%">

For example, you may insert a script that will allow connecting to a Linux server directly <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">from the Customer Portal</a> or <a href="https://gcore.com/docs/cloud/bare-metal-servers/connect-to-your-bare-metal-server-via-ssh" target="_blank">via SSH</a> (this script is not needed to connect to a Windows server). Enter this code with the password chosen by you into the **User data** field:

```    
#cloud-config  
password: **your password**  
chpasswd: { expire: False }  
ssh_pwauth: True
```

Using the specified password you will be able to connect to the server. It is not necessary to specify the password explicitly, you can enter its hash (the same password, only in a converted form; the system will be able to read it, but for a person, it looks like a random set of symbols). Then, even if someone gets into the system, he or she won’t know the password — only the hash will be stored inside. And the system will open its doors only to the user who knows the password.
    
To generate a hash, you can use the Python script:

```    
#!/usr/bin/env python3  
\# based on [https://stackoverflow.com/a/17992126/117471](https://stackoverflow.com/a/17992126/117471)  
\# pip3 install passlib  
import sys  
from getpass import getpass  
from passlib.hash import sha512_crypt  
passwd = input() if not sys.stdin.isatty() else getpass()  
print(sha512_crypt.hash(passwd , rounds = 5000 ))
```

9\. Tags are key-value pairs that form the metadata of the machine description. Also, you can tag your server. To to do it, activate the **Tags** option, and set the necessary ones. 

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/tags.png" alt="A menu with tag settings" width="80%">
    
10\. If you want to create multiple Bare Metal machines with the same configuration, specify the number you want (the maximum is limited by your <a href="https://gcore.com/docs/cloud/getting-started/request-a-quota-increase" target="_blank">quotas</a>) and add names (only Latin characters, underscores, spaces, and dots are allowed). 

To complete the configuration, click **Create server**, and then the server will be deployed in the cloud.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/servers-number.png" alt="A menu with option to choose a number of servers" width="80%">
    
## Limitations of Bare Metal servers

There are several important limitations for Bare Metal servers:

*   You can't add an external volume to the server
*   You can't change the volume configuration
*   It's not possible to add more than 6 networks to the server
*   Once a Bare Metal server is deployed, the private network interface can be attached or detached only manually via the OS.
