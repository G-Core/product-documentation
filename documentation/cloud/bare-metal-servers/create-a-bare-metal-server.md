---
title: create-a-bare-metal-server
displayName: Create a bare metal server
published: true
order: 20
toc:
pageTitle: Create a bare metal server | Gcore
pageDescription: Create a bare metal server in the Cloud for high-performance computing. Customize configurations and connect via SSH.
---
# Create a bare metal server

**Bare metal server** in the cloud is a machine deployed on dedicated physical hardware for a single tenant.

Physical servers are being managed from the regular Cloud interface, but the virtualization software is not installed on the servers.

## What is the difference between a virtual server and a Bare metal server?

**A virtual server** in the cloud does not interact directly with a physical computer; it uses a software layer called a hypervisor. The hypervisor allocates physical computing resources such as CPU, RAM, and Storage for each instance. The computing resources for these instances are allocated from the shared physical hardware on which the created virtual server data is deployed. The hypervisor acts as a traffic cop of sorts, directing and allocating the bare metal's resources to each of the various new virtual machines, ensuring they don't disrupt each other.

The disadvantage of a virtual server is limited performance, which can be critical for some applications.

**Bare Metal** is considered to be a more high-performance solution.

In this case, all physical server resources are allocated to a single user and can provide better performance than a comparable virtual server. Resources are not shared, as in the case of instance, and the hypervisor level is not required, which allows the application to allocate more computing resources.

Please note that due to the features of the bare metal infrastructure, creating a compatible custom image requires a special program to build the image for a physical server and code from a dedicated repository.

We have prepared very detailed instructions with all the necessary files available via the  <a href="https://github.com/G-Core/baremetal-dib-elements" target="_blank">link</a>.

## Create a bare metal server

Physical machines are created inside the project. You can use the default project or create a new one (for more information, see the article "How to create and delete a project").

**Note**! By default, physical servers are not available for ordering. To create a physical server, you need to request a <a href="https://gcore.com/docs/cloud/getting-started/request-a-quota-increase" target="_blank">quota increase</a>.

Quotas of physical machines are carried out according to the server types - "Basic", "High-frequency", "Infrastructure". For more information on managing quotas, see the article <a href="https://gcore.com/docs/cloud/getting-started/request-a-quota-increase" target="_blank">"Reqest a quota increase</a>..

Go inside the project, section **Bare Metal Servers** → **Create Bare Metal Server**.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/1._________________.png" alt="1._________________.png">

You will see the page for configuring and creating a new server.

1.  Select the region.
    
2.  Select the image to install. You can choose a system from the prepared templates or from custom images that you've previously uploaded. You can find more information about uploading the images in the article <a href="https://gcore.com/docs/cloud/images/upload-an-image-to-the-storage" target="_blank">"Upload an image to the storage"</a>. Please note that only prepared images can be used for bare metal servers.

<media-gallery>
<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/mceclip3.png" alt="mceclip3.png">

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/4._____________.png" alt="4._____________.png">
</media-gallery>

3.  Select the server type. Currently, "High-Frequency" and "Infrastructure" servers are available.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/5.____________.png" alt="5.____________.png">
    
4.  Add network interfaces. You can create a public and private interface. 

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/6.__________.png" alt="6.__________.png">

If you have created <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-network" target="_blank">networks</a> before, select the created network from the drop-down list. To create a new network, click on the Add a new network button, and enter the network name. **Note!** While creating a network you need to select the **Bare Metal Network** (VLAN) option. 
    
<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/7.__________.png" alt="7.__________.png">                            

After creating a network, you should configure a subnet (address range for machines in the cloud). If you have early created <a href="https://gcore.com/docs/cloud/networking/create-and-manage-a-subnetwork" target="_blank">subnets</a>, select the created subnet from the drop-down list.
    
To create a new subnet, click on the Add a new subnetwork button, enter the subnet name, and set the CIDR range for the subnet (the valid range for the subnet mask is: 16-24): 
    
    *   10.0.0.0 - 10.255.255.255
    *   172.16.0.0 - 172.31.255.255
    *    192.168.0.0 - 192.168.255.255
    
Only private IPv4 addresses can be used in subnets. 

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/8._Subnet.png" alt="8._Subnet.png">
    
Please note that after creating a bare metal server, you will not be able to attach an external network to it. You can not attach more than 6 networks to the server. 
    
5. Add an SSH key or generate a new one for a remote connection to a server. For more information about adding a key, see the article <a href="https://gcore.com/docs/cloud/bare-metal-servers/connect-to-your-bare-metal-server-via-ssh" target="_blank">"Connect to your bare metal server via SSH"</a>. You can connect via SSH to all machines except Windows servers.
    
<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/9._SSH.png" alt="9._SSH.png"> 

If you select Windows Server OS, you should set a password for the Admin user. It can contain Latin letters (a-zA-Z), numbers (0-9) and special characters (!#$%&'()*+,-./:;<=>?@[]^_{|}~). Valid length is from 8 to 16 characters. You can connect to the Windows server <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">from your Control Panel</a> or from your computer using the RDP protocol.
    
<img style="font-size: 15px;" src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/10._Admin.png" alt="10._Admin.png">

6. In "Additional options", you can add metadata for processing by a cloud-init agent running on a virtual machine. To do it insert your script in the "User data" field.

 <img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/11._User_data.png" alt="11._User_data.png">

For example, you may insert a script that will allow connecting to a Linux server directly <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">from your Control Panel</a> or <a href="https://gcore.com/docs/cloud/bare-metal-servers/connect-to-your-bare-metal-server-via-ssh" target="_blank">via SSH</a> (this script is not needed to connect to a Windows server). Enter this code with the password chosen by you into the User data field:

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

7. Tags are key-value pairs that form the metadata of the machine description. Also, you can tag your server. To to do it, activate the Tags option, and set the necessary ones. Tags are key-value pairs that form the metadata of the bare metal machine description.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/12._Tags.png" alt="12._Tags.png">
    
8. If you want to create multiple bare metal machines with the same configuration, specify the number you want (the maximum is limited by your <a href="https://gcore.com/docs/cloud/getting-started/request-a-quota-increase" target="_blank">quotas</a>) and add names (only Latin characters, underscores, spaces, and dots are allowed). To complete the configuration, click on "Create server" button, and then the server will be deployed in the cloud.

<img src="https://assets.gcore.pro/docs/cloud/bare-metal-servers/create-a-bare-metal-server/13._Create.png" alt="13._Create.png">
    

## Features of bare metal servers

There are several important limitations for bare metal servers:

*   You can not add an external Volume to the server
*   You can not change the Volume configuration
*   You can not add more than 6 networks to the server
*   Once a bare metal server is deployed, the private network interface can be attached/detached only manually via the OS
