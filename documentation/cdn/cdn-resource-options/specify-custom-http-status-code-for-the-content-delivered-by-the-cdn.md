---
title: specify-custom-http-status-code-for-the-content-delivered-by-the-cdn
displayName: Custom HTTP status code
published: true
order: 50
toc:
pageTitle: Apply Custom HTTP Codes to CDN Content | Gcore
pageDescription: Discover how to specify custom HTTP status codes for content delivered by a CDN, either for all content or specific files.
---
# Specify custom HTTP status code for the content delivered by the CDN

With this feature, you can apply custom HTTP code to the CDN content. For example, you can send to the end users 403 code instead of certain files. Or set up redirection to another URL. The feature is available in the CDN resource settings and in the "Rules" section.

Activate the Status code option in the Content section of resource or rule settings.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn/_______________.jpg" alt="Content section " width="50%">

Specify any HTTP code except  408, 444, 494, 495, 496, 497, 499 codes in the "Status Code" field. You can add only one HTTP code to the field. Specify a URL for a redirect or an HTTP status code text, If you need.

**Note**: If you activate Status Code in the resource settings, it applies to all CDN content.

If you need to apply HTTP code only to certain files, use this option in the <a href="https://gcore.com/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files" target="_blank">Rules</a> section.