---
title: ai-nudity detection
displayName: AI nudity detection
published: true
order: 20
toc:
   --1--Overview: "ai-nudity-detection-overview"
   --1--Billig: "billing"
   --1--Objects to be detected: "what-objects-can-be-detected"
   --1--Analyze for nudity: "analyze-videos-for-nudity"
   --2--1. Obtain an MP4 link: "step-1-obtain-an-mp4-link"
   --2--2. Create a nudity detection task: "step-2-create-a-nudity-detection-task"
   --2--Pause detection if a stop tag is triggered: "pause-detection-if-a-stop-tag-is-triggered"
   --2--3. Get the task result: "step-3-get-the-task-result"
   --1--Assessing the probability: "assessing-the-probability-of-inappropriate-content"
   --1--How to use results in practice: "how-to-use-results-in-practice"
pageTitle: Guide to Gcore's AI Nudity Detection for Video Content Moderation | Gcore
pageDescription: Learn how to use Gcore's AI nudity detection for moderating video content, ensuring it's suitable for your audience.
---
# AI nudity detection

## AI nudity detection overview

The AI nudity detection feature is a part of the <a href="https://gcore.com/docs/streaming-platform/video-hosting/ai-video-service" target="_blank">AI Video Services</a>, designed to identify explicit content in videos. This method provided by <a href="https://api.gcore.com/docs/streaming#tag/AI/operation/post_ai_detectnudity" target="_blank">Gcore API method</a> is suitable for automatic visual content analysis, recognition, and moderation, utilizing machine learning. 

Gcore's AI nudity detection can be used for moderating User-Generated Content (UGC). It aids in determining whether the video is suitable for all user categories without age restrictions, or if it should be prohibited.

## Billing 

Billing takes into account either the duration of the analyzed video or the length of time up to the <a href="https://gcore.com/docs/streaming-platform/video-hosting/ai-video-service/ai-nudity detection#pause-detection-if-a-stop-tag-is-triggered
">stop tag</a>, if the condition was triggered during the analysis.

## What objects can be detected?

Gcore's AI nudity moderation can identify explicit content, involving either real individuals or deepfakes, as well as anthropomorphic cartoon characters. It is capable of detecting the following objects, whether they are fully or partially visible:

<table>
<thead>
<tr>
<th>Class</th>
<th>Definitions</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left"><pre>ANUS_EXPOSED</pre></td>
<td style="text-align: left">Human anus when it is nude or covered with sheer clothing</td>
</tr>
<tr>
<td style="text-align: left"><pre>BUTTOCKS_EXPOSED</pre></td>
<td style="text-align: left">Human buttocks when they are nude or covered with sheer clothing</td>
</tr>
<tr>
<td style="text-align: left"><pre>FEMALE_BREAST_EXPOSED</pre> <pre>MALE_BREAST_EXPOSED</pre></td>
<td style="text-align: left">Nude female or male breasts with nipples</td>
</tr>
<tr>
<td style="text-align: left"><pre>FEMALE_GENITALIA_EXPOSED</pre> <pre>MALE_GENITALIA_EXPOSED</pre></td>
<td style="text-align: left">Human female genitalia (including vulva, vagina, and pubic hair) and male genitalia (including the penis, scrotum, and pubic hair)</td>
</tr>
</tbody>
</table>

## Analyze videos for nudity

Gcore's AI nudity detection is compatible with any MP4 video. This means you can upload files to <a href="https://gcore.com/streaming-platform/video-hosting" target="_blank">Gcore Video Hosting</a> or use MP4 videos from external storage sources, like AWS. Furthermore, nudity detection is not limited to videos; you can also detect explicit content in JPEG format images. For billing purposes the picture will be treated as a 1-second long-view video.

### Step 1. Obtain an MP4 link

If you're using a third-party video storage service other than Gcore, obtain an appropriate link to the MP4 video. If you're using Gcore's Video Hosting, you need to execute the following API request to obtain the MP4 link:

```
curl -L 'https://api.gcore.com/streaming/videos/{video_id}' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey {your_api_key}' \
```

Ensure you replace the example values `{video_id}` and `{your_api_key}` with the MP4 video URL and your actual <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API token</a>.

Copy the value of the `mp4_url` field from the response.

<alert-element type="warning" title="Warning">

If the `mp4_url` field does not appear in the response, reach out to [technical support](mailto:support@gcore.com). It's possible that MP4 support may be disabled for your account. Technical support can enable it for you.

</alert-element>

<expandable-element title="Example of obtaining MP4 URL">

Request sample:

```
curl -L 'https://api.gcore.com/streaming/videos/4428031' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey {your_api_key}' \
```

Response sample:

```
{
    "id": 4428031,
    "name": "Sprite Fright, Blender (cut 30 seconds version for AI subtitles generation demo in API docs)",
    ...
    "hls_url": "https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt/master.m3u8",
    "iframe_url": "https://player.gvideo.co/videos/2675_G8EuYJFTsvIyW",
    "iframe_embed_code": "<iframe width="560" height="315" src="https://player.gvideo.co/videos/2675_G8EuYJFTsvIyWmKt" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>",
    "converted_videos": [
        {
            "name": "vod720n",
            "width": 1720,
            "height": 720,
            "mp4_url": "https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt/720.mp4"
        },
        {
            "name": "vod480n",
            "width": 1146,
            "height": 480,
            "mp4_url": "https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt.mp4"
        },
       ...
    ]
}
```

The value required for the next step is in the mp4_url field: ```https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt.mp4```.

