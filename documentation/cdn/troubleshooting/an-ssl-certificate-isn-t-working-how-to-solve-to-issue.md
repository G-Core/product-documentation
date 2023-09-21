---
title: an-ssl-certificate-isn-t-working-how-to-solve-to-issue
displayName: Attaching or issuing an SSL certificate 
published: true
order: 40
toc:
   --1--Can't attach a personal certificate to a resource: "cant-attach-a-personal-certificate-to-a-resource"
   --1--Can't get Let's Encrypt certificate: "cant-get-lets-encrypt-certificate"
pageTitle: SSL certificate Issues | Gcore
pageDescription: What to do if you can't attach personal or Let's Encrypt certificates.
---
# An SSL certificate isn't working: how to solve to issue

## Can't attach a personal certificate to a resource

**Check whether there is an empty line at the end of a certificate chain**. The line is often forgotten, the error occurs because of this. This is how the chain with an empty line at the end looks:

<img title="" src="https://assets.gcore.pro/docs/cdn/troubleshooting/an-ssl-certificate-isn-t-working-how-to-solve-to-issue/image-3.png" alt="Can't attach a personal certificate to a resource" width="50%">

Full instructions for attaching a certificate: <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/add-an-ssl-certificate-to-deliver-content-over-https#add-an-ssl-certificate-during-resource-creation" target="_blank">Add an SSL certificate to deliver content over HTTPS</a>.

## Can't get Let's Encrypt certificate

**Check whether the <a href="https://gcore.com/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files" target="_blank">rules</a> you created overlap the path "/.well-known/acme-challenge/<TOKEN>".** This is the path for issuing a certificate, in many cases, such a rule (for example, with the path "/.\*") does not allow issuing the certificate. Disable the rule, get the certificate, and enable the rule again.

You can check whether the rule blocks the certificate issuance path using <a href="https://regex101.com/r/Hy9bKy/1" target="_blank">this service</a>.

**Check whether you have added a CNAME record with our domain**. Your domain's DNS records must have a CNAME record with your personal zone as the value. The certificate cannot be issued without it. You will find the value for the record in the second step of the setup guide for the resource:

<img title="" src="https://assets.gcore.pro/docs/cdn/troubleshooting/an-ssl-certificate-isn-t-working-how-to-solve-to-issue/image-4.png" alt="Can't get Let's Encrypt certificate" width="80%">

If these tips don’t help, write to technical support via the chat in the corner of the screen — we will help you.