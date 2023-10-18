---
title: integrate-cdn-resource-with-wordpress-gcore-plugin
displayName: Gcore plugin
published: true
order: 10
toc:
   --1--Install the plugin: "install-the-plugin"
   --1--Working with the plugin: "working-with-the-plugin"
   --2--Integration with CDN: "integration-with-cdn"
   --2--File types: "file-types"
   --2--Folders: "folders"
   --2--Exceptions: "exceptions"
   --2--Plugin workflow: "plugin-workflow"
pageTitle: Integrate CDN with Gcore plugin for WordPress Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with the Gcore plugin for CMS WordPress to enhance your site's speed and user experience.
---
# Integrate CDN resource with WordPress (Gcore plugin)

## Install the plugin

Go to your WordPress admin panel, select Plugins - > Add new. In the plugin search box, type "Gcore CDN". Install the found plugin.

To activate the plugin, click on the Activate button or go to Plugins -> Installed.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-gcore-plugin/________________.png" alt="Install the plugin" width="50%">

You can also download the Gcore plugin via the <a href="https://wordpress.org/plugins/g-core-labs-cdn" target="_blank">link</a>.
After successful installation, you will see the Gcore plugin in the WordPress menu.

## Working with the plugin

### Integration with CDN

To integrate your site with the Gcore CDN, go to the plugin settings: find it in the menu and click on CDN Settings > General.

**Note**: All changes in plugin settings are automatically saved.

Activate the Enable CDN checkbox, fill in the Personal domain field, and click Save.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-gcore-plugin/___________________.png" alt="Integration with CDN" width="80%">

### File types

Specify the file extensions that you want to distribute via CDN.

There are available two configuration modes: basic and advanced.

1\. In basic mode, you can select file extensions offered on the page.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-gcore-plugin/________________________.png" alt="Specify the file extensions " width="80%">

2\. Use advanced mode if you need to add specific file extensions.

To do this, activate the Advanced settings:

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-gcore-plugin/_________________________________.png" alt="Advanced settings" width="80%">

Add the extensions one by one. They will be displayed in the "File types" section.

### Folders

Specify the paths to the folders you want to deliver over the CDN in the "Folders" section.

Two configuration modes are available: basic and advanced.

1\. In basic mode, you can select folders offered on the page.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-gcore-plugin/__________________.png" alt="Folders" width="80%">

2\. Use advanced mode if you need to add specific folders paths.

To do this, activate the advanced settings:

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-gcore-plugin/_____________________.png" alt="advanced settings" width="80%">

Add the paths one by one. The added folders will be displayed in the section.

**Note**: If you do not specify a folder, adding a personal domain indicated in the General section to the URL of files will depend on the file extension.

### Exceptions

Specify URLs of the files that should not be delivered over the CDN in the "Exceptions" section. Add the URLs one by one. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/integrate-cdn-with-cms/wordpress/integrate-cdn-resource-with-wordpress-gcore-plugin/_______________.png" alt="Exceptions" width="50%">

### Plugin workflow

If you want to deliver a file over the CDN, your domain name in the file URL will be replaced with the personal domain that you specified in the General section.

Request processing logic:

- Is the URL from which the content is requested in the Exceptions section?
    - If yes, the domain name substitution does not occur, the file is distributed as usual.
    - If not, or exceptions are not specified, then check the next point.
- Is the content in the folder listed under Folders?
    - If yes, the domain name substitution does not occur, the file is distributed as usual.
    - If not, or folders are not specified, then check the next point.
- Are extensions included in the list of extensions for which the URL changes?
    - If yes, the domain name substitution does not occur, the file is distributed as usual.
    - If yes, then a personal CDN domain is substituted.