---
title: upload-video-via-api
displayName: Upload video via API
published: true
order: 60
toc:
   --1--Video Hosting: "how-is-gcore-video-hosting-organized"
   --1--Statuses of videos: "video-upload-and-processing-statuses"
   --1--Copy from another storage: "copy-from-external-storage"
   --2--Overview: "overview"
   --2--Example: "example-of-api-request"
   --2--How it works: "how-it-works"
   --1--Upload from a local device: "upload-from-a-local-device"
   --2--Step 1. Create a video and get an ID: "step-1-create-a-video-entity-and-get-a-video-identifier"
   --2--Step 2. Get TUS parameters: "step-2-get-tus-session-parameters"
   --2--Step 3. Upload video via TUS protocol: "step-3-upload-file-via-tus-chunked-protocol"
   --1--Batch upload (in development): "batch-upload-to-migrate-a-vast-number-of-videos-from-other-services"
pageTitle: Guide for VOD Upload via API | Gcore
pageDescription: Follow our step-by-step guide, including a tus standard script example for seamless VOD upload to storage in two ways, Pull and Push. 
---
# Upload video via API to VOD storage

## How is Gcore Video Hosting organized?

Video Hosting refers to cloud storage of videos that are ready to be distributed and watched on end devices via the public internet. You can upload original video files in <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/what-initial-parameters-of-your-live-streams-and-videos-we-can-accept" target="_blank">different formats</a>, we process the videos in various ways, and we save the result to our internal storage. As a result, you get videos in <a href="https://gcore.com/docs/streaming-platform/video-hosting/hls-and-mp4" target="_blank">HLS/MP4 format</a> with <a href="https://gcore.com/docs/streaming-platform/video-hosting/subtitles-and-closed-captions-for-vod" target="_blank">subtitles</a>, <a href="https://gcore.com/docs/streaming-platform/video-hosting/timeline-hover-previews-use-in-players-and-roku-devices" target="_blank">timeline previews</a>, and other features available.

You can upload videos to the storage via the control panel or API. Learn how to <a href="https://gcore.com/docs/streaming-platform/video-hosting/upload-a-video-and-embed-it-to-your-app" target="_blank">add a video via the control panel</a>.

Upload of videos via API can be done in three ways, which we describe in detail in this article. Quickly navigate to your chosen method here:  

- Copy from external storage  
- Upload from a local device 
- Batch upload to migrate a vast number of videos from other services (available soon)

## Video upload and processing statuses

When uploading a video to our storage and its processing, the file may have one of the following statuses:  

- **Empty** means the video entity has been created, but the origin video file has not yet been uploaded. In case of a long delay, check the “error” field for more details.  
- **Pending** means the video is being processed; the original video file has been downloaded and submitted for processing.
- **Viewable** means the video is available for watching at least in 1 quality (but not in all qualities.)
- **Ready** means the video is ready and available in all qualities.

**Note**: In the status “Viewable,” manifest.m3u8 has already been generated. End users in any player can watch the video, but a limited number of qualities are available. Qualities will be added automatically to manifest.m3u8 as they are ready; you don’t have to do anything. After adding all qualities, the video will be moved to “Ready.”

Example of the response of a video under processing:

```
{ 
  "id": 2558721, 
  "name": "Gcore Demo", 
  "description": "Video copied from an external S3 Storage", 
  "status": "pending", 
  "screenshots": [], 
  "origin_url": "https://s-ed1.cloud.gcore.lu/demo-video/gcore.mp4", 
  ... 
  "converted_videos": [ 
    { 
      "name": "vod480n", 
      "progress": 0, 
      "status": "processing", 
      "error": "", 
      ... 
   }, 
   ... 
  ] 
} 
```

If the video fails while uploading and checking, it will remain in “empty” status with details in the “error” field. Most commonly, this happens when an end user uploads a non-video file or has a connectivity issue. In that case, re-upload the video from the origin, or delete the entity and create a new one with the correct video file.

Example of the response if an error occurs during video processing:


```
{ 
  "id": 2558799, 
  "name": "Gcore Demo", 
  "description": "Video copied from an external S3 Storage", 
  "status": "empty", 
  "error": "File Invalid", 
  "origin_url": "https://s-ed1.cloud.gcore.lu/demo-video/master.m3u8", 
  ... 
  "converted_videos": [] 
} 
```
## Copy from external storage

In the section, we explain how to copy files from a third-party, external storage to the Gcore Streaming Platform. We will explain the process, offer an example API request, then explain how it works.

### Overview

If your videos are available by public HTTPS URL, this is the best option to copy video files directly from external storage.

**Note**: The original file must be in MP4 format or one of the following formats: 3g2, 3gp, asf, avi, dif, dv, flv, f4v, m4v, mov, mp4, mpeg, mpg, mts, m2t, m2ts, qt, wmv, vob, mkv, ogv, webm, vob, ogg, mxf, quicktime, x-ms-wmv, mpeg-tts, vnd.dlna.mpeg-tts.

