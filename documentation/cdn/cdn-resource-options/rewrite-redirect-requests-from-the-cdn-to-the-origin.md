---
title: rewrite-redirect-requests-from-the-cdn-to-the-origin
displayName: Rewrite
published: true
order: 70
toc:
---
Rewrite option is useful for changing or redirecting query paths. The option works accordingly to [nginx](https://nginx.ru/en/docs/http/ngx_http_rewrite_module.html) configuration.

To enable Rewrite click Add Option in Content section and choose Enable Rewrite. You also can set up Rewrite in the Rules section.

After the option activation, some default values are shown in Rewrite body field. Clear the field and enter two space-separated directives: a path the Rewrite option is applied to and a path to be used instead. Use regular expressions. 

<img src="https://support.gcore.com/hc/article_attachments/115011465265/Screenshot-2018-1-7_G-Core_Labs___________CDN-___________________1_.png" alt="Screenshot-2018-1-7_G-Core_Labs___________CDN-___________________1_.png">

How to set up Rewrite

For example, you need to apply Rewrite to all the resource and make CDN-servers get the content from the certain directory on your origin.

Let's say that origin is example.com and directory is /media/

Fill the Rewrite field with the following:

/(.\*) /media/$1

where:

*   /(.\*) - the group of variables for which one Rewrite is applied. With this (.\*) group Rewrite; will be applied for all of the possible variants which can appear after / in example.com/;
*   /media/ - directory, where CDN-servers will go for the content;
*   $1 - the number of the group of variables. If you have more than one group, the next numbers will be $2, $3 and so on.

Break flag is applied to the option by default. It is not shown in the field. 

You may apply to the option any other ngnix flags via [API-documentation](https://apidocs.gcore.com/cdn#tag/Resources).