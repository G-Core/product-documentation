---
title: insert-html-overlays-in-live-streams
displayName: Overlay
published: true
order: 65
toc:
   --1--Overlays: "what-is-an-overlay"
   --1--Example: "overlay-example"
   --1--Gcore overlays: "gcore-supports-html-overlays"
   --1--Gcore vs. OBS: "comparison-of-gcore-overlays-and-obs-studio-overlays"
   --1--Configure via API: "configure-gcore-overlays-via-api"
   --2--Get the list: "get-all-overlays"
   --2--Create: "create-overlays"
   --2--Change: "change-overlays"
   --2--Delete: "delete-an-overlay"
pageTitle: Enhance Streams with Gcore Overlays | Gcore 
pageDescription: Explore Gcore's API-powered overlays for live streams and know how to manage overlays seamlessly across multiple streams.
---
# Insert an overlay (HTML widgets) in your live stream

## What is an overlay?

An overlay (or an HTML widget) is a graphic placed over the stream footage. Overlays include webcam pop-up, chat, alert, advertisement banner, and time or weather widgets. Streamers from different industries (games, education, news, sports events) use overlays to enhance their streams’ visual appeal and functionality.

There are two approaches to implementing overlays:

1. **Overlays are embedded OVER the live stream in the player**. In this case, you get two “layers”: the lower one is the video stream, and the upper one is the overlay shown by the particular player.

2. **Overlays are embedded INTO the live stream**. In this case, the overlay is part of the live stream.

The drawback of the first approach is that if you change the player, the overlay will be lost. In the second case, the overlay will be shown no matter the player used.

## Overlay example

In the example below, you can see the game score widget in the upper left corner, the weather widget in the upper right corner, the poll widget in the lower right corner, and the time and date widget in the lower left corner.

<img loading="lazy" src="https://assets.gcore.pro/docs/streaming-platform/live-streaming/insert-html-overlays-in-live-streams/coffee_run_overlays.gif" alt="Example of Gcore overlay">

## Gcore supports HTML overlays

Gcore Streaming Platform now supports overlays embedded into the live stream, which can be managed using the API. Contact support (via [email](maito:support@gcore.com) or chat—click the chat icon on the bottom right of our webpages) or your personal manager to enable the ability to send API requests to the overlay feature endpoints.

The main features of overlays via API are:

- Use more than one overlay per live stream
- Size options: small overlays or overlays stretched over a full frame
- Transparent areas in overlays
- 1 FPS frequency update
- Automatic size scaling for <a href="https://gcore.com/docs/streaming-platform/live-streams-and-videos-protocols-and-codecs/how-we-optimize-live-stream-and-video-performance-by-creating-different-bitrates" target="_blank">adaptive bitrate</a> qualities
- Place overlays in any area of the screen

## Comparison of Gcore overlays and OBS studio overlays

OBS has functionality for using overlays. Let’s compare it to Gcore’s overlay feature: 

<table>
<thead>
<tr>
<td></td>
<td><b>OBS</b></td>
<td><b>Gcore</b></td>
</tr>
</thead>
<tbody>
<tr>
<td><b>Scalability*</b></td>
<td>1 live stream</td>
<td>1000 live streams and beyond</td>
</tr>
<tr>
<td><b>Animated overlays**</b></td>
<td>Yes</td>
<td>No</td>
</tr>
</tbody>
</table>

*While using OBS overlays, you need to keep the OBS app open. Computational resources are enough for only one live stream with overlay, which cannot be scaled to multiple live streams. While using Gcore overlays, you embed the overlay into a live stream. The widget is automatically available everywhere (for Gcore’s player, <i>.m3u8</i> link, and <i>.mpd</i> link) and scales to any number of live streams. We scale the service automatically—you don't need to do anything, just start as many streams as you need. 

**OBS allows you to use animated widgets of different complexity within a single stream. We allow the overlay in 1000+ streams, but the Frame rate (FPS) will be 1 second. Therefore, animations will freeze. 

## Configure Gcore overlays via API

We support the following types of overlays: times and clocks, weather, statistics, exchange rates, and banner ads. For the graphic component of your overlay, you can use the following methods:

