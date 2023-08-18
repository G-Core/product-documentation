---
title: change-the-port-for-ssh-connections
displayName: Change port for SSH connections
published: true
order: 36
toc:
pageTitle: Change port for SSH connections | Gcore
pageDescription: Discover the step-by-step guide on how to easily change the port for SSH connections on your Linux server.
---

# Change the port for SSH connections

Follow these instructions to modify the SSH port through which you connect to your dedicated Linux server.

1. Log in to your server.

2. Navigate to the SSH directory using the following command:

```
cd /etc/ssh/
```

3. Open the SSH configuration file with root privileges using this command:

```
sudo nano sshd_config
```

4. Find the **Port** line in the open file and replace the value 22 with the port number you want to use. Also, remove the **#** symbol if it is present before the **Port** line.

<media-gallery>

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/connect/change-the-port-for-ssh-connections/1-port-22.png" alt="">

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/connect/change-the-port-for-ssh-connections/2-port-2233.png" alt="">

</media-gallery>

5. Press **Ctrl+O** to save the changes.

6. Restart the SSH service.
For Ubuntu, Debian, or CentOS, use the following command:

```
sudo systemctl restart ssh 
```

For FreeBSD, use:

```
sudo service sshd restart
```

7. Add a rule to permit traffic exchange on the new port using the command:

```
sudo ufw allow 2233
```
Replace “2233” with the chosen port.

8. Verify if everything is functioning properly by using the command:

```
telnet 8.8.8.8 2233
```

Replace “8.8.8.8” with your server IP address, and “2233” with the chosen port.

The output should look like this:

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/connect/change-the-port-for-ssh-connections/3-output.png" alt="">

9. Attempt to establish a connection to your server using the new port in a separate window **without closing your current session**. This step is crucial to prevent any potential loss of access to your server. If you encounter difficulties connecting to your server through the new port, revert the port back to 22 and then try again.
