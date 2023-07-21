---
title: troubleshoot-issues-with-ssh-connection
displayName: SSH connection
published: true
toc:
    --1--Incorrect firewall rules. Errors. Connection timed out: "incorrect-firewall-rules-errors-connection-timed-out"
    --1--Incorrectly added SSH key. Errors. Connection refused. Connection timed out: "incorrectly-added-ssh-key-errors-connection-refused"
    --1--No floating (public) IP address. Connection refused error: "no-floating-public-ip-address-connection-refused-error"
    --1--The failure to connect to the remote server with Windows OS on it. Connection error.: "the-failure-to-connect-to-the-remote-server-with-windows-os-on-it-connection-error"
pageTitle: Troubleshoot issues with an SSH connection | Gcore
pageDescription: Learn how to troubleshoot issues with an SSH connection
---
# Troubleshoot issues with an SSH connection

## **Incorrect firewall rules. Errors: Connection timed out**

In most cases, the error is caused by the incorrect configuration of the firewall rules.

In order to connect, you should allow all incoming connections via ICMP Protocol in the Inbound rules (if the connection is not allowed, the packets won't reach the machine when you try to ping).

Also, for SSH connection, you should set up a rule to allow incoming SSH connections over TCP on a given port.

In the default group, which is configured by default for all users, the above settings are initially set. You can choose this firewall group while creating a virtual machine if you have difficulties with the configuration of a custom one.

## **Incorrectly added SSH key. Errors: Connection refused.**

While generating a key with the PuttyGen utility, you should keep in mind that PuTTY and OpenSSH use different formats of public SSH keys. If the public key has a format like BEGIN SSH2 PUBLIC KEY, it will not work. The key should start with \\"ssh-rsa AAAA...\\".

When creating a key from the PuttyGen utility, you can just use The OpenSSH format key that appears in the interface after generation. You should copy it from the field \\"Public key for pasting into OpenSSH authorized_keys file\\"

## **No floating (public) IP address. Connection refused error**

If you used a previously created subnet while creating the machine, the system allows you to create a server without a floating IP.

The SSH connection would not be possible in this case, because an internal IP address is not announced on the Internet. You should add <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">a floating IP address</a> to the newly created machine for the connection from external networks.

## **The failure to connect to the remote server with Windows OS on it. Connection error.**

The Connection error occurs when you are trying to connect to the remote machine with Windows OS on it.

In most cases, it is due to an incorrectly selected VM connection Protocol. It is not possible to connect to a Windows OS-based server through SSH.

You should use the RDP Protocol (Remote Desktop Protocol). On a Windows PC, the distribution is installed by the default.