---
title: view-your-live-stream-metrics
displayName: Monitoring
published: true
order: 70
toc:
   --1--About Live Stream Monitoring: "about-live-stream-monitoring"
   --1--Open the monitoring page: "open-the-monitoring-page"
   --1--Use the monitoring page: "use-the-monitoring-page"
   --1--Use stream metrics to troubleshoot: "use-stream-metrics-to-troubleshoot"
pageTitle: Live Stream Monitoring | Gcore 
pageDescription: A guide on how to view your live stream metrics.
---
# View your live stream metrics
  
## About Live Stream Monitoring

You can monitor how a particular stream performs using _Live Stream Monitoring_. This tool provides metrics that can help you observe the performance of a stream and detect and resolve issues as they happen or retrospectively (i.e., once the stream has ended). These data are stored for a year for recordkeeping purposes.

Live Stream Monitoring allows you to monitor the following metrics:

- **Video bitrate.** This displays the bitrate of the source stream (in Kbps).
- **FPS.** This displays the frame rate of the source stream (in fps).
- **Interval between key frames.** This displays the key frame interval of the source stream.

## Open the monitoring page

To view the Live Stream Monitoring page:

1\. Go to **Streaming** on the Control Panel dashboard.
2\. Click **Streaming**, then open **Live streams**.
3\. Click the three dots next to the stream whose metrics you want to view (it can be a finished or ongoing stream).
4\. Select **Monitoring**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/view-your-live-stream-metrics/10318231817105.png" alt="Streaming ">

## Use the monitoring page

The Live Stream Monitoring page consists of the following elements:

1. **Metrics.** This allows you to select the metric to monitor. It defaults to Video bitrate.
2. **Date.** This allows you to select the date for which you want to monitor the metric. It defaults to the current date.
3. **Time.** This allows you to select the 1-hour time range for which you want to monitor the metric. It defaults to the current hour.
4. **Time series graph.** This displays the data for the selected metric, date, and time range at a 1-minute step.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/view-your-live-stream-metrics/10318226324753.png" alt="Live Stream Monitoring page" width="80%">

You can hover the cursor over any data point on the chart to see the value of the selected metric (Kbps, fps, or key frame interval) in the tooltip. In this example, we have a point that shows the value of the key frame interval.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/view-your-live-stream-metrics/10318231896465.png" alt="chart " width="80%">

## Use stream metrics to troubleshoot

Live Stream Monitoring can be useful in debugging issues that originate at the source stream. For example, you see an unstable bitrate, too many key frames, or gaps in the graph. This indicates that there might be some missing or dropped frames with the source. You can then check your source and start working on the problem.