</expandable-element>

### Step 2. Create a nudity detection task

Execute the following API request to create a task:

```
curl -L 'https://api.gcore.com/streaming/ai/detect-nudity' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey {your_api_key}' \
-d '{
    "url": "https://demo-files.gvideo.io/{your_video_url.mp4}" 
}'
```

Ensure you replace the example values `{your_api_key}` and `{your_video_url.mp4}` with the MP4 video URL and your actual <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API token</a>.

In the response, you will get a unique task ID. It'll come in handy in the next step. For example: ```"task_id": "abc12345-6def…"```

<expandable-element title="Example of a nudity detection task creation">

Request sample:

```
curl -L 'https://api.gcore.com/streaming/ai/detect-nudity' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey 1234$abcd...' \
-d '{
    "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4" 
}'
```

Response sample:

```
{
    "task_id": "34d0ba5a-23f6-4462-85ff-fe343b0cdb2d"
}
```

The required value for the next step is in the task_id field: `34d0ba5a-23f6-4462-85ff-fe343b0cdb2d`.

</expandable-element>

### Pause detection if a stop tag is triggered

There are times when an object detected at the beginning of the video immediately indicates that further analysis of the video is unnecessary. For such instances, you can add stop tags in the body of the nudity detection creation task. 

Use the `stop_objects` parameter to specify stop tags, separating each one with a comma. You can also set a probability threshold value, expressed as a percentage. If this value is exceeded, the stop tag will be triggered.

Response sample:

```
curl -L 'https://api.gcore.com/streaming/ai/detect-nudity' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey {your_api_key}' \
-d '{
    "url": "https://demo-files.gvideo.io/{your_video_url.mp4}",
    "stop_objects": "MALE_GENITALIA_EXPOSED:0.8,FEMALE_GENITALIA_EXPOSED" 
}'
```

Ensure you replace the example values `{your_api_key}` and `{your_video_url.mp4}` with the MP4 video URL and your actual <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API token</a>.

### Step 3. Get the task result

Wait a few minutes for the AI to complete nudity detection. To get the task result, execute the following API request:

```
curl -L 'https://api.gcore.com/streaming/ai/results/{your_task_id}' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey {your_api_key}' \
```

<alert-element type="info" title="Info">

Webhooks for AI methods will be available soon. Additionally, batch methods are currently in the early stages of development. As soon as they are ready for use, we will ensure to notify you promptly.

</alert-element>

There are five potential statuses (PENDING, STARTED, SUCCESS, FAILURE, and REVOKE) that reflect the progression of AI video processing. You should wait for the final statuses, either SUCCESS or FAILURE. 

As a result of the processing, you will receive a JSON file containing an array of entries if explicit content is detected. This final text result can be used to configure the logic of processes (for example, deciding whether to publish a video or not) on your backend. Below, we've provided an example of how this could be implemented.

<expandable-element title="Example of the response">

Response sample: 


```
{
    "task_data": {
        "url": "https://12345.gvideo.io/videos/12345_ZGNUY4U2NkhlF4xW/qid87v1_1080.mp4"
    },
    "task_id": "34d0ba5a-23f6-4462-85ff-fe343b0cdb2d",
    "processing_time": {
        "completed_at": "2024-03-26T07:00:07Z",
        "started_at": "2024-03-26T07:00:03Z",
        "total_time_sec": 3
    },
    "progress": 100,
    "status": "SUCCESS",
    "result": {
        "detection_results": [
            {
                "class": "FEMALE_BREAST_EXPOSED",
                "score": 0.5,
                "frame-no": 5
            }, …
         ]
    }
}
```

</expandable-element>

If there’s no nudity detected the array will be empty:

```  
{
      "detection_results": []
}
```

The following response elements may be useful for further video moderation:

- **class**—a nudity type; see more details in <a href="https://gcore.com/docs/streaming-platform/video-hosting/ai-video-service/ai-nudity-detection#what-objects-can-be-detected">What objects can be detected</a>, for example, `FEMALE_BREAST_EXPOSED`. 
- **score**—the probability that the object does relate to nudity, for example, `0.5`.  
- **frame-no**— the video frame number where nudity was found, for example, `5`.

<alert-element type="" title="">

AI evaluates all objects in the video and analyzes how well they fit the abovementioned criteria. If the percentage probability is greater than or equal to 30% (0.3), the object's class will be listed in the API response and the second at which it was first encountered. 

</alert-element>

## Assessing the probability of inappropriate content 

There's no one-size-fits-all criterion or nudity score that can definitively determine whether a video is inappropriate. Different video hosting services cater to specific audiences such as adults, children, or educational groups, etc. For instance, an acceptable nudity percentage for a site dedicated to sex education would be higher than for a hosting site that uploads entertainment videos intended for children. 

You can set a probability threshold to determine when a video is inappropriate for your specific use case. One method is to run videos for one day and analyze the resulting probability coefficient.

## How to use results in practice?

Here's a procedure for utilizing Gcore's AI nudity detection when checking User-Generated Content (UGC): 

1. A user uploads a video to your app. You can use a platform like Gcore Video Hosting for video storage, but other platforms are also acceptable. 

2. During the upload process, the video is transcoded and simultaneously checked for nudity (if you're using Gcore Video Hosting). If the video is from external storage, simply send us a link for AI nudity moderation. 

3. The backend logic for deciding whether to publish is based on two parameters: 

- The video has been transcoded and is now viewable.
- The video has been scanned for nudity (based on the analyzed coefficient) and no explicit content has been detected