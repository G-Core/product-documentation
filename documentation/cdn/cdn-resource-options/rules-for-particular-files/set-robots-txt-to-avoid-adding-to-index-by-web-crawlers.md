---
title: set-robots-txt-to-avoid-adding-to-index-by-web-crawlers
displayName: Set robots.txt
published: true
order: 30
toc:
   --1--How it is going to work?: "how-it-is-going-to-work"
---
When you put your website domain as the Origin-Source, the copy of your website that located on your personal domain name (cname) could be indexed by search engines. 

If you want to prevent it: 

1.  Create a folder _on the origin_ and add a _robots.txt_ file with the following settings:   
    User-agent: \*    
    Disallow: / 
2.  Create a _Rule for your CDN-resource_ with the following settings:   
    Match Type: Regular expression   
    Rule pattern: robots.\*   
    Rewrite: /(.\*) /folder/$1 

Where **folder** is the name of the folder that you’ve created in the first step.

Example: 

<img src="https://support.gcore.com/hc/article_attachments/360011410098/______.png" alt="______.png" width="470" height="721">

How it is going to work? 
-------------------------

The **robots.****txt** file controls how search engine spiders see and interact with your webpage. 

The added rule allows us to rewrite a path for **robots.****txt** that will be used by web crawlers. For example,  if your personal domain is **_cdn.domain.com_**, the search engine crawlers will request the **_cdn.domain.com/robots.txt URL_** which contains restrictions for indexing. 

Consequently, domain _**cdn.domain.**__**com**_ won’t be indexed.

! These settings don’t affect the website itself.