---
title: how-we-optimize-live-stream-and-video-performance-by-creating-different-bitrates
displayName: Adaptive Streaming
published: true
order: 30
toc:
   --1--How adaptive streaming works: "how-adaptive-streaming-works"
pageTitle: Exploring Adaptive Streaming Optimization | Gcore
pageDescription: An overview of how adaptive streaming works in optimizing live stream and video performance, adjusting video quality based on user-specific parameters.
---
# How we optimize live stream and video performance by creating different bitrates

Adaptive streaming is a default feature that helps to optimize the stream performance in the end-user's browser.  

To get the full benefits of the feature, send us the highest quality stream or video so we would be able to split it into several ones with different bitrates. 

## How adaptive streaming works 

1\. We create a manifest with embedded streams with different resolutions and bitrates.  

2\. A player in the end-user's browser constantly analyzes available bandwidth, player window size, display resolution, and processor performance.  

3\. Based on the parameters, our player adjusts the quality of the stream. For example, If the end-users have a slow connection, they will receive a stream with a low bitrate.