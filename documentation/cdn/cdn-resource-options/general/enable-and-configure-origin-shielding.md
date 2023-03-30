---
title: enable-and-configure-origin-shielding
displayName: Enable shielding (paid)
published: true
order: 50
toc:
   --1--What is Origin shielding?: "what-is-origin-shielding"
   --1--Enable it: "enable-origin-shielding"
---


What is Origin shielding?
-------------------------

Origin shielding is a Gcore CDN paid option that helps protect your origin server from being overloaded with requests from multiple CDN servers. This option accumulates all CDN server requests at a special server called a shield or precache server.

The shield server works like a usual CDN server but is located between your origin server and the entire content delivery network. It receives requests, caches content, transmits files from the cache, and requests the source only if it doesn’t have the needed file in the cache. When a burst in traffic occurs, the shield server receives all the requests from CDN servers, thus protecting your server from being overloaded.

<img src="https://support.gcore.com/hc/article_attachments/9421139226769/Shield_server.jpeg" alt="Shield server.jpeg">

Enable Origin shielding
-----------------------

1\. Go to the Origin shielding section in Resource settings and complete the remaining steps there.

<img src="https://support.gcore.com/hc/article_attachments/13341830161809" alt="mceclip0.png">

2\. Turn on the **Enable origin shielding** toggle.

3\. Choose the location for the precache server from the drop-down list. In most cases, you need to choose the closest location to your origin server.

4\. Save changes.

The option will begin to activate. It takes less than 15 minutes. You’ll see the notification:

<img src="https://support.gcore.com/hc/article_attachments/9421163382289/Activation.png" alt="Activation.png">