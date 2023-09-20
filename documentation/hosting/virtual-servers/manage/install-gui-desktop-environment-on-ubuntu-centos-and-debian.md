---
title: install-gui-desktop-environment-on-ubuntu-centos-and-debian
displayName: GUI (desktop environment)
published: true
order: 20
toc:
   --1--What is the desktop environment: "what-is-the-desktop-environment"
   --1--Install XFCE desktop environment: "install-xfce-desktop-environment"
   --2--On Ubuntu: "Install XFCE on Ubuntu"
   --2--On CentOS: "install-xfce-on-centos"
   --2--On Debian: "install-xfce-on-debian"
   --1--Open terminal inside XFCE: "how-to-open-a-terminal-inside-xfce"
   --1--Quit the XFCE desktop environment: "how-to-log-out-of-xfce"
   --2--For Ubuntu server with "lightdm": "for-ubuntu-server-with-lightdm"
   --2--For all other servers: "for-all-other-servers"
pageTitle: Install GUI (desktop environment) | Gcore
pageDescription: Discover how to install the desktop environment on Ubuntu, CentOS, and Debian servers for a user-friendly graphical interface.
---
# Install GUI (desktop environment) on Ubuntu, CentOS and Debian

## What is the desktop environment

The desktop environment is a graphical interface that looks like a desktop. After installing it, you will see the system in its usual appearance: with folders, shortcuts, and a menu. This will not delete the terminal — you can still open it and enter commands.

<media-gallery>
 <img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image2.png" alt="Desktop environment" width="80%">
 
 <img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image25.png" alt="Terminal" width="80%">
</media-gallery>

In this article, we will show you how to install the XFCE desktop environment — it is easy to use, does not require many resources, and can be installed on even the weakest server. If you wish, you can install any other desktop environment according to the instructions from the Internet.

## Install XFCE desktop environment

### Install XFCE on Ubuntu

1\. Connect to the server through your Control Panel or via SSH. To connect through the Control Panel, go to the server control panel and click the monitor icon.

<media-gallery>
<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12899747666833.png" alt="Server control panel" width="80%"> 

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12899761970449.png" alt="Dashboard" width="80%">
</media-gallery>

You can find the login and password for connection in your Control Panel in the "Instructions" section.

<media-gallery>
<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12900025590289.png" alt="Server control panel" width="80%">

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12900217123473.png" alt="Server information" width="80%">
</media-gallery>

2\. Update the package list with the command:

```
sudo apt-get update
```

3\. Install the XFCE environment and additional components (panel, file manager, various plugins) with the command:

```
sudo apt-get install xfce4-session xfce4-goodies
```

The system will warn you that the installation will take several hundred megabytes of hard disk space.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image8.png" alt="Warning">

Confirm the operation with: ```y```

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image12.png" alt="Confirmation">

4\. Install a tool for initialization of a graphical system (it will launch the XFCE environment).

In some versions of the OS, the system will offer a choice of "gdm3" and "lightdm" tools. Select "lightdm" and press Enter. The system will install it.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/4411242128145.png" alt="Warning with the choice of gdm3 and lightdm tools" width="80%">

In other OS versions, you need to install the tool yourself. Install the tool "xinit" using the command:

```
sudo apt install xinit
```

The system will warn you that the installation will take several megabytes of hard disk space.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image20.png" alt="Warning">

Confirm the operation with: ```y```

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image24.png" alt="Confirmation">

5\. The desktop environment will be ready to run.

If you installed "lightdm" at step no. 4 the graphical interface will start after the server reboots. Reboot it using the command:

```
shutdown -r now
```

If at step no. 4 you installed xinit, start the graphical interface using the command:

```
startx  
```

6\. If you have installed "Xinit" it will launch XFCE automatically. If you have installed "lightdm" select launching XFCE (Xfce Session) and log in with your username and password.

In some cases, at the first start, the system gives a choice of whether to use the default configuration or create an empty panel. If you are working with XFCE for the first time, select the first option — then the taskbar, clock, pre-configured Start menu, and other important things for work will appear on the desktop. In an empty panel, you will have to configure everything yourself.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image11.png" alt="Warning" width="80%">

That's how the desktop with default configuration looks (little details may vary):

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image2.png" alt="Descktop with default configuration" width="80%">

If only folders and widgets are visible on the desktop and there is no panel with the "Applications" button, it’s okay — the panel is simply hidden at the top. Move the slider up to see it.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image33.png" alt="Move the slider up" width="80%">

Everything is ready, use your server with XFCE on it. If you restart the server, it will open the terminal again. You can start the desktop environment using the "startx" command.

### Install XFCE on CentOS

1\. Connect to the server through your Control Panel or via SSH. To connect through the Control Panel, go to the server control panel and click the monitor icon.

<media-gallery>
<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12899747666833.png" alt="Connect to the server through your Control Panel or via SSH"> 

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12899761970449.png" alt="Connect to the server through your Control Panel or via SSH">
</media-gallery>

You can find the login and password for connection in your Control Panel in the "Instructions" section.

<media-gallery>
<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12900025590289.png" alt="Login and password for connection in your Control Panel">  

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12900217123473.png" alt="Login and password for connection in your Control Panel">
</media-gallery>

2\. Install EPEL (Extra Packages for Enterprise Linux) — an open and free repository that contains additional software packages for Linux distributions. This includes the XFCE desktop environment packages. Install EPEL with the command:

```
yum -y install epel-release
```

3\. Install BaseX or X11 (depends on which one is supported by your system) — a system that provides tools and protocols for a graphical interface. It will make windows on the desktop work and help the system control windows by mouse and keyboard. Start the installation with the command:

(for CentOS 7)

```
yum -y groupinstall x11
```

(for CentOS 8)

```
yum -y groupinstall base-x
```

4\. Install the XFCE desktop environment from the EPEL repository with the command:

```
yum --enablerepo=epel -y groups install "Xfce"
```

5\. Create a script for xinit, a tool for the initialization of a graphical system. You use a script to tell xinit to use the XFCE desktop environment when launching the graphical interface. Create a script with the  
command:

```
echo "exec /usr/bin/xfce4-session" >> ~/.xinitrc
```

The desktop environment is installed and ready to run. Start it with the command:

```
startx
```

**Note**: If the system gives an error, most likely, you made a mistake when entering the command in step no. 5. Repeat step no. 5 and then start XFCE with the "startx" command.

At the first start, the system will ask you to choose whether you want to use the default configuration or create an empty panel. If you are working with XFCE for the first time, select the first option — then the taskbar, clock, pre-configured Start menu, and other important things for work will appear on the desktop. In an empty panel, you will have to configure everything yourself.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image28.png" alt="Servers panel" width="80%">

That's how the desktop with default configuration looks:

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image22.png" alt="Servers panel" width="80%">

If only folders and widgets are visible on the desktop and there is no panel with the "Applications" button, it’s okay — the panel is simply hidden at the top. Move the slider up to see it.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image34.png" alt="Move the slider up" width="80%">

Everything is ready to go. Use your server with XFCE on it.

If you restart the server, it will open the terminal again. You can start the desktop environment using the "startx" command.

### Install XFCE on Debian

1\. Connect to the server through your Control Panel or via SSH. To connect through the Control Panel, go to the server control panel and click the monitor icon.

<media-gallery>
<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu
-centos-and-debian/12899747666833.png" alt="Service control panel">

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12899761970449.png" alt="Dashboard">
</media-gallery>

You can find the login and password for connection in your Control Panel in the "Instructions" section.

<media-gallery>
<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12900025590289.png" alt="Service control panel>  
  
<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/12900217123473.png" alt="Server information">
</media-gallery>

2\. Install XFCE with the command:

```
apt-get install xfce4
```

The system will warn you that the installation will take several hundred megabytes of hard disk space.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image16.png" alt="Warning">

Confirm the operation with: ```y```

3\. Install additional components for XFCE (panel, file manager, and various plugins) with the command:

```
apt-get install xfce4-goodies
```

The system will warn you that the installation will take several megabytes of hard disk space.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image27.png" alt="Confirmation">

Confirm the operation with: ```y```

After installation, the graphical environment will be ready to run. Start XFCE with the command:

```
startx
```

At the first start, the system will ask you to choose whether you want to use the default configuration or create an empty panel. If you are working with XFCE for the first time, select the first option — then the taskbar, clock, pre-configured Start menu, and other important things for work will appear on the desktop. In an empty panel, you will have to configure everything yourself.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image30.png" alt="Warning at the first start" width="80%">

That's how the desktop with default configuration looks:

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image21.png" alt="Desktop with default configuration" width="80%">

Everything is ready, use your server with XFCE on it. If you restart the server, it will open the terminal again. You can start the desktop environment using the "startx" command.

## How to open a terminal inside XFCE


Click on "Applications" in the upper-left corner and select "Terminal Emulator". The terminal will open.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image7.png" alt="Click on Applications in the upper-left corner and select Terminal Emulator" width="80%">

## How to log out of XFCE

### For Ubuntu server with "lightdm"

Press Ctrl + Alt + F1 — you will be returned to the terminal without a graphical interface. When you restart the server, the desktop will open again.

### For all other servers

Click on the "Applications" button in the upper-left corner of the screen. Select "Log Out" in the drop-down menu.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image19.png" alt="Click on the Applications button" width="80%">

Select "Log Out" in the pop-up window.

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/manage/install-gui-desktop-environment-on-ubuntu-centos-and-debian/image29.png" alt="Select Log Out in the pop-up window" width="80%">

You will be returned to the terminal. You can start XFCE again with the "startx" command.