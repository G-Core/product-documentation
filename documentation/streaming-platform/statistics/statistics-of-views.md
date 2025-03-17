---
title: statistics-of-views
displayName: Statistics of Views
published: true
order: 20
pageTitle: Video views and delivered minutes | Gcore
pageDescription: Learn how to check the views of your videos and monitor the delivery minutes through Gcore CDN.
---

# Video views and delivered minutes

Gcoed Video Hosting provides you with statistics on the views of your videos and the delivery minutes through Gcore CDN. This information helps you monitor the popularity of your content and the efficiency of your video delivery.

## Check video statistics

To check the views of your videos, follow these steps:

1. Open the **Video Hosting** tab in the **Gcore Customer Portal**.
2. Click the video name or the three-dot icon next to it to open the video settings.
3. Select the **Statistics** tab.

## Explanation of video statistics

This tab displays data on unique views gathered through Gcore CDN. Each viewer is counted only once, regardless of how many times they connect or disconnect or which player they use. For more information on how the data is collected and counted, check our <a href="https://api.gcore.com/docs/streaming#tag/Statistics" target="_blank">API documentation</a>. 

The displayed statistics correspond to the period set by the table filters. 

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/video-statistics-tab.png" alt="General statistics tab" width="80%">  

After you upload the video, you can check its: 

* **Unique views**:  The number of individual viewers who have watched the video. 

* **Delivery minutes**: The amount of traffic and the duration (in minutes) of video downloaded through Gcore CDN. 

<alert-element type="info" title="Info">
 
Certain video players may download the entire video to the buffer, even if users don't watch it completely. This can lead to unnecessary consumption of your traffic and inflated view count without actual user engagement. 

To prevent this, adjust your player settings to optimize downloading to the buffer. For example, the <a href="https://gcore.com/docs/streaming-platform/extra-features/customize-appearance-of-the-built-in-player" target="_blank">Gcore built-in player</a> downloads only the first few video fragments. 
 
</alert-element>
