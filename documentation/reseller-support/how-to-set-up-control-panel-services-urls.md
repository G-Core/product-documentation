---
title: how-to-set-up-control-panel-services-urls
displayName: How to set up control panel services URLs
published: true
toc:
---

# How to set up control panel services URLs

The client control panel is a combination of different services. Here are the service URL examples for G-Core Labs clients:

*   auth.gcorelabs.com — authorization service,
*   accounts.gcorelabs.com — user account management service,
*   storage.gcorelabs.com — Storage service,
*   cloud.gcorelabs.com — Cloud service,
*   media.gcorelabs.com — Media Platform service,
*   control.gcorelabs.com — service for CDN and DDoS Protection. The products will get their own services in the future.

We are using Single Sign-On authentication between the services, so once users log in to the control panel (authorization service), they can access other services automatically.

All of the URLs above have the same base — gcorelabs.com — which we call Base control panel domain. Services' subdomains are added automatically to the Base control panel domain.

You need to inform your manager which Base control panel domain you would like to have, and we will set up the services for your users' control panel.

_The goal of this article is to explain how the clients' control panel works. To avoid issues with the control panel performance we recommend you abstain from making changes to CDN Resources described below._

A CDN Resource powers every service. We create those resources in your technical account. The technical account is your first client account in the admin panel. It's created automatically; its email and company name match reseller's email and company name.

The technical account is used to collect statistics and to form monthly reports. All admin panel users (Reseller and Sellers) are listed under this account. The technical account can't be deleted. We recommend you abstain from making any changes to this account on your own. 

Due to the security reasons the control panel works only via HTTPS so for each CDN Resource an SSL-certificate must be added or you can add one wildcard SSL-certificate for the Base control panel domain value.

Once we set up the CDN Resources we ask you to add new records to your DNS settings. You need to create a CNAME record for each service URL. CNAME record is pointed to you personal domain zone which we also provide.

When everything is ready we put your Base control panel domain into the field with the same name in the "Branding" section.
