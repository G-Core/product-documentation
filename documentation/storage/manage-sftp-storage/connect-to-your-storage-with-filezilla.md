---
title: connect-to-your-storage-with-filezilla
displayName: Connect with FileZilla
published: true
order: 10
toc:
   --1--Install FileZilla: "install-filezilla"
   --1--Configure connection: "configure-connection"
   --2--Connect with a password: "connect-with-a-password"
   --2--Connect with an SSH key: "connect-with-an-ssh-key"
pageTitle: Guide to connect to storage with FileZilla | Gcore
pageDescription: A guide on how to install FileZilla and configure its connection to your storage either using a password or an SSH key.
---
# Connect to your storage with FileZilla

## Install FileZilla

You can use bash to connect to the SFTP storage. In the example, we use the FTP client FileZilla.

To download and install FileZilla, use <a href="https://filezilla-project.org" target="_blank">this link</a>.

## Configure connection

Start by opening up Site Manager:

<img src="https://assets.gcore.pro/docs/storage/manage-sftp-storage/connect-to-your-storage-with-filezilla/13822230046353.png" alt="Site Manager" width="80%">

In an open window, click on the **New Site** button:

<img src="https://assets.gcore.pro/docs/storage/manage-sftp-storage/connect-to-your-storage-with-filezilla/13814505201553.png" alt="New Site button" width="50%">

Give it a name and navigate to the General tab on the right.

### Connect with a password

Choose SFTP - SSH File Transfer Protocol in the "Protocol" field drop-down menu.

Put the **Hostname** from the Control Panel in the "Host" field, and specify port **2200**.

Logon Type should be Ask for password.

The user is your storage name.

Click **OK** to save the changes and Connect to establish a connection to the storage.

### Connect with an SSH key

Choose SFTP - SSH File Transfer Protocol in the Protocol field drop-down menu.

In the "Host" field put the Hostname from the Control Panel, specify port 2200.

Logon Type should be Key file.

User is your storage name.

For the Key file specify the path to the private key on your computer.

Click **OK** to save the changes and Connect to establish a connection to the storage.