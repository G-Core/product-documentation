---
title: troubleshoot-issues-with-ssh-connection
displayName: SSH connection
published: true
toc:
---

SSH connection uses 22 port, so, first, check the server availability via 22 port running _telnet_ command or by using the Putty application.


For example:  
_telnet 92.000.000.00 22 (92.000.000.00 – server's IP, а 22 – port)_


If you see this kind of result, server can connect via SSH.

_telnet 92.000.000.00 22_  
_Trying 92.000.000.00..._  
_Connected to 92.000.000.00_  
_Escape character is '^\]'._  
_**SSH-2.0-OpenSSH\_7.2 FreeBSD-20161230**_  
_Connection closed by foreign host._


Putty interface:


![\"mceclip0.png\"](\"https://support.gcore.com/hc/article_attachments/360010081637/mceclip0.png\")


Specify the IP address in the field, be sure to have 22 port typed, then press Open. Enter the credentials from the Instruction (example follows next). A little note, User goes for Login).


![\"mceclip1.png\"](\"https://support.gcore.com/hc/article_attachments/360010185998/mceclip1.png\")



If 22 port is opened, and you are still having issues with connection, check login and password.


Find login and password in the Control Panel. Choose the server and then click the Instructions button.


![](\"https://support.gcore.com/hc/article_attachments/360000746957/mceclip0.png\")


You need User and Password fields located after Server IP address.


![](\"https://support.gcore.com/hc/article_attachments/360000736678/mceclip1.png\")


_**Note, if you change the password in OS by yourself it won't change in the Instruction.**_


In case of having errors via telnet connection or Putty, check OS settings by connecting the server via VNC in VMmanager (for a Virtual Private Server) and IPMI in DCImanager (for a Dedicated Server). Credentials to access these panels are found in the Instruction as well.


If you're sure that the 22 port is not blocked from your side, contact us via chat or create a ticket from the Control Panel.