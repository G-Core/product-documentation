---
title: get-webhooks-from-the-streaming-service
displayName: Webhooks
published: true
order: 40
toc:
   --1--What is a webhook?: "what-is-a-webhook"
   --1--What is it used for?: "what-are-the-streaming-platform-webhooks-used-for"
   --1--Configure the webhook integration: "configure-the-webhook-integration"
   --1--Examples of available webhooks: "webhook-examples-of-all-streaming-platform-events"
---
  
  
  

What is a webhook?
------------------

A webhook is a free automated notification about an event in our service. You can receive notifications about the following events of our Streaming Platform:

*   A live stream has started or finished.
*   Recording of a live stream has started or paused.
*   Updates on processing of a live stream recording: a recording has started processing, partially processed, or completely processed.
*   Updates on broadcast statuses: pending, live, paused, or finished.
*   A video is uploaded to the Platform.
*   Updates on video processing: a video has started processing, partially processed, or completely processed.

Whenever any of these events happens, our server will create an HTTP POST request and notify you about it. You will receive the information in JSON format. Below is an example of a webhook triggered when a live stream starts.

{   
    "type": "stream",   
     "message": {   
           "stream": {   
             "id": 12345 **(stream ID in your control panel)**,   
             "live": true **(the Platform is receiving your stream)**,   
             "recording": false **(your stream is not being recorded)**   
           }   
      }   
}

What are the Streaming Platform webhooks used for?
--------------------------------------------------

Webhooks are used by apps integrated with the Streaming Platform. You can configure your app so that it will activate automatic workflows whenever it receives a webhook.

For example, users share videos in your app. When a user adds a new video, it is uploaded and processed through our Streaming Platform. Then you need to embed the video in your application. You set up the auto-posting: as soon as the video is processed, the Streaming Platform will send a webhook, and your app will post the video.

Configure the webhook integration
---------------------------------

1\. Prepare your HTTP server to receive webhooks.

