---
title: integrate-cdn-resource-with-b2evolution
displayName: B2evolution
published: true
order: 20
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

 Use your СNAME (cdn.site.com) that you specified in the G-CORE [control panel](https://control.gcdn.co/) for the following steps. Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration

One single file needs to be edited in order to set the path variables to point to the CDN location:  blogs/conf/\_advanced.php

Add a new variable in the beginning.

Replace the following variables in the code

Replace _cdnurl_ with your CNAME. For example: ‘http://cdn.site.com/’; 

| Before                               | After replacement                    |
|------------------------------------------|------------------------------------------|
 | $rsc_url = $baseurl.$rsc_subdir;     | $rsc_url = $cdnurl .$rsc_subdir;     |
| $skins_url = $baseurl.$skins_subdir; | $skins_url = $cdnurl .$skins_subdir; |
| $media_url = $baseurl.$media_subdir; | $media_url = $cdnurl .$media_subdir; |


Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.
