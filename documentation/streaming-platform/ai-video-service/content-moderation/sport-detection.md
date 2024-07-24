---
title: sport-detection
displayName: Sport detection
published: true
order: 50
pageTitle: Sport detection in videos | Gcore
pageDescription: Learn how to use Gcore's AI tasks to detect sport activities in videos hosted on the Gcore's platform or externally.
---
# Sport detection

The sport detection content moderation task identifies various sporting activities in a video. This can include detecting specific types, actions, events, and moments. 

The check returns information about the object identified, video frame number where it was found, and probability of the detected object. Objects with a probability of at least 30% are included in the response.  

For a full list of activities that can be detected with the sport detection check, read our <a href="https://api.gcore.com/docs/streaming?_gl=1*1rw278g*_gcl_au*MTM0OTcwMzMxMC4xNzE3MTQ0ODk3*_ga*OTkwMzM5NjM4LjE3MDkxMDg3OTU.*_ga_Y79HRL8RPR*MTcyMTI4NzExMi4xMjIuMS4xNzIxMjg3MjMzLjYwLjAuMA..#tag/AI/operation/post_ai_contentmoderation_sport" target="_blank">API documentation</a>. 

<alert-element type="tip" title="Tip">
 
For proper analysis, make sure your video is at least 10-15 seconds long.
 
</alert-element>

To run the sport detection check: 

1\. In the Gcore Customer Portal, navigate to **Streaming** > **AI**. The **AI tasks** page will open.

<img src="https://assets.gcore.pro/docs/streaming-platform/ai-video-services/content-moderation/ai-tasks-page.png" alt="AI tasks page" width="80%">

2\. In the **Origin URL** field, enter the link to your MP4 video. You have two options: 

* **Paste video origin URL**: If your video is stored externally, provide a URL to its location. Ensure that the video is accessible via HTTP or HTTPS protocols.  

   To check the example of correctly formatted URL, use the link under the field. It will autogenerate a sample URL and you can adjust your URL accordingly. 

   <img src="https://assets.gcore.pro/docs/streaming-platform/ai-video-services/content-moderation/example-url-link.png" alt="Example of the origin URL" width="80%">

* **Select from uploaded videos**: choose a video hosted on the Gcore platform. 

3\. In the **Task type**, choose **Content moderation**. 

4\. In the following dropdown, select **Sport detection**. 

5\. Click **Generate task**.

6\. Wait until the task is processed and has the **Sucess** status, click the task ID to view task details. 

7\. Check out the **Task result** field. You can have one of the following outputs: 

* **Sport detection: not found**. This means that your video doesn't contain sport activities. 

* If some sport activities are detected, you’ll get the info about the detected element, relevant iFrame, and the confidence level in % of how sure AI is that this content contains sport activities.  

<img src="https://assets.gcore.pro/docs/streaming-platform/ai-video-services/content-moderation/sport-detection.png" alt="Sport detection task details" width="70%">