---
title: protect-cdn-resource-from-owasp-top-10-with-basic-waf
displayName: Basic WAF (free)
published: true
order: 120
toc:
   --1--What is "Basic WAF"?: "what-is-basic-waf"
   --1--How to enable: ""
   --1--What to do if "Basic WAF" blocks some content: ""
---
  
  

What is "Basic WAF"?
--------------------

"Basic WAF" is a firewall that protects your resource from attacks related to the following vulnerabilities:

*   Injections
*   Broken Authentication
*   Sensitive Data Exposure
*   XML External Entities (XXE)
*   Broken Access control
*   Security misconfigurations
*   Cross Site Scripting (XSS)
*   Insecure Deserialization
*   Using Components with known vulnerabilities
*   Insufficient logging and monitoring

The option is free. The number of protected requests for one resource may be limited.

How to enable "Basic WAF"
-------------------------

You can activate the firewall for the whole resource or for specific URLs. To enable "Basic WAF" for a resource, go to "Resource settings" and toggle on the "Basic WAF" option.

<img src="https://support.gcore.com/hc/article_attachments/5622112482449/mceclip0.png" alt="mceclip0.png" width="656" height="637">

If you want to activate the firewall for specific URLs, go to settings of the [rule](https://support.gcore.com/hc/en-us/articles/115005383865) managing these URLs, add the "Basic WAF" option and enable it. 

<img src="https://support.gcore.com/hc/article_attachments/5622149724305/mceclip1.png" alt="mceclip1.png" width="655" height="603">

What to do if "Basic WAF" blocks some content
---------------------------------------------

Our protection is based on the [NGINX ModSecurity WAF modul](https://docs.nginx.com/nginx-waf/admin-guide/nginx-plus-modsecurity-waf-owasp-crs/). This module uses a standard set of rules that protects against OWASP Top 10. If a request was blocked, it means that the request has fallen under one of the rules.

If only certain URLs are blocked, we recommend not deactivating the firewall completely, but deactivating it only for blocked URLs. To do this:

1.  Create a [rule](https://support.gcore.com/hc/en-us/articles/115005383865) with the _location_ that is blocked by "Basic WAF".
2.  Add the "Basic WAF" option to the rule and turn it off.

<img src="https://support.gcore.com/hc/article_attachments/5622393028497/mceclip2.png" alt="mceclip2.png" width="656" height="678">

If you need more flexible settings, use the paid product "[Web Application Security](https://gcore.com/web-security)" — with it, you can install WAF, protect it from hacking, install protection against bots and DDoS attacks, define black and white lists. Contact our technical support to consult — we will be happy to tell you more about "Web Application Security".