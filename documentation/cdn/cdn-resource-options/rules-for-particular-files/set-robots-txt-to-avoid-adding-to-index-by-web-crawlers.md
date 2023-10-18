---
title: set-robots-txt-to-avoid-adding-to-index-by-web-crawlers
displayName: Avoid indexing
published: true
order: 30
toc:
   --1--Problem with indexing: "what-is-the-problem-with-cdn-custom-domain-indexing"
   --1--Prohibit indexing: "how-to-prohibit-web-crawlers-from-indexing-your-cdn-custom-domain"
pageTitle: Avoid Indexing with a Directive in User-agent | Gcore
pageDescription: Guide on setting up User-agent to prevent web crawlers from indexing your CDN's custom domain, keeping your main website unaffected.
---
# Avoid indexing of your CDN resource by web crawlers

Search engines use web crawlers to index content from various websites, making it discoverable to users. However, when your CDN resources are indexed, it can lead to problems, so we’ll explain how to avoid it here.

## What is the problem with CDN custom domain indexing?

When you <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">create a CDN resource for static assets</a> for your original website, part of your content is available from the main (e.g., website-example.com/image.png) and <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CDN custom domains</a> (e.g., cdn.website-example.com/image.png.) This can lead to duplicated content in search results which negatively affects SEO, degrading your site’s position on search engines like Google. By using the <a href="https://gcore.com/docs/cdn/cdn-resource-options/specify-custom-http-status-code-for-the-content-delivered-by-the-cdn" target="_blank">Status code</a> option, you can forbid crawlers from indexing custom domains hence avoiding duplicate content.

## How to prohibit web crawlers from indexing your CDN custom domain

1\. Go to the <a href="" target="_blank">CDN resource</a> and click the custom domain of the CDN resource you want to prohibit from indexing.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/set-robots-txt-to-avoid-adding-to-index-by-web-crawlers/web-crawlers-10.png" alt="CDN resource" width="80%">

A new page will open, where you will perform the remaining steps.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/rules-for-particular-files/set-robots-txt-to-avoid-adding-to-index-by-web-crawlers/web-crawlers-20.png" alt="A new page ">

2\. Click **Content**, then **Status code**.

3\. Enable the **Status code** option.

4\. In the **URL or code text (optional)** field, enter the following directive:

```
User-agent: *\nDisallow: /\n
```

5\. Save changes.

That’s it. You have successfully prevented content requested from the custom CDN domain from being indexed. 

**Note**: This configuration doesn’t affect the website itself.



