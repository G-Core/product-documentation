---
title: create-a-cdn-resource-rule-template-manually-or-use-a-system-one
displayName: Create a template for rules
published: true
order: 20
toc:
   --1--What is a template?: "what-is-a-template"
   --1--Create your own template: "create-a-template"
   --1--Use a system template: "use-a-system-template"
   --1--Create a rule from a template: "create-a-rule-from-a-template"
pageTitle: Understanding of Rule Templates | Gcore
pageDescription: A comprehensive guide on how to create a template for rules or use a system one.
---
# Create a CDN resource rule template manually or use a system one
  
## What is a template?

A template is a template rule for CDN resources. It contains all necessary settings: file paths, an origin pull protocol, enabled and disabled options. All you have to do is to add this rule with three clicks: open the resource rules, select a template, and click "Create rule".

We have prepared some templates for you in advance. They are called "system". You can also create your own templates.

## Create a template

1\. In the CDN resource settings, open the "Rules" tab, go to the "Templates" section and click **Create template**.  
  
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-cdn-resource-rule-template-manually-or-use-a-system-one/image_1506.png" alt="Create a template" width="80%">

As the "Create template" page opens, do the remaining steps in it.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-cdn-resource-rule-template-manually-or-use-a-system-one/image_1507.png" alt="Create a template" width="80%">

2\. Specify the template name. You can search a template by its name after creation.

3\. Specify the path to the file or folder for which the rule will be applied. The path must start with “^/” or “/". You can specify a URL or use <a href="https://en.wikipedia.org/wiki/Regular_expression" target="_blank">regular expressions (regex)</a>.

4\. Select the protocol that the CDN resource will use to pull the files specified at Step 3. If files are accessible over the same protocol as an origin, select "Inherit from resource". If not, select the appropriate option: HTTP, HTTPS or both protocols at once.

5\. View the list of additional options and configure the necessary ones. If you don't need those options, skip this step.

6\. Save the template.

## Use a system template

A system template is a template that we have developed for common cases of our customers. Such templates have the "System" label.  

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-cdn-resource-rule-template-manually-or-use-a-system-one/image_1510.png" alt="Use a system template">

**Video segments template (.ts)** is a rule template for caching chunks (<a href="https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs" target="_blank">streaming via CDN</a>).

**Playlists template (.m3u8)** is a rule template for caching playlists (<a href="https://gcore.com/docs/cdn/cdn-resource-options/configure-live-streams-and-video-delivery-via-cdn-only-for-paid-tariffs" target="_blank">streaming via CDN</a>).

**Let's Encrypt HTTP-01 challenge** is a rule template for validating a Let's Encrypt certificate that is issued with the <a href="https://letsencrypt.org/docs/challenge-types" target="_blank">HTTP—01 challenge</a> method and not via the Gcore UI. To ensure your certificate is validated, create a CDN resource, create a rule from the template and only then request a certificate. Without this rule, the resource settings will block certificate validation.

**Static content** is a rule template for caching static files of the resources integrated with the DNS.

**Image optimization** is a rule template for compressing PNG and JPG images using <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif" target="_blank">WebP Compression</a> (paid option; contact our technical support to activate it). Add a rule from the Image optimization template to your resource, and compression will start working. If you don’t want to compress all the files, only some of them, edit the file path when creating the rule.

## Create a rule from a template 

1\. Open the settings of the required CDN resource. In the "Rules" tab, click "Create rule" and select a template from the list. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-cdn-resource-rule-template-manually-or-use-a-system-one/image_1508.png" alt="Create a rule from a template " width="80%">

2\. You will see the form for creating a new rule with pre-filled settings from the template. Check if all the settings suit you; edit it, if necessary. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-cdn-resource-rule-template-manually-or-use-a-system-one/image_1509.png" alt="Create a rule from a template " width="80%">

3\. Click **Create rule**.