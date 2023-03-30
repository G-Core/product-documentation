---
title: upload-video-via-api
displayName: Upload video to VOD storage
published: true
order: 60
toc:
    --1--Pull: "pull"
    --1--Push: "push"
---
There are two ways to upload VOD to VOD storage: pull or push.

Pull
----

Specify origin\_url in Create video request. The video will be downloaded to the storage.

Push
----

Requires three steps:

1\. Send [Create video](https://apidocs.gcore.com/streaming#operation/post_api_videos) request, don't specify origin\_url parameter.

2\. Send [Get URL and token to upload video](https://apidocs.gcore.com/streaming#operation/get_api_videos_id_upload) request. To send it, use the video ID parameter from the previous request.

**Note.** Token is valid for 5 minutes. This is enough because token is involved only in request «Submit video for download». As soon as the video is sent, the token is no longer needed, and processing occurs without it.

3\. Write a script using the tus standard: [https://tus.io/](https://tus.io/). Here is a script example: [https://github.com/tus/tus-js-client](https://github.com/tus/tus-js-client).

Keep in mind that the following metadata must be specified for the uploading process to go smoothly:

*   *   video name (filename),
    *   client ID (client\_id),
    *   video ID (video\_id),
    *   token.

Use your script and the data from the [Get URL and token to upload video](https://apidocs.gcore.com/streaming#tag/Videos/operation/get_api_videos_id_upload) request to upload your videos to our server.