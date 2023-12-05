---
title: troubleshoot-blocked-smtp-ports
displayName: SMTP ports
published: true
order: 50
toc:
pageTitle: Troubleshoot blocked SMTP ports | Gcore
pageDescription: Learn how to troubleshoot blocked SMTP ports. 
---
# Troubleshoot blocked SMTP ports

If you can't send email through SMTP ports 25, 465 and 587, most likely your virtual server is suspected of sending spam.

Go to "Support tickets" in your control panel and check if there are any messages about blocking.

<media-gallery>
<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/troubleshooting/troubleshoot-blocked-smtp-ports/10138328512401.png" alt="Troubleshoot blocked SMTP ports">

<img src="https://assets.gcore.pro/docs/hosting/virtual-servers/troubleshooting/troubleshoot-blocked-smtp-ports/10138347613713.png" alt="Troubleshoot blocked SMTP ports">
</media-gallery>

According to paragraph 2 (d) of the <a href="https://gcore.com/legal" target="_blank">Acceptable Use Policy</a>, servers cannot be used to send unsolicited emails, chain letters, or spam. You are only allowed to send emails to users of the services located on the Gcore servers rented by you. If you haven't violated our Acceptable Use Policy, please <a href="https://gcore.com/docs/hosting/contact-our-technical-support" target="_blank">contact our technical support</a> for details. 

| Case                                                                                          | Solution                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You send legitimate emails                                                                    | Ask the technical support to unblock the ports and specify in your request:   • The domain name of the service whose users you sent the mailing to                                                                                                                                             |
| You did not send mailing, but you still received blocking messages.                           | Check the server settings. For some reason, your server sends a lot of traffic via SMTP ports, and our system recognizes this as spam. Fix the settings and ask the tech support to unblock the ports. Specify in your request:  <br> • An error in settings you fixed <br>  • How you fixed the error |
| You did not send mailings, did not receive blocking messages, but the ports still do not work | Ask the technical support to unblock the ports and specify in your request:  <br> • That you did not receive blocking messages  <br> • Whether you changed the network settings or not                                                                                                                 |
