---
title: install-an-os-from-a-template-in-vmmanager-6
displayName: Install an OS from a template in VMmanager 6
published: true
order: 31
toc:
pageTitle: Install an OS from a template in VMmanager 6| Gcore
pageDescription: Learn how to install an OS from a template for a virtual server in VMManager 6.
---
# Install an operating system from a template in VMmanager 6

In VMmanager 6, you have the option to install various operating systems using templates. The available OS templates include: 

- CentOS 7
- Debian 10, 11
- FreeBSD 12
- Ubuntu 18.04, 20.04, 22.04

For more information about VMmanager 6’s features and functions, refer to <a href="https://gcore.com/docs/hosting/virtual-servers/manage/main-features-and-functions-of-vmmanager-6" target="_blank">our PD article</a>.


To proceed with the OS installation, follow these steps:

1. Go to the <a href="https://bix-v6.vm.gcore.com/vm/manager/host" target="_blank">**Virtual machines** page</a> and find the desired server.

2. Click the three-dot menu on the right-hand side and select Reinstall OS.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/operating-system/install-an-os-from-a-template/1-menu.png" alt="Virtual machines page ">

3. On the next page, select the operating system you want to install.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/operating-system/install-an-os-from-a-template/2-configuration-options.png" alt="next page,">

4. For **Applications and scripts**, select the relevant scripts that can prepare your server for specific necessary operations: install packages, edit configuration files, etc. The scripts will automate necessary steps involved in setting up your server’s applications and environment. This means that after the OS installation, you don’t have to manually perform these tasks. You can create your own script in advance or use the default one from the VMmanager repository. If you don’t want to use any scripts, select the **Without script** option.

5. Configure the new VM password: Save the suggested password or generate your own.

**Please note**: After the OS reinstallation, the old password will become invalid. If you want to keep your current password, enter it to the new password field.

6. Click **Reinstall**. 

Once the VM status changes back to **Active**, your machine will be ready to run again.
