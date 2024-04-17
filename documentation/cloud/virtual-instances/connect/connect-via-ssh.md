---
title: connect-via-ssh
displayName: Connect to an instance via SSH
published: true
pageTitle: Connect to a VM via SSH | Gcore
pageDescription: Learn how to connect to a Gcore Virtual Machine with SSH keys 
---
# Connect to a Virtual Machine via SSH

The SSH protocol is a method for secure remote login from one server to another. You can use SSH to connect to Gcore Virtual Machines running the Linux operating system.

The connection can be established in two ways: by using only SSH keys or the keys and a password. The second option is available only if you set up the password during instance creation. Learn how to set up a password for Linux in our guide about <a href="https://gcore.com/docs/cloud/virtual-instances/customize-initial-setup-for-your-instance#customize-the-initial-setup-for-your-instance" target="_blank">customizing the initial setup of your VM</a>.

<alert-element type="info" title="Info">

If you want to connect to an instance from the Gcore Customer Portal, follow the instructions from our guide on <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">connecting to a VM</a>.

</alert-element>

## Steps to establish an SSH connection

1\. <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">Configure and manage SSH keys</a>: Create and set up a pair of keys: a public key stored in the Gcore Customer Portal and a private key stored in your local storage. 

2\. (Optional). <a href="https://gcore.com/docs/cloud/ssh-keys/convert-an-ssh-key-from-pem-to-ppk" target="_blank">Convert your keys to .ppk format</a>: If you generated SSH keys via PuTTY, convert the keys to the supported .ppk format.

3\. <a href="https://gcore.com/docs/cloud/networking/add-and-configure-a-firewall#use-the-default-firewall" target="_blank">Configure firewall settings</a>: Set up the necessary protocols in firewall settings to allow outgoing and incoming connections to an instance.

4\. <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-via-ssh/establish-ssh-connection-to-an-instance" target="_blank">Establish an SSH connection with an instance</a>: Authenticate a VM using the recommended method for your operating system.
