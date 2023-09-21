---
title: integrate-cdn-resource-with-vbulletin
displayName: vBulletin
published: true
order: 200
toc:
pageTitle: Integrate CDN with vBulletin Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with vBulletin CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with vBulletin

Before you take any steps please back up your files and database. The plugin works only with the default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

1\. Login to your vBulletin control panel.

2\. Go to Styles, then to Replacement Variable Manager.

3\. Choose Add New Replacement Variable.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-vbulletin/vbulletin.png" alt="Integrate CDN resource with vBulletin" >

Using your CNAME from the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a> (```cdn.site.com```). Create a new replacement variable for each item in the following table. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-vbulletin/bulletin_______.png" alt="Gcore Control panel " width="80%">



| Find in the text                                                       | Replace with                                                                                                   |
|----------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
|   src="customavatars/                                                  | src="http://cdn.site.com/customavatars/                                                                        |
|   src="customprofilepics/                                              |   src="http://cdn.site.com/customprofilepics/                                                                  |
|   src="images/                                                         |   src="http://cdn.site.com/images/                                                                             |
|   url("clientscript                                                    |   url("cdn.site.com                                                                                            |
|   src="clientscript/                                                   |   src="http://cdn.site.com/                                                                                    |
|   src="{vb:raw vboptions.bburl}/clientscript/                          |   src="http://cdn.site.com/                                                                                    |
|   href="clientscript/                                                  |   href="http://cdn.site.com/                                                                                   |
|   url(./images/                                                        |   url(http://cdn.site.com/images/                                                                              |
|   url(images/                                                          |   url(http://cdn.site.com/images/                                                                              |
|   var IMGDIR_MISC="images/misc";var IMGDIR_BUTTON="images/buttons";  |   var IMGDIR_MISC="http://cdn.site.com/images/misc";var IMGDIR_BUTTON="http://cdn.site.com/images/buttons";  |

4\. If you have more directories for your images repeat the process for each of them.

5\. Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.