2\. Contact us via chat or email [support@gcore.com](mailto:support@gcorelabs.com) and ask to enable the webhook integration. Specify your ID (personal client ID) and the URL of the server that will receive webhooks. You can find your ID in your [control panel](https://accounts.gcore.com/reports/dashboard).

<img src="https://support.gcore.com/hc/article_attachments/6873270568849/image.png" alt="image.png">

The message template: "Good afternoon! Please configure the Streaming Platform webhook integration for my account with ID..... The URL of my server to send webhooks to is ....".

3\. We will notify you when we configure the webhook integration.

We deliver webhooks for free from the IP range 92.223.123.0/24_._

We can send webhooks of one account only to one server. If your server is unavailable, undelivered webhooks won't be sent again. You will only receive a webhook of the next event.

Webhook examples of all Streaming Platform events 
--------------------------------------------------

Below are examples of all the webhooks that you can get from our service. Parameters are explained in round brackets.

**A live stream has started**

{   
  "type": "stream",   
  "message": {   
    "stream": {   
      "id": 12345 **(stream ID in your control panel)**,   
      "live": true **(the Platform is receiving your stream)**,   
      "recording": false **(your stream is not being recorded)**   
    }   
  }   
}

**A live stream is paused**

{   
  "type": "stream",   
  "message": {   
    "stream": {   
      "id": 12345 **(stream ID in your control panel)**,   
      "live": false **(the Platform is not receiving your stream)**,   
      "recording": false **(your stream is not being recorded)**   
    }   
  }   
} 

**Recording has started**

{  
  "type": "stream",   
  "message": {   
    "stream": {   
      "id": 12345 **(stream ID in your control panel)**,   
      "live": true **(the Platform is receiving your stream)**,   
      "recording": true **(your stream is being recorded)**   
    }   
  }   
}

**Recording has finished**

{   
  "type": "stream",   
  "message": {   
    "stream": {   
       "id": 12345 **(stream ID in your control panel)**,   
       "live": true **(the Platform is receiving your stream)**,   
       "recording": false **(your stream is not being recorded)**   
    }   
  }   
}

**A recording has started processing**

{   
  "type": "video",   
  "message": {   
    "video": {   
      "id": 12345 **(recording ID in your control panel)**,   
      "slug": "ZeC44gtQQ4E97N9S" **(video ID presented as a random set of characters, which prevents a video URL from stealing if the webhook is intercepted)**,   
      "name": "Stream Record: test, 2022-05-27 09:08:40 +0000 **("test" will be replaced with your stream name)**",   
      "duration": 19580 **(recording duration in seconds)**,   
      "status": "viewable",   
      "converted\_videos": \[   
        {   
          "name": "vod720n" **(720p video)**,   
          "status": " processing" **(the recording is being processed)**   
        },   
        {            
           "name": "vod480n" **(480p video)**,   
           "status": "processing" **(the recording is being processed)**   
        },   
        {   
          "name": "vod360n" **(360p video)**,   
          "status": "processing" **(the recording is being processed)**   
        },   
        {   
           "name": "vod240n" **(240p video)**,   
           "status": "processing" **(the recording is being processed)**   
        }   
      \]    
    }   
  }   
}

**A recording is partially processed**

{   
  "type": "video",   
  "message": {   
    "video": {   
      "id": 12345 **(recording ID in your control panel)**,   
      "slug": "ZeC44gtQQ4E97N9S" **(video ID presented as a random set of characters, which prevents a video URL from stealing if the webhook is intercepted)**,   
      "name": "Stream Record: test, 2022-05-27 09:08:40 +0000" **("test" will be replaced with your stream name)**,   
      "duration": 19580 **(recording duration in seconds)**,   
      "status": "viewable",   
      "converted\_videos": \[   
        {   
          "name": "vod720n" **(720p video)**,   
          "status": "complete" **(processing completed)**   
        },   
        {   
          "name": "vod480n" **(480p video)**,   
          "status": "processing" **(the recording is being processed)**   
        },   
        {   
          "name": "vod360n" **(360p video)**,   
          "status": "processing" **(the recording is being processed)**   
        },   
        {   
          "name": "vod240n" **(240p video)**,    
          "status": "processing" **(the recording is being processed)**   
        }   
      \]   
    }   
  }   
}

**A recording is completely processed**

{   
  "type": "video",   
  "message": {   
    "video": {   
      "id": 12345 **(recording ID in your control panel)**,   
      "slug": "ZeC44gtQQ4E97N9S" **(video ID presented as a random set of characters, which prevents a video URL from stealing if the webhook is intercepted)**,   
      "name": "Stream Record: test, 2022-05-27 09:08:40 +0000" **("test" will be replaced with your stream name)**,   
      "duration": 19580 **(recording duration in seconds)**,   
      "status": "ready",   
      "converted\_videos": \[   
        {   
          "name": "vod720n" **(720p video)**,   
          "status": "complete" **(processing completed)**   
        },   
        {   
           "name": "vod480n" **(480p video)**,   
           "status": "processing" **(processing completed)**   
        },  
        {   
          "name": "vod360n" **(360p video)**,   
          "status": "processing" **(processing completed)**   
        },   
        {   
          "name": "vod240n" **(240p video)**,    
          "status": "processing" **(processing completed)**   
        }   
      \]   
    }   
  }   
} 

**A broadcast status is updated to "Waiting to start"**

{   
  "type": "broadcast",   
  "message": {   
    "broadcast": {   
      "id": 12345 **(broadcast ID in your personal account)**,   
      "status": "pending" **(status "Waiting to start")**   
    }   
  }   
}

**A broadcast status is updated to "Live"**

{   
  "type": "broadcast",   
  "message": {   
    "broadcast": {   
      "id": 12345 **(broadcast ID in your personal account)**,   
      "status": "live" **(status "Live")**   
    }   
  }   
}

**A broadcast status is updated to "Finished"**

{   
  "type": "broadcast",   
  "message": {   
    "broadcast": {   
      "id": 12345 **(broadcast ID in your personal account)**,   
      "status": "finished" **(status "Finished")**   
    }   
  }   
}

**A broadcast status is updated to "Paused"**

{   
  "type": "broadcast",   
  "message": {   
    "broadcast": {   
      "id": 12345 **(broadcast ID in your personal account)**,   
      "status": "paused" **(status "Paused")**   
    }   
  }   
}

**A video is uploaded to the Platform**

{   
  "type": "video",   
  "message": {   
    "video": {   
      "id": 54321 **(video ID in your control panel)**,   
      "slug": "Lfsq14hKvLkNsExx" **(video ID presented as a random set of characters, which prevents a video URL from stealing if the webhook is intercepted)**,   
      "name": "SampleVideo" **(video name)**,   
      "duration": 170859 **(duration in seconds)**,   
      "status": "empty" **(the video has not been processed yet)**,   
      "converted\_videos": \[\]   
    }   
  }   
} 

**A video has started processing**

{   
  "type": "video",   
  "message": {   
    "video": {   
      "id": 784280 **(video ID in your control panel)**,   
      "slug": "Lfsq14hKvLkNsExx" **(video ID presented as a random set of characters, which prevents a video URL from stealing if the webhook is intercepted)**,   
      "name": "SampleVideo" **(video name)**,   
      "duration": 170859 **(duration in seconds)**,   
      "status": "pending" **(pending processing)**,   
      "converted\_videos": \[   
        {   
          "name": "vod720n" **(720p video)**,   
          "status": "processing" **(the video is being processed)**   
        },   
        {   
          "name": "vod480n" **(480p video)**,   
          "status": "processing" **(the video is being processed)**   
        },   
        {   
          "name": "vod360n" **(360p video)**,   
          "status": "processing" **(the video is being processed)**   
        },   
        {   
          "name": "vod240n" **(240p video)**,   
          "status": "processing" **(the video is being processed)**   
        }   
      \]   
    }   
  }   
}

**A video is partially processed**

{   
  "type": "video",   
  "message": {   
    "video": {   
      "id": 784280 **(video ID in your control panel)**,   
      "slug": "Lfsq14hKvLkNsExx" **(video ID presented as a random set of characters, which prevents a video URL from stealing if the webhook is intercepted)**,   
      "name": "SampleVideo" **(video name)**,   
      "duration": 170859 **(duration in seconds)**,   
      "status": "pending" **(pending processing)**,   
      "converted\_videos": \[   
        {   
          "name": "vod720n" **(720p video)**,   
          "status": "complete" **(processing completed)**   
        },   
        {   
          "name": "vod480n" **(480p video)**,   
          "status": "processing" **(the video is being processed)**   
        },   
        {   
          "name": "vod360n" **(360p video)**,   
          "status": "processing" **(the video is being processed)**   
        },   
        {   
          "name": "vod240n" **(240p video)**,   
          "status": "processing" **(the video is being processed)**   
        }   
      \]   
    }   
  }  
}

**A video is completely processed**

{   
  "type": "video",  
  "message": {   
    "video": {   
      "id": 784280 **(video ID in your control panel)**,   
      "slug": "Lfsq14hKvLkNsExx" **(video ID presented as a random set of characters, which prevents a video URL from stealing if the webhook is intercepted)**,   
      "name": "SampleVideo" **(video name)**,   
      "duration": 170859 **(duration in seconds)**,   
      "status": "pending" **(pending processing)**,   
      "converted\_videos": \[   
        {   
          "name": "vod720n" **(720p video)**,   
          "status": "complete" **(processing completed)**   
        },   
        {   
          "name": "vod480n" **(480p video)**,   
          "status": "complete" **(processing completed)**   
        },   
        {   
          "name": "vod360n" **(360p video)**,   
          "status": "complete" **(processing completed)**   
        },   
        {   
          "name": "vod240n" **(240p video)**,   
          "status": "complete" **(processing completed)**   
        }   
      \]   
    }   
  }  
}