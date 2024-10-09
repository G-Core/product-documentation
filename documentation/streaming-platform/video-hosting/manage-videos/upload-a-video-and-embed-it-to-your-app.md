---
title: upload-a-video-and-embed-it-to-your-app
displayName: All videos
published: true
order: 10
toc:
   --1--Step 1. Upload a video: "step-1-upload-a-video-to-the-customer-portal"
   --1--Step 2. Update video settings: "step-2-update-video-settings"
   --1--Step 3. Choose a player UI customization: "step-3-choose-a-player-ui-customization-and-video-projection"
   --1--Step 4. Export video: "step-4-export-video"
   --1--Step 5. Check video statistics: "step-5-check-video-sstatistics"
   --1--Step 6. Check player metrics: "step-6-check-player-metrics "              
pageTitle: Video Upload and Embedding Guide | Gcore
pageDescription: Step-by-step instructions on uploading, customizing, and embedding videos in your application for a seamless viewing experience and statistics tracking.
customUrl: /streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app
---
# Upload a video and embed it to your app

Upload videos to <a href="https://gcore.com/streaming-platform/video-hosting" target="_blank">Gcore Video Hosting</a> for secure storage and seamless broadcasting to your audiences. You can share videos in different formats and resolutions, optimizing content for various devices and network conditions.

## Step 1. Upload a video to the Customer Portal
  
Navigate to the <a href="https://streaming.gcore.com/video/list" target="_blank">Video Hosting</a> tab and upload a video using one of the following actions: 

* **Upload the video**. On this tab, you can add locally stored videos. Either click the **Click to upload** button or drag and drop your files to the designated upload area.

  <img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/upload-video-tab.png" alt="Video Hosting tab">

* **Download from the source**. Here you can upload a video from the origin by specifying the video title and video origin URL.

  <img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/download-from-source.png" alt="Video Hosting tab">

* **Import from Google Drive**. To add a video, click the **Click here** area, sign in to your Google account, and then choose the required video from your Google Drive. 

  <img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/import-from-google-drive.png" alt="Video Hosting tab">

Wait until your video is uploaded and processed. Waiting time varies depending on video size and internet speed.  
  
<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/video-uploading-process.png" alt="Wait until your video is uploaded">

## Step 2. Update video settings

If you need to adjust some video configuration, get links to export the video or set up subtitles and tags. You can do so on the **Main settings** tab: 

1\. Open video settings by clicking the video name or the three-dot icon next to it.
  
<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/video-settings.png" alt="settings of the uploaded video" width="80%">

2\. Update the following video settings if necessary:

- **Name**: Change its name (it will be displayed in the Gcore Customer Portal)
- **Description**: Enter a description (it will be displayed in the Gcore Customer Portal)
- **Player**: Select custom player, if you enabled the <a href="https://gcore.com/docs/streaming-platform/extra-features/customize-appearance-of-the-built-in-player" target="_blank">Players</a> feature
- **Tags**: Select <a href="https://gcore.com/docs/streaming-platform/video-hosting/organize-uploaded-videos#how-to-use-tags" target="_blank">tags</a> for a video
- **Subtitles**: Add <a href="https://gcore.com/docs/streaming-platform/video-hosting/subtitles-and-closed-captions-for-vod#control-panel">subtitles and choose a subtitle language</a>
- **Screensaver**: Select a screensaver from screenshots or upload a screensaver from your computer

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/video-main-settings-update.png" alt="Video settings" width="80%"> 

3\. Select one of the automatically created video posters or upload a new one from your local storage.

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/choose-video-poster.png" alt="Video poster settings" width="80%"> 

## Step 3. Choose a player UI customization and video projection

Customize the functionality and appearance of a <a href="https://gcore.com/docs/streaming-platform/extra-features/customize-appearance-of-the-built-in-player" target="_blank">built-in HTML web player</a> for the uploaded video. Note that these settings apply only to the built-in player and won’t affect viewers using external or OS-native players. 

In the **Player** dropdown, you can choose the existing configuration. To add a new built-in player and customize its settings, refer to our <a href="https://gcore.com/docs/streaming-platform/extra-features/customize-appearance-of-the-built-in-player" target="_blank">dedicated guide</a>. 

You can also apply **Video projection** settings. If you select the **180/360 projection** option, the player will project the video not like a regular “flat” video but <a href="https://en.wikipedia.org/wiki/360-degree_video" target="_blank">volumetric with superposition on a sphere</a>. 

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/player-projection.png" alt="Player customization & projection settings" width="80%"> 

## Step 4. Export video

In the **Links for export** section, choose the relevant export method: 

* **Video page URL**: A Web player URL to access and play the video directly from a website. 

* **HLS manifest URL**: A URL to a master playlist HLS (master.m3u8) with MPEGTS container. 

* **iFrame embed code**: A URL to our HTML video player with the video inside. It can be inserted into an iframe on your website and the video will automatically play on all browsers. 

In the Links for export section, you can also choose the video size and download the uploaded video in the required quality by selecting its bitrate and clicking **Download video**.    

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/export-links.png" alt="Export tab" width="80%">  

## Step 5. Check video statistics 

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

## Step 6. Check player metrics

On this tab, you view comprehensive information about the views in the built-in player. 

<alert-element type="tip" title="Tip">

All data displayed on the Player metrics tab reflects only the statistics collected by the built-in HTML player. If users viewed video in external or OS-native players, those views and interactions are not included in the metrics. 

</alert-element>

Player statistics are available in Coordinated Universal Time (UTC) or in your local time zone format.  

By default, the date is presented for the last 24 hours. However, you can adjust the displayed information based on the date and time filters. To keep the data up to date without refreshing the page manually, you can choose the preferred auto refresh interval in the dropdown. 

### Average view duration 

This graph shows how many minutes the audience watched the video in the built-in player.  This graph shows how many minutes the audience watched the video in the built-in player. 

Based on this data, you can see how many viewers started watching your video and where they stopped, without completing it.  

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/player-metrics-tab.png" alt="Player metrics showing average video views" width="80%">  

### Browsers 

In the **Browsers** section, you can view information about the browsers your viewers use to watch your video. 

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/browsers-section.png" alt="Player metrics showing user browser data" width="80%">  

### Geography 

The **Geography** section displays a world map highlighting the countries where viewers have watched your videos for at least 5 seconds. The viewer's country is determined by their IP address. 

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/geography-section.png" alt="Player metrics showing geography data" width="80%">  

### Hosts 

The **Hosts** section provides data on the URLs of requested pages. Only views lasting longer than five seconds are counted.  

The `streaming.gcore.com` URL means a video was watched from a personal Gcore account.   

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/hosts-section.png" alt="Player metrics showing hosts data" width="80%">  

### OS 

The OS section features statistics on users' operating systems. 

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/os-section.png" alt="Player metrics showing OS data" width="80%">  

### Amount of viewers 

In the Amount of viewers section, you can analyze the following information about user interaction with a video: 

* **Uploads**: The number of times users opened a video. 

* **Starts**: The number of times users clicked the Play button. 

* **Viewers**: The total number of viewers who have watched a video for at least 5 seconds. 

* **Unique viewers**: The number of unique viewers. It's determined by criteria such as IP address, screen size, browser, and cookies.  

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app/amount-viewers-section.png" alt="Player metrics showing amount viewers data" width="80%"> 
