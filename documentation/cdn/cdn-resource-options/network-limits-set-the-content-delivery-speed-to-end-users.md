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
---
  
  
  
  
  

The _Download Speed Limit_ option allows you to control the content delivery speed to end users.

Option setting
--------------

To configure the speed limit via the control panel:

1. Go to **CDN** and select the CDN resource you want to configure.

<img src="https://support.gcore.com/hc/article_attachments/12392392470929" alt="CDN_resource.png">

2. In the navigation panel, under the **Network limits** section, click **Download speed limit**.

<img src="https://support.gcore.com/hc/article_attachments/12420512653457" alt="Download_Speed_Limit_option.png">

This option has 2 modes: _Static_ and _Dynamic_.

<img src="https://support.gcore.com/hc/article_attachments/12392873863953" alt="DL_3_1.png" width="524" height="304">

Static
------

This mode sets a limit on all content that is transmitted through the CDN. When this mode is selected, you can define the _Connection Speed_ and _Limit After_ parameters.

### Connection Speed

This setting defines the maximum download speed per connection in Kilobytes per second (KB/s). This parameter only accepts values equal to or higher than 1 KB/s.

<img src="https://support.gcore.com/hc/article_attachments/12393083235729" alt="Connection_speed.png" width="524" height="304">

### Limit After

This setting defines the amount of data that can be downloaded without limit before the Connection Speed parameter takes effect. If set to 0, the download speed will be limited immediately from the first byte.

<img src="https://support.gcore.com/hc/article_attachments/12393083820561" alt="Limit_After.png" width="524" height="304">

Dynamic
-------

This mode sets different limits for different users or for different types of content. The speed is adjusted based on requests with the _speed_ and _buffer_ arguments.

<img src="https://support.gcore.com/hc/article_attachments/12393281637393" alt="Dynamic.png" width="524" height="179">

The _speed_ sets the maximum download speed, while the _buffer_ sets how much data will be transferred without the speed limit. The buffer argument is optional.

Typically, these arguments are passed as parameters in a query string. For example, the following URL would limit download speed to 50 KB/s after downloading 500 KB:

http://cdn.example.com/video.mp4?speed=50k&buffer=500k

Option features
---------------

*   For both modes, the limit is set per request, so if the client opens two connections at the same time, the total speed will be twice the specified limit.
*   [Ignore Query String](https://www.gcore.com/support/articles/115002223049/) option does not affect the Download Speed Limit option. They can be used together.