Streaming formats like HLS (.m3u8/.ts) and DASH (.mpd/.m4v) are intended for the final video distribution to end viewers, so they cannot be used as original file formats.

Examples of good and bad links to video files from external storage:  

- **Good link**: ```https://demo-files.gvideo.io/gcore.mp4``` (13,8MB) 
- **Bad link** (because of chunked HLS format): ```https://demo-files.gvideo.io/hls/master.m3u8```  

Below, we explain how to <a href="https://gcore.com/docs/streaming-platform/video-hosting/upload-video-via-api#batch-upload-to-migrate-a-vast-number-of-videos-from-other-services">get HTTP public access links</a> in different external storages. 

To copy a video from another server, specify the attribute ```origin_url``` in the <a href="https://api.gcore.com/docs/streaming#tag/Videos/operation/post_api_videos" target="_blank">POST API request</a>. The original video will be downloaded for Video Hosting on our server side. 

**Note**: You can only upload one video per request.

### Example of API request 

Here is an example of the API request to set a task for copying a video from external storage:

```
curl -L 'https://api.gcore.com/streaming/videos/' \ 
-H 'Content-Type: application/json' \ 
-H 'Authorization: APIKey 1234$0d16599c' \ 
-d '{ 
  "video": { 
    "name": "Gcore Demo", 
    "description": "Video copied from an external S3 Storage", 
    "origin_url": "https://s-ed1.cloud.gcore.lu/demo-video/gcore.mp4" 
  } 
}
```

Example of the response:


```
{ 
  "id": 2496039, 
  "name": "Gcore Demo", 
  "description": "Video copied from an external S3 Storage", 
  ... 
}
``` 


After setting the task for downloading, it is queued. You can queue an unlimited number of files, and each one will be processed as soon as possible.

**Note**: Please be aware of <a href="https://api.gcore.com/docs/iam#section/Rate-limits" target="_blank">RPS limits for using API</a>.

### How it works

Here’s how the platform works on our end. We attempt to download a file three times, expecting a 200 OK response to access your provided link. If the download fails, the video entity will stay in the “Empty” status, and details will be added to the field ```error```. You need to delete the empty video entity and try to create a new one with the correct origin URL.

Once successfully uploaded and processed, the video will be available on our platform. You can check the status of the video by the <a href="https://api.gcore.com/docs/streaming#tag/Videos/operation/get_api_videos_id" target="_blank">GET API request</a> or via webhook <a href="https://gcore.com/docs/streaming-platform/extra-features/get-webhooks-from-the-streaming-platform" target="_blank">notifications</a>. 

## Upload from a local device

When you develop your service, a video must be uploaded from the local host (your backend) or by users from a browser or mobile app. 

We use the <a href="https://tus.io" target="_blank">TUS resumable upload protocol</a> for uploading files, which works by cutting the video for upload into small segments and, if an interruption occurs, continuing from the point of interruption.  

The uploading process consists of three steps.

### Step 1. Create a video entity and get a video identifier

Specify the main parameters, and do not use the ```origin_url``` attribute in the <a href="https://api.gcore.com/docs/streaming#tag/Videos/operation/post_api_videos" target="_blank">POST API request</a>.

Example of the request:

```
curl -L 'https://api.gcore.com/streaming/videos/' \ 
-H 'Content-Type: application/json' \ 
-H 'Authorization: APIKey 1234$0d16599c' \ 
-d '{ 
  "video": { 
    "name": "Gcore Demo", 
    "description": "Uploaded via TUS session" 
  } 
}'
```
Example of the response:

```
{ 
  "id": 2501637, 
  "name": "Gcore Demo", 
  "description": "Uploaded via TUS session", 
  "duration": null, 
  "slug": "70NbFUCZyXU2s3tY", 
  "status": "empty", 
  ... 
} 
```

### Step 2. Get TUS session parameters

To upload a file, you must get a TUS server URL and secret token. Specify the “id” parameter from step 1 and <a href="https://api.gcore.com/docs/streaming#tag/Videos/operation/get_api_videos_id_upload" target="_blank">get the TUS session parameters</a>.

Example of the request:

```

curl -L 'https://api.gcore.com/streaming/videos/2501637/upload' \ 
-H 'Authorization: APIKey 1234$0d16599c' 
```

Example of the response:

```
{ 
  "servers": [ 
   { 
      "id": 561, 
      "role": "upload", 
      "hostname": "vod-uploader-ed-2.gvideo.co", 
      "active": true, 
      "ssl": true 
    }, 
    ... 
  ], 
  "token": "eyJhbGciOiJIUzI3O6kc3Og...", 
  "video": { 
    "id": 2501637, 
    "name": "Gcore Demo", 
    "description": "Uploaded via TUS session", 
    "duration": null, 
    "slug": "70NbFUCZyXU2s3tY", 
    "status": "empty", 
    ... 
   } 
} 
```

