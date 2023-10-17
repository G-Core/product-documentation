---
title: create-and-configure-a-restream-to-social-media
displayName: Restreaming (paid)
published: true
order: 30
toc:
   --1--About Restreams: "about-restreams"
   --1--Configure: "configure-a-restream"
pageTitle: Overview of the Restreaming Feature and Its Setup | Gcore
pageDescription: A step-by-step guide on how to push your broadcasts to social media.
---
# Create and configure a restream to social media
  
## About Restreams

**What is it?** Restreams is a paid feature that helps to broadcast your <a href="https://gcore.com/docs/streaming-platform/live-streaming/create-a-live-stream">live stream</a> or playlists to YouTube, Facebook, and other platforms simultaneously.

Example: you use our Streaming Platform for an educational site where you hold webinars. One day, you decide to expand your audience and start to broadcast on several more platforms (e.g., Facebook and YouTube). In this case, you must push a total of three live streams: the first one for your site through our Streaming platform, the second one for Facebook, and the third one for YouTube. This requires a powerful device for streaming because when you push three separate streams at the same time, it’s a high load on the processor. To optimize this process, we recommend using Restreams. In this case, you push only one stream into our Streaming Platform and then route it to the necessary platforms.

**How it works.** You get the credentials from the target platform (Facebook, YouTube, Twitch, etc.): stream URL and stream key. Then create a restream in our Control panel. When creating the restream, add credentials and choose the appropriate live stream. The setup is complete. You can begin the live stream; it will be broadcast on our player and the target platform.

**Features.** Restreams can be broadcast on an unlimited number of platforms. The price of the service depends on how many platforms you want to stream to. The fewer platforms there are, the cheaper it is. By default, when you enable the feature, you will be able to stream to one platform. To increase the number of platforms, contact technical support. We will change the limit and the price of the service.

## Configure a restream

1\. To enable the feature, send us a request via [support@gcore.com](mailto:support@gcore.com) or the chat window in the bottom-right corner of <a href="https://gcore.com" target="_blank">our website</a>. Please specify your ID in the request, so that we can identify your account. You can find it on the main page of your <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-and-configure-a-restream-to-social-media/Your_ID.png" alt="Configure a restream" width="80%">

The message template: *"Greetings! Please enable the Restreams feature for an account with ID … (your ID)"*.

By default, we enable one available restream per account. If you want to use more than one, specify the number of restreams in the message.

We will notify you when the feature is activated. After that, you will be able to use it for your account.

2\. Get credentials from the target platform for the restream. Our guides for popular platforms describe how to do it: <a href="https://en-gb.facebook.com/help/587160588142067?helpref=faq_content" target="_blank">Facebook</a>, <a href="https://support.google.com/youtube/answer/2907883?hl=en" target="_blank">YouTube</a> and <a href="https://help.twitch.tv/s/article/twitch-stream-key-faq" target="_blank">Twitch</a>.

For example, we want to broadcast our live stream on YouTube. To do so, we should go to <a href="https://youtube.com" target="_blank">YouTube</a> and click **Go live**. Then select a Streaming software solution. There we will need the credentials (stream URL and stream key). We will use them in step 6 of this guide.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-and-configure-a-restream-to-social-media/Stream_key.png" alt="Configure a restream">

3\. Go to the <a href="https://streaming.gcore.com/restreams/list" target="_blank">Restreams</a> section and click **Create a restream**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-and-configure-a-restream-to-social-media/Create_a_restream.png" alt="Restreams section" width="80%">

The configuration page opens. Complete the remaining steps in it.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-and-configure-a-restream-to-social-media/9665929864593.png" alt=" remaining steps" width="50%">

4\. Turn on the **Active** toggle if you want to broadcast your video content after configuration. If you don’t turn the toggle off, an inactive restream won’t be broadcasted.

5\. Give a name to your restream.

6\. Enter the credentials from step 2 of this guide as follows:

```
URL/KEY
```

For example, our stream URL is: *rtmp://a.rtmp.youtube.com/live2* and stream key is: *ab123-cde4-f56g-hi78-90j*. So, in the URL field, we should add the following:

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-and-configure-a-restream-to-social-media/rtmp.png" alt="stream URL ">

where:

- *rtmp://a.rtmp.youtube.com/live2* is the URL
- */* is the connecting symbol
- *ab123-cde4-f56g-hi78-90j* is the KEY

7\. Select which type of video content you want to restream. You can broadcast live streams and playlists.

**Note**: Playlists must be looped so that you can restream them.

8\. Pick a stream or playlist that you want to broadcast from the drop-down list.

9\. Save changes.

Then you should enable the live stream or playlist (depending on your choice), wait several minutes while the settings are applied, and restart the <a href="https://streaming.gcore.com/restreams/list" target="_blank">Restreams</a> page. If everything was set up correctly, you would see the **Live** label.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-and-configure-a-restream-to-social-media/Live.png" alt="Restreams page" width="80%">

You can do this if the live stream or playlist is over, but you want to restream it again in a while. If the key and URL were not changed, and the restream still exists in the Control panel, there are no additional settings. If the key or URL were changed, you should add current credentials in the configuration of restream.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-and-configure-a-restream-to-social-media/Settings.png" alt="Restreams page" width="80%">