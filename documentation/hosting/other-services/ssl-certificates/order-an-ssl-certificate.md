---
title: order-an-ssl-certificate
displayName: Order
order: 20
published: true
toc:
    --1--Certificate settings: "certificate-settings"
    --2--Request: "request"
    --2--Information: "information"
    --1--Generating a key: "generating-a-key"
    --1--Enter the contact information: "enter-the-contact-information"
    --1--Confirm domain ownership: "confirm-domain-ownership"
pageTitle: Activate an SSL certificate | Gcore
pageDescription: Learn how to buy an SSL certificate.
---
# Order an SSL certificate

In the hosting control panel, go to the Products / Services section, then select the SSL certificates tab.

<img src="https://assets.gcore.pro/docs/hosting/other-services/ssl-certificates/order-an-ssl-certificate/SSL-certificates.JPG" alt="Order an SSL certificate" width="50%">

A new SSL certificate selection form will be opened, and you will see available providers and types of certificates.

Select the certificate you wish to order and click the **Order** button.

<img src="https://assets.gcore.pro/docs/hosting/other-services/ssl-certificates/order-an-ssl-certificate/SSL-cert_list.JPG" alt="Select the certificate " width="80%">

## Certificate settings

### Request

You can generate the request for a new certificate right in the control panel or you can import an existenting request file.

### Information

- Enter a domain for which a certificate will be issued. If you want to protect only one domain, enter www.example.com. If you want to use certificates that can also be used for subdomains, enter ```*.example.com```
- Enter your country and region
- Enter a name of your Organization. Please note that if you order OV certificate you may need to confirm the data which you specify on this stage.

## Generating a key

At this step, a secret key for the certificate is generated. This part of the key will be saved in the billing system after the certificate is issued. For security reasons, we recommend you delete it from the control panel and save locally so that you can access this information whenever you need. The secret part of the key is needed when you install the certificate on a server.

If you lose an access to the secret part of the key which was generated at this step, you will need to reissue the certificate.

## Enter the contact information

You must specify contacts of administrative and technical representatives of your project. As an administrative contact should act a person on behalf of a company. He or she will get a copy of the certificate by email.

A person designated as a technical representative will receive a copy of the certificate after a release, and further notifications about certificate renewal will be received.

## Confirm domain ownership

You need to make sure that on the mail server that serves your domain there is one of the mailboxes offered by the system:

- ```admin@example.com```
- ```administrator@example.com```
- ```hostmaster@example.com```
- ```postmaster@example.com```
- ```webmaster@example.com```

You will receive instructions how to confirm an ownership of the domain on this mailbox.