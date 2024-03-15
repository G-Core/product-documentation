---
title: connect-via-ssh
displayName: Connect to an instance via SSH
published: true
pageTitle: Connect to an Instance via SSH | Gcore
pageDescription: Learn how to connect to a virtual instance with SSH keys 
---
# Connect to an instance via SSH

The SSH protocol is a method for secure remote login from one server to another. You can use SSH to connect to virtual instances running the Linux operating system.

The connection can be established in two ways: by using only SSH keys or the keys and a password. However, the second option is available only if you set up the password during instance creation. Learn how to set up a password for Linux in this guide: <a href="https://gcore.com/docs/cloud/virtual-instances/customize-initial-setup-for-your-instance#customize-the-initial-setup-for-your-instance" target="_blank">Customize the initial setup of your instance</a>.

<alert-element type="info" title="Info">

If you want to connect to an instance from the Gcore Customer Portal, follow the instructions from this guide: <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">Connect to an instance via Customer Portal</a>.

</alert-element>

## Steps to establish an SSH connection

1\. <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">Configure and manage SSH keys</a>: create and set up a pair of keys—a public key stored in the Customer Portal and a private key placed in your local storage. 

2\. (Optional). <a href="https://gcore.com/docs/cloud/ssh-keys/convert-an-ssh-key-from-pem-to-ppk" target="_blank">Convert your keys to .ppk format</a>: if you generated SSH keys via PuTTY, convert the keys to the supported .ppk format.

3\. <a href="https://gcore.com/docs/cloud/networking/add-and-configure-a-firewall#use-the-default-firewall" target="_blank">Configure firewall settings</a>: set up the necessary protocols in firewall settings to allow outgoing and incoming connections to an instance.

4\. <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-via-ssh/establish-ssh-connection-to-an-instance" target="_blank">Establish an SSH connection with an instance</a>: authenticate to an instance using the recommended method for your operating system.