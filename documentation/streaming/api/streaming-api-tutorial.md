---
title: streaming-api-tutorial
displayName: Streaming API tutorial
published: true
order: 10
toc:
   --1--How integration works: "how-integration-works"
   --1--Basic operations: "basic-operations"
   --2--Stage 1. Setup: "stage-1-setup"
   --2--Stage 2. Test: "stage-2-test"
   --2--Stage 3. Live: "stage-3-live"
   --2--Stage 4. Stop: "stage-4-stop"
   --1--Special cases: "special-cases"
   --1--Other API methods: "other-api-methods"
   --2--Step 1. Create a stream: "step-1-create-a-stream"
   --2--Step 2. Create a broadcast: "step-2-create-a-broadcast"
   --2--Step 3. Enable the stream: "step-3-enable-the-stream"
   --2--Step 4. Send a webhook when the stream has started: "step-4-send-a-webhook-when-the-stream-has-started"
   --2--Step 5. Change broadcast status to Live: "step-5-change-the-broadcast-status-to-live"
   --2--Step 6. Send a webhook when the broadcast has transitioned to Live status: "step-6-send-a-webhook-when-the-broadcast-has-transitioned-to-live-status"
   --2--Step 7. Start recording: "step-7-start-recording"
   --2--Step 8. Send a webhook when stream recording has started: "step-8-send-a-webhook-when-stream-recording-has-started"
   --2--Step 9. Stop recording: "step-9-stop-recording"
   --2--Step 10. Send a webhook when stream recording has stopped: "step-10-send-a-webhook-when-stream-recording-has-stopped"
   --2--Step 11. Send a webhook when the recorded video is being processed: "step-11-send-a-webhook-when-the-recorded-video-is-being-processed"
   --2--Step 12. Change broadcast status to Finished: "step-12-change-broadcast-status-to-finished"
   --2--Step 13. Send a webhook when the broadcast has transitioned to Finished status: "step-13-send-a-webhook-when-the-broadcast-has-transitioned-to-finished-status"
   --2--Step 14. Disable the stream: "step-14-disable-the-stream"
   --2--Step 15. Send a webhook when the stream has ended: "step-15-send-a-webhook-when-the-stream-has-ended"
   --2--Step 16. Delete the broadcast: "step-16-delete-the-broadcast"
   --2--Step 17. Send a webhook when the recorded video is partially processed: "step-17-send-a-webhook-when-the-recorded-video-is-partially-processed"
   --2--Step 18. Send a webhook when the recorded video is completely processed: "step-18-send-a-webhook-when-the-recorded-video-is-completely-processed"
   --2--Step 19. Get video information: "step-19-get-video-information"
---
  
  
  
  
  
  
  

You can integrate your product to use the Streaming Platform for unlimited video streaming and hosting services. In this guide, we’ll take you through the API and webhook operations involved in integrating with the Streaming Platform.

How integration works
---------------------

Typically, your app presents users with an interface through which they can create and manage a stream. Each user action represents a request to an endpoint in the streaming API and a webhook. The following diagram shows the typical high-level sequence of the operations grouped into stages:

<img src="https://support.gcore.com/hc/article_attachments/12876274382481" alt="" width="555" height="1318">

You’ll need to have:

