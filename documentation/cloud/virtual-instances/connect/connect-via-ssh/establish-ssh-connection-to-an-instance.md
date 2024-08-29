---
title: establish-ssh-connection-to-an-instance
displayName: Establish SSH connection to a Virtual Machine
order: 30
published: true
toc:
   --1--Connect from Terminal, Command Prompt, or WSL: "connect-from-terminal-command-prompt-or-wsl"
   --1--Connect with PuTTY: "connect-with-putty"
   --1--Connect via OpenSSH: "connect-via-openssh"
---

# Establish SSH connection to a Virtual Machine 

After you generate a pair of SSH keys and ensure that a public key is available in the Gcore Customer Portal, you can use these keys to connect to your instance.

Before you proceed with the connection steps, make sure that:

- If your Virtual Machine is only connected to a private network, it has a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">floating IP address</a>. 
- You have set up the <a href="https://gcore.com/docs/cloud/networking/add-and-configure-a-firewall#use-the-default-firewall" target="_blank">necessary protocols in firewall settings</a> to allow outgoing and incoming connections to an instance. 

## Connect from Terminal, Command Prompt, or WSL

Follow these instructions to connect to a Virtual Machine from Linux, macOS, or Windows 10/11 devices:

1\. Open Terminal (Linux, macOS), Windows Subsystem for Linux, or Command Prompt (cmd.exe on Windows OS).

2\. Connect to your Virtual Machine in one of the following ways:

* To connect using a pair of SSH keys, run the following command: 

```
ssh -i ~/path/to/your/private-key username@public-ip-of-your-instance
``` 

For example:  `ssh -i ~/.ssh/id_rsa ubuntu@185.188.146.129`

* To connect with a password (only if you configured it during VM creation), run the following command and enter the password when prompted:

```
ssh username@192.168.1.92. 
```
<alert-element type="tip" title="Tip">
 
If you don't know your instance's username and public IP, you can check this information in the Customer Portal. Go to the “Cloud” section, select “Virtual Instances”, and then open your instance. Next to the **Access to Console** link, you'll find the information in the following format: `[login]@[ip-of your-instance]`. 

Typically, the login coincides with the name of the OS. For example, `ubuntu`.
 
</alert-element>

3\. You’ll be asked to add the device to the list of known devices. Write yes to add or no to not add. Press **Enter**.

4\. You’ve successfully connected to the instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/establish-ssh-connection-to-an-instance/linux-connected.png" alt="Ubuntu terminal displaying successful connection" width="80%">

## Connect with PuTTY

Follow these instructions to connect to a Virtual Machine from Windows 10/11 devices:

1\. Run the <a href="https://putty.org/" target="_blank">PuTTY app</a>.

2\. Open the “Session” section and enter the instance's IP address in the “HostName (or IP address)” field. 

3\. Ensure that port 22 is set in the “Port" field. This is the standard port for SSH connection. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/establish-ssh-connection-to-an-instance/puttygen-session.png" alt="Puttygen application with highlighted Port and Host name fields" width="80%">

<alert-element type="tip" title="Tip">
 
You can find the IP address of your Virtual Machine in the Gcore Customer Portal on the “Virtual Instances” tab. It will be displayed in the “IP Address” column.
 
</alert-element>

4\. Make sure that the “Connection type” parameter is set to SSH. 

5\. From the sidebar, go to **Connection** > **SSH** > **Auth** > **Credentials**. 

6\. Select **Browse** and find your private SSH key.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/establish-ssh-connection-to-an-instance/puttygen-session-annotated.png" alt="PuttyGen application with open Credentials tab" width="80%">

7\. Load the file with the private key to the Virtual Machine in the .ppk format. 

8\. Select **Open** to launch the PuTTY terminal window. 

9\. If you connect to the Virtual Machine for the first time, you’ll be asked if you want to save the host key of your instance. Select **Accept**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/establish-ssh-connection-to-an-instance/putty-cache-server.png" alt="Putty security alert that asks to cache the server's host key" width="80%">

10\. Log in by using the following credentials: 

* **login**: enter the username that was specified during the creation of your instance.
* **password** (optional): if you configured a password while creating an instance, enter your password. 

<alert-element type="tip" title="Tip">
 
If you don't know your instance's username and public IP, you can check this information in the Customer Portal. Go to the “Cloud” section, select “Virtual Instances”, and then open your instance. Next to the **Access to Console** link, you'll find the information in the following format: `[login]@[ip-of your-instance]`. 

Typically, the login coincides with the name of the OS. For example, `ubuntu`.
 
</alert-element>

11\. Press **Enter**.  

12\. You’ve successfully connected to the instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/establish-ssh-connection-to-an-instance/putty-connected.png" alt="Putty terminal displaying successful connection" width="80%">

## Connect via OpenSSH  

Windows has a built-in OpenSSH client that allows you to access the server via console, like on Linux. By default, this component is not activated.
Follow these steps to activate OpenSSH:

1\. Open “Windows Settings”. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/establish-ssh-connection-to-an-instance/windows-settings.png" alt="Windows settings page" width="80%">

2\. Go to the “Apps” section and select **Optional features**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/establish-ssh-connection-to-an-instance/windows-optional-features.png" alt="Windows Apps and features page" width="80%">

3\. Find OpenSSH Client, click to expand the detailed description, and select **Install**. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/establish-ssh-connection-to-an-instance/windows-openssh.png" alt="Windows Apps and features page that displays OpenSSH Client app" width="80%">

4\. After the OpenSSH client is installed, restart your computer to apply the settings correctly. OpenSSH client will become available from Command Prompt (cmd.exe).

5\. Open the Command Prompt and connect to a Virtual Machine in one of the following ways:

* To connect using a pair of SHH keys, run the following command: 

```
ssh username@192.168.1.92 -i ~/path/to/your/private-key username@public-ip-of-your-instance
```
* To connect with a password (only if you configured it during Virtual Machine creation), run the following command and enter a password when prompted:

```
ssh username@192.168.1.92
```

<alert-element type="tip" title="Tip">
 
If you don't know your instance's username and public IP, you can check this information in the Customer Portal. Go to the “Cloud” section, select “Virtual Instances”, and then open your instance. Next to the **Access to Console** link, you'll find the information in the following format: `[login]@[ip-of your-instance]`. 

Typically, the login coincides with the name of the OS. For example, `ubuntu`.
 
</alert-element>

6\. You’ll be asked to add the device to the list of known devices. Write yes to add or no to not add. Press **Enter**.

7\. You’ve successfully connected to the instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/establish-ssh-connection-to-an-instance/linux-connected.png" alt="Ubuntu terminal displaying successful connection" width="80%"> 