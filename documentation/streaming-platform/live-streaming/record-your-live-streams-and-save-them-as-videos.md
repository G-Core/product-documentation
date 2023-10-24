---
title: record-your-live-streams-and-save-them-as-videos
displayName: Record
published: true
order: 50
toc:
   --1--What is the Record feature: "what-is-the-record-feature"
   --1--Enable the feature: "enable-the-record-feature"
   --1--Record a live stream: "how-to-record-a-live-stream"
   --2--Via Сontrol panel: "how-to-record-your-live-stream-via-the-control-panel"
   --2--Via API: "how-to-record-your-live-stream-via-api"
   --1--Where records are kept: "where-the-records-are-kept"
pageTitle:  Overview of Live Streams Recording | Gcore
pageDescription: A step-by-step guide on how to record your live streams and where to get the recordings.    
---
# Record your live streams and save them as videos
  
## What is the Record feature

Record is a free feature that allows you to record your live streams and store them in the Streaming storage. You can automatically record entire streams or manually record only desired fragments.

## Enable the Record feature

Please, send us the request to activate the option via [support@gcore.com](mailto:support@gcore.com) or the chat window in the bottom-right corner of our website. Specify your ID in the request so that we can identify your account. You can find it on the main page of your control panel.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos/9612975911185.png" alt="Enable the Record feature" width="80%">

The message template: *"Good afternoon! Please enable the Record feature for an account with ID … (your ID)"*.

We will notify you when we activate the Record feature. After that, you will be able to work with recordings.

## How to record a live stream

### How to record your live stream via the Control panel

To record a live stream manually:

1\. Start a live stream in your encoder.

2\. Open the settings of the desired live stream in the Control panel.

3\. Press the **Start record** button.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos/9612975915665.png" alt="Start record button" width="80%">

After 5–10 seconds, the recording will start. You will see the timer and the **Stop record** button.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos/9612975948817.png" alt="recording" width="50%">

In cases of accidentally interrupting the live stream (bad internet connection, broken cable, etc.), recording will be continued when the live stream resumes. The recording will be saved as one video if the interruption is less than one minute. The recording will be divided into several videos if the interruptions are more than one minute.

4\. If you want to record not the whole live stream, but a certain fragment of it, press the **Stop record** button at the desired moment. The fragment will be saved. Please note: it must be 10 seconds or longer.

If you want to record the whole live stream, don’t press the **Stop** button. The recording will stop automatically. Please note: recordings longer than 4 hours will be divided into fragments of 4 hours each—this is the optimal fragment size for video processing.

After stopping and processing, the recording will be saved in the Streaming Storage.

### How to record your live stream via API

When <a href="https://api.gcore.com/docs/streaming" target="_blank">creating or editing</a> the stream via API, to enable auto recording, change the parameter in the API request in the following way:

```
auto_record: true
```

The recording will be saved in the Streaming Storage.

## Where the records are kept

After you record a stream, the recording is saved in the Streaming’s storage. To get it:

1. Open the **Videos** tab.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos/9612975963921.png" alt="Videos tab" width="80%">

2. Go to the recording settings to the **Export** tab. Here you can copy the iFrame code to embed the recording on your website and download the recording of the quality you want.

<img src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/record-your-live-streams-and-save-them-as-videos/9612950210193.png" alt="Export tab" width="80%">