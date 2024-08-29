---
title: ai-nudity detection
displayName: Hard nudity detection
published: true
order: 20
pageTitle: Hard nudity content detection in videos | Gcore
pageDescription: Learn how to use Gcore's AI tasks to detect hard nudity in videos hosted on the Gcore's platform or externally.
customUrl: /streaming-platform/ai-video-service/ai-nudity-detection
---
# Hard nudity detection

The hard nudity content moderation task detects explicit nudity of the human body (involving genitals) in a video. This method is often used to detect whether videos can be published to all users, or the publication should be prohibited due to offensive and inappropriate content. 

This task detects fewer objects than soft-nudity detection. Hard nudity detection works faster and better when you only need to detect exposed body parts. For a full list of objects that can be detected with the soft nudity check, read our <a href="https://api.gcore.com/docs/streaming?_gl=1*1rw278g*_gcl_au*MTM0OTcwMzMxMC4xNzE3MTQ0ODk3*_ga*OTkwMzM5NjM4LjE3MDkxMDg3OTU.*_ga_Y79HRL8RPR*MTcyMTI4NzExMi4xMjIuMS4xNzIxMjg3MjMzLjYwLjAuMA..#tag/AI/operation/post_ai_contentmoderation_hardnudity" target="_blank">API documentation</a>. 

If hard nudity content is detected, the AI model will provide its confidence level (in percentage) of how sure it is that the content is hard nudity.  

To run the Hard nudity detection check: 

1\. In the Gcore Customer Portal, navigate to **Streaming** > **AI**. The **AI tasks** page will open.

<img src="https://assets.gcore.pro/docs/streaming-platform/ai-video-services/content-moderation/ai-tasks-page.png" alt="AI tasks page" width="80%">

2\. In the **Origin URL** field, enter the link to your MP4 video. You have two options: 

* **Paste video origin URL**: If your video is stored externally, provide a URL to its location. Ensure that the video is accessible via HTTP or HTTPS protocols.  

   To check the example of correctly formatted URL, use the link under the field. It will autogenerate a sample URL and you can adjust your URL accordingly. 

   <img src="https://assets.gcore.pro/docs/streaming-platform/ai-video-services/content-moderation/example-url-link.png" alt="Example of the origin URL" width="80%">

* **Select from uploaded videos**: choose a video hosted on the Gcore platform. 

3\. In the **Task type**, choose **Content moderation**. 

4\. In the following dropdown, select **Hard nudity detection**. 

5\. Click **Generate task**.

6\. Wait until the task is processed and has the **Sucess** status, click the task ID to view task details. 

7\. Check out the **Task result** field. You can have one of the following outputs: 

* **Hard nudity detection: not found**. This means that your video has no hard nudity content. 

* If some sensitive content is found, you’ll get the info about the detected element, relevant iFrame, and the confidence level in % of how sure AI is that this content is hard nudity. For example, you can get the following output: *“FEMALE_BREAST_EXPOSED: detected at frame №2 with score 41%”address*. 

<img src="https://assets.gcore.pro/docs/streaming-platform/ai-video-services/content-moderation/hard-nudity-detection.png" alt="Hard nudity detection task details" width="70%">