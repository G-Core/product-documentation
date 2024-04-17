---
title: connect-to-your-instance-via-control-panel
displayName: Connect via Customer Portal
published: true
order: 10
toc:
   --1--Connect to a Windows instance: "connect-to-a-windows-instance"
   --1--Connect to a Linux instance: "connect-to-a-linux-instance"
pageTitle: Connect to a VM via Customer Portal | Gcore
pageDescription: Connect to your Linux or Windows VM from the Gcore Customer Portal
customUrl: /cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel
---
# Connect to a VM via the Gcore Customer Portal

You can connect to a Gcore Virtual Machine by using the <a href="https://en.wikipedia.org/wiki/Virtual_Network_Computing" target="_blank">VNC console</a> in the Gcore Customer Portal. This method is available for Windows and Linux VMs. The method allows you to establish a connection even if a VM has no internet access, which is particularly useful if you are experiencing internet connectivity issues.

Connecting to a Linux instance from the Gcore Customer Portal is only possible if you have <a href="https://gcore.com/docs/cloud/virtual-instances/customize-initial-setup-for-your-instance#set-a-password-for-an-instance" target="_blank">configured a password when creating the VM</a>. If you didn't set a password, you'll need to connect to the VM using SSH keys. 

<tabset-element>

## Connect to a Windows VM

<alert-element type="info" title="Info">
 
On Gcore Edge Cloud VMs with Windows OS, you can't use the password parameter both in the Access and “User data” fields. Since the Access field is required, configuring user data on a Windows VM is not possible. Read more about permitted VM parameters in our <a href="https://api.gcore.com/docs/cloud#tag/Instances/operation/InstanceCreateSetV2.post" target="_blank">API docs</a>.
 
</alert-element>

To connect to a VM:

1\. In the Customer Portal, navigate to **Cloud** > **Virtual Instances**.

2\. Find the VM you want to access and click its name to open it.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/cloud-instances.png" alt="A virtual instances tab in the Gcore Customer Portal" width="80%">

3\. Next to your VM's IP address, select the **Access to Console** link.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/windows-access-to-console.png" alt="Overview of a virtual instance with the Access to console link highlighted" width="80%">

4\. The VNC console will open. In the upper-right corner of the screen, click **SendCtrlAltDel**. 

5\. Enter the password you configured during VM creation. The login for all VMs is "Admin". 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/windows-login.png" alt="Windows login screen" width="80%">

You've successfully connected to the VM.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/windows-connected.png" alt="Windows desktop" width="80%"> 

## Connect to a Linux VM 

If you <a href="https://gcore.com/docs/cloud/virtual-instances/customize-initial-setup-for-your-instance#set-a-password-for-an-instance" target="_blank">didn't set a password</a> when creating a Linux VM, you can't connect to that VM via the Gcore Customer Portal. Instead, <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-via-ssh" target="_blank">connect with SSH keys</a>.

<alert-element type="info" title="Info">

If your VM is located only in a private subnet, the <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance#enable-DHCP" target="_blank">Dynamic Host Configuration Protocol</a> must be enabled in the settings of this subnet so you can log in with a password. 

</alert-element>

To connect to a VM:

1\. In the Gcore Customer Portal, navigate to **Cloud** > **Virtual Instances**.

2\. Find the VM you want to access and click its name to open it.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/cloud-instances.png" alt="A virtual instances tab in the Gcore Customer Portal" width="80%">

3\. Next to your VM's IP address, select the **Access to Console** link.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/linux-access-to-console.png" alt="Overview of a virtual instance with the Access to console link highlighted" width="80%"> 

4\. The VNC console will open. Log in using the following credentials:

* **login**: This information is displayed next to the **Access to Console** link in the format `[login]@[ip-of your-VM]`. Typically, the login is the same as the name of the OS. For example, `ubuntu`.

* **password**: Enter the password you configured in the user data field in the “Additional options” section when creating the VM. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/linux-credentials.png" alt="Ubuntu terminal displaying login information" width="80%">

<alert-element type="tip" title="Tip">
 
If you forgot your password, you can find it in the system by connecting to the VM via SSH. 

Run the `sudo cat /var/lib/cloud/instance/user-data.txt` command and view a password in the following line: `password: [your password]`. If you entered the password as a hash, you will see the hash on the screen. In this case, you will not be able to check the password.
 
</alert-element>

You've successfully connected to the VM.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/linux-connected.png" alt="Ubuntu terminal displaying successful connection to an instance" width="80%">

</tabset-element> 
