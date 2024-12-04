---
title: generate-captions-via-api
displayName: Via API
published: true
order: 20
toc:
   --1--1. Obtain an MP4 link: "step-1-obtain-an-mp4-link"
   --1--2. Assign a transcription task to AI: "step-2-assign-a-transcription-task-to-ai"
   --1--3. Get the task result: "step-3-get-the-task-result"
   --1--4. Add subtitles to videos: "step-4-add-ai-asr-subtitles-to-videos"
pageTitle: Generate and translate AI subtitles via the Gcore API | Gcore
pageDescription: Learn how to create AI tasks for generating and translating AI subtitles by executing API methods.
---
# Generate and translate AI captions for a new VOD

You can upload video and generate captions automatically during process of uploading new videos to the Video Streaming platform. https://api.gcore.com/docs/streaming#tag/Videos/operation/post_api_videos 

In the process of uploading a video, it is necessary to add one new attribute "auto_transcribe_audio_language". Thanks to it, the system will automatically create a task for transcribing the video, and the finished result will be added to the video as a subtitle.

```
POST https://api.gcore.com/streaming/videos
{
    "name": "Spritefright Blender",
    "description": "Video copied from an external S3 Storage",
    "origin_url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4",
    "auto_transcribe_audio_language": "auto"
}
```

# Generate and translate AI captions for an exist VOD

For existing videos, the process of creating AI subtitles is as simple as when uploading a new video.

To do this, run the add subtitle method, but instead of specifying the subtitle text, specify the "auto_transcribe_audio_language" parameter, and the system will also run the AI ​​task to generate and attach the subtitle to the video. https://api.gcore.com/docs/streaming#tag/Subtitles/operation/post_api_videos_video_id_subtitles 

```
POST hhttps://api.gcore.com/streaming/videos/{video_id}/subtitles
{
    "auto_transcribe_audio_language": "auto"
}
```


# Extended use of AI API for any video inside or outside the Video Streaming platform

AI ​​system can process any video stored in an MP4 container and available via a direct download link. 
Please note that links to YouTube and Vimeo, etc. are not links to a video file, so they cannot be used for processing.

### Step 1. Obtain an MP4 link 

If the video is on an external source, get a link to this video. The link must be HTTP/S and the file must be available for downloading without authorization.

Let's look at an example of getting a link from our video storage.

To obtain an MP4 link to your video with 240p, 360p, or 468p quality. That quality is sufficient because it contains an <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/output-parameters-after-transcoding-bitrate-frame-rate-and-codecs#output-parameters-after-transcoding" target="_blank">64Kbps audio track</a> suitable for AI automatic speech recognition and transcription. To get your MP4 link, execute the following API request https://api.gcore.com/streaming#tag/Videos/operation/get_api_videos_id : 

```
GET https://api.gcore.com/streaming/videos/{id}
```

From the response, copy the value of the ```mp4_url``` field.

<alert-element type="warning" title="Warning"> 

If the mp4_url field isn't shown in the response, contact [technical support](maito:support@gcore.com). MP4 support may be disabled for your account. Technical support will enable it for you.

</alert-element>

<expandable-element title="Example of obtaining MP4 URL">

Request sample:

```
GET https://api.gcore.com/streaming/videos/4428031
```

Response sample:

```
{
    "id": 4428031,
    "name": "Sprite Fright, Blender",
    ...
    "hls_url": "https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt/master.m3u8",
    "iframe_url": "https://player.gvideo.co/videos/2675_G8EuYJFTsvIyW",
    "iframe_embed_code": "<iframe src="https://player.gvideo.co/videos/2675_G8EuYJFTsvIyWmKt" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>",
    "converted_videos": [
        {
            "name": "vod240n",
            "mp4_url": "https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt/qid96v1_200_240.mp4"
        },
       ...
    ]
}
```

The value required for the next step is in the mp4_url field: ```https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt/qid96v1_200_240.mp4```.

</expandable-element>

### Step 2. Assign a transcription task to AI

To assign a transcription task to Gcore AI ASR, execute the following API request:

```
curl -L 'https://api.gcore.com/streaming/ai/transcribe' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey {your_api_key}' \
-d '{
    "url": "https://demo-files.gvideo.io/{your_video_url/{quality}.mp4" 
}'
```

Ensure you replace the example values ```{your_api_key}``` and ```{your_video_url}/{quality}.mp4``` with your actual <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API token</a> and MP4 video URL.

In the response, you will get a task ID. It'll come in handy in the next step. For example: ```"task_id": "abc12345-6def…"```

<expandable-element title="Example of assigning a transcription task to AI">

