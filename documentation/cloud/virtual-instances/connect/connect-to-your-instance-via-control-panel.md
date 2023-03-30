---
title: connect-to-your-instance-via-control-panel
displayName: Connect via Control Panel
published: true
order: 10
toc:
   --2--Connect to Linux instance: "connect-to-linux-instance"
   --2--Connect to Windows instance: "connect-to-windows-instance"
---
To connect to an instance via the Console in your Control Panel, click on the desired instance, and in the next window — on "Access to Console".

<img src="https://support.gcore.com/hc/article_attachments/5286387063825/mceclip0.png" alt="mceclip0.png">

[<img src="https://support.gcore.com/hc/article_attachments/360020585258/image4.png" alt="image4.png">](https://support.gcorelabs.com/hc/article_attachments/360020585258/image4.png)

To connect, the system will ask you to enter your username and password. The location of them depends on the instance’s OS.

  

Connect to Linux instance 
--------------------------

You will see the login to the right of the “Access to Console” button. There is an inscription of the “\[login\]@\[IP of the instance\]” type. Most often, the login coincides with the name of the OS. For example, for the instance below it is "ubuntu".

[<img src="https://support.gcore.com/hc/article_attachments/360020483437/image7.png" alt="image7.png">](https://support.gcorelabs.com/hc/article_attachments/360020483437/image7.png)

You entered the password during the creation of the instance when you [filled in the user data in the "Additional features"](https://support.gcorelabs.com/hc/en-us/articles/360004547478-Create-Instance#h_01EMPF24ZVRTYKKC26M9B2BBPX). Please note: if the instance is only in a private subnet, DHCP must be enabled in the settings of this subnet so you can log in with a password.

[<img src="https://support.gcore.com/hc/article_attachments/360020585238/image3.png" alt="image3.png">](https://support.gcorelabs.com/hc/article_attachments/360020585238/image3.png)

If you forgot your password, you can find it inside the system: [connect to the instance via SSH](https://support.gcorelabs.com/hc/en-us/articles/360012635517), enter the command “sudo cat /var/lib/cloud/instance/user-data.txt” and you will see the password in the line “password: \[your password\]”.

[<img src="https://support.gcore.com/hc/article_attachments/360020585318/image6.png" alt="image6.png">](https://support.gcorelabs.com/hc/article_attachments/360020585318/image6.png)

_Please note: if you entered the password as a hash, you will see the hash on the screen. In this case, you will not be able to find out the password._

Enter your username and password when connecting, and you will access the instance.

[<img src="https://support.gcore.com/hc/article_attachments/360020583258/image12.png" alt="image12.png">](https://support.gcorelabs.com/hc/article_attachments/360020583258/image12.png)

Connect to Windows instance
---------------------------

The login for all instances is "Admin". You entered the password in the "Access" field when creating the instance.

[<img src="https://support.gcore.com/hc/article_attachments/360020585278/image5.png" alt="image5.png">](https://support.gcorelabs.com/hc/article_attachments/360020585278/image5.png)

Enter your password and you will access the instance.

[<img src="https://support.gcore.com/hc/article_attachments/360020485997/image1.png" alt="image1.png">](https://support.gcorelabs.com/hc/article_attachments/360020485997/image1.png)