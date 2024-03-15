---
title: connect-to-your-instance-via-control-panel
displayName: Connect via Customer Portal
published: true
order: 10
toc:
   --1--Connect to a Windows instance: "connect-to-a-windows-instance"
   --1--Connect to a Linux instance: "connect-to-a-linux-instance"
pageTitle: Connect to a VM via Control Panel | Gcore
pageDescription: Connect to your Linux or Windows machine from the Gcore Control Panel
customUrl: /cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel
---
# Connect to an instance via Customer Portal

You can connect to a virtual instance by using the <a href="https://en.wikipedia.org/wiki/Virtual_Network_Computing" target="_blank">VNC console</a> in the Gcore Customer Portal. This method is available for Windows and Linux instances. It lets you establish a connection even if an instance has no Internet access, which is particularly useful if you need to fix Internet connectivity issues.

Connecting to a Linux instance from the Customer Portal is only possible if you have <a href="https://gcore.com/docs/cloud/virtual-instances/customize-initial-setup-for-your-instance#set-a-password-for-an-instance" target="_blank">configured a password when creating an instance</a>. If you didn't set a password, connect to the instance with SSH keys. 

<tabset-element>

## Connect to a Windows instance

<alert-element type="info" title="Info">
 
On Cloud instances with Windows OS, you can't use the password parameter both in the Access and “User data ” fields. Since the Access field is required, configuring user data on Windows instances is not possible. Read more about the allowed instance parameters in our <a href="https://api.gcore.com/docs/cloud#tag/Instances/operation/InstanceCreateSetV2.post" target="_blank">API docs</a>.
 
</alert-element>

To connect to an instance:

1\. In the Customer Portal, navigate to **Cloud** > **Virtual Instances**.

2\. Find the instance you want to access and click its name to open it.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/cloud-instances.png" alt="A virtual instances tab in the Gcore Customer Portal" width="80%">

3\. Next to your instance's IP address, select the **Access to Console** link.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/windows-access-to-console.png" alt="Overview of a virtual instance with the Access to console link highlighted" width="80%">

4\. The VNC console will open. In the upper-right corner of the screen, select **SendCtrlAltDel**. 

5\. Enter the password you configured during instance creation. The login for all instances is "Admin". 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/windows-login.png" alt="Windows login screen" width="80%">

6\. You've successfully connected to the instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/windows-connected.png" alt="Windows desktop" width="80%"> 

</tabset-element>

<tabset-element>

## Connect to a Linux instance 

If you <a href="https://gcore.com/docs/cloud/virtual-instances/customize-initial-setup-for-your-instance#set-a-password-for-an-instance" target="_blank">didn't set a password</a> when creating a Linux instance, you can't connect to that instance via the Customer Portal. Instead, <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-via-ssh" target="_blank">connect with SSH keys</a>.

<alert-element type="info" title="Info">

If your instance is only in a private subnet, the [Dynamic Host Configuration Protocol (DHCP)](https://gcore.com/docs/cloud/virtual-instances/create-an-instance#enable-DHCP) must be enabled in the settings of this subnet so you can log in with a password. 

</alert-element>

To connect to an instance:

1\. In the Customer Portal, navigate to **Cloud** > **Virtual Instances**.

2\. Find the instance you want to access and click its name to open it.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/cloud-instances.png" alt="A virtual instances tab in the Gcore Customer Portal" width="80%">

3\. Next to your instance's IP address, select the **Access to Console** link.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/linux-access-to-console.png" alt="Overview of a virtual instance with the Access to console link highlighted" width="80%"> 

4\. The VNC console will open. Log in by using the following credentials:

* **login**: this information is displayed next to the **Access to Console** link in the format `[login]@[ip-of your-instance]`. Typically, the login coincides with the name of the OS. For example, `ubuntu`.

* **password**: enter the password you configured in the user data field in the “Additional options” section when creating the instance. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/linux-credentials.png" alt="Ubuntu terminal displaying login information" width="80%">


<alert-element type="tip" title="Tip">
 
If you forgot your password, you can find it inside the system by connecting to the instance via SSH. 

Run the `sudo cat /var/lib/cloud/instance/user-data.txt` command and view a password in the following line: `password: [your password]`. If you entered the password as a hash, you will see the hash on the screen. In this case, you will not be able to find out the password.
 
</alert-element>

5\. You've successfully connected to the instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/linux-connected.png" alt="Ubuntu terminal displaying successful connection to an instance" width="80%">

</tabset-element> 
