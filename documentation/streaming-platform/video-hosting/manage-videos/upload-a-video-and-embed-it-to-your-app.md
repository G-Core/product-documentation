---
title: upload-a-video-and-embed-it-to-your-app
displayName: Upload videos
published: true
order: 10
toc:
   --1--Step 1. Upload a video: "step-1-upload-a-video-to-the-customer-portal"
   --1--Step 2. Update video settings: "step-2-update-video-settings"
   --1--Step 3. Choose a player UI customization: "step-3-choose-a-player-ui-customization-and-video-projection"
   --1--Step 4. Export video: "step-4-export-video"
pageTitle: Video Upload and Embedding Guide | Gcore
pageDescription: Step-by-step instructions on uploading, customizing, and embedding videos in your application for a seamless viewing experience and statistics tracking.
customUrl: /streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app
---
# Upload a video and embed it into your app

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

3\. (Optional) After you upload the video, it’ll be transсoded with different qualities and bitrates. Click the **Video transcoding data** link under the video to check the transcoding details.

4\. Select one of the automatically created video posters or upload a new one from your local storage.

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
