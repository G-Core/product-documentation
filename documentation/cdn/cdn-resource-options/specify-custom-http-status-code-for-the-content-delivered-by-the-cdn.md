---
title: specify-custom-http-status-code-for-the-content-delivered-by-the-cdn
displayName: Custom HTTP status code
published: true
order: 50
toc:
---
With this feature, you can apply custom HTTP code to the CDN content.

For example, you can send to the end users 403 code instead of certain files. Or set up redirection to another URL.

The feature is available in the CDN resource settings and in the Rules section.

Activate the Status code option in the Content section of resource or rule settings.

<img src="https://support.gcore.com/hc/article_attachments/4407362720017/_______________.jpg" alt="_______________.jpg">

Specify any HTTP code except  408, 444, 494, 495, 496, 497, 499 codes in the Status Code field.

You can add only one HTTP code to the field. 

Specify a URL for a redirect or an HTTP status code text, If you need.

**Important!** If you activate Status Code in the resource settings, it applies to all CDN content.

If you need to apply HTTP code only to certain files, use this option in the [Rules](https://www.gcore.com/support/articles/115005383865/) section.