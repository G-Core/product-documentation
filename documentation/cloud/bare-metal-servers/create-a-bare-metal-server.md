---
title: create-a-bare-metal-server
displayName: Create a bare metal server
published: true
toc:
---
# Create a bare metal server

**Bare metal** in the cloud is a machine deployed on dedicated physical hardware for a single tenant.

Physical servers are being managed from the regular Cloud interface, but the virtualization software is not installed on the servers.

## **What is the difference between a virtual server and a Bare metal server?**

**A virtual server** in the cloud does not interact directly with a physical computer; it uses a software layer called a hypervisor. The hypervisor allocates physical computing resources such as CPU, RAM, and Storage for each instance. The computing resources for these instances are allocated from the shared physical hardware on which the created virtual server data is deployed. The hypervisor acts as a traffic cop of sorts, directing and allocating the bare metal's resources to each of the various new virtual machines, ensuring they don't disrupt each other.

The disadvantage of a virtual server is limited performance, which can be critical for some applications.

**Bare metal** is considered to be a more high-performance solution.

In this case, all physical server resources are allocated to a single user and can provide better performance than a comparable virtual server. Resources are not shared, as in the case of instance, and the hypervisor level is not required, which allows the application to allocate more computing resources.

#### **Please, note! Bare metal images:**

Due to the features of the Bare metal infrastructure, creating a compatible custom image requires a special program to build the image for a physical server and code from a dedicated repository.

