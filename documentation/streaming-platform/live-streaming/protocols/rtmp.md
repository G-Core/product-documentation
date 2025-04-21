---
title: rtmp-rtmps
displayName: RTMP
published: true
order: 10
pageTitle: Guide to RTMP ingest | Gcore
pageDescription: A step-by-step tutorial on how to create and stop live streams using Gcore's interface or customer's environment.
---

# The Real Time Messaging Protocol

The Real Time Messaging Protocol (RTMP) is the most common way to stream to video streaming platforms. Gcore Live Streaming supports both RTMP and RTMPS.

<alert-element type="info" title="Info">

RTMP is limited to the H264 codec only. If you want to use other codecs, please <a href="https://gcore.com/docs/streaming-platform/live-streaming/protocols/srt" target="_blank">use SRT</a> instead.

We're planning to support H265/HVEC and other extensions from the Enhanced RTMP specification. Stay tuned for updates.

</alert-element>

## Push streams

Gcore Video Streaming provides you with two endpoints for pushing a stream, a default one and a backup one. The default endpoint is the one that is closest to your location. The backup endpoint is in a different location and used if the default one is unavailable.

By default, Gcore will route your stream to free ingest points with the lowest latency. If you need to set a fixed ingest point or if you need to set the main and backup ingest points in the same region (i.e., to not send streams outside the EU or US), please contact our support team.

### Obtain the server URLs and stream key

There are two ways to obtain the server URLs and stream key: via the Gcore Customer Portal or via the API.

#### Via the Gcore Customer Portal

1\. In the **Gcore Customer Portal**, navigate to **Streaming** > <a href="https://portal.gcore.com/streaming/streaming/list">**Live Streaming**</a>.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/live-stream-list.png" alt="List of live streams">

2\. Click on the stream you want to push to. This will open the **Live Stream Settings**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/live-stream-settings.png" alt="Live stream settings">

3\. Ensure that the **Ingest type** is set to **Push**.
4\. Ensure that the protocol is set to **RTMP** or **RTMPS** in the **URLs for encoder** section.
5\. Copy the **Server** URL and **Stream Key** from the **URLs for encoder** section.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/urls-for-encoder.png" alt="URLs for encoder section">

#### Via the API

You can also obtain the URL and stream key via the Gcore API. They endpoint returns the complete URLs for the default and backup ingest points, as well as the stream key.

Example of the API request:

```http
GET /streaming/streams/{stream_id}
```

Example of the API response:

```json
{
  "push_url": "rtmp://vp-push-anx2.domain.com/in/123?08cd54f0",
  "backup_push_url": "rtmp://vp-push-ed1.domain.com/in/123b?08cd54f0",
  ...
}
```

Read more in <a href="https://api.gcore.com/docs/streaming#tag/Streams/operation/post_streams_id" target="_blank">the API documentation</a>.

## Pull streams

Gcore Video Streaming can pull video data from your external server.

Main rules of pulling:

-   The URL of the stream to pull from must be **publicly available** and **return a 200 status** for all requests.
-   You can specify **multiple media servers** (separated with space characters) in the **URL** input field. The maximum length of all URLs is 255 characters and the round robin is used when polling the list of specified servers.
-   If a stream is closed (i.e., its connection is terminated) or there is no video data in the stream for 30 seconds, then the next attempt will be made in the next steps progressively (10s, 30s, 60s, 5min, 10min).
-   The stream will be deactivated after 24 hours of inactivity.
-   If you need to set an allowlist for access to the stream, please contact support to get an up-to-date list of networks.

### Setting up a pull stream

There are two ways to set up a pull stream: via the Gcore Customer Portal or via the API.

#### Via the Gcore Customer Portal

1\. In the **Gcore Customer Portal**, navigate to **Streaming** > <a href="https://portal.gcore.com/streaming/streaming/list">**Live Streaming**</a>.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/live-stream-list.png" alt="List of live streams">

2\. Click on the stream you want to pull from. This will open the **Live Stream Settings**.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/create-a-live-stream/live-stream-settings.png" alt="Live stream settings">

3\. Ensure that the **Ingest type** is set to **Pull**.
4\. In the **URL** field, insert a link to the stream from your media server.
5\. Click the **Save changes** button on the top right.

#### Via the API

You can also set up a pull stream via the Gcore API. The endpoint accepts the URL of the stream to pull from.

Example of the API request:

```http
PATCH /streaming/streams/{stream_id}
```

```json
{
  "stream": {
    "pull": true,
    "uri": "rtmp://example.com/path/to/stream",
    ...
  }
}
```

Read more in <a href="https://api.gcore.com/docs/streaming#tag/Streams/operation/patch_streams_id" target="_blank">the API documentation</a>.
