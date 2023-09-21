---
title: always-online-provide-the-stale-cache-if-the-origin-is-unavailable
displayName: Use stale cache if origin is unavailable
published: true
order: 50
toc:
pageTitle: Explanation of the Always Online CDN Feature | Gcore
pageDescription: A guide on providing the stale cache if the origin experience outages.
---
# Always online: provide the stale cache if the origin is unavailable

The option allows serving stale cached content in case of the following errors: error (network or connectivity issues), timeout, invalid_header, updating (cache updating),http_500, http_502, http_503, http_504, http_403, http_404, http_429.

HTTP response for the stale content will contain the header X-Cache: Stale. CDN will check origin availability with each user’s request. As soon as the origin becomes available, fresh files will be cached and served. If the origin is unavailable for a long time, CDN will send Stale content until origin becomes available. 

Please, note that when the site is unavailable, the CDN cache may have not enough content for a correct page display. Situations, when a user will not be able to see some images, style sheets, or other static content, are possible.

To manage this option go to your Resource Advanced Settings, find the Cache section, click **Add Option** and choose "Always Online". You can enable the option and choose error codes for which a CDN serves stale content. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/cache/always-online-provide-the-stale-cache-if-the-origin-is-unavailable/Screenshot-2018-1-3_G-Core_Labs_Resources_Settings.png" alt="Always Online" width="80%">