Where: 

- ```servers```: A list of available servers to upload the file; you can use any of them.
- ```token```: A secret token for starting the TUS session, valid for 4 hours which is long enough because as soon as the session starts, the token is no longer needed.
- ```video```: A copy of the main data pertaining to your video entity.

### Step 3. Upload file via TUS chunked protocol

For uploading, use the session parameters taken from the previous step:

```
endpoint = "https://{hostname}/upload/" 
chunksize = 10000000 
filename = "{filename}" 
filetype = "{file_mime_type}" 
token = "{tus_token}"  
video_id = {video_id} 
client_id = {client_id} 
```

**Note**: The ```chunksize``` number is given in bytes. Take care to choose the chunk size appropriately:

- The larger the size of a chunk, the faster each chunk will be uploaded using the maximum bandwidth. But in the case of failure to upload, TUS will only start uploading from the last successful chunk, which may have been some time ago. So with large sizes, the speed will be faster, but if it fails, the additional reupload time will be significant.
- With small sizes, the risk of uploading errors decreases. However, due to the features of HTTP (handshakes, etc.) for each chunk’s request, the upload speed will significantly reduce. So small chunk sizes mean a slow but reliable upload speed.

Try the <a href="https://codepen.io/apih9000/pen/wvQmNEW?editors=1011" target="_blank">CodePen template</a> by copying your ```token```, ```video_id```, and ```client_id``` to find out the upload functionality of the TUS protocol:  

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/upload-video-via-api/codepen-example.png" alt="CodePen template">

Example of JS code: 

```
const options = { 
  endpoint,   
  chunkSize, 
  retryDelays: [0, 1000, 3000], 
  metadata: { 
    filename: file.name, 
    filetype: file.type, 
    // must provide these 3 fields too 
    token: token, 
    video_id: videoid, 
    client_id: clientid 
  }, 
  onError(error) { 
    ... 
  }, 
  onProgress(bytesUploaded, bytesTotal) { 
    ... 
  }, 
  onShouldRetry: function (err, retryAttempt, options) { 
    // tus-js-client should retry 
    return true 
  }, 
  onSuccess() { 
    ... 
  } 
} 
 
upload = new tus.Upload(file, options) 
upload.findPreviousUploads().then((previousUploads) => { 
  askToResumeUpload(previousUploads, upload) 
 
  upload.start() 
  uploadIsRunning = true 
}) 
```

Choose your TUS implementation: 

- JS: We support 2.x version of tus-js-client, for details check out <a href="https://github.com/tus/tus-js-client/releases?q=v2.&expanded=true" tarhet="_blank">GitHub</a>  
- Android: <a href="https://github.com/G-Core/android-demo-vod-hosting" tarhet="_blank">Gcore’s open-source Kotlin demo app</a> 
- iOS: <a href="https://github.com/G-Core/ios-demo-vod-hosting" tarhet="_blank">Gcore’s open-source Swift demo app</a>
- Other implementation options can be found on the <a href="https://tus.io/implementations" tarhet="_blank">official TUS website</a>

Most common TUS errors: 

- **HTTP 405 Method Not Allowed**. Unexpected response while creating upload session; check parameters of the request.
- **HTTP 429 Too Many Requests**. Try to send a request later.
- **HTTP 500 Internal Server Error**:
    - Error: token invalid (null)
    - Error: token invalid (eyJhbGciOi...)
    - Error: token video (12345) does not match this video (23456)
    - Error: token client (123) does not match this client (234)

## Batch upload to migrate a vast number of videos from other services

When moving a huge collection of video files, batch upload is the best method. This option will be available soon. Please ask our [support team](mailto:support@gcore.com) for details.

We can help you to migrate from several storage types. We have compiled a list of storage types with instructions on how to get an HTTP link to access the file:

- <a href="https://support.google.com/drive/answer/2494822?hl=en&co=GENIE.Platform%3DDesktop&oco=0#zippy=%2Cshare-multiple-files" target="_blank">Google Drive</a> 
- Amazon S3 (step 1: <a href="https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteAccessPermissionsReqd.html" target="_blank">Setting permissions for website access</a>, step 2: <a href="https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html" target="_blank">Get the list of objects</a>)
- <a href="https://help.vimeo.com/hc/en-us/articles/12426150952593-Direct-links-to-video-files" target="_blank">Vimeo</a>
- <a href="https://docs.mux.com/guides/video/download-for-offline-editing#retrieving-the-url-to-the-master" target="_blank">Mux</a>
- <a href="https://help.dropbox.com/share/create-and-share-link" target="_blank">Dropbox</a>
- <a href="https://gcore.com/docs/storage/manage-s3-storage/manage-buckets-via-the-control-panel#manage-files" target="_blank">General SFTP or S3 storage with HTTP file access</a>

If your storage type isn’t mentioned in this list, ask our [support team](mailto:support@gcore.com) and we will be happy to help you with your video migration.