- Create your own (e.g., with the <a href="https://www.canva.com/create/twitch-overlays/" target="_blank">Free Twitch overlay maker from Canva</a>)
- Use a template (e.g., <a href="https://www.barnardos.org.uk/ready-player-b/streamer-toolkit" target="_blank">Bernardo’s Streamer Toolkit</a>)
- Use ready overlay systems (e.g., <a href="https://www.donationalerts.com/" target="_blank">DonationAlerts</a>, <a href="https://tracker.gg/overlays" target="_blank">Stream Overlays from Tracker Network</a>)

**Note**: Before using overlays, [ask tech support](mailto:support@gcore.com) or your personal manager to enable the feature for your account. Then, set the ```html_overlay``` attribute to ```true``` for your live stream and specify the array of live streams.

For detailed information, refer to our <a href="https://api.gcore.com/docs/streaming#tag/Overlays" target="_blank">API documentation</a>.

### Get all overlays

The <a href="https://api.gcore.com/docs/streaming#tag/Overlays/operation/get_overlays" target="_blank">API method</a> returns a list of HTML overlay widgets attached to a live stream.

Example of the request:

```
curl -L -X GET 'https://api.gcore.com/streaming/streams/12345/overlays' \
-H 'Authorization: APIKey 1234$0d1659...' \
-H 'Content-Type: application/json' \
```

In response, you will receive an array of overlays. Example of the response:

```
[
    {
        "id": 1,
        "stream_id": 12345,
        "url": "http://domain.tld/myoverlay1.html",
        "width": 120,
        "height": 40,
        "x": 10,
        "y": 10,
        "stretch": false,
        "created_at": "2023-09-20T00:01:01.000Z",
        "updated_at": "2023-10-01T12:01:01.000Z"
    },
    {
    }
]
```

### Create overlays

The <a href="https://api.gcore.com/docs/streaming#tag/Overlays/operation/post_overlays" target="_blank">API method</a> lets you insert overlays into your live stream. Please review the requirements for overlays to work correctly in the <a href="https://api.gcore.com/docs/streaming#tag/Overlays/operation/post_overlays" target="_blank">API documentation</a>.

Example of the request:

```
curl -L -X POST https://api.gcore.com/streaming/streams/12345/overlays \
-H 'Authorization: APIKey 1234$0d1659...' \
-H 'Content-Type: application/json' \
-d '{
    "url": "http://domain.tld/myoverlay1.html",
    "width": "120",
    "height": "40",
    "x": "30",
    "y": "30",
    "stretch": "false",      
}'
```

Example of the response:

```
{
    "url": "http://domain.tld/myoverlay1.html",
    "width": 120,
    "height": 40,
    "x": 30,
    "y": 30,
    "stretch": false,
    "id": 1,
    "stream_id": 12345,
    "created_at": "2023-09-20T00:01:01.000Z",
    "updated_at": "2023-10-01T12:01:01.000Z"
}
```

After creating the overlay, you can request it with the <a href="https://api.gcore.com/docs/streaming#tag/Overlays/operation/get_overlays_id" target="_blank">API method</a> by specifying its ID.

### Change overlays

The <a href="https://api.gcore.com/docs/streaming#tag/Overlays/operation/patch_overlay" target="_blank">API method</a> updates settings for a set of overlays. This method allows changing the settings of several overlays. If you have only one, try <a href="https://api.gcore.com/docs/streaming#tag/Overlays/operation/patch_overlay_id" target="_blank">this one</a>. 

Example of the request:

```
curl -L -X PATCH https://api.gcore.com/streaming/streams/12345/overlays \
-H 'Authorization: APIKey 1234$0d1659...' \
-H 'Content-Type: application/json' \
-d '{
    "url": "http://domain.tld/myoverlay_new_3.html",
    "width": "120",
    "height": "40",
    "x": "0",
    "yt": "0",
    "stretch": "false",
    "id": "1",
}'
```

Example of the response:

```
[
    {
        "url": "http://domain.tld/myoverlay_new_3.html",
        "width": 120,
        "height": 40,
        "x": 0,
        "y": 0,
        "stretch": false,
        "id": 1
    }
]
```

### Delete an overlay

The <a href="https://api.gcore.com/docs/streaming#tag/Overlays/operation/delete_overlays_id" target="_blank">API method</a> lets you delete the overlay.

Here’s an example of the request:

```
curl -L -X DELETE https://api.gcore.com/streaming/streams/12345/overlays/1 \
-H 'Authorization: APIKey 1234$0d1659...' \
```

If all IDs are correct, you will get a response 200: ```Overlay has been deleted successfully```. 