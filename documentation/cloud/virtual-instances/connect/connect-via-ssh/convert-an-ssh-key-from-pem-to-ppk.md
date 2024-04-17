---
title: convert-an-ssh-key-from-pem-to-ppk
displayName: Convert an SSH key to PPK format
order: 20
published: true
toc:
pageTitle: Convert an SSH Key to PPK | Gcore
pageDescription: Learn how to convert an SSH key to PPK format.
customUrl: /cloud/ssh-keys/convert-an-ssh-key-from-pem-to-ppk 
---
# Convert an SSH key to PPK format

If you generated your SSH keys via PuTTYgen or in the Gcore Customer Portal and want to use PuTTY to connect to a virtual instance, you need to convert the keys to a .ppk format. 

To do this, you can use PuTTYgen:

1\. Make sure that <a href="https://putty.org" target="_blank">PuTTY</a> is installed on your device.

2\. Launch the PuTTYgen app.  

3\. Click **Load**. Then, find the file with the key that you want to convert.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/puttygen-load-key.png" alt="Puttygen app with the Load button highlighted" width="80%">

<alert-element type="info" title="Info">

By default, Windows will display only .ppk files. To view all file types, select **All files** in the "Open file" dialog.

</alert-element>

4\. PuTTYgen will prompt you to confirm that you want to import the key. Select **OK**.

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/puttygen-convert-key.png" alt="Puttygen confirmation that the key has been imported" width="80%">

5\. Select a converted key by clicking either **Save private key** or **Save public key**. 

<img src="https://assets.gcore.pro/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh/puttygen-save-keys.png" alt="Puttygen app with the Save public key and Save private key buttons highlighted" width="80%">

6\. Save the key on your device for future use.
