---
title: configure-and-check-the-host-header
displayName: Manage the Host header
published: true
order: 40
toc:
   --1--What is the Host header?: "what-is-the-host-header"
   --1--Manage: "how-to-manage-the-host-header"
   --1--Disable: "how-to-disable-the-change-host-header-option"
   --1--Check: "how-to-check-the-host-header"
pageTitle: Understanding Host Header | Gcore
pageDescription: A guide on configuring and checking the Host header.
---
# Configure and check the Host header
  
## What is the Host header?

The Host header is the mandatory header of HTTP requests. CDN servers send it to the origin when they request content. The Host header helps determine which website or web application, out of all those stored on the server, contains the requested content.

The Change Host header option controls the Host header. It is automatically enabled and populated when you <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">create a CDN resource</a> and specify the origin’s domain name/IP address or select a group of origins. In the latter case, the domain name or IP address of the first resource in the group will be used as the Host header.

For example, let’s create a CDN resource and specify _yourdomain.com_ in the Origin section as follows:

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header/11698761812241.png" alt="What is the Host header" width="80%">

This value will appear at the "Change Host header" option as follows:

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header/11698730009873.png" alt="Change Host heade" width="50%">

## How to manage the Host header

If you change the origin source after resource creation, the Host header value will not be changed automatically. You will need to manually change it. If the value is not corrected, the CDN resource will refer to the new source using the old Host header, resulting in an error for end users instead of content.

1\. Open the Resource settings in the control panel.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header/11774871054737.png" alt="Resource settings in the control panel" width="80%">

2\. Go to the HTTP headers section and select the Host header option.

3\. Configure the option. There are two ways to set it up:

- Custom Host header option: Select this if you use only one origin source, and specify the domain or IP address.
- Forward Host header: select this if it is important to send the same Host header in the request to the origin as was sent in the request to the CDN server.

4\. Save your changes.

Don’t forget to <a href="https://gcore.com/docs/cdn/clear-cdn-resource-cache-by-url-pattern-or-all" target="_blank">clear the CDN cache</a> afterwards.

## How to disable the Change Host header option

In most cases, end users will get 4xx or 5xx errors if the Change Host header option is disabled. To avoid this, you should enable the option and set the appropriate value.

If you are <a href="https://gcore.com/docs/streaming-platform/how-the-streaming-platform-interact-with-the-cdn" target="_blank">using a default CDN resource (*.gvideo.io) for streaming</a>, the Host header will take the value of the CNAME of the CDN resource. This is the value that the option will take as soon as it is disabled.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/http-headers/configure-and-check-the-host-header/11774870575761.png" alt="How to disable the Change Host header option" width="80%">

## How to check the Host header

To check if the Host header used is correct, run the following command in the terminal (Windows) or console (macOS):

<code-block>
curl -H "Host: <span style="color:#FF5913">example.com</span>" -I <span style="color:#FF5913">http(s)://10.0.0.1/file.txt</span>
</code-block>

Where:

- <span style="color:#FF5913">example.com</span> is the value of the Host header;
- <span style="color:#FF5913">http(s)</span> is the protocol value, which depends on the protocol used by the source;
- <span style="color:#FF5913">10.0.0.1</span> is the IP address of your website source; and
- <span style="color:#FF5913">file.txt</span> is any static file that is delivered via CDN.

If you receive a 400 Bad Request or 403 Forbidden Response error in the response, your server is unable to process the specified Host header. In this case, follow the instructions above to manage the option.