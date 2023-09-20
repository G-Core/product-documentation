---
title: integrate-cdn-resource-with-joomla
displayName: Joomla
published: true
order: 120
toc:
   --1--Check the Joomla Version: "check-the-joomla-version"
   --1--Install the plugin: "install-the-plugin"
   --1--Set up the extension: "set-up-the-extension"
pageTitle: Integrate CDN with Joomla Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Joomla CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with Joomla

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

## Check the Joomla version

Open the administration panel, click on System, then System Information. You will see a window with the system details.

Your system should meet the following requirements:

- Joomla 3.4.1 or later
- PHP 5.3.13
- PHP mbstring (Multibyte String) - should be enabled
- MySQL 5 or later

## Install the plugin 

Download the extension CDN for Joomla! from NoNumber.nl. (you don't need to unpack the file). The extension is for versions after Joomla 3.4.1. If you use Joomla 2, download the CDN for Joomla 2 extension. Login to Joomla administration area.

Click the "Extensions" tab on the top navigation bar and go to the Extension Manager section. You will be automatically transferred to the Install section, if not - click **Install** at the top.

Find the "Upload Package File" section, click the **Choose File** button and find the CDN extension for Joomla, which you have downloaded.

Click the **Upload & Install** button to upload and install the extension on your website.

## Set up the extension 

Click the "Extensions" tab on the top navigation bar and go to Plugins.

Find the CDN plugin for Joomla! It will be displayed as System - CDN for Joomla!, click it to edit settings.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-joomla/joomla-1-edit.png" alt="Extensions" width="80%">

In the CDN section of the settings page type the CNAME that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>.

Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for.

Click **Save** to save settings.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/integrate-cdn-resource-with-joomla/joomla-1-edit.png" alt="save settings" width="80%">

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.