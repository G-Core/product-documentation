---
title: vod-issues
displayName: VOD issues
published: true
order: 40
pageTitle: Solving VOD Issues | Gcore
pageDescription: An explanation of common basic checks to address issues that may arise when working with VOD.
---

# VOD issues

Common issues you may encounter when working with VOD, as well as steps you can take to troubleshoot them.

## Video is not uploaded

_Possible cause_: Upload has been interrupted by closing or reloading the window.  
_Suggested solution_: Try uploading again and be careful not to interrupt the process. If the size of the video is more than 500 MB, the upload will resume where it left off.

_Possible cause_: Not enough storage space to complete the upload.  
_Suggested solution_: Confirm in the Storage statistics that you have used up your storage. Contact our [support team](mailto:support@gcore.com) to increase the storage space.

## Upload to the Gcore Customer Portal is interrupted by a session timeout (force logout)

_Possible cause_: Video is too large to upload through UI.  
_Suggested solution_:

-   Upload during late night or early morning hours when there is less load on the queue.
-   Upload a small batch of videos (e.g., 10 at a time).
-   <a href="https://gcore.com/docs/streaming-platform/video-hosting/upload-video-via-api" target="_blank">Upload via API</a>.

## Upload is stuck in the Processed state for a long time

_Possible cause_: Processing queue is too long or loaded with large videos.  
_Suggested solution_: Wait a while and then try uploading again.
