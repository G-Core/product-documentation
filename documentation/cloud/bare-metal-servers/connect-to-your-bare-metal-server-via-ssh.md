---
title: connect-to-your-bare-metal-server-via-ssh
displayName: Connect to your bare metal server via SSH
published: true
toc:
   --1--Connecting using a pair of SSH keys. Preparation: "connecting-using-a-pair-of-ssh-keys-preparation"
   --2--SSH keys generation (Windows 7/8): "generate-ssh-keys-windows-7-8"
   --2--SSH keys generation (Windows 10, Linux OS, macOS): ""
   --2--SSH keys generation in the personal account: "how-to-add-ssh-keys-to-your-gcore-cloud-personal-account"
   --2--How to delete an SSH key: "how-to-delete-ssh-keys-in-your-gcore-cloud-personal-account"
   --2--How to generate SSH keys when creating an Instance or Bare Metal server: "how-to-generate-and-add-ssh-keys-when-creating-an-instance-or-bare-metal-server"
   --1--Connecting using a password. Preparation: "connecting-using-a-password-preparation"
   --2--Configuring a password: "configuring-a-password"
   --1--Connecting via SHH: "connecting-via-ssh"
   --2--Connecting from Windows 7/8: "connecting-from-windows-7-8"
   --2--Connecting from Windows 10, Linux OS, macOS: "connecting-from-windows-10-linux-os--macos"
---
#### You can connect to an instance or a baremetal server using a pair of SSH keys or a password. We tell you in detail about each method.

The SSH protocol (also referred to as Secure Shell) is a method for secure remote login from one server to another. To connect via SSH, make sure that all the necessary rules for incoming traffic are in the firewall settings set.