*   Your own video streaming interface created
*   A Gcore account with an active [Streaming](https://gcore.com/support/articles/4406059230737/) subscription
*   An [authentication](https://apidocs.gcore.com/streaming) set up using the user credentials
*   A [webhook](https://gcore.com/support/articles/6874132929553/) set up

Basic operations
----------------

### Stage 1. Setup

The user of your app creates a stream at this stage.

  
  
  

### Step 1. Create a stream

Use the [post\_streams\_id](https://apidocs.gcore.com/streaming) method to create a stream object in the Streaming Platform.

Sample request payload:

*   To prevent errors due to the quota for concurrent active sessions, set the **active** property to **false**.
*   Choose the right transcoding region based on the user’s location.

{
    "stream": {
        "name": "test\_stream",
        "pull": false,
        "uri": null,
        "active": false,
        "transcoding\_region": "ix1",
        "auto\_record": false,
        "webrtc": false,
        "dvr\_enabled": false,
        "cdn\_id": 53949,
        "projection": "regular"
    }
}

Sample response payload:

*   If successful, the method returns information about the stream that you created.
*   Save the returned **id** and other necessary data to use later.

{
    "id": 320423,
    "active": false
    ...
}

### Step 2. Create a broadcast

Use the [post\_broadcasts](https://apidocs.gcore.com/streaming) method to create a broadcast object.

Sample request payload:

*   Set **stream\_ids** property to the returned id from Step 1 to bind the broadcast and stream together.
*   Set **status** property to **pending**.

{
    "broadcast": {
        "name": "test\_broadcast",
        "status": "pending",
        "share\_url": "",
        "custom\_iframe\_url": "",
        "show\_dvr\_after\_finish": false,
        "pending\_message": "Please wait ...",
        "ad\_id": null,
        "stream\_ids": \[320423\]
        ...
    }
}

Sample response payload:

*   If successful, the method returns information about the broadcast that you created.
*   Save the returned **id** and other necessary data to use later.

{
   "id": 192470,
   "status": "pending",
   "stream\_ids": \[320423\],
   ...
}

### Step 3. Enable the stream

Having received a successful response from your app, the user can now publish the stream. Use the [patch\_streams\_id](https://apidocs.gcore.com/streaming) method to activate the stream.

Sample request payload:

{
   "stream": {
      "active": true
   }
}

Sample response payload:

{
    "id": 320423,
    "active": true
    ...
}

### Step 4. Send a webhook when the stream has started

The Streaming Platform sends a webhook that contains **"live": true** to your subscribed endpoint.

Sample webhook payload:

{
   "type": "stream",
   "message": {
      "stream": {
        "id": 320423,
        "live": true,
        "recording": false
      }
   }
}

### Stage 2. Test

The user tests the broadcast at this stage.

  

### Step 5. Change the broadcast status to _Live_

Use the [patch\_broadcasts\_id](https://apidocs.gcore.com/streaming) method to update the broadcast status to _Live_.

Sample request payload:

{
   "broadcast": {
      "status": "live"
   }
}

Sample response payload:

{
   "id": 192470,
   "status": "live"
   ...
}

### Step 6. Send a webhook when the broadcast has transitioned to Live status

The Streaming Platform sends a webhook that contains **"status": live** to your subscribed endpoint.

Sample webhook payload:

{
   "type": "broadcast",
   "message": {
      "broadcast": {
        "id": 192470,
        "status": "live"
    }
  }
}

### Stage 3. Live

The user starts streaming at this stage. The broadcast is visible to the audience.

  

### Step 7. Start recording

Use the [put\_streams\_id\_start\_recording](https://apidocs.gcore.com/streaming) method to begin recording.

If the returned HTTP status code is 204, the request is successful.

### Step 8. Send a webhook when stream recording has started

The Streaming Platform sends a webhook that contains **"recording": true** to your subscribed endpoint.

Sample webhook payload:

{
   "type": "stream",
   "message": {
      "stream": {
        "id": 320423,
        "live": true,
        "recording": true
    }
  }
}

### Stage 4. Stop

The user stops streaming at this stage.

  
  
  
  
  
  
  
  
  
  

### Step 9. Stop recording

Use the [put\_streams\_id\_stop\_recording](https://apidocs.gcore.com/streaming) method to stop recording

The response to this request contains information about the recorded video.

Sample response payload:

{
    "id": 803111,
    "name": "Stream Record: test\_stream, 2022-06-03 13:25:16 +0000",
    "recording\_started\_at": "2022-06-03T13:24:29.000Z",
    "created\_at": "2022-06-03T13:25:16.000Z",
    ...
}

### Step 10. Send a webhook when stream recording has stopped

The Streaming Platform sends a webhook that contains **"recording": false** to your subscribed endpoint.

Sample webhook payload:

{
   "type": "stream",
   "message": {
      "stream": {
        "id": 320423,
        "live": true,
        "recording": false
    }
  }
}

### Step 11. Send a webhook when the recorded video is being processed

The Streaming Platform sends a webhook that contains **"status": "pending"** to your subscribed endpoint.

Sample webhook payload:

{
  "type": "video",
  "message": {
    "video": {
      "id": 803111,
      "slug": "MTdaAbW7IzBsjgvy",
      "name": "Stream Record: test\_stream, 2022-06-03 13:25:16 +0000",
      "duration": 48410,
      "status": "pending",
      ...
      \]
    }
  }
}

### Step 12. Change broadcast status to _Finished_

Use the [patch\_broadcasts\_id](https://apidocs.gcore.com/streaming) method to update the broadcast status to _Finished_.

Sample request payload:

{
   "broadcast": {
      "status": "finished"
   }
}

Sample response payload:

{
   "id": 192470,
   "status": "finished"
   ...
}

### Step 13. Send a webhook when the broadcast has transitioned to _Finished_ status

The Streaming Platform sends a webhook that contains **"status": "finished"** to your subscribed endpoint.

Sample webhook payload:

{
   "type": "broadcast",
   "message": {
      "broadcast": {
        "id": 192470,
        "status": "finished"
    }
  }
}

### Step 14. Disable the stream

Use the [patch\_streams\_id](https://apidocs.gcore.com/streaming) method to deactivate the stream.

Sample request payload:

{
   "stream": {
      "active": false
   }
}

Sample response payload:

{
   "id": 320423,
   "live": true,
   "transcoded\_qualities": \["360n", "480n", "720n"\],
   "transcoding\_speed": 1.0,
   "active": false,
   "rtmp\_play\_url": \[ "rtmp://pull-ix1.gvideo.co:1939/in/320423?4a5d279b6371c7bcc5ce47afb0f74637",
"rtmp://pull-ix1.gvideo.co:1939/out/58725\_320423\_360n?4a5d279b6371c7bcc5ce47afb0f74637?vhost=out",
"rtmp://pull-ix1.gvideo.co:1939/out/58725\_320423\_480n?4a5d279b6371c7bcc5ce47afb0f74637?vhost=out",
"rtmp://pull-ix1.gvideo.co:1939/out/58725\_320423\_720n?4a5d279b6371c7bcc5ce47afb0f74637?vhost=out"
    \],
   "transcoding\_enabled": true,
   ...
}

### Step 15. Send a webhook when the stream has ended

The Streaming Platform sends a webhook that contains **"live": false** to your subscribed endpoint.

Sample webhook payload:

{
   "type": "stream",
   "message": {
      "stream": {
        "id": 320423,
        "live": false,
        "recording": false
    }
  }
}

### Step 16. Delete the broadcast

Use the [delete\_broadcasts\_id](https://apidocs.gcore.com/streaming) method to delete the broadcast.

If the returned HTTP status code is 204, the request is successful.

### Step 17. Send a webhook when the recorded video is partially processed

This indicates that one quality version of the video currently being processed is ready for the viewers to watch.

The Streaming Platform sends a webhook that contains **"status": "viewable"** to your subscribed endpoint.

Sample webhook payload:

{
   "type": "video",
   "message": {
      "video": {
        "id"": 803111,
        "slug": "MTdaAbW7IzBsjgvy",
        "name": "Stream Record: test\_stream, 2022-06-03 13:25:16 +0000",
        "duration": 48410,
        "status": "viewable",
        "converted\_videos": \[
          {
            "name": "vod720n",
            "status": "complete"
          },
          {
            "name": "vod480n",
            "status": "processing"
          },
          {
            "name": "vod360n",
            "status": "processing"
          },
          {
            "name": "vod240n",
            "status": "processing"
        }
      \]
    }
  }
}

### Step 18. Send a webhook when the recorded video is completely processed

This indicates that all quality versions of the video are ready for viewers to watch.

The Streaming Platform sends a webhook that contains **"status": "ready"** to your subscribed endpoint.

Sample webhook payload:

{
   "type": "video",
   "message": {
      "video": {
        "id": 803111,
        "slug": "MTdaAbW7IzBsjgvy",
        "name": "Stream Record: test\_stream, 2022-06-03 13:25:16 +0000",
        "duration": 48410,
        "status": "ready",
        "converted\_videos": \[
          {
            "name": "vod720n",
            "status": "complete"
          },
          {
            "name": "vod480n",
            "status": "complete"
          },
          {
            "name": "vod360n",
            "status": "complete"
          },
          {
            "name": "vod240n",
            "status": "complete"
        }
      \]
    }
  }
}

### Step 19. Get video information

Use the [get\_api\_videos\_id](https://apidocs.gcore.com/streaming) method to retrieve detailed information about the video.

Sample response payload:

{
    "id": 803111,
    "name": "Stream Record: test\_stream, 2022-06-03 13:25:16 +0000",
    "client\_id": 58725,
    "duration": 48410,
    "stream\_id": 320423,
    "recording\_started\_at": "2022-06-03T13:24:29.000Z",
    "created\_at": "2022-06-03T13:25:16.000Z",
    "sprite": "https://s-ed1.cloud.gcore.lu/videoplatform/sprites/58725/803111\_803111.mp4\_sprite.jpg",
    ...
}

Special cases
-------------

### Reuse of a stream

The user can reuse the same stream for each broadcast. In this case, you don’t need to create a new one. Just update the stream using the [patch\_streams\_id](https://apidocs.gcore.com/streaming) method with the appropriate transcoding region.

Sample request payload:

{
   "stream": {
      "transcoding\_region": dt1
   }
}

Sample response payload:

{
   "id": 320423,
   "live": false,
   "backup\_live": false,
   "transcoded\_qualities": \["360n", "480n", "720n"\],
   "transcoding\_speed": 1.0,
   "push\_url": "rtmp://vp-push-dt1.gvideo.co/in/320423?6460e735eda6b61bd4c99e02abf0c8df",
   "backup\_push\_url": "rtmp://vp-push-ix1.gvideo.co/in/320423b?6460e735eda6b61bd4c99e02abf0c8df",
   "push\_url\_srt": "srt://vp-push-dt1-srt.gvideo.co:5001?streamid=320423#6460e735eda6b61bd4c99e02abf0c8df",
   "backup\_push\_url\_srt": "srt://vp-push-ix2-srt.gvideo.co:5001?streamid=320423b#6460e735eda6b61bd4c99e02abf0c8df",
   ...
}

### Interruption during streaming

*   The Streaming Platform sends a webhook when the stream is briefly interrupted.

Sample webhook payload:

{
   "type": "stream",
   "message": {
      "stream": {
        "id": 320423,
        "live": false,
        "recording": false
    }
  }
}

*   You can also check for the stream status using the [get\_streams\_id](https://apidocs.gcore.com/streaming) method. If the response contains **"active": false** and the stream wasn’t manually interrupted, then you can call the [patch\_broadcasts\_id](https://apidocs.gcore.com/streaming) method to transition the broadcast to _Paused_ status.

Sample request payload:

{
   "broadcast": {
     "status": "paused"
  }
}

Sample response payload:

{
   "id": 192470,
   "status": "paused",
   ...
}

*   You can also [stop the recording](https://apidocs.gcore.com/streaming) when the user has an interruption (even for a couple of minutes) during streaming. Your app can prompt the user to start the stream again. The stream recording will be broken into two files: data recorded up to the interruption and data recorded when the user renews streaming.

The Streaming Platform can’t currently reconnect without interrupting the recording if the stream gets temporary disruption. But we plan to implement this in the future.

### Stream deletion

You can delete streams that have been inactive for some time and are associated with a deleted user account. To do this, use the [delete\_api\_videos\_id](https://apidocs.gcore.com/streaming) method.

If the returned HTTP status code is 204, the request is successful.

Other API methods
-----------------

Check out our Streaming API [documentation](https://apidocs.gcore.com/streaming) for more methods that might come in handy for other use cases.