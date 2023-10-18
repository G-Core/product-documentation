---
title: add-an-ssl-certificate-to-deliver-content-over-https
displayName: SSL overview
published: true
order: 10
toc:
   --1--SSL certificate: "what-is-an-ssl-certificate"
   --1--Types: "ssl-certificate-types-in-gcore"

pageTitle: Adding, Renewing, and Deleting of SSL Certificates | Gcore
pageDescription: Learn how to add your certificate or get a free Let's Encrypt certificate, renew, and delete SSL certificates.
---
# Add an SSL certificate to deliver content over HTTPS

## What is an SSL certificate?

An SSL certificate is a unique digital signature for your website that verifies the authenticity of your domain and allows you to configure the HTTPS protocol for the site. This protocol provides a secure connection between a client and a server. It is essential when sensitive information is being transferred, such as during financial transactions. Learn more about SSL certificates in our <a href="https://gcore.com/learning/what-are-ssl-certificates/" target="_blank">Learning article</a>.

If you want to deliver content using our CDN via secured HTTPS protocol, you need to add an SSL certificate for your CDN resource’s <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">custom domain</a>.  

**Note**: You can only attach one certificate per CDN resource.

## SSL certificate types in Gcore

In Gcore, two types of SSL certificates are available:

1. Your own SSL certificate. You can issue a certificate for the custom domain in the format, e.g., cdn.example.com from a third-party company and add its data to the control panel. Either do so during <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate#method-1-add-ssl-certificate-during-cdn-resource-creation" target="_blank">CDN resource creation</a> or <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-your-own-ssl-certificate#method-2-add-ssl-certificate-for-an-existing-cdn-resource" target="_blank">add it later</a>.   

2. Free Le</a>t’s Encrypt certificate. You can issue a free Let’s Encrypt certificate for your custom domain. All data will be added automatically by Gcore. Either do so during <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-lets-encrypt-certificate#during-resource-creation" target="_blank">CDN resource creation</a> or <a href="https://gcore.com/docs/cdn/ssl-certificates/configure-lets-encrypt-certificate#for-created-resource" target="_blank">add it later</a>.