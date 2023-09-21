---
title: view-statistics-of-live-streams-videos-and-billing
displayName: Statistics
published: true
order: 30
toc:
   --1--Video and live streaming statistics: "video-and-live-streaming-statistics"
   --1--Billing statistics: "billing-statistics"
pageTitle: Broadcast, Video and Billing Statistics | Gcore
pageDescription: How the tab for viewing the statistics of the Streaming Platform is arranged.
---
# View statistics of live streams, videos, and billing  
  
## Video and live streaming statistics  

Statistics data is collected only when you use the standard player.  

The "Statistics" section shows information about <a href="https://streaming.gcore.com/video/list" target="_blank">videos</a> and <a href="https://streaming.gcore.com/streaming/list" target="_blank">live streams</a>: viewers, their browsers and operating systems, geography, popular videos (only for the "Video" section), as well as URLs of pages that host a player with your video. The statistic data is updated every five minutes and stored for one year. 

You can see statistics on all videos/live streams total or only on a single one. To see overall statistics: 

1\.  Go to the "Statistics" section and select the subsection: "Video" or "Live streaming". 
2\.  Select an interval (24 hours, 48 hours, week, or month) and dates.
3\.  Select a statistics parameter ("Viewers", "Browsers", "OS", or another).

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing/image_1307.png" alt="Statistics section">

**"Viewers"** is the number of viewers. We collect the following information about their behavior:  

- "Uploads" shows how many times users opened a video or live stream page,  
- "Starts" indicates how many times users clicked the "Play" button, 
- "Viewers" specifies how many viewers have watched a video or a live stream for at least 5 seconds,
- "Unique viewers" represents the number of unique viewers (we distinguish viewers using several parameters at once: an IP address, screen size, browser, and cookie). 

**"Popular videos"** (available only for videos) is a list of the most viewed videos. We consider only views that are longer than five seconds. 

**"Browsers"** shows statistics on browsers that your viewers use to watch your video/live stream.  

**"OS"** represents statistics on users' operating systems. 

**"Hosts"** contains static data on the URL of requested pages. We consider only views that are longer than five seconds. The ```"streaming.gcore.com"```. URL means a video was watched from a personal account.  

**"Geography"** is a world map that highlights countries where your viewers watch videos/live streams for at least 5 seconds. A user's IP address determines a country. 

If you want to see statistics on a specific video or live stream, navigate to it and open the "Statistics" tab.  
  
<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing/____________2_.gif" alt="Statistics tab" width="80%">

## Billing statistics  

The Billing section displays statistics on resource consumption. It determines how much you’ll pay for Streaming Platform services. Billing terms are described in <a href="https://accounts.gcore.com/billing/services" target="_blank">your plan</a>, which is located in the Streaming section.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing/10599562362129.png" alt="Statistics tab" width="50%">

You can sort statistics by several metrics:

| Metric            | Explanation                                                                                                                 | Paid or free                           |
|-------------------|-----------------------------------------------------------------------------------------------------------------------------|----------------------------------------|
| Transcoding       | The time used to process streams/videos and prepare an adaptive bitrate                                                     | Free                                   |
| VOD uploaded mins | The duration of the uploaded videos                                                                                         | Paid This metric is calculated for VoD |
| Computer vision   | The duration of videos and streams for which Computer Vision works (our service for recognizing objects from video content) | Paid                                   |
| Real-Time Video              | Call duration per person in Real-Time Video (our service for video calls, video conferences, and webinars in real-time)                | Paid                                   |


*All metrics are calculated in minutes.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/view-statistics-of-live-streams-videos-and-billing/10599503863057.png" alt="Billing statistics" width="80%">

VoD plans calculate the total duration of all videos uploaded to the Streaming Platform. Let’s say, for example, that one day, you upload 50 minutes of video. On the next, you upload 100 minutes of video and then delete the first video. You will be billed for 150 minutes of video.
