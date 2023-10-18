---
title: network-limits-set-the-content-delivery-speed-to-end-users
displayName: Network limits
published: true
order: 100
toc:
   --1--Option setting: "option-setting"
   --1--Static configuration: "static"
   --2--Connection Speed: "connection-speed"
   --2--Limit After: "limit-after"
   --1--Dynamic configuration: "dynamic"
   --1--Option features: "option-features"
pageTitle: Managing CDN Content Delivery Speed | Gcore
pageDescription: Instructions on how to set the content delivery speed to end users using Download Speed Limit option in CDN.
---
# Network limits: set the content delivery speed to end users
  
## Option setting

The "Download Speed Limit" option allows you to control the content delivery speed to end users.

To configure the speed limit via the Control panel:

1\. Go to CDN and select the CDN resource you want to configure.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/network-limits-set-the-content-delivery-speed-to-end-users/12392392470929.png" alt="CDN_resource.png">

2\. In the navigation panel, under the "Network limits" section, click **Download speed limit**.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/network-limits-set-the-content-delivery-speed-to-end-users/12420512653457.png" alt="Download_Speed_Limit_option.png" width="80%">

This option has 2 modes: *Static* and *Dynamic*.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/network-limits-set-the-content-delivery-speed-to-end-users/12392873863953.png" alt="Static and Dynamic" width="50%">

## Static

This mode sets a limit on all content that is transmitted through the CDN. When this mode is selected, you can define the "Connection Speed" and "Limit After" parameters.

### Connection Speed

This setting defines the maximum download speed per connection in Kilobytes per second (KB/s). This parameter only accepts values equal to or higher than 1 KB/s.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/network-limits-set-the-content-delivery-speed-to-end-users/12393083235729.png" alt="Connection_speed.png" width="50%">

### Limit After

This setting defines the amount of data that can be downloaded without limit before the Connection Speed parameter takes effect. If set to 0, the download speed will be limited immediately from the first byte.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/network-limits-set-the-content-delivery-speed-to-end-users/12393083820561.png" alt="Limit_After.png" width="50%">

## Dynamic

This mode sets different limits for different users or for different types of content. The speed is adjusted based on requests with the "speed" and "buffer" arguments.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/network-limits-set-the-content-delivery-speed-to-end-users/12393281637393.png" alt="Dynamic.png" width="50%">

The *speed* sets the maximum download speed, while the *buffer* sets how much data will be transferred without the speed limit. The buffer argument is optional.

Typically, these arguments are passed as parameters in a query string. For example, the following URL would limit download speed to 50 KB/s after downloading 500 KB:

```
http://cdn.example.com/video.mp4?speed=50k&buffer=500k
```

## Option features

- For both modes, the limit is set per request, so if the client opens two connections at the same time, the total speed will be twice the specified limit.
- <a href="https://gcore.com/docs/cdn/cdn-resource-options/cache/ignore-the-set-cookie-or-query-string-parameters-when-caching-content-on-cdn-servers#query-string-setting" target="_blank">Ignore Query String</a> option does not affect the Download Speed Limit option. They can be used together.