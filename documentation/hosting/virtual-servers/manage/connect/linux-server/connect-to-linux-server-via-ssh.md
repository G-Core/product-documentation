---
title: connect-to-linux-server-via-SSH
displayName: SSH connection
order: 20
published: true
toc:
---
Via SSH, you can remotely connect to CentOS, Debian, Ubuntu and FreeBSD servers. You can [connect to a Windows server](https://gcorelabs.com/support/articles/360019539758/) using the RDP protocol.

1\. Open the list of your servers and click on the one you need. Click the **Instructions** button.

<img src="https://support.gcore.com/hc/article_attachments/13264688301585" alt="mceclip0.png">

A tab with instructions will open. You will need a username, a server IP address, and a password.

<img src="https://support.gcore.com/hc/article_attachments/12329792750609" alt="mceclip1.png">

2\. Open a terminal (for Linux) or a command line (for Windows) on your computer. Enter the command: 

ssh **\[username\]**@**\[server IP\]**

For example, if the instructions say "user: root" and "server IP address: 185.14.67.190", then the command would be:

<img src="https://support.gcore.com/hc/article_attachments/12329845428113" alt="mceclip2.png">  
3\. The connection will prompt you for a password. Enter the password from the instructions. For example, if the instructions say "password: YHr4mhn7hFJeN", enter YHr4mhn7hFJeN.

**Please note**: The password cannot be copied and pasted; it must be entered manually. The letters you enter will not be displayed on the screen to protect your password. Type the symbols and press Enter.

[<img src="https://support.gcore.com/hc/article_attachments/4408223674257/mceclip0.png" alt="mceclip0.png">](https://support.gcorelabs.com/hc/article_attachments/4408223674257/mceclip0.png)  
Once the connection is established, you can manage the virtual server remotely from your computer.