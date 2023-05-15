---
title: create-and-configure-a-protected-resource
displayName: Create protected resource
published: true
order: 30
toc:
   --1--Control panel settings: "control-panel-settings"
   --1--Origin settings: "origin-settings"
   --1--Additional measures: "additional-protective-measures"
---
# Create and configure a protected resource

To protect your website, change your IP address to ours (you can get it once you set up a resource in the Control Panel).

## Сontrol panel settings

Go to the Web Protection tab and click on the **Create DDoS resource** button.

<img src="https://support.gcore.com/hc/article_attachments/8945657763089/mceclip0.png" alt="" width="70%">

Type your website URL without *http(s)://* in the "Your Domain" field.

If you have a third-level domain which you want to protect add it in the Aliases field. Click on plus right from the field to add more than one domain.

Check the Redirect from WWW to the primary domain box if you don't use www third-level domain. 

If you want requests from the DDoS protection servers to your origin sent via http check the Redirect from https to http box.

Add your IP address to the Original IP address field. We will send legitimate traffic there. Click on Identify Automatically to automatically fill in the IP.

Click on *Save changes*. Activation will take a couple of minutes.

To add an SSL certificate to your domain or subdomains go to the resource Settings -> SSL -> Edit

<img src="https://support.gcore.com/hc/article_attachments/8945718376849/mceclip1.png" alt="" width="70%">

There are three options:

- None (no SSL certificate is added, the requests are sent via HTTP)
- Let's Encrypt (we order and automatically renew a free SSL certificate from Let's Encrypt. **Works only if you have already pointed your domain name to the protected IP address in your DNS** **settings**)
- Custom (add your SSL certificate by uploading the certificate in PEM format and your private key).

More information on SSL certificates can be found in the <a href="https://gcore.com/docs/web-security/add-an-ssl-certificate-to-your-resource" target="_blank">Add an SSL certificate to your resource</a> article.

## Origin Settings

On the Web Protection tab find the protected IP for your resource. Change the A-record in your DNS settings: replace your current IP with the protected one. A DNS record renewal depends on a Time To Live (TTL) value: it determines how long the record is cached by the servers.

## Additional Protective Measures

To protect your website you need to hide your real IP address. Once you finish the basic setup DNS servers will start providing our IP to the requests but that is not the only way to get the website's real IP. Follow our recommendation for <a href="https://gcore.com/docs/web-security/configure-additional-protection-settings" target="_blank">additional protective measures</a> to ensure your website security.

The recommendations are also available in the Control Panel: go to the Web Protection tab -> click on the arrow near Settings button -> Setup guide.