_Please note_: you cannot connect to Windows instances or servers via SSH. But you can connect to them via RDP protocol or [from the console in Control Panel](https://support.gcorelabs.com/hc/en-us/articles/360020733518). With the rest of instances and servers, you can establish a connection via SSH or [from your Control Panel](https://support.gcorelabs.com/hc/en-us/articles/360020733518).

*   [How to add an SSH key to your personal account](#how-to-add-ssh-keys-to-your-gcore-cloud-personal-account) 

Connecting using a pair of SSH keys. Preparation
================================================

To connect to an instance or Bare Metal server, create a public key that will be stored on your machine and a private key that will be placed on your local storage.  

**Generate SSH keys (Windows 7/8)** 
------------------------------------

! SSH key generation using the command line interface (cmd) is not available for Windows 7/8 operating systems.  

1\. To generate key pairs, use the [PuTTY and PuTTYgen](https://www.putty.org/) apps.  

2\. Download and install [the PuTTY](https://www.putty.org/) package.  

3\. Launch the PuTTYgen app. 

4\. In the Type of key to generate field, specify the RSA. 

5\. And for the Number of bits in a generated key field, set the value to 2048. 

6\. Click Generate.  

<img src="https://support.gcore.com/hc/article_attachments/360011018357/putty_gen.png" alt="putty_gen.png" width="390" height="381">

Important! During the key generation, move the cursor in the Key field until the key appears in the field. <img src="https://support.gcore.com/hc/article_attachments/360011018457/___________.png" alt="___________.png" width="429" height="422">

7\. In the Key passphrase field, enter a password.  

8\. Confirm the password in the "Confirm passphrase" field. 

9\. Click Save private key and save the private key. 

**Attention!** Never pass your private key and password to third parties. 

10\. Click Save public key and save the public key on your local storage.  

11\. You can always open and copy the saved key with the Notepad app.  

 <img src="https://support.gcore.com/hc/article_attachments/360011027977/notepad.png" alt="notepad.png" width="457" height="255">

 **Generate SSH keys (Windows 10, Linux OS, macOS)** 

1\. To generate keys on Linux/macOS/Windows 10: 

2\. Open the console, terminal (macOS), or command line (cmd.exe for Windows OS).  

3\. Run the command: _ssh-keygen -t rsa -b 2048_ 

4\. Enter the key name in the Enter file in which the key should be saved field. 

**Attention!** If you do not specify a directory (for example, .ssh/), the keys are saved in~. /<key name> (for Linux/macOS) or in C:\\Users\\<user\_name>\\<key name> (for Windows 10). 

5\. Press Enter. 

6\. Then enter the password for the key or leave the field empty and press Enter if you want to create a key without a password.  

<img src="https://support.gcore.com/hc/article_attachments/13378163376145" alt="_______________________1.jpg">

7\. Confirm the password or leave the field empty and press Enter to save the key without a password.   

8\. The key was created in the default directory or in the one you specified.  

<img src="https://support.gcore.com/hc/article_attachments/13378185655953" alt="_____________1.png">

9\. The public part of the key will be saved in the <key\_name>.pub file. Use it to add it to your machine. You can open the ssh key file in text format for copying in the Notepad app. 

**Generate SSH keys in the personal account** 

To create an ssh key from your personal account, follow the steps below. 

1\. In the Gcore Cloud control panel, go to SSH Keys. 

2\. Click Autogenerate SSH key. 

<img src="https://support.gcore.com/hc/article_attachments/360011030697/autogenetae.png" alt="autogenetae.png">3\. Enter the key name and click Create SSH key. 

<img src="https://support.gcore.com/hc/article_attachments/360011096738/________________________.png" alt="________________________.png">  
**Important!** Only Latin characters, underscores, spaces, and dots can be used. The length must be between 3 and 63 characters.  

4\. The key will be generated and displayed in the list of ssh keys, its public part will already be stored in the system, and the private key will be downloaded to your local storage.  

5\. To view the private key, find it in your local storage and open it using the Notepad app.   

**How to add SSH keys to your Gcore Cloud personal account** 
-------------------------------------------------------------

To add an already created SSH key to your personal account: 

1.  In the Gcore Cloud control panel, go to SSH Keys. 

2\. Click Add SSH key. 

<img src="https://support.gcore.com/hc/article_attachments/360011030997/add_a_ssh.png" alt="add_a_ssh.png">

3\. In the SSH key Content field, insert the public part of the SSH key. 

4\. Enter the key name in the Name field. 

<img src="https://support.gcore.com/hc/article_attachments/360011106038/add_an_ssh_2.png" alt="add_an_ssh_2.png" width="453" height="327">

5\. Click Add SSH key. 

6\. The key will appear in the list of SSH keys. 

**How to delete SSH keys in your Gcore Cloud personal account** 
----------------------------------------------------------------

1\. Select the SSH key you want to delete. 

2\. Click on the three-point sign.  

3\. Select Delete. 

<img src="https://support.gcore.com/hc/article_attachments/360011106078/ssh_delete.png" alt="ssh_delete.png">

**How to generate and add SSH keys when creating an Instance or Bare Metal server** 
------------------------------------------------------------------------------------

In your personal account, you can create and add an SSH key when creating an instance or Bare Metal server. 

When creating a machine, in the SSH key section, you will be asked to _add a key that is already stored in your personal account_ by selecting it from the drop-down list, _add an already generated key stored in your local storage_, or _generate a new key_ here. 

 <img src="https://support.gcore.com/hc/article_attachments/360011106138/_________________________________.png" alt="_________________________________.png">

1\. When you click Add SHH key, a dialog box opens. Add the public part of the SSH key, enter the key name to identify it in our system, and save it. 

<img src="https://support.gcore.com/hc/article_attachments/360011031417/______________.png" alt="______________.png" width="408" height="295">

Next, select a key from the drop-down list to add it to your machine.  

 2. When you click Autogenerate SSH key, a dialog box opens. Enter the key Name to identify it in the system. 

<img src="https://support.gcore.com/hc/article_attachments/360011106378/autogenerate_2.png" alt="autogenerate_2.png">

The key will be automatically added to your machine.  

 After adding or generating a new SSH key, the keys will appear in the SSH Keys section. 

<img src="https://support.gcore.com/hc/article_attachments/5287479947537/mceclip0.png" alt="mceclip0.png">

Connecting using a password. Preparation
========================================

**Configuring a password**
--------------------------

To connect using a password, configure it while creating an instance or Bare Metal server. In Additional options click on "User data". This will open a field, where you can enter the script that will be processed by a cloud-init agent running on your machine. 

<img src="https://support.gcore.com/hc/article_attachments/360008785018/13.png" alt="13.png">  
Paste the code below with the password chosen by you:

#cloud-config  
password: **your password**  
chpasswd: { expire: False }  
ssh\_pwauth: True

Using the specified password, you will be able to connect to the instance or Bare Metal server via SSH or [from your Control Panel](https://support.gcorelabs.com/hc/en-us/articles/360020733518).

It is not necessary to specify the password explicitly, you can enter its hash (the same password, only in a converted form; the system will be able to read it, but for a person, it looks like a random set of symbols). Then, even if someone gets into the system, he or she won’t know the password — only the hash will be stored inside. And the system will open its doors only to the user who knows the password. To generate a hash, you can use the Python script:

#!/usr/bin/env python3  
\# based on [https://stackoverflow.com/a/17992126/117471](https://stackoverflow.com/a/17992126/117471)  
\# pip3 install passlib  
import sys  
from getpass import getpass  
from passlib.hash import sha512\_crypt  
passwd = input() if not sys.stdin.isatty() else getpass()  
print(sha512\_crypt.hash(passwd , rounds = 5000 ))

Connecting via SSH
==================

**Connecting from Windows 7/8**
-------------------------------

!Connecting to an instance or Bare Metal server over ssh using the command line (cmd) is not available on Windows 7/8 operating systems.  

To connect, use [the PuTTY](https://www.putty.org/) app. 

1\. Download and run [the PuTTY](https://www.putty.org/) app.  

2\. Go to the Session section, in the Host Name (or IP address) field enter the machine's IP address. 

<img src="https://support.gcore.com/hc/article_attachments/360011031597/____________________________.png" alt="____________________________.png" width="537" height="415">

**Important!** If you create a machine with only a private address, add a floating IP.

<img src="https://support.gcore.com/hc/article_attachments/360011032017/add_ip_float.png" alt="add_ip_float.png">

3\. In the Port field, set 22 port which is the standard port for SSH connection.  

4\. Next, set the Connection type field to SSH. 

5\. (Step for connecting using a pair of SSH keys only) on the right side of the screen, go to Connection - > SSH -> Auth. 

6\. (Step for connecting using a pair of SSH keys only) click Browse. 

 <img src="https://support.gcore.com/hc/article_attachments/360011025197/browse.png" alt="browse.png">

7\. (Step for connecting using a pair of SSH keys only) select the file with the private key for your machine in .ppk format.  

**Important!** If your private key is saved in .pem format, convert it to .ppk format following the [instructions](https://support.gcore.com/hc/en-us/articles/360012640597). 

8\. Click Open. The console will open. 

 <img src="https://support.gcore.com/hc/article_attachments/360011099078/login_as.png" alt="login_as.png" width="545" height="345">9\. In the "login" field, enter the user name that was given when creating the instance or Bare Metal server. You can find it in the instance's tab, you will see is an inscription of the “\[login\]@\[IP of your machine\]” type. Most often, the login coincides with the name of the OS. For example, for the machine below it is "Ubuntu".

10\. (Step for connecting using a pair of SSH keys only) enter the password you configured while creating an instance or Bare Metal server.

11\. Press Enter.  

12\. You have connected to your machine.  

**Connecting from Windows 10, Linux OS, macOS** 
------------------------------------------------

_Attention! If you use Linux OS or macOS, go to step 7._ 

Windows 10 has a built-in OpenSSH client that allows you to access the server via the console, like on Linux OS. By default, this component is not activated.  

Follow the steps below to activate it. 

1\. Open Settings. 

<img src="https://support.gcore.com/hc/article_attachments/360011032077/SETTINGS.png" alt="SETTINGS.png" width="519" height="366">

2\. Go to the Apps section and click Optional features. 

<img src="https://support.gcore.com/hc/article_attachments/360011107278/OPTIONAL_FEATURES.png" alt="OPTIONAL_FEATURES.png" width="543" height="260">

3\. Find OpenSSH Client and click to expand the detailed description.  

<img src="https://support.gcore.com/hc/article_attachments/360011032137/instal_open_sssh.png" alt="instal_open_sssh.png">

4\. Click Install. 

5\. Wait for the installation to be completed. After SSH Client is installed, restart your computer to apply the settings correctly. SSH utility will become available for cmd. 

6\. Open the command prompt and enter the command with your own values:

_"ssh username__[@192.168.1.92](mailto:root@192.168.1.92) " —_ to connect using a password;

_"ssh username[@192.168.1.92](mailto:root@192.168.1.92) \-i "C:\\Users\\username\\.ssh\\id\_rsa" —_ to connect using a pair of SHH keys_._

| \nusername \n                          | \nYour username, you can find it to the right of \"Access to Console\" button\n                                                                                                                 |
|----------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \n192.168.1.92  \n                     | \nIP address of your instance.\n \nImportant! If you created an instance with only a private interface, create a floating IP address and use it when connecting to the instance over ssh. \n \n |
| \nC:\\Users\\username\\.ssh\\id_rsa \n | \nThe path to the private key file on your computer. \nThe key must be in PEM format.  \n                                                                                                       |


7\. The utility will warn you that you're trying to connect to an unknown device and ask if you want to continue. Type "yes" and press Enter. 

<img src="https://support.gcore.com/hc/article_attachments/360011099638/yes.png" alt="yes.png">

8\. (Step for connecting using a password only) enter the password you configured while creating an instance or Bare Metal server.

9\. You have connected to your machine.
