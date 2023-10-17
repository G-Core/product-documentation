---
title: solve-common-streaming-platform-issues
displayName: Streaming issues
published: true
order: 10
toc:
   --1--General troubleshooting steps: "general-troubleshooting-steps"
   --1--Other common issues and solutions: "other-common-issues-and-solutions"
   --2--Playback: "playback"
   --2--Upload: "upload"
   --2--Player: "player"
   --1--Open a support ticket: "open-a-support-ticket"
pageTitle: Solving Streaming Platform Issues | Gcore
pageDescription: An explanation of common basic checks to address issues that may arise when working with a streaming platform.
---

# Solve common Streaming Platform issues
  
We are covering some issues you may encounter when working with both Live and VOD streams, as well as steps you can take to troubleshoot them.

## General troubleshooting steps

For the most common issues, such as video not playing, taking a long time to start streaming, or looking blurry, these basic checks should help:

- **Status page**. Check if the issue you are experiencing is related to any known issue or is an isolated one by visiting the <a href="https://status.gcore.com" target="_blank">status page</a>.
- **Source video**. Ensure that the source content is uploaded for streaming. If the same issue occurs in the source, re-upload the video or restart the stream.
- **Stream URL and code**. Make sure to use the exact URL and embed code that appear in the Streaming settings.
- **Streaming settings**. Make sure the stream is enabled. If configured to pull a stream, make sure the source URL is correct.
- **Encoder settings**. Make sure you are using the <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/what-initial-parameters-of-your-live-streams-and-videos-we-can-accept" target="_blank">recommended settings</a>. If configured to push a stream, make sure the server URL and stream key are accurate.

Other things to try:

- Clear the browsing data.
- Disable any interfering browser extensions.
- Ensure that the network connection is stable. Try connecting with or without a VPN.
- Verify that the streaming ports are open on the firewall.
- Update the browser or device OS.

## Other common issues and solutions

### Playback

**Stream does not appear on some devices**

*Possible cause*: Device is too old.  
*Suggested solution*: Streaming should work on most devices, but some devices may not be compatible. Try using a modern device with enough processing power and memory to successfully stream video.

**Stream returns an HTTP 404 error**

*Possible cause*: Transcoding is in progress.  
*Suggested solution*: Each video chunk may take several seconds to transcode. Allow 10 to 15 seconds for this to happen. Once the chunks have been transcoded, the stream should be ready to play.

*Possible cause*: Low Latency is enabled on the admin panel, but not on the control panel.  
*Suggested solution*: Contact our [support team](mailto:support@gcore.com) to activate this option.

**Stream returns an HTTP 502 error**

*Possible cause*: CDN resource settings have been changed from the preset settings.  
*Suggested solution*: Contact our [support team](mailto:support@gcore.com) to assist you in restoring the settings.

*Possible cause*: Token configuration is not synchronized.  
*Suggested solution*: Contact our [support team](mailto:support@gcore.com) to help you restore the settings.

**Current broadcast contains DVR chunks of the previous broadcast**

*Possible cause*: The broadcast is over, but the stream has not been stopped.  
*Suggested solution*: This is a normal behavior. 

To avoid this situation:

- Stop the stream when the broadcast is finished.
- Delete the DVR archive before starting a new broadcast.

**Low latency mode has a delay of more than 5 seconds**

*Possible cause*: The player does not support the DASH.JS library.  
*Suggested solution*: Our low latency solution has a latency of 4-5 seconds. If the delay is more than 5 seconds:

- Make sure that the player supports the DASH.JS library.
- Try testing your low latency stream at the open source <a href="https://reference.dashif.org/dash.js" target="_blank">DASH.JS player</a>.

### Upload

**Video is not uploaded**

*Possible cause*: Upload has been interrupted by closing or reloading the window.  
*Suggested solution*: Try uploading again and be careful not to interrupt the process. If the size of the video is more than 500 MB, the upload will resume where it left off.

*Possible cause*: Not enough storage space to complete the upload.  
*Suggested solution*: Confirm in the Storage statistics that you have used up your storage. Contact our [support team](mailto:support@gcore.com) to increase the storage space.

**Upload to the control panel is interrupted by a session timeout (force logout)**

*Possible cause*: Video is too large to upload through UI.  
*Suggested solution*:

- Upload during late night or early morning hours when there is less load on the queue.
- Upload a small batch of videos (e.g., 10 at a time).
- <a href="https://gcore.com/docs/streaming-platform/video-hosting/upload-video-via-api" target="_blank">Upload via API</a>.

**Upload is stuck in the Processed state for a long time**

*Possible cause*: Processing queue is too long or loaded with large videos.  
*Suggested solution*: Wait a while and then try uploading again.

### Player

**No sound when using Gcore player**

*Possible cause*: The audio is encoded with an unsupported codec.  
*Suggested solution*: Set the audio codec to AAC. Note that if you are using Adobe FMLE on Windows, you need to purchase an AAC encoder plugin in order to use the AAC audio format.

**Selected Gcore player does not render on the page**

*Possible cause*: Some parameters have been added to the URL in the embed code.  
*Suggested solution*: Contact our [support team](mailto:support@gcore.com) to troubleshoot the issue further.

**No playback controls on the Gcore player**

*Possible cause*: Disable Skin is active.  
*Suggested solution*: Turn this option off.

## Open a support ticket

If none of the above work or apply to your issue, contact our [support team](mailto:support@gcore.com) with the following information:

1.  Link to the stream.
2.  Description of the issue and steps to reproduce.
3.  List of steps taken to troubleshoot the issue.
4.  Screenshot of the information shown in http://iam.gcdn.co/info.
5.  Screenshot of the response to this command: 

```
curl http://iam.gcdn.co/info/json
```
6.  Screenshot of the speed test result using http://iam.gcdn.co/info.
7.  HAR file. This <a href="https://toolbox.googleapps.com/apps/har_analyzer/?lang=en" target="_blank">page</a> describes how to generate one in Chrome, Firefox, and Edge.