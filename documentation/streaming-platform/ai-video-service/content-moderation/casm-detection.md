---
title: casm-detection
displayName: Child sexual abuse materials
published: true
order: 40
pageTitle: Child sexual abuse materials detection in videos | Gcore
pageDescription: Learn how to use Gcore's AI tasks to detect child sexual abuse materials in videos hosted on the Gcore's platform or externally.
---
# Child sexual abuse materials (CSAM)

The child pornography content moderation task detects child sexual abuse materials (CSAM). 

To identify this content, we first run the <a href="https://gcore.com/docs/streaming-platform/ai-video-service/content-moderation/soft-nudity-detection" target="_blank">soft nudity</a> and <a href="https://gcore.com/docs/streaming-platform/ai-video-service/content-moderation/soft-nudity-detection" target="_blank">hard nudity detection</a> tasks. If both methods indicate the presence of obscene content with the involvement of children (child's face) in a frame, then such a video is marked as obscene. Frames are designated by the age category of identified children. 

The check returns information with the number of the video frame in which the child's face was found and the child’s age. Objects with a probability of at least 30% are included in the response. 

To run the child pornography detection check:

1\. In the Gcore Customer Portal, navigate to **Streaming** > **AI**. The **AI tasks** page will open.

<img src="https://assets.gcore.pro/docs/streaming-platform/ai-video-services/content-moderation/ai-tasks-page.png" alt="AI tasks page" width="80%">

2\. In the **Origin URL** field, enter the link to your MP4 video. You have two options: 

* **Paste video origin URL**: If your video is stored externally, provide a URL to its location. Ensure that the video is accessible via HTTP or HTTPS protocols.  

   To check the example of correctly formatted URL, use the link under the field. It will autogenerate a sample URL and you can adjust your URL accordingly. 

   <img src="https://assets.gcore.pro/docs/streaming-platform/ai-video-services/content-moderation/example-url-link.png" alt="Example of the origin URL" width="80%">

* **Select from uploaded videos**: choose a video hosted on the Gcore platform. 

3\. In the **Task type**, choose **Content moderation**. 

4\. In the following dropdown, select **Child pornography detection**. 

5\. Click **Generate task**.

6\. Wait until the task is processed and has the **Sucess** status, click the task ID to view task details. 

7\. Check out the **Task result** field. You can have one of the following outputs: 

* **Child pornography detection: not found**. This means that your video has no child sexual abuse materials. 

* If some sensitive content is found, you’ll get the info about the detected element, relevant iFrame, and the confidence level in % of how sure AI is that this content contains child sexual abuse materials.  

<img src="https://assets.gcore.pro/docs/streaming-platform/ai-video-services/content-moderation/child-pornography-detection.png" alt="Child pornography detection task details" width="70%">