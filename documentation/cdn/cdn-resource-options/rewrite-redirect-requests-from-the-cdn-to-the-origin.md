---
title: rewrite-redirect-requests-from-the-cdn-to-the-origin
displayName: Rewrite
published: true
order: 70
toc:
pageTitle: Setting Up Redirect Requests via CDN Rewrite | Gcore
pageDescription: Learn how to redirect requests from CDN to origin using the Rewrite option, applying it to paths and directories.
---
# Rewrite: redirect requests from the CDN to the origin

Rewrite option is useful for changing or redirecting query paths. The option works accordingly to <a href="https://nginx.ru/en/docs/http/ngx_http_rewrite_module.html" target="_blank">nginx</a> configuration.

To enable Rewrite click **Add Option** in "Content" section and choose Enable Rewrite. You also can set up Rewrite in the Rules section.

After the option activation, some default values are shown in Rewrite body field. Clear the field and enter two space-separated directives: a path the Rewrite option is applied to and a path to be used instead. Use regular expressions. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rewrite-redirect-requests-from-the-cdn-to-the-origin/Screenshot-2018-1-7_G-Core_Labs___________CDN-___________________1_.png" alt="Rewrite body field" width="50%">

For example, you need to apply Rewrite to all the resource and make CDN-servers get the content from the certain directory on your origin. Let's say that origin is example.com and directory is /media/, to set up Rewrite fill the "Rewrite" field with the following:

<code-block>
<span style="color:#FF5913">/(.*) /media/$1</span>
</code-block>

where:

- <span style="color:#FF5913">/(.*)</span> is the group of variables for which one Rewrite is applied. With this (.*) group Rewrite; will be applied for all of the possible variants which can appear after / in example.com/;
- <span style="color:#FF5913">/media/</span> is the directory, where CDN servers will go for the content;
- <span style="color:#FF5913">$1</span> is the number of the group of variables. If you have more than one group, the next numbers will be $2, $3 and so on.

Break flag is applied to the option by default. It is not shown in the field. You may apply to the option any other ngnix flags via <a href="https://api.gcore.com/docs/cdn#tag/Resources" target="_blank">API documentation</a>.