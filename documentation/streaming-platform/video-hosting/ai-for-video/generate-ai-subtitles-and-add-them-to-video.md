---
title: generate-ai-subtitles-and-add-them-to-video
displayName: AI subtitles
published: true
order: 20
toc:
   --1--Overview: "overview"
   --1--Benefits: "benefits-of-gcore-ai-subtitle-generation"
   --1--Generate subtitles and add to videos: "generating-subtitles-with-ai-and-adding-them-to-videos"
   --2--1. Obtain an MP4 link: "step-1-obtain-an-mp4-link"
   --2--2. Set a task for AI: "assign-a-transcription-task-to-ai"
   --3--Translation: "if-you-need-translation"
   --2--3. Get the result: "step-3-get-the-task-result"
   --2--4. Add subtitles to videos: "step-4-add-ai-generated-subtitles-to-videos"

pageTitle: AI-Generated Subtitles with Translations | Gcore
pageDescription: Effortlessly generate and add AI subtitles in various languages with Gcore.
---
# Generating AI subtitles and adding them to videos 

## Overview 

At Gcore Video Streaming, you can automatically generate <a href="https://gcore.com/docs/streaming-platform/video-hosting/subtitles-and-closed-captions-for-vod#what-are-subtitles-and-closed-captions" target="_blank">video subtitles</a> using AI models. There are two key functionalities for this purpose: 

- **Transcription**, which allows for audio-to-text conversion. The subtitles will be in the original language in the video. 
- **Translation**, which allows text to be translated from one language to another, making it accessible to speakers of different languages. 

We can prepare subtitles for any MP4 videos. There's no need to upload videos to Gcore Video Hosting. You can apply API methods to automatically generate subtitles with AI for videos stored externally, such as on AWS. 

For advanced video content processing, we use <a href="https://openai.com/research/whisper" target="_blank">Whisper ASR</a> (automatic speech recognition) from OpenAI, along with various specialized AI models. These AI ASR models operate on the Gcore infrastructure, ensuring that no files are transferred to external services.

## Benefits of Gcore AI subtitle generation

- **Affordable pricing.** Transcription is free, while translation costs vary depending on the length of the original video analyzed. 
- **Ease of use.** With just four API requests, you can have ready-to-use subtitles. 
- **Reduced transcription errors.** The use of machine-learning AI Whisper, developed by industry leaders OpenAI, along with additional models, minimizes errors that may occur during automatic speech recognition. 
- **Supported languages.** AI can recognize and transcribe audio in over 100 languages worldwide. If your desired language isn't listed, please contact our [technical support](maito:support@gcore.com), and we will add it. 
- **Multi-language support.** We support the recognition of multiple languages in a video (the “code-switching” feature), such as when video participants switch between several languages or from their native language to English and back. 

## Generating subtitles with AI and adding them to videos

To generate subtitles using AI: 

### Step 1. Obtain an MP4 link 

Obtain an MP4 link to your video with 480p quality. This is necessary because this version contains a <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/output-parameters-after-transcoding-bitrate-frame-rate-and-codecs#output-parameters-after-transcoding" target="_blank">128kbps audio track</a> suitable for AI. To get a link, execute the following API request: 

```
GET https://api.gcore.com/docs/streaming#tag/Videos/operation/get_api_videos_id
```

From the response, copy the value of the ```mp4_url``` field.

<alert-element type="warning" title="Warning">

If the mp4_url field isn't in your response, contact [technical support](maito:support@gcore.com). This field may be missing because MP4 support is disabled for your account. Technical support will enable it for you.

</alert-element>

<expandable-element title="Example of Obtaining MP4 URL">

A request sample:

```
GET https://api.gcore.com/streaming/videos/4428031
```

A response sample:

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
            "mp4_url": "https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt/480.mp4"
        },
       ...
    ]
}
```

The wanted value for the next step is in the mp4_url field (```https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt/480.mp4```.) 

</expandable-element>

### Step 2. Assign a transcription task to AI

To assign a transcription task to AI, execute the following API request:


```
curl -L 'https://api.gcore.com/streaming/ai/transcribe' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey {your_api_key}' \
-d '{
    "url": "https://demo-files.gvideo.io/{your_video_url/480.mp4}" 
}'
```

Ensure you replace the example values ```{your_api_key}``` and ```{your_video_url/480.mp4}``` with your actual <a href="https://gcore.com/docs/account-settings/create-use-or-delete-a-permanent-api-token" target="_blank">API token</a> and MP4 video URL.

In the response, you will get a task ID. It'll come in handy in the next step. For example: ```"task_id": "abc12345-6def…"```

<expandable-element title="Example of assigning a transcription task to AI">

A request sample:

```
curl -L 'https://api.gcore.com/streaming/ai/transcribe' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey 1234$abcd...' \
-d '{
    "url": "https://demo-files.gvideo.io/apidocs/spritefright-blender-cut30sec.mp4" 
}'
```

A response sample:

```
{
    "task_id": "34d0ba5a-23f6-4462-85ff-fe343b0cdb2d"
}
```

The wanted value for the next step is in the task_id field (```34d0ba5a-23f6-4462-85ff-fe343b0cdb2d```.)

</expandable-element>

### If you need translation

We support subtitle transcription and translation in 100+ languages. See the full list in the <a href="https://api.gcore.com/docs/streaming#tag/AI/operation/post_ai_transcribe" target="_blank">API documentation</a>. You can specify the language explicitly in the audio_language attribute in the body of the API request, and AI will use this info to create subtitles. If this attribute is not set, AI will run auto language identification, and the subtitles will be in the detected language.

By default, the transcription language is the same as the audio language. In the example above, the video was in English, so there was no need to set the subtitle language separately. 

If the language of the video is different from English and subtitles are needed for example in English, you need to add to the request body the ```"subtitles_language"``` parameter.

So, this is how the request body will look like if the original language is different from English, and subtitles should be translated into English:

```
curl -L 'https://api.gcore.com/streaming/ai/transcribe' \
-H 'Content-Type: application/json' \
-H 'Authorization: APIKey {your_api_key}' \
-d '{
    "url": "https://demo-files.gvideo.io/{your_video_url.mp4}"
    "audio_language": 'bre'   
    "subtitles_language": 'eng'  
}'
```

You can skip an ```"audio_language"``` field, and AI will detect it automatically. For the "code-switching" feature mentioned above, ```audio_language``` must be skipped.

### Step 3. Get the task result

Wait a few minutes for the AI to complete the transcription and translation. To get the task result, execute the following API request: 

```
GET https://api.gcore.com/streaming/ai/results/{your_task_id}
```

You will receive a response containing the text transcribed from the audio and translated (if set). 

The following response elements will be useful for futher video processing:

- **"subtitles" array** contains transcription divided into individual timecoded sentences. It includes ```"start_time"```, ```"end_time"``` and ```"text"``` fields. 
- **"concatenated_text" field** contains a full text recognized from audio. It can be used for robot scanning, Google indexing, or passed to ChatGPT for summarization.  
- **"vttContent" field** contains marked-up text that can be saved as a .*vtt* file and added to any system as ready-to-use subtitles.


<expandable-element title="Example of getting the result">

A request sample:

```
GET https://api.gcore.com/streaming/ai/results/34d0ba5a-23f6-4462-85ff-fe343b0cdb2d
```

A response sample:

```
{
    "task_data": {
        "url": "https://demo-public.gvideo.io/videos/2675_G8EuYJFTsvIyWmKt/480.mp4"
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

### Step 4. Add AI-generated subtitles to videos

1\. Copy the value of the ```"vttContent"``` field from the previous step. This will be used as a subtitle for your video. 

2\. Add the subtitle to the video by executing the following API request: 

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

<alert-element type="warning" title="Warning">

We are working on fully integrating subtitle generation into the video upload process. Soon, you'll be able to generate subtitles using unique attributes in the POST /videos method. Stay tuned!

</alert-element>