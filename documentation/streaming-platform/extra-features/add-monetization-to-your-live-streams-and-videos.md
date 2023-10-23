---
title: add-monetization-to-your-live-streams-and-videos
displayName: Ads
published: true
order: 20
toc:
   --1--What is Ads?: "what-is-the-ads-feature"
   --1--Enable: "enable-the-ads-feature"
   --1--Configure: "configure-the-ads-feature"
pageTitle: Overview of the Ads Feature and Its Setup | Gcore
pageDescription: A step-by-step guide on how to add monetization to your video content. 
---
# Add monetization to your live streams and videos  
  
## What is the Ads feature?

Ads is a free feature for adding custom ads in any part of videos (VOD) and live streams that allows you to monetize content. We support different ad formats: Videos, banners, hyperlinks, and various advertising vendors such as Google, Criteo, Adfox, etc.

We use VAST (Video Ad Serving Template) integration, which contains all the information about the ad: Its physical location, format, URLs that will be invoked when different events occur, and more.

## Enable the Ads feature

To enable the feature, send us a request via [support@gcore.com](mailto:support@gcore.com) or the chat window in the bottom-right corner of our website. Please specify your ID in the request so we can identify your account. You can find it on the main page of your control panel.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/add-monetization-to-your-live-streams-and-videos/9770456996369.png" alt="Please specify your ID" width="80%">

The message template: *"Greetings! Please enable the Ads feature for the account with ID … (Your ID)"*.

We’ll notify you when the feature is enabled. After that, you can use it for your account.

## Configure the Ads feature

1\. Go to the Ads tab and click the **New template** button.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/add-monetization-to-your-live-streams-and-videos/9770456995857.png" alt="Ads tab" width="80%">

2\. Enter the template name (it’ll only be displayed on our control panel) and click **Create**.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/add-monetization-to-your-live-streams-and-videos/9770457085585.png" alt="the template name" width="50%">

The configuration page will open. Complete the remaining steps in it.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/add-monetization-to-your-live-streams-and-videos/9770485427089.png" alt="The configuration page" width="80%">

3\. You can set ads as default for videos (VOD) and live streams with a check box. If checked, ads will be automatically added to all VODs and live streams. If not, you can add them manually. To do this, open the video settings from the <a href="https://streaming.gcore.com/video/list" target="_blank">video list</a> or the multicamera settings (for live streams) from the <a href="https://streaming.gcore.com/multicamera/list" target="_blank">multicamera list</a>. Then, select the created template from the drop-down list and save the changes.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/add-monetization-to-your-live-streams-and-videos/9770457213457.png" alt="multicamera list." width="80%">

4\. Enable the ad modes you’re interested in. There are six modes available that determine when your ad will play:

- **Preroll**: The ad will be shown before the beginning of the video
- **Middleroll** (only for VODs): The ad will play in the middle of the video
- **Pauseroll**: The ad will appear when the video is paused
- **Postroll**: Ads will be shown after the video
- **Repeatableroll**: Ads will appear at the specified time in seconds after the beginning of the video
- **SCTE-35** are special timestamps at which ads will be played.

5\. Specify the URL of your ad and click **Add**. If you want to show several ads one by one, repeat this step.

For Repeatableroll mode, specify the time in seconds after the beginning of the video for the ad to play.

6\. Click **Save changes**.