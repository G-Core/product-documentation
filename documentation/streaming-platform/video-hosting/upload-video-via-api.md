---
title: upload-video-via-api
displayName: Upload video to VOD storage
published: true
order: 60
toc:
   --1--Pull: "pull"
   --1--Push: "push"
---
# Upload Video via API

There are two ways to upload VOD to VOD storage: pull or push.

## Pull

Specify *origin_url* in "Create video" request. The video will be downloaded to the storage.

## Push

Requires three steps:

1\. Send <a href="https://apidocs.gcore.com/streaming#operation/post_api_videos" target="_blank">Create video</a> request, don't specify origin\_url parameter.

2\. Send <a href="https://apidocs.gcore.com/streaming#operation/get_api_videos_id_upload" target="_blank">Get URL and token to upload video</a> request. To send it, use the video ID parameter from the previous request.

**Note**: Token is valid for 5 minutes. This is enough because token is involved only in request "Submit video for download". As soon as the video is sent, the token is no longer needed, and processing occurs without it.

3\. Write a script using the <a href="https://tus.io/" target="_blank">tus standard</a>. Here is a <a href="https://github.com/tus/tus-js-client" target="_blank">script example</a>.

Keep in mind that the following metadata must be specified for the uploading process to go smoothly:

- video name (filename),
- client ID (client_id),
- video ID (video_id),
- token.

Use your script and the data from the <a href="https://apidocs.gcore.com/streaming#tag/Videos/operation/get_api_videos_id_upload" target="_blank">Get URL and token to upload video</a> request to upload your videos to our server.