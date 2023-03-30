---
title: troubleshoot-blocked-smtp-ports
displayName: SMTP ports
published: true
toc:
---
#### If you can't send email through SMTP ports 25, 465 and 587, most likely your virtual server is suspected of sending spam.

Go to "Support tickets" in your control panel and check if there are any messages about blocking.

[<img src="https://support.gcore.com/hc/article_attachments/10138328512401" alt="Screenshot_2022-10-26_at_09.50_1.png">](https://support.gcorelabs.com/hc/article_attachments/360019842577/mceclip4.png)

<img src="https://support.gcore.com/hc/article_attachments/10138347613713" alt="Screenshot_2022-10-26_at_09.57_1.png">

According to paragraph 2 (d) of the [Acceptable Use Policy](https://gcorelabs.com/legal/), servers cannot be used to send unsolicited emails, chain letters, mailbombs, or spam. You are only allowed to send emails to users of the services located on the Gcore servers rented by you. If you haven't violated our Acceptable Use Policy, [contact our technical support](https://support.gcorelabs.com/hc/en-us/articles/115003753885), we will unblock you. 

| Case                                                                                          | Solution                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| You send legitimate emails                                                                    | \nAsk the technical support to unblock the ports and specify in your request:\n   • The domain name of the service whose users you sent the mailing to \n                                                                                                                                            |
| You did not send mailing, but you still received blocking messages.                           | \nCheck the server settings. For some reason, your server sends a lot of traffic via SMTP ports, and our system recognizes this as spam. Fix the settings and ask the tech support to unblock the ports. Specify in your request:\n   • An error in settings you fixed   • How you fixed the error\n |
| You did not send mailings, did not receive blocking messages, but the ports still do not work | \nAsk the technical support to unblock the ports and specify in your request:\n   • That you did not receive blocking messages   • Whether you changed the network settings or not\n                                                                                                                 |
