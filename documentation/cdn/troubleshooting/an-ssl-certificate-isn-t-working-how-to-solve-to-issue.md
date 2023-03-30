---
title: an-ssl-certificate-isn-t-working-how-to-solve-to-issue
displayName: Attaching or issuing an SSL certificate 
published: true
order: 40
toc:
    --1--Can't attach a personal certificate to a resource: "cant-attach-a-personal-certificate-to-a-resource"
    --1--Can't get Let's Encrypt certificate: "cant-get-lets-encrypt-certificate"
---
Can't attach a personal certificate to a resource
-------------------------------------------------

**Check whether there is an empty line at the end of a certificate chain**. The line is often forgotten, the error occurs because of this. This is how the chain with an empty line at the end looks:

[<img title="" src="https://support.gcore.com/hc/article_attachments/4410656833937/image-3.png" alt="" width="569" height="165">](https://support.gcorelabs.com/hc/article_attachments/4410656833937/image-3.png)  
Full instructions for attaching a certificate: [How to attach a personal certificate to a resource](https://gcorelabs.com/support/articles/213970109/#h_548bd48f-d293-45f4-a4ee-5f373b52fbfd).

Can't get Let's Encrypt certificate
-----------------------------------

**Check** **whether** **the** **[rules](https://gcorelabs.com/support/articles/115005383865/)** **you created overlap the path "/.well-known/acme-challenge/<TOKEN>".** This is the path for issuing a certificate, in many cases, such a rule (for example, with the path "/.\*") does not allow issuing the certificate. Disable the rule, get the certificate, and enable the rule again.

You can check whether the rule blocks the certificate issuance path using this service: [https://regex101.com/r/Hy9bKy/1](https://regex101.com/r/Hy9bKy/1).

**Check whether you have added a CNAME record with our domain**. Your domain's DNS records must have a CNAME record with your personal zone as the value. The certificate cannot be issued without it. You will find the value for the record in the second step of the setup guide for the resource:

[<img title="" src="https://support.gcore.com/hc/article_attachments/4410656834705/image-4.png" alt="" width="718" height="162">](https://support.gcorelabs.com/hc/article_attachments/4410656834705/image-4.png)[<img title="" src="https://support.gcore.com/hc/article_attachments/4410644741265/image-5.png" alt="" width="351" height="276">](https://support.gcorelabs.com/hc/article_attachments/4410644741265/image-5.png)

If these tips don’t help, write to technical support via the chat in the corner of the screen — we will help you.