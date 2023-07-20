---
title: integrate-cdn-resource-with-perch
displayName: Perch
published: true
order: 150
toc:
pageTitle: Integrate CDN with Perch Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Perch CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with Perch

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Login to your Perch control panel at *yoursite.com/perch*. Open this file: ```perch/config/config.php```. Search the following line:

```
define('PERCH_RESPATH', PERCH_LOGINPATH . '/resources');
```

Update the line to the following. Instead of cdn.site.com type in the CNAME  that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration

<code-block>
define('PERCH_RESPATH', '<span style="color:#FF5913">http://cdn.site.com</span>' . PERCH_LOGINPATH . '/resources');
</code-block>

Where <span style="color:#FF5913">http://cdn.site.com</span> is the domain of your CDN resource.

In case you have custom buckets lists and want to deliver them through CDN, you need to add a prefix to ```web_path``` parameters.

Open this file: ```perch/config/buckets.php```. Search the following line:

```
'web_path' => '/my/bucket/path',
```

Update the lines as follows:

<code-block>
'web_path' => '<span style="color:#FF5913">http://cdn.site.com/path/to/my/bucket/</span>', 
</code-block>

Where <span style="color:#FF5913">http://cdn.site.com/path/to/my/bucket/</span> is the path to your bucket with the domain name of your CDN resource.

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.