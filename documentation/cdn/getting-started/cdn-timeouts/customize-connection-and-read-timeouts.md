---
title: customize-connection-and-read-timeouts
displayName: Connection and read timeouts
published: true
order: 40
toc:   
pageTitle: Customize connection and read timeouts for your origin | Gcore 
pageDescription: Enable connection and read timeouts to set the allowable wait time for accessing your origin.
---
# Customize connection and read timeouts

Custom connection and read timeouts are analogous features that let you set the allowable wait time when Gcore edge nodes access your origin:

- Custom connection timeout determines the time for establishing a connection.

- Custom read timeout defines the time for getting a response from your origin server. This timeout is set only between two successive read operations, not for the transmission of the whole response. 

When designated timeouts are exceeded, users receive a “504 Gateway Timeout” error. 

## Configure custom timeouts

1\. In the Gcore Customer Portal, navigate to <a href="https://portal.gcore.com/cdn/resources/list" target="_blank">CDN</a>.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/timeouts/cdn-resources.png" alt="CDN page with a list of CDN resources" width="80%">

2\. Click the CNAME of the required CDN resource to open **Resource settings**.

The new page opens. Perform the remaining steps there.

3\. Click the **General** section to open nested features.

4\. Click **Custom connection timeout** or **Custom read timeout**, depending on your tasks. 

5\. Enable the **Customize connection timeout** or **Customnise read timeou**t toggle correspondingly. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/timeouts/resource-settings.png" alt="Resource settings with custom timeouts section open" width="80%">  

6\. Specify the desired value in the corresponding field. You can set any feature or both at the same time. Values should be less than default Gcore values: under 5 seconds for connection timeout and 30 seconds for read timeout. You can read about other timeouts in the guide <a href="https://gcore.com/docs/cdn/getting-started/cdn-timeouts" target="_blank">CDN timeouts</a>.

7\. Save changes. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/timeouts/enable-connection-read-timeouts.png" alt="A dialog with enabled custom read and connection timeouts" width="80%">  
