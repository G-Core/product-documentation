---
title: manage-ssh-keys
displayName: SSH key
order: 31
published: true
toc:
---
# Manage SSH keys

Manage SSH-keys in the <a href="https://gcore.com/docs/hosting/dedicated-servers/manage/log-in-to-dcimanager" target="_blank">DCImanager</a>.

To create a key, go to the SSH keys section and click on Add button.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/connect/manage-ssh-keys/joxi_screenshot_1509788651407.png" alt="">

Fill in the fields for Key Name and Public Key. Pay attention to the key format, try not to move the lines.

<img src="https://assets.gcore.pro/docs/hosting/dedicated-servers/manage/connect/manage-ssh-keys/joxi_screenshot_1509788759836.png" alt="" width="70%">

SSH key will be automatically added to all future servers and used OS. That is, using a specific key, you can connect to the server if:  
- You had added an SSH key and bought a server later  
- You had bought a server, had added an SSH key and later reinstalled the OS on the server

To change the key go toSSH keys - "Edit". To delete it go to SSH keys - "Delete".