---
title: specify-custom-http-status-code-for-the-content-delivered-by-the-cdn
displayName: Status code
published: true
order: 50
toc:
   --1--Set status code in Resource settings: "resource-settings"
   --1--Set status via Rules: "rules"
pageTitle: How to Set HTTP Status Codes for Content Hosted on the CDN | Gcore
pageDescription: Discover how to specify custom HTTP status codes for content delivered by a CDN, either for all content or for specific files.
---
# Configuring HTTP Status Codes for CDN-Hosted Content

The “Set status code” option enables you to establish custom HTTP status codes for content hosted on the Gcore CDN, which can be applied based on a schedule. 

For instance, in accordance with certain jurisdictions' laws, children under the age of 16 are not allowed to access specific content past 22:00. To comply with this regulation, the “Set status code” option can be configured to either send a 403 error code to users or redirect them to a different page when they attempt to access this restricted content. The schedule should be set such that this code is only activated after 22:00.

You can configure the option in two ways:

- Via **Resource settings**: the custom code will be applied to all the CDN resource's content
-Via **Rules**: the custom code will be applied only to certain files

Select the appropriate method and click the desired tab below to learn how to configure this option.

<tabset-element>

## Resource settings

1\. In the Gcore Customer Portal, navigate to <a href="https://portal.gcore.com/cdn/resources/list" target="_blank">CDN</a>.

2\. Click the CNAME of the required CDN resource to open **Resource settings**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn/set-custom-code-10.png" alt="Open settings of the special CDN resource" width="75%">

3\. Click the **Content** section to open nested options.

4\. Click **Status code**.

5\. Enable the **Set status code** toggle.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn/set-custom-code-20.png" alt="Enable the Set status code option" width="80%">

6\. Specify the desired HTTP status code in the field.

<alert-element type="caution" title="Caution">

You can’t specify 408, 444, 494, 495, 496, 497, or 499 codes. 

</alert-element>

7\. (Optional) Specify a URL for a redirect or an HTTP status code text.

8\. (Optional) Enable a schedule. In the expanded block, set the time when the custom status code will be applied, as well as the time zone.   

9\. Save changes. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn/set-custom-code-30.png" alt="Configure the Set status code option" width="80%">

That’s it! The custom code will be applied to all files delivered via the CDN.

## Rules

1\. In the Gcore Customer Portal, navigate to <a href="https://portal.gcore.com/cdn/resources/list" target="_blank">CDN</a>.

2\. Click the CNAME of the needed CDN resource to open **Resource settings**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn/set-custom-code-10.png" alt="Open settings of the special CDN resource" width="80%">

3\. Go to the **Rules** tab.

4\. Click **Create rule**.

5\. In the menu that opens, click **Create blank rule**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn/set-custom-code-50.png" alt="Open rules to set a custom code for specific files" width="80%">

On the page that opens, specify to which files the rule for custom code will be applied. Configure the other settings on the page. Our guide on <a href="https://gcore.com/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files#create-a-rule-manually" target="_blank">creating a rule manually</a> explains the configuration options in depth.

6\. At the end of the page, click **Add option**.  

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn/set-custom-code-60.png" alt="Add an option in the rule to set a custom code for specific files" width="75%">

7\. Click **Status code** in the list to add the option to the rule.

8\. Click **Close**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn/set-custom-code-70.png" alt="Apply the “Set custom code” option to the rule" width="75%">

9\. Enable the **Set status code** toggle.

10\. Specify the desired HTTP status code in the field.

<alert-element type="caution" title="Caution">

You can’t specify 408, 444, 494, 495, 496, 497, or 499 codes. 

</alert-element>

11\. (Optional) Specify a URL for a redirect or an HTTP status code text.

12\. (Optional) Enable a schedule. In the expanded block, set the time when the custom status code will be applied, as well as the time zone. 

13\. Save changes. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn/set-custom-code-80.png" alt="Configure the Set status code option in the rule" width="80%">

That’s it! The rule with the set custom code will be applied to specified files delivered via the CDN.

</tabset-element>
