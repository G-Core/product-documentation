---
title: integrate-cdn-resource-with-b2evolution
displayName: B2evolution
published: true
order: 20
toc:
pageTitle: Integrate CDN with B2evolution Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with B2evolution CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with B2evolution

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Use your СNAME (cdn.site.com) that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a> for the following steps. Ensure that your  <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

One single file needs to be edited in order to set the path variables to point to the CDN location: ```blogs/conf/_advanced.php```

Add a new variable in the beginning.

Replace the following variables in the code

Replace *cdnurl* with your CNAME. For example: ```http://cdn.site.com/```

<table>
<thead>
  <tr>
    <th><strong>Before</strong></th>
    <th><strong>After replacement</strong></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>$rsc_url = $baseurl.$rsc_subdir;</td>
    <td>$rsc_url = $cdnurl .$rsc_subdir;</td>
  </tr>
  <tr>
    <td>$skins_url = $baseurl.$skins_subdir;</td>
    <td>$skins_url = $cdnurl .$skins_subdir;</td>
  </tr>
  <tr>
    <td>$media_url = $baseurl.$media_subdir;</td>
    <td>$media_url = $cdnurl .$media_subdir;</td>
  </tr>
</tbody>
</table>

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.