We have prepared very detailed instructions with all the necessary files available via the link [https://github.com/G-Core/baremetal-dib-elements](https://github.com/G-Core/baremetal-dib-elements)

## **Create a bare metal server in the Cloud**

Physical machines are created inside the project. You can use the default project or create a new one (for more information, see the article "How to create and delete a project").

**Note**! By default, physical servers are not available for ordering. To create a physical server, you need to request a [quota](https://support.gcore.com/hc/en-us/articles/360002420957) change.

Quotas of physical machines are carried out according to the server types - “Basic”, “High-frequency”, “Infrastructure”. For more information on managing quotas, see the "[Quotas](https://support.gcore.com/hc/en-us/articles/360002420957)" article.

Go inside the project, section "Baremetal" → "Create Baremetal Server".

<img src="https://support.gcore.com/hc/article_attachments/360014351917/1._________________.png" alt="1._________________.png">

You will see the page for configuring and creating a new server

1.  Select the region to create the machine in. Regions, where Baremetal is available for order, are highlighted.
    
2.  Select the image to install. You can choose a system from the prepared templates or from custom images that you've previously uploaded. You can find more information about uploading the images in the "[Images](https://support.gcore.com/hc/en-us/articles/360002429818)" article. Please, note! Only prepared images can be used for Bare metal servers (for more information, see the section Bare metal images)<img src="https://support.gcore.com/hc/article_attachments/360020173678/mceclip3.png" alt="mceclip3.png"><img src="https://support.gcore.com/hc/article_attachments/360014438398/4._____________.png" alt="4._____________.png">
    
3.  Select the server type. Currently, "High-Frequency" and "Infrastructure" servers are available.

<img src="https://support.gcore.com/hc/article_attachments/360014352117/5.____________.png" alt="5.____________.png">
    
4.  Add network interfaces. You can create a public and private interface. 

<img src="https://support.gcore.com/hc/article_attachments/360014352257/6.__________.png" alt="6.__________.png">

If you have created [networks before](https://support.gcorelabs.com/hc/ru/articles/360002703678), select the created network from the drop-down list. To create a new network, click on the Add a new network button, and enter the network name. **Note!** While creating a network you need to select the "Baremetal Network" (VLAN) option. 
    
<img src="https://support.gcore.com/hc/article_attachments/360014438738/7.__________.png" alt="7.__________.png">                            

After creating a network, you should configure a subnet (address range for machines in the cloud). If you have early created [subnets,](https://support.gcorelabs.com/hc/en-us/articles/360002703678-Networks-Subnetworks-Floating-IPs-Firewalls) select the created subnet from the drop-down list.
    
To create a new subnet, click on the Add a new subnetwork button, enter the subnet name, and set the CIDR range for the subnet (the valid range for the subnet mask is: 16-24): 
    
    *   10.0.0.0 - 10.255.255.255
    *   172.16.0.0 - 172.31.255.255
    *    192.168.0.0 - 192.168.255.255
    
Only private IPv4 addresses can be used in subnets. 

<img src="https://support.gcore.com/hc/article_attachments/360014352477/8._Subnet.png" alt="8._Subnet.png">
    
**Please, note!** After creating a Baremetal server, you will not be able to attach an external network to it. You can not attach more than 6 networks to the server. 
    
5. Add an SSH key or generate a new one for a remote connection to a server. For more information about adding a key, see the [Connect to Instance or Bare Metal server via SSH article](https://support.gcorelabs.com/hc/en-us/articles/360019377137). You connect via SSH to all machines except Windows servers.
    
<img src="https://support.gcore.com/hc/article_attachments/360014352577/9._SSH.png" alt="9._SSH.png"> 

If you select Windows Server OS, you should set a password for the Admin user. It can contain Latin letters (a-zA-Z), numbers (0-9) and special characters (!#$%&'()\*+,-./:;<=>?@\[\]^\_{|}~). Valid length is from 8 to 16 characters. You can connect to the Windows server [from Control Panel](https://support.gcorelabs.com/hc/en-us/articles/360020733518) or from your computer using the RDP protocol.
    
<img style="font-size: 15px;" src="https://support.gcore.com/hc/article_attachments/360014438858/10._Admin.png" alt="10._Admin.png">

6. In "Additional options", you can add metadata for processing by a cloud-init agent running on a virtual machine. To do it insert your script in the "User data" field.

 <img src="https://support.gcore.com/hc/article_attachments/360014352657/11._User_data.png" alt="11._User_data.png">

For example, you may insert a script that will allow connecting to a Linux server [directly from your Control Panel](https://support.gcorelabs.com/hc/en-us/articles/360020733518) or [via SSH using a password](https://support.gcorelabs.com/hc/en-us/articles/360019377137) (this script is not needed to connect to a Windows server). Enter this code with the password chosen by you into the User data field:
    
#cloud-config  
password: **your password**  
chpasswd: { expire: False }  
ssh\_pwauth: True
    
Using the specified password you will be able to connect to the server. It is not necessary to specify the password explicitly, you can enter its hash (the same password, only in a converted form; the system will be able to read it, but for a person, it looks like a random set of symbols). Then, even if someone gets into the system, he or she won’t know the password — only the hash will be stored inside. And the system will open its doors only to the user who knows the password.
    
To generate a hash, you can use the Python script:
    
#!/usr/bin/env python3  
\# based on [https://stackoverflow.com/a/17992126/117471](https://stackoverflow.com/a/17992126/117471)  
\# pip3 install passlib  
import sys  
from getpass import getpass  
from passlib.hash import sha512\_crypt  
passwd = input() if not sys.stdin.isatty() else getpass()  
print(sha512\_crypt.hash(passwd , rounds = 5000 ))
    
7. Tags are key-value pairs that form the metadata of the machine description. Also, you can tag your server. To to do it, activate the Tags option, and set the necessary ones. Tags are key-value pairs that form the metadata of the Baremetal machine description.<img src="https://support.gcore.com/hc/article_attachments/360014438918/12._Tags.png" alt="12._Tags.png">
    
8. If you want to create multiple Baremetal machines with the same configuration, specify the number you want (the maximum is limited by your [quotas)](https://support.gcorelabs.com/hc/ru/articles/360002420957) and add names (only Latin characters, underscores, spaces, and dots are allowed). To complete the configuration, click on "Create server" button, and then the server will be deployed in the cloud.

<img src="https://support.gcore.com/hc/article_attachments/360014438958/13._Create.png" alt="13._Create.png">
    

### **Features of Baremetal servers**

There are several important limitations for Baremetal servers :

*   You can not add an external Volume to the server
*   You can not change the Volume configuration
*   You can not add more than 6 networks to the server
*   After the Bare metal server was deployed, the private network interface can be attached/detached only manually via the OS
