---
title: integrate-cdn-resource-with-perch
displayName: Perch
published: true
order: 150
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to your Perch control panel at yoursite.com/perch

Open this file: perch/config/config.phpSearch the following line:

define('PERCH\_RESPATH', PERCH\_LOGINPATH . '/resources');

Update the line to the following. Instead of cdn.site.com type in the CNAME  that you specified in the G-Core [control panel](https://control.gcdn.co/). Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration

define('PERCH\_RESPATH', 'http://_**cdn.site.com**_' . PERCH\_LOGINPATH . '/resources');

In case you have custom buckets lists and want to deliver them through CDN, you need to add a prefix to web\_path parameters.

Open this file: perch/config/buckets.php

Search the following line:

'web\_path' => '/my/bucket/path',

Update the lines follows:

'web\_path' => 'http://_**cdn.site.com**_/path/to/my/bucket/', 

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.