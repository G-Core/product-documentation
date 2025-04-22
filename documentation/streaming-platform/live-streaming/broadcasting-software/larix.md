---
title: larix
displayName: Larix (Android/iOS)
published: true
order: 20
pageTitle: Live Stream Setup with Larix | Gcore
pageDescription: A step-by-step guide to pushing live streams via Larix.
---

# Larix

Larix is a free encoder for video recording, screencasting, and live streaming. It’s suitable for video game streaming, blogging, educational content, and more.

Larix links your mobile device (e.g., a smartphone or a tablet) to different streaming platforms (e.g., Gcore Video Streaming, YouTube, Twitch, etc.). It takes an image captured by a camera, converts it into a video stream, and then sends it to the streaming platform.

## Setup

1\. Install Larix on your mobile device. You find the download instructions on the <a href="https://softvelum.com/larix/" target="_blank">official website</a>.

2\. To get the server URL and stream key, go to the <a href="https://streaming.gcore.com/streaming/list" target="_blank">Streaming list</a>, open the **Live stream settings** you need, and copy the relevant value from the **URLs for the encoder** section.

For example, if you see these values on the **Live stream settings** page:

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/push-live-streams-software/push-live-streams-via-obs/11774973436177.png" alt="Live stream settings" width="50%">

Concatenate them to form the full RTMP URL for the stream:

    rtmp://vp-push-ix1.gvideo.co/in/400448?cdf2a7ccf990e464c2b…

3\. Open <a href="https://softvelum.com/larix/grove/" target="_blank">Larix Grove</a>, where you can create the configuration for the Larix app that you can share via QR code.
4\. In Larix Grove, scroll down to the **Connection** section.
5\. Enter the RTMP URL and a name for your connection.
6\. Click the QR-Code button to generate a QR code. You can scan this code with the Larix app on your mobile device to automatically configure the connection.
7\. Open the Larix app on your mobile device and tap the gear icon to open the settings.
8\. Tap **Larix Grove** and then tap **Scan Grove QR code**.
9\. Scan the QR code you generated in Larix Grove. The app will automatically configure the connection.
10\. Go back to the main screen of the Larix app and tap the big white button to start streaming.

## Configure the stream parameters for optimal performance

To ensure optimal streaming performance, we recommend configuring the stream parameters you will send to our server.

You can adjust these settings with <a href="https://softvelum.com/larix/grove/" target="_blank">Larix Grove</a>, where the configuration together with the connection URL is generated as a QR code. This allows you to easily share the configuration with team members.

After you changed the settings, click the **QR-Code** button to generate a new QR code for sharing.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/broadcasting-software/larix-grove.png" alt="Larix Grove">

### Camera parameters

If you need to reduce the original resolution (downscale), follow the instructions in this section.

If you need to increase the FPS to 60, make sure to also increase the bitrate accordingly for optimal stream quality (i.e., double it).

If no resolution change is required, you can skip this step.

-   **Resolution:** 1280×720
-   **Frame rate:** 30

### Video encoder parameters

-   **Video Bitrate:** 2000000 for 720p resolution or 4000000 for 1080p resolution.
-   **Keyframe Interval:** 60 (i.e., 2 seconds)

### Audio encoder parameters

-   **Audio Bitrate:** 128000
-   **Sample Rate**: 44100 or 48000
-   **Channels**: 2
