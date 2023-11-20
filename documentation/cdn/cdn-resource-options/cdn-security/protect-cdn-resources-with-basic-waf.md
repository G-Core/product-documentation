---
title: protect-cdn-resources-with-basic-waf
displayName: Basic WAF (Beta)
published: true
order: 10
toc:
   --1--Basic WAF: "what-is-basic-waf-beta"
   --1--Enable: "how-to-enable-basic-waf"
   --2--CDN resource: "cdn-resource"
   --2--Specific URLs: "specific-urls"
   --1--Basic WAF blocks some unwanted content: "what-to-do-if-basic-waf-blocks-some-content-that-should-not-be-blocked"
pageTitle: Protection from cyberthreads with Gcore Basic WAF | Gcore
pageDescription: A comprehensive guide on how to protect the entire CDN resource or specific urls.
---
# Protect CDN resources with Basic WAF

## What is Basic WAF (Beta)?

Basic WAF is the firewall that protects you against the most widespread cyberthreats. The feature is available in beta testing and is available for free. The volume of requests per resource that can be safeguarded by the firewall may be subject to limitations.

## How to enable Basic WAF

You can activate the firewall for the entire CDN resource or specific URLs. 

### CDN resource

To enable Basic WAF for an entire CDN resource:

1. Go to the **Security** section in the Resource settings.
2. Toggle on the **Enable Basic WAF** feature.
3. Save changes.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cdn-security/protect-cdn-resources-with-basic-waf/basic-waf-10.png" alt="Enabling Basic WAF for the entire CDN resource">

### Specific URLs

To apply Basic WAF to particular files, in the CDN resource settings (“Rules” tab), create a rule where you specify URLs or regular expressions and enable the Basic WAF feature for them. To do that, <a href="https://gcore.com/docs/cdn/cdn-resource-options/rules-for-particular-files/create-a-rule-manually-or-from-a-template-to-configure-settings-for-particular-files" target="_blank">consult our dedicated guide</a>. 

## What to do if Basic WAF blocks some content that should not be blocked?

If Basic WAF blocks content that you want to be allowed, you can set an exception with a rule rather than disabling the feature for the entire resource. To do so: 

1. In the CDN resource settings (“Rules” tab), create a rule with the URLs or regular expression of files blocked by Basic WAF.
2. Add the Basic WAF option to the rule by clicking **Add option** and turn it off.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cdn-security/protect-cdn-resources-with-basic-waf/basic-waf-20.png" alt="disable WAF for specific URLs via rules" width="70%">

If you need more flexible settings, use <a href="https://gcore.com/web-security" target="_blank">Web Application Security</a>. It’s a paid product that allows you to install WAF, protect it from hacking, install protection against bots and DDoS attacks, and define blacklist and whitelists. 