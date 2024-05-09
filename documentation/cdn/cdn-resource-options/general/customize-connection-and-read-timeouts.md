---
title: customize-connection-and-read-timeouts
displayName: Connection and read timeouts
published: true
order: 70
toc:   
pageTitle: Customize connection and read timeouts for your origin | Gcore 
pageDescription: Enable connection and read timeouts to set the allowable wait time for accessing your origin.
---
# Customize connection and read timeouts

Custom connection and read timeouts are analogous features that let you specify how long Gcore edge nodes should wait when connecting to your origin server.

- A custom connection timeout sets the duration allowed for establishing a connection.

- A custom read timeout specifies the time allowed for receiving a response from your origin server. This timeout applies only between two successive read operations, not for the entire response transmission.

When designated timeouts are exceeded, users receive a “504 Gateway Timeout” error. 

## Configure custom timeouts

1\. In the Gcore Customer Portal, navigate to <a href="https://portal.gcore.com/cdn/resources/list" target="_blank">CDN</a>.

<img src="https://assets.gcore.pro/docs/cdn/getting-started/timeouts/cdn-resources.png" alt="CDN page with a list of CDN resources" width="80%">

2\. Click the CNAME of the required CDN resource to open **Resource settings**.

A new page will open. Perform the remaining steps there.

3\. Click **General** to open nested features.

4\. Click **Custom connection timeout** or **Custom read timeout**, depending on your task. 

5\. Enable the **Customize connection timeout** or **Customize read timeout** toggle correspondingly. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/timeouts/resource-settings.png" alt="Resource settings with custom timeouts section open" width="80%">  

6\. Specify the desired value in the corresponding field. You can configure either feature individually or both at once. Values should be less than default Gcore values: <5 seconds for connection timeout and <30 seconds for read timeout. Learn more in our <a href="https://gcore.com/docs/cdn/getting-started/cdn-timeouts" target="_blank">guide to CDN timeouts</a>.

7\. Save changes. 

<img src="https://assets.gcore.pro/docs/cdn/getting-started/timeouts/enable-connection-read-timeouts.png" alt="A dialog with enabled custom read and connection timeouts" width="80%">  
