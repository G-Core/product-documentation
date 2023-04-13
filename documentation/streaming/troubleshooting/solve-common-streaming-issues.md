---
title: solve-common-streaming-issues
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
---
  
  
  
  
  

We are covering some issues you may encounter when working with both Live and VOD streams, as well as steps you can take to troubleshoot them.

General troubleshooting steps
-----------------------------

For the most common issues, such as video not playing, taking a long time to start streaming, or looking blurry, these basic checks should help:

*   **Status page.** Check if the issue you are experiencing is related to any known issue or is an isolated one by visiting the [status page](https://status.gcore.com/).
*   **Source video.** Ensure that the source content is uploaded for streaming. If the same issue occurs in the source, re-upload the video or restart the stream.
*   **Stream URL and code.** Make sure to use the exact URL and embed code that appear in the Streaming settings.
*   **Streaming settings.** Make sure the stream is enabled. If configured to pull a stream, make sure the source URL is correct.
*   **Encoder settings.** Make sure you are using the [recommended settings](https://gcore.com/support/articles/360000604025/). If configured to push a stream, make sure the server URL and stream key are accurate.

Other things to try:

*   Clear the browsing data.
*   Disable any interfering browser extensions.
*   Ensure that the network connection is stable. Try connecting with or without a VPN.
*   Verify that the streaming ports are open on the firewall.
*   Update the browser or device OS.

Other common issues and solutions
---------------------------------

### Playback

**Stream does not appear on some devices**

_Possible cause_**:** Device is too old.  
_Suggested solution_**:** Streaming should work on most devices, but some devices may not be compatible. Try using a modern device with enough processing power and memory to successfully stream video.

**Stream returns an HTTP 404 error**

_Possible cause_**:** Transcoding is in progress.  
_Suggested solution_**:** Each video chunk may take several seconds to transcode. Allow 10 to 15 seconds for this to happen. Once the chunks have been transcoded, the stream should be ready to play.

_Possible cause_**:** Low Latency is enabled on the admin panel, but not on the control panel.  
_Suggested solution_**:** Contact our [support team](mailto:support@gcore.com) to activate this option.

**Stream returns an HTTP 502 error**

_Possible cause_**:** CDN resource settings have been changed from the preset settings.  
_Suggested solution_**:** Contact our [support team](mailto:support@gcore.com) to assist you in restoring the settings.

_Possible cause_**:** Token configuration is not synchronized.  
_Suggested solution_**:** Contact our [support team](mailto:support@gcore.com) to help you restore the settings.

**Current broadcast contains DVR chunks of the previous broadcast**

_Possible cause_**:** The broadcast is over, but the stream has not been stopped.  
_Suggested solution_**:** This is a normal behavior. To avoid this situation:

*   Stop the stream when the broadcast is finished.
*   Delete the DVR archive before starting a new broadcast.

**Low latency mode has a delay of more than 5 seconds**

_Possible cause_**:** The player does not support the DASH.JS library.  
_Suggested solution_**:** Our low latency solution has a latency of 4-5 seconds. If the delay is more than 5 seconds:

*   Make sure that the player supports the DASH.JS library.
*   Try testing your low latency stream at the open source [DASH.JS player](https://reference.dashif.org/dash.js/).

### Upload

**Video is not uploaded**

_Possible cause_**:** Upload has been interrupted by closing or reloading the window.  
_Suggested solution_**:** Try uploading again and be careful not to interrupt the process. If the size of the video is more than 500 MB, the upload will resume where it left off.

_Possible cause_**:** Not enough storage space to complete the upload.  
_Suggested solution_**:** Confirm in the Storage statistics that you have used up your storage. Contact our [support team](mailto:support@gcore.com) to increase the storage space.

**Upload to the control panel is interrupted by a session timeout (force logout)**

_Possible cause_**:** Video is too large to upload through UI.  
_Suggested solution_**:**

*   Upload during late night or early morning hours when there is less load on the queue.
*   Upload a small batch of videos (e.g., 10 at a time).
*   [Upload via API](https://gcore.com/support/articles/360002050917/).

**Upload is stuck in the Processed state for a long time**

_Possible cause_**:** Processing queue is too long or loaded with large videos.  
_Suggested solution_**:** Wait a while and then try uploading again.

### Player

**No sound when using Gcore player**

_Possible cause_**:** The audio is encoded with an unsupported codec.  
_Suggested solution_**:** Set the audio codec to AAC. Note that if you are using Adobe FMLE on Windows, you need to purchase an AAC encoder plugin in order to use the AAC audio format.

**Selected Gcore player does not render on the page**

_Possible cause_**:** Some parameters have been added to the URL in the embed code.  
_Suggested solution_**:** Contact our [support team](mailto:support@gcore.com) to troubleshoot the issue further.

**No playback controls on the Gcore player**

_Possible cause_**:** Disable Skin is active.  
_Suggested solution_**:** Turn this option off.

Open a support ticket
---------------------

If none of the above work or apply to your issue, contact our [support team](mailto:support@gcore.com) with the following information:

1.  Link to the stream
2.  Description of the issue and steps to reproduce
3.  List of steps taken to troubleshoot the issue
4.  Screenshot of the information shown in [http://iam.gcdn.co/info](http://iam.gcdn.co/info)
5.  Screenshot of the response to this command: curl [http://iam.gcdn.co/info/json](http://iam.gcdn.co/info/json)
6.  Screenshot of the speed test result using [http://iam.gcdn.co/info](http://iam.gcdn.co/info)
7.  HAR file. This [page](https://toolbox.googleapps.com/apps/har_analyzer/?lang=en) describes how to generate one in Chrome, Firefox, and Edge