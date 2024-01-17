---
title: set-up-a-mailing-server-in-gcore-cloud-vm
displayName: Set up a mailing server
order: 10
published: true
toc:
pageTitle: Set up a mailing server | Gcore
pageDescription: Discover how to set up your own mail server on Gcore Cloud VM using Postfix and Dovecot and manage DNS records for optimal performance.
---
# Set up a mailing server in Gcore Cloud VM

This article outlines basic steps for setting up a mail server using popular components such as Postfix and Dovecot. Please note that mail server setup may vary depending on the selected software and operating system, as well as the environment’s specific settings. This article is focused on the Ubuntu and Debian operating systems.

**Please note**: The use of email sending services must not violate <a href="https://gcore.com/legal" target="_blank">our terms of use</a>. Suspicious requests will be rejected and, if necessary, accounts will be blocked.

1. Create an instance.

Install Cloud VM using <a href="https://gcore.com/docs/cloud/virtual-instances/create-an-instance" target="_blank">our guide</a>. The minimum available configuration—1vCPU and 2 GB RAM—will be enough to install and run a mail server on your instance.

2. Check internet access.

Check the **Network settings** tab in the machine settings. The interface must be set to the public to access the internet.

<img src="https://assets.gcore.pro/docs/cloud/use-cases/1.png" alt="Network settings tab in the machine settings">

However, if you first chose the option private method, then you need to get a <a href="https://gcore.com/docs/cloud/networking/ip-address/create-and-configure-a-floating-ip-address" target="_blank">floating IP address</a> to access the internet.

**Please note**: By default, Gcore Cloud VM has limits on SMTP port 25. In order to open a port and successfully install a mail server, <a href="https://accounts.gcore.com/tickets/all" target="_blank">contact support</a> and click **Create Ticket**.

<img src="https://assets.gcore.pro/docs/cloud/use-cases/2.png" alt="Create Ticket">

3. Connect to your Gcore Cloud VM via either <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-ssh" target="_blank">SSH</a> or <a href="https://gcore.com/docs/cloud/virtual-instances/connect/connect-to-your-instance-via-control-panel" target="_blank">the VNC concole</a> in your control panel.

4. Install Postfix.

<a href="https://www.postfix.org/" target="_blank">Postfix</a> is one of the popular Mail Transfer Agents (MTAs) responsible for sending and delivering mail messages. To install Postfix, run the following commands:

```
sudo apt-get update
sudo apt-get install postfix
```

During Postfix installation, you will be prompted to select a configuration type. Select the `Internet Site` option and enter the fully qualified hostname of your server, then click `<Ok>`.

<img src="https://assets.gcore.pro/docs/cloud/use-cases/3.png" alt="Internet Site option">

5. Configure Postfix.

Navigate to the Postfix configuration file:

```
sudo nano /etc/postfix/main.cf
```

In this configuration file, edit the following parameters:

```
myhostname = your_server_domain.com
mydestination = your_server_domain.com, localhost.localdomain, localhost
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
```

- **myhostname**: Specify the fully qualified domain name of the virtual server on which Postfix is running.

- **mydestination**: Specify the domains for which mail will be delivered locally instead of being forwarded to another host.

- **mynetworks**: Specify a list of networks or IP addresses from which mail messages are allowed to be sent through this server.

<img src="https://assets.gcore.pro/docs/cloud/use-cases/4.png" alt="Configure Postfix">

Save the changes and restart Postfix:

```
sudo service postfix restart
```

More information about Postfix is available in their <a href="https://www.postfix.org/documentation.html" target="_blank">documentation</a>.

6. Install Dovecot.

<a href="https://www.dovecot.org/" target="_blank">Dovecot</a> is an IMAP (Internet Message Access Protocol) and POP3 (Post Office Protocol 3) server that provides access to mailboxes. It is required during the mail server setup, so installing it will be the next step. Use the following command to install Dovecot:

```
sudo apt-get install dovecot-imapd dovecot-pop3d
```

7. Configure Dovecot.

Add the following SSL parameters:

```
listen = *, ::
ssl = required
ssl_cert = </etc/ssl/certs/ssl-cert-snakeoil.pem
ssl_key = </etc/ssl/private/ssl-cert-snakeoil.key
```

Insert the required SSL parameters below, as noted in the screenshot, after `listen = *, ::`.

<img src="https://assets.gcore.pro/docs/cloud/use-cases/5.png" alt="required SSL parameters">

Save your changes and restart Dovecot:

```
sudo service dovecot restart
```

8. Create mailboxes.

Now you have successfully configured and installed Postfix and Dovecot, you can create mailboxes for users. For each user, run this command:

```
sudo useradd -m -s /usr/sbin/nologin username
sudo passwd username
```

Create a password for each user and retype it. The password will be saved automatically.

<img src="https://assets.gcore.pro/docs/cloud/use-cases/6.png" alt="Create a password">

9. Add DNS records.

Next, you should manage the DNS settings. Use <a href="https://gcore.com/docs/dns/dns-records/set-up-dns-for-sending-email" target="_blank">our PD guide</a> to get step-by-step configuration instructions.

10. Test and verify.

Restart Postfix and Dovecot to apply the changes. 

```
sudo service postfix restart
sudo service dovecot restart
```

You can use an email client (for example, <a href="https://www.thunderbird.net/" target="_blank">Thunderbird</a>) to send a test email from one of the email addresses you created. After sending a test email, check your email client or webmail to receive this email. Analyze the Postfix and Dovecot logs, located in the following directory:

```
/var/log/mail.log
``` 
