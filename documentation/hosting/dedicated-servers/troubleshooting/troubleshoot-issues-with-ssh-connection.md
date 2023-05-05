---
title: troubleshoot-issues-with-ssh-connection
displayName: SSH connection
published: true
order: 10
toc:
---
# Troubleshoot issues with SSH connection

SSH connection uses 22 port, so, first of all, check the server availability via 22 port running _telnet_ command or by using <a href="https://www.putty.org/" target="_blank">Putty</a> application.

For example:  

<code-block>
telnet <span style="color:#FF5913">92.000.000.00 22</span> 
</code-block>

Where: 
- <span style="color:#FF5913">92.000.000.00</span> – server's IP, 
- <span style="color:#FF5913">22</span> – port.

If you see this kind of result server is able to connect via SSH.

<code-block>
telnet 92.000.000.00 22 
Trying 92.000.000.00...  
Connected to 92.000.000.00  
Escape character is '^]'.  
<span style="color:#FF5913">**SSH-2.0-OpenSSH\_7.2 FreeBSD-20161230</span>
Connection closed by foreign host.
</code-block>

Putty interface:

<img src="https://support.gcore.com/hc/article_attachments/360010081637/mceclip0.png" alt="" width="60%">

Specify the IP address in the field, be sure to have 22 port typed, then press Open. Enter the credentials from the Instruction (example follows next). A little note, User goes for Login.

<img src="https://support.gcore.com/hc/article_attachments/360010185998/mceclip1.png" alt="" width="70%">

If 22 port is opened and you are still having issues with connection, check login and password.

Find login and password in the Control Panel. Choose the server and then click Instructions button.

<img src="https://support.gcore.com/hc/article_attachments/360010185998/mceclip1.png" alt="" width="70%">

You need User and Password fields located after Server IP address.

<img src="https://support.gcore.com/hc/article_attachments/360000736678/mceclip1.png" alt="">

**Note**: If you change the password in OS by yourself it won't change in the Instruction.

In case of having errors via telnet connection or Putty, check OS settings by connecting the server via VNC in VMmanager (for a Virtual Private Server) and IPMI in DCImanager (for a Dedicated Server). Credentials to access these panels are found in the Instruction as well.

If you're sure that 22 port is not blocked from your side, contact us via chat or create ticket from the Control Panel.