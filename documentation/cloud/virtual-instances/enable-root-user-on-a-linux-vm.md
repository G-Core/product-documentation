---
title: enable-root-user-on-a-linux-vm
displayName: Enable root user
order: 22
published: true
toc:
pageTitle: Enable root user on a Linux VM | Gcore
pageDescription: Learn how to enable root user on a Linux VM using "sudo" or "sudo su" commands. Understand the differences and alternative methods.
---
# Enable root user on a Linux VM

Once you have connected to your virtual machine via <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">Control Panel</a> or <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">SSH</a>, you can perform commands with root user rights. To do this, you can use one of the two options: the `sudo` command or the `sudo su` superuser (root user) shell.

## sudo vs sudo su

**`sudo`** (which stands for <a href="https://sudo.ws" target="_blank">Super Do</a>) is a free command-line utility used in Unix-like operating systems such as the Linux family of distributions (including Ubuntu, Debian, and CentOS). `sudo` allows a regular user to temporarily elevate their privileges to a higher level, such as root, in order to execute tasks that require root user rights.

**`sudo su`** is a combination of `sudo` and `su`, where `su` means “switch user” or “substitute user.” Using `sudo su`, you can switch to being the root user for the duration of an active session. Consequently, all actions within the current session will be performed with root user permissions.

Remember to exercise caution when using these commands because operating with root permissions allows for system-wide changes. Misuse could lead to unintentional system alterations or compromise.

### Should you use sudo or sudo su?

Use `sudo` if you want to execute a specific command as a root user while staying logged in as a regular user.

Use `sudo su` if you want to log in as a root user and perform all commands with root permissions.

## How to use sudo

Add `sudo` to the beginning of your command. For example:

```
sudo apt-get update
```

All commands with `sudo` at the beginning will be executed with root user rights. Commands without `sudo` will be executed with regular rights.

## How to use sudo su

Enter the command:
```
sudo su
```
Having now logged in with the `sudo su` command, you are in the superuser (root) shell. All further commands will be performed with root user rights.
To exit superuser mode and return to your user account, simply run the command `exit`.

## Alternative ways to enable root user

You can also enter an interactive and non-interactive superuser (root) shell:

- Interactive: `sudo -i`
- Non-interactive: `sudo -s`

Before using `sudo -i`, the system might require your password to verify your identity and ensure that you have sudo rights, typically granted to administrators or users in the sudo group.

Unlike `sudo -i`, `sudo -s` starts a superuser shell without the need to enter the superuser password. This is handy if you need to run successive commands with superuser privileges within the current shell.
