---
title: create-and-configure-a-restream-to-social-media
displayName: Restreaming (paid)
published: true
order: 30
toc:
   --1--About Restreams: "about-restreams"
   --1--Configure: "configure-a-restream"
---
  

About Restreams
---------------

**What is it?** Restreams is a paid feature that helps to broadcast your [live stream](https://gcore.com/support/articles/5307972492945/) or playlists to YouTube, Facebook, and other platforms simultaneously.

Example: you use our Streaming for an educational site where you hold webinars. One day, you decide to expand your audience and start to broadcast on several more platforms (e.g., Facebook and YouTube). In this case, you must push a total of three live streams: the first one for your site through our Streaming platform, the second one for Facebook, and the third one for YouTube. This requires a powerful device for streaming because when you push three separate streams at the same time, it’s a high load on the processor. To optimize this process, we recommend using Restreams. In this case, you push only one stream into our Streaming platform and then route it to the necessary platforms.

**How it works.** You get the credentials from the target platform (Facebook, YouTube, Twitch, etc.): stream URL and stream key. Then create a restream in our control panel. When creating the restream, add credentials and choose the appropriate live stream. The setup is complete. You can begin the live stream; it will be broadcast on our player and the target platform.

**Features.** Restreams can be broadcast on an unlimited number of platforms. The price of the service depends on how many platforms you want to stream to. The fewer platforms there are, the cheaper it is. By default, when you enable the feature, you will be able to stream to one platform. To increase the number of platforms, contact technical support. We will change the limit and the price of the service.

Configure a restream
--------------------

1\. To enable the feature, send us a request via [support@gcore.com](mailto:support@gcore.com) or the chat window in the bottom-right corner of [our website](https://gcore.com/). Please specify your ID in the request, so that we can identify your account. You can find it on the main page of your [control panel](https://accounts.gcore.com/reports/dashboard).

<img src="https://support.gcore.com/hc/article_attachments/9394655645585/Your_ID.png" alt="Your ID.png">

The message template: _“Greetings! Please enable the Restreams feature for an account with ID … (your ID)”_.

By default, we enable one available restream per account. If you want to use more than one, specify the number of restreams in the message.

We will notify you when the feature is activated. After that, you will be able to use it for your account.

2\. Get credentials from the target platform for the restream. Our guides for popular platforms describe how to do it: [Facebook](https://en-gb.facebook.com/help/587160588142067?helpref=faq_content), [YouTube,](https://support.google.com/youtube/answer/2907883?hl=en) and [Twitch](https://help.twitch.tv/s/article/twitch-stream-key-faq).

For example, we want to broadcast our live stream on YouTube. To do so, we should go to [YouTube](https://www.youtube.com/) and click **Go live**. Then select a Streaming software solution. There we will need the credentials (stream URL and stream key). We will use them in step 6 of this guide.

<img src="https://support.gcore.com/hc/article_attachments/9394658339857/Stream_key.png" alt="Stream key.png">

3\. Go to the [Restreams](https://streaming.gcore.com/restreams/list) section and click **Create a restream**.

<img src="https://support.gcore.com/hc/article_attachments/9394645040785/Create_a_restream.png" alt="Create a restream.png">

The configuration page opens. Complete the remaining steps in it.

<img src="https://support.gcore.com/hc/article_attachments/9665929864593" alt="Create_a_restream.png">

4\. Turn on the **Active** toggle if you want to broadcast your video content after configuration. If you don’t turn the toggle off, an inactive restream won’t be broadcasted.

5\. Give a name to your restream.

6\. Enter the credentials from step 2 of this guide as follows:

URL/KEY

For example, our stream URL is: _rtmp://a.rtmp.youtube.com/live2_ and stream key is: _ab123-cde4-f56g-hi78-90j_. So, in the URL field, we should add the following:

<img src="https://support.gcore.com/hc/article_attachments/9394682501137/rtmp.png" alt="rtmp.png">

where:

*   _rtmp://a.rtmp.youtube.com/live2_ is the URL
*   _/_ is the connecting symbol
*   _ab123-cde4-f56g-hi78-90j_ is the KEY

7\. Select which type of video content you want to restream. You can broadcast live streams and playlists.

**Note:** Playlists must be looped so that you can restream them.

8\. Pick a stream or playlist that you want to broadcast from the drop-down list.

9\. Save changes.

Then you should enable the live stream or playlist (depending on your choice), wait several minutes while the settings are applied, and restart the [Restreams](https://streaming.gcore.com/restreams/list) page. If everything was set up correctly, you would see the **Live** label.

<img src="https://support.gcore.com/hc/article_attachments/9394773658257/Live.png" alt="Live.png">

You can do this if the live stream or playlist is over, but you want to restream it again in a while. If the key and URL were not changed, and the restream still exists in the control panel, there are no additional settings. If the key or URL were changed, you should add current credentials in the configuration of restream.

<img src="https://support.gcore.com/hc/article_attachments/9394744437777/Settings.png" alt="Settings.png">