---
title: connect-to-your-instance-via-control-panel
displayName: Connect via Control Panel
published: true
order: 10
toc:
   --1--Linux instance: "connect-to-a-linux-instance"
   --1--Windows instance: "connect-to-a-windows-instance"
pageTitle: Connect to a VM via Control Panel | Gcore
pageDescription: Connect to your Linux or Windows machine from the Gcore Control Panel
---
# Connect to your instance via Control Panel

To connect to an instance via the Console in your Control Panel, click on the desired instance, and in the next window — on "Access to Console".

<media-gallery>
<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/mceclip0.png" alt="mceclip0.png">

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/image4.png" alt="image4.png">
</media-gallery>

To connect, the system will ask you to enter your username and password. The location of them depends on the instance’s OS.

## Connect to a Linux instance 

You will see the login to the right of the "Access to Console" button. There is an inscription of the "\[login\]@\[IP of the instance\]" type. Most often, the login coincides with the name of the OS. For example, for the instance below it is "ubuntu".

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/image7.png" alt="image7.png">

You entered the password during the <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">creation of the instance</a> when you filled in the user data in the "Additional options" field. Please note: if the instance is only in a private subnet, DHCP must be enabled in the settings of this subnet so you can log in with a password.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/image3.png" alt="image3.png">

If you forgot your password, you can find it inside the system by <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">connecting to the instance via SSH</a>. Enter the `sudo cat /var/lib/cloud/instance/user-data.txt` command and you will see the password in the line "password: \[your password\]".

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/image6.png" alt="image6.png">

Please note: if you entered the password as a hash, you will see the hash on the screen. In this case, you will not be able to find out the password.

Enter your username and password when connecting, and you will access the instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/image12.png" alt="image12.png">

## Connect to a Windows instance

The login for all instances is "Admin". You entered the password in the "Access" field when creating the instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/image5.png" alt="image5.png">

Enter your password and you will access the instance.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel/image1.png" alt="image1.png">