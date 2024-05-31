---
title: connect-to-your-instance-via-control-panel
displayName: Connect via Customer Portal
published: true
order: 10
toc:
   --1--Connect to a Windows instance: "connect-to-a-windows-virtual-machine"
   --1--Connect to a Linux instance: "connect-to-a-linux-virtual-machine"
pageTitle: Connect to a VM via Customer Portal | Gcore
pageDescription: Connect to your Linux or Windows virtual machine from the Gcore Customer Portal
customUrl: /cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel
---
# Connect to a virtual machine via the Gcore Customer Portal

You can connect to a Gcore Virtual Machine (VM) by using the <a href="https://en.wikipedia.org/wiki/Virtual_Network_Computing" target="_blank">VNC console</a> in the Gcore Customer Portal. This method is available for Windows and Linux VMs. The method allows you to establish a connection even if a virtual machine has no internet access, which is useful if you experience internet connectivity issues.

Connecting to a Linux Virtual Machine from the Gcore Customer Portal is only possible if you have <a href="https://gcore.com/docs/cloud/virtual-instances/customize-initial-setup-for-your-instance#set-a-password-for-an-instance" target="_blank">configured a password while creating a Virtual Machine</a>. If you didn't set a password, you'll need to connect to the VM using SSH keys. 

<tabset-element>

## Connect to a Windows virtual machine

<alert-element type="info" title="Info">
 
On virtual machines with Windows OS, you can't use the password parameter both in the Access and “User data” fields. Since the Access field is required, configuring user data on a Windows VM is not possible. Read more about the permitted VM parameters in our <a href="https://api.gcore.com/docs/cloud#tag/Instances/operation/InstanceCreateSetV2.post" target="_blank">API docs</a>.
 
</alert-element>

To connect to a virtual machine:

1\. In the Customer Portal, navigate to **Cloud** > **Virtual Instances**.

2\. Find the VM you want to access and click its name to open it.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/cloud-instances.png" alt="A virtual instances tab in the Gcore Customer Portal" width="80%">

3\. Next to your VM's IP address, select the **Access to Console** link. The VNC console will open.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/windows-access-to-console.png" alt="Overview of a Virtual Machine with the Access to console link highlighted" width="80%">

4\. In the top-right corner of the screen, click **SendCtrlAltDel**. 

5\. Enter the password you configured during VM creation. The login for all VMs is "Admin". 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/windows-login.png" alt="Windows login screen" width="80%">

You've successfully connected to the VM.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/windows-connected.png" alt="Windows desktop" width="80%"> 

## Connect to a Linux virtual machine

If you <a href="https://gcore.com/docs/cloud/virtual-instances/customize-initial-setup-for-your-instance#set-a-password-for-an-instance" target="_blank">didn't set a password</a> when creating a Linux VM, you can't connect to that VM via the Gcore Customer Portal. Instead, <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-via-ssh" target="_blank">connect with SSH keys</a>.

<alert-element type="info" title="Info">

If your VM is located only in a private subnet, the <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance#enable-DHCP" target="_blank">Dynamic Host Configuration Protocol</a> must be enabled in the settings of this subnet so you can log in with a password. 

</alert-element>

To connect to a virtual machine:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Virtual Instances**.

2\. Find the VM you want to access and click its name to open it.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/cloud-instances.png" alt="A virtual instances tab in the Gcore Customer Portal" width="80%">

3\. Next to your VM's IP address, select the **Access to Console** link. The VNC console will open.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/linux-access-to-console.png" alt="Overview of a Virtual Machine with the Access to console link highlighted" width="80%"> 

4\. Log in using the following credentials:

* **login**: This information is displayed next to the **Access to Console** link in the format `[login]@[ip-of your-VM]`. Typically, the login is the same as the name of the OS. For example, `ubuntu`.

* **password**: Enter the password you configured in the user data field in the “Additional options” section when creating the instance. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/linux-credentials.png" alt="Ubuntu terminal displaying login information" width="80%">

<alert-element type="tip" title="Tip">
 
If you forgot your password, you can find it in the system by connecting to the virtual machine via SSH. 

Run the `sudo cat /var/lib/cloud/instance/user-data.txt` command and view a password in the following line: `password: [your password]`. If you entered the password as a hash, you will see the hash on the screen. In this case, you will not be able to check the password.
 
</alert-element>

You've successfully connected to the virtual machine.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/linux-connected.png" alt="Ubuntu terminal displaying successful connection to an instance" width="80%">

</tabset-element> 