Request sample:

```
curl -L 'https://api.gcore.com/streaming/ai/tasks' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey 1234$abcd...' \
-d '{
    "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4",
    "task_name": "transcription"
}'
```

Response sample:

```
{
    "task_id": "34d0ba5a-23f6-4462-85ff-fe343b0cdb2d"
}
```

The required value for the next step is in the task_id field: ```34d0ba5a-23f6-4462-85ff-fe343b0cdb2d```.

</expandable-element>

### If you need translation

As well as original-language transcription, we support subtitle translation in 100+ languages. The full language list is available in the <a href="https://api.gcore.com/docs/streaming#tag/AI/operation/post_ai_transcribe" target="_blank">API documentation</a>. Specify the language explicitly in the audio_language attribute in the body of the API request, and Gcore AI ASR will use this info to create subtitles. If this attribute is not set, AI will run auto language identification, and the subtitles will be in the original language.

By default, the transcription language is the same as the audio language. In the example above, the video was in English and the desired subtitle language was also English, so there was no need to set the subtitle language separately. 

However, if the language of the video differs from the desired subtitle language, you need to add to the request body the ```"subtitles_language"``` parameter.

So, this is how the request body will look like if the original language is _not_ English, and subtitles are desired in English:

```
curl -L 'https://api.gcore.com/streaming/ai/tasks' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey {your_api_key}' \
-d '{
    "url": "https://demo-files.gvideo.io/{your_video_url.mp4}",
    "task_name": "transcription",
    "subtitles_language": "ger"
}'
```

You can skip the ```"audio_language"``` field, and Gcore AI ASR will detect it automatically.

For the "code-switching" feature mentioned above, ```audio_language``` must be skipped.

### Step 3. Get the task result

Wait a few minutes for the AI to complete the transcription and translation. To get the task result, execute the following API request: 

```
GET https://api.gcore.com/streaming/ai/tasks/{your_task_id}
```

You will receive a response containing the transcribed and translated (if set) text. 

The following response elements may be useful for further video processing:

- **"subtitles" array** contains transcription divided into individual timecoded sentences. It includes ```"start_time"```, ```"end_time"``` and ```"text"``` fields. 
- **"concatenated_text" field** contains the full audio text. It can be used for robot scanning, Google indexing, or summarization using a service like ChatGPT.  
- **"vttContent" field** contains marked-up text that can be saved as a .vtt file and added to any system as ready-to-use subtitles.


<expandable-element title="Example of obtaining the result">

Request sample:

```
GET https://api.gcore.com/streaming/ai/tasks/34d0ba5a-23f6-4462-85ff-fe343b0cdb2d
```

Response sample:

```
{
    "task_data": {
        "url": "https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt/qid96v1_200_240.mp4"
    },
    "task_id": "34d0ba5a-23f6-4462-85ff-fe343b0cdb2d",
    "processing_time": {
        "completed_at": "2024-03-13T08:15:19Z",
        "started_at": "2024-03-13T08:13:27Z",
        "total_time_sec": 112
    },
    "progress": 100,
    "status": "SUCCESS",
    "result": {
        "subtitles": [
            {
                "start_time": "00:00:17.648",
                "end_time": "00:00:18.868",
                "text": "Hello, Mr. Snail."
            },
            ...
            {
                "start_time": "00:10:00.551",
                "end_time": "00:10:00.891",
                "text": "Did it, kid."
            }
        ],
        "vttContent": "WEBVTT\n\n1\n00:00:17.648 --> 00:00:18.868\nHello, Mr. Snail...00:10:00.551 --> 00:10:00.891\nDid it, kid.\n\n",
        "concatenated_text": "Hello, Mr. Snail. Oh, you cute little corny wasp-assum. Latin name, bonus points...You made it, kids. Did it, kid. "
   }
}
```

</expandable-element>

### Step 4. Add AI ASR subtitles to videos

1\. Copy the value of the ```"vttContent"``` field from the previous step. This contains the subtitles for your video. 

2\. Add the subtitles to the video by executing the following API request: 

```
curl -L 'https://api.gcore.com/streaming/videos/{video_id}/subtitles' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey 1234$abcd...' \
-d '{
     "name": "English (AI-translate)",
     "language": "eng",
     "vtt": "{your_vtt_field_content}"
}'
```

That's it! You can now generate subtitles using AI, add translations (if necessary), and upload subtitles to your video. 

<alert-element type="info" title="Info">

We are working on fully integrating subtitle generation into the video upload process. Soon, you'll be able to generate subtitles using unique attributes in the POST /videos method. Stay tuned!

</alert-element>
