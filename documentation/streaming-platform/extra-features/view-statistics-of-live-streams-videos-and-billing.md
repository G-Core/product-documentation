---
title: view-statistics-of-live-streams-videos-and-billing
displayName: Reports
published: true
order: 30
toc:
   --1--Video and live streaming statistics: "video-and-live-streaming-statistics"
   --1--Billing statistics: "billing-statistics"
pageTitle: Broadcast, Video and Billing Statistics | Gcore
pageDescription: How the tab for viewing the statistics of the Video Streaming is arranged.
---
# View statistics of live streams, videos, and billing  
  
## Video and live streaming statistics  

Statistics data is collected only when you use the standard player.  

The **Reports** page shows information about <a href="https://streaming.gcore.com/video/list" target="_blank">videos</a> and <a href="https://streaming.gcore.com/streaming/list" target="_blank">live streams</a>: viewers, their browsers and operating systems, geography, popular videos (only for the **Video** page), as well as URLs of pages that host a player with your video. The data is updated every five minutes and stored for one year. 

You can check reports for all videos and live streams or only for a single one. To see overall statistics: 

1\. In the Gcore Customer Portal, navigate to **Streaming** > **Reports**. 

2\. Choose the relevant subsection: **Built-in player: VOD** or **Built-in player: Live**. 

2\. Select the preferred interval (24 hours, 48 hours, week, or month) and dates.

3\. Choose one or more parameters: **Browsers**, **Geography**, **Hosts**, **OS**, or **Viewers**.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing/reports.png" alt="Reports page" width="80%">

### Parameters overview

* **Viewers**: The number of viewers. We collect the following information about their behavior:  
   * **Uploads**: Shows how many times users opened a video or live stream page.
   * **Starts**: Indicates how many times users clicked the **Play** button.
   * **Viewers**: Specifies how many viewers have watched a video or a live stream for at least 5 seconds.
   * **Unique viewers**: Represents the number of unique viewers (we distinguish viewers using several parameters at once: an IP address, screen size, browser, and cookie). 

* **Popular videos** (available only for videos): A list of the most viewed videos. We consider only views that are longer than five seconds. 
* **Browsers**: Statistics on browsers that your viewers use to watch your video/live stream.
* **OS**: Statistics on users' operating systems. 
* **Hosts**: Static data on the URL of requested pages. We consider only views that are longer than five seconds. The ```"streaming.gcore.com"```. URL means a video was watched from a personal account.  
* **Geography**: A world map that highlights countries where your viewers watch videos/live streams for at least 5 seconds. A user's IP address determines a country. 

If you want to see reports for a specific video or live stream, open its settings and navigate to the **Statistics** tab. 

## Billing statistics  

The **Billing** page displays statistics on resource consumption. It determines how much you’ll pay for Video Streaming services. Billing terms are described in <a href="https://accounts.gcore.com/billing/services" target="_blank">your plan</a>, which is located in the Streaming section.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing/10599562362129.png" alt="Statistics tab" width="50%">

You can sort statistics by several metrics:

| Metric            | Explanation                                                                                                                 | Paid or free                           |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Transcoding       | The time used to process streams/videos and prepare an adaptive bitrate                                                     | Free                                   |
| VOD uploaded mins | The duration of the uploaded videos                                                                                         | Paid This metric is calculated for VoD |
| Computer vision   | The duration of videos and streams for which Computer Vision works (our service for recognizing objects from video content) | Paid                                   |
| Real-Time Video              | Call duration per person in Real-Time Video (our service for video calls, video conferences, and webinars in real-time)                | Paid                                   |


*All metrics are calculated in minutes.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing/billing.png" alt="Billing statistics" width="80%">

VoD plans calculate the total duration of all videos uploaded to the Video Streaming. Let’s say, for example, that one day, you upload 50 minutes of video. On the next, you upload 100 minutes of video and then delete the first video. You will be billed for 150 minutes of video.
