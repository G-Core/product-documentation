---
title: set-up-control-panel-services-urls
displayName: Set up product URLs
published: true
order: 50
toc:
---
#  Set up Customer Portal product URLs

The customer's Customer Portal is a combination of different products. Here are the product URL examples for Gcore customers:

- auth.gcore.com — authorization
- accounts.gcore.com — customer account management
- cdn.gcore.com - CDN product
- cloud.gcore.com — Edge Cloud product
- streaming.gcore.com — Video Streaming product
- storage.gcore.com — Storage product
- control.gcore.com — Web Application Security product
- dns.gcore.com — Managed DNS product
- api.gcore.com/docs - API Documentation
- api.gcore.com - API domain.

We are using Single Sign-On authentication between the products, so once users log in to the Customer Portal (authorization service), they can access other products automatically.

All of the URLs above have the same base — gcore.com — which we call Base Customer Portaldomain. Products' subdomains are added automatically to the Base Customer Portal domain.

You need to inform your manager which Base Customer Portal domain you would like to have, and we will set up the products for your users' Customer Portal.

**Note**: The goal of this article is to explain how the customers' Customer Portal works. To avoid issues with the Customer Portal performance we recommend you abstain from making changes to CDN Resources described below.

A CDN Resource powers every product. We create those resources in your technical account. The technical account is your first customer account in the Admin Portal. It's created automatically; its email and company name match reseller's email and company name.

The technical account is used to collect statistics and to form monthly reports. All Admin Portal users (Reseller and Sellers) are listed under this account. The technical account can't be deleted. We recommend you abstain from making any changes to this account on your own. 

Due to the security reasons, the Customer Portal works only via HTTPS so for each CDN Resource an SSL-certificate must be added or you can add one wildcard SSL-certificate for the Base Customer Portal domain value.

Once we set up the CDN Resources we ask you to add new records to your DNS settings. You need to create a CNAME record for each product URL. CNAME record is pointed to you personal domain zone which we also provide.

When everything is ready we put your Base Customer Portal domain into the field with the same name in the "Branding settings" section.