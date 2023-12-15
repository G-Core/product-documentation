---
title: subtitles-and-closed-captions-for-vod
displayName: Subtitles & Captioning
published: true
order: 90
toc:
   --1--Subtitles and closed captions: "what-are-subtitles-and-closed-captions"
   --1--Formats: "formats-of-subtitles-and-captions"
   --2--SRT: "srt"
   --2--WebVTT: "webvtt"
   --1--Generating: "how-to-get-subtitles-and-captions"
   --2--Gcore (in development): "gcore"
   --2--Third-play: "third-play"
   --2--External platforms: "how-to-extract-subtitles-and-captions-from-external-platforms"
   --1--Managing: "how-to-add-and-manage-subtitles-and-captions"
   --2--Control panel: "control-panel"
   --2--API: "api"
   --3--Add: "add-subtitles-or-captions"
   --3--Get: "get-subtitles-or-captions"
   --3--Modify: "modify-subtitles-or-captions"
   --3--Delete: "delete-subtitles-or-captions"
   --1--Viewing: "how-to-view-subtitles-or-captions"
   --2--Gcore Player: "gcore-player"
   --2--Custom players: "custom-playback-via-api"
   --2--Players with HLS support: "native-playback-with-hls"
   --2--Examples: "examples-of-different-players-playback-interfaces"
pageTitle: Guide to subtitles and captions in Gcore Player | Gcore
pageDescription: Comprehensive guide to using subtitles and closed captions in videos with Gcore Player, supporting formats like SRT and WebVTT. 
---
# Subtitles and closed captions for VOD

## What are subtitles and closed captions?

*Subtitles* are the transcribed speech in your video, including narration, dialogues, and monologues.

*Closed captions* or just *captions* are transcribed speech showing what is said in your video and explaining any audio context, such as background music, comments about moods, and emotions behind the spoken words.

By using timed text tracks for your videos’ subtitles and closed captions, you can engage wider audiences, such as deaf and hard-of-hearing people or non-native speakers. 

Your videos may need text accompaniment in the following cases:

- Watching muted videos on web pages with autoplay
- Watching videos without headphones in a noisy public environment
- Watching foreign videos with translation to the user’s language
- Improving SEO and searchability through text indexation
- Enhancing learning and comprehension, especially in an educational context 

Gcore Player supports timed text tracks for videos: subtitles and closed captions, as in the example:

<img loading="lazy" src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/subtitles-and-closed-captions-for-vod/captions-10.gif" alt="Gcore Player" width="">

## Formats of subtitles and captions

We support SRT and WebVTT formats for timed text tracks.

### SRT

SRT (SubRip file format) is a simple text file saved in the SubRip file format with the .srt extension.

**Example**:

```
1
00:00:19,570 --> 00:00:24,592
Oh, you cute little corny little spursome. Latin name, bonus points.

2
00:00:44,014 --> 00:00:52,156
...Come on, team. We must not have dilly-dally when there's so much nature to see. I was thinking we should call our class project Fun Guys in the Forest...
```

### WebVTT

WebVTT (Web Video Text Tracks) is a text file with the .vtt extension. It is based on the SRT but expanded without backward compatibility. A WebVTT can contain captions, descriptions, chapters, and metadata cues such as caption alignment.

**Note**: We recommend using WebVTT. It is supported by most devices, players, and browsers.

**Example**:

```
1
00:00:19,570 --> 00:00:24,592 position:10%,line-left align:left size:35%
Oh, you cute little corny little spursome. 
Latin name, bonus points.NOTE I’m not sure the timing is right on the following cue.

2
00:00:44,014 --> 00:00:52,156 position:90% align:right size:35%
...Come on, team. We must not have dilly-dally when there's so much nature to see. I was thinking we should call our class project Fun Guys in the Forest...
```

## How to get subtitles and captions

### Gcore

**Note**: Gcore will provide AI-generated subtitles soon. More information will be available soon when the service goes into beta testing.

For now, automatically generated text tracks can only be subtitles (not closed captions.) Additional ambiance accompaniment is unavailable, since the subtitles use the voice from the video.

The quality of automatic subtitle generation depends on the quality of the audio and the ability to parse the pronunciation of words automatically. The accuracy threshold for automated captions is around a 15% word error rate, which can fluctuate.

By default, subtitles will be created in the video’s original language. After that, the subtitle can be automatically translated into other languages.

### Third-play

Many third-party tools will allow you to generate subtitles on your side and then attach them as a file. Free services include <a href="https://www.veed.io/tools/auto-subtitle-generator-online" target="_blank">Veed</a> and <a href="https://www.veed.io/tools/auto-subtitle-generator-online" target="_blank">Kapwing</a>.

**Note**: External services may have use limitations; we are not responsible for them.  

### How to extract subtitles and captions from external platforms

Here are some helpful guides on how to download subtitles from popular external platforms:

- <a href="https://developers.google.com/youtube/v3/docs/captions" target="_blank">Youtube</a>
- <a href="https://help.vimeo.com/hc/en-us/articles/12425955868817-Download-a-video-with-captions-or-subtitles" target="_blank">Vimeo</a>
- <a href="https://support.zoom.us/hc/en-us/articles/360060958752-Saving-closed-captions-in-a-meeting" target="_blank">Zoom</a>
- <a href="https://help.webex.com/en-us/article/ng387ab/Manage-notes,-meeting-minutes,-and-closed-captions-in-Webex-Meetings-and-WebexWebinars" target="_blank">Webex</a>
- <a href="https://support.microsoft.com/en-au/office/use-live-captions-in-microsoft-teams-meetings-4be2d304-f675-4b57-8347-cbd000a21260" target="_blank">MS Teams</a>
- <a href="https://learn.microsoft.com/en-us/stream/portal-add-subtitles-captions#download-subtitles-or-captions" target="_blank">Sharepoint</a>

## How to add and manage subtitles and captions

### Control panel

1\. Go to the <a href="https://streaming.gcore.com/video/list" target="_blank">Video Hosting</a> section and open the video where you want to add subtitles or captions.

<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/subtitles-and-closed-captions-for-vod/captions-20.png" alt="Video Hosting section" width="80%">

2\. Click **Add subtitles**. You can add several files.

3\. Select the subtitle language for each file from the dropdown list.

4\. Click **Save**.

**Note**: It takes about 15 minutes for the changes to take effect. Then you will see an icon to the left of the time indicator to switch on subtitles, and by clicking on it, you can select the subtitle language.

### API

Explore our <a href="https://api.gcore.com/docs/streaming#tag/Subtitles" target="_blank">API documentation</a> which describes working with subtitles and captions. Here are some methods for the most helpful actions.

#### Add subtitles or captions

The <a href="https://api.gcore.com/docs/streaming#tag/Subtitles/operation/post_api_videos_video_id_subtitles" target="_blank">API method</a> lets you add subtitles attached to a video.

**Note**: Specify the language using a three-letter language code according to <a href="https://en.wikipedia.org/wiki/List_of_ISO_639-2_codes" target="_blank">ISO-639-2 (bibliographic code)</a>.

Example of the request:

```
curl -L 'https://api.gcore.com/streaming/videos/2474732/subtitles' \
-H 'Authorization: APIKey 1234$0d1659...' \
-H 'Content-Type: application/json' \
-d '{
    "name": "German (AI-generated)",
    "language": "ger",
    "vtt": "WebVTT\n\n1\n00:00:18,350 --> 00:00:24,350\nOh, du süßes, kühles, schmuckiges Schmuck. Latin Name, Bonus-Punkte.\n\n2\n00:00:44,014 --> 00:00:52,156\nKomm schon, Team. Wir müssen nicht auf Dilly Dally, Ich dachte..."         
}'
```

In response, you will get all original data and the “id” field of a new entity of subtitle. Example of the response:

```
{
    "id": 5850,
    "name": "German (AI-generated)",
    "language": "ger",
    "vtt": "WebVTT\n\n1\n00:00:18,350 --> 00:00:24,350\nOh, du süßes, kühles, schmuckiges Schmuck. Latin Name, Bonus-Punkte.\n\n2\n00:00:44,014 --> 00:00:52,156\nKomm schon, Team. Wir müssen nicht auf Dilly Dally, Ich dachte..."         
}'
```

#### Get subtitles or captions

The <a href="https://api.gcore.com/docs/streaming#tag/Subtitles/operation/get_api_videos_video_id_subtitles_id" target="_blank">API method</a> lets you attach subtitles or captions to a video.

Example of the request:

```
curl -L 'https://api.gcore.com/streaming/videos/2474732/subtitles' \
-H 'Authorization: APIKey 1234$0d1659...'
```

Example of the response:

```
[
    {
        "id": 5823,
        "name": "English (AI-generated)",
        "language": "eng",
        "vtt": "WebVTT\n\n1\n00:00:19,570 --> 00:00:24,592\nOh, you cute little corny little spursome. Latin name, bonus points.
\n\n2\n00:00:44,014 --> 00:00:52,156\nCome on, team. We must not have dilly-dally when \nthere's so much nature to see..."
    },
    {
        "id": 5850,
        "name": "German (AI-generated)",
        "language": "ger",
        "vtt": "WebVTT\n\n1\n00:00:18,350 --> 00:00:24,350\nOh, du süßes, kühles, schmuckiges Schmuck. Latin Name, Bonus-Punkte.\n\n2\n00:00:44,014 --> 00:00:52,156\nKomm schon, Team. Wir müssen nicht auf Dilly Dally, Ich dachte..."
    }
]
```

#### Modify subtitles or captions

The <a href="https://api.gcore.com/docs/streaming#tag/Subtitles/operation/patch_api_videos_video_id_subtitles_id" target="_blank">API method</a> lets you modify any field of the subtitle or caption entity: to update vtt subtitles or just update the entity's name.

Example of the request:

```
curl -L -X PATCH 'https://api.gcore.com/streaming/videos/2474732/subtitles/5850' \
-H 'Authorization: APIKey 1234$0d1659...' \
-H 'Content-Type: application/json' \
-d '{
    "name": "German (AI-generated)"
}'
```

#### Delete subtitles or captions

The <a href="https://api.gcore.com/docs/streaming#tag/Subtitles/operation/delete_api_videos_video_id_subtitles_id" target="_blank">API method</a>
 allows you to delete the subtitle or caption entity.

Example of the request:

```
curl -L -X DELETE 'https://api.gcore.com/streaming/videos/2474732/subtitles/5850' \ 
-H 'Authorization: APIKey 1234$0d1659...'
```

## How to view subtitles or captions

### Gcore Player

Captions are integrated into Gcore's Player. Just click the icon located to the left of the volume indicator in the bottom panel of the Player to get captions.

<iframe width="720" height="360" src="https://demo-public.gvideo.io/videos/2675_QtN3sYHVPy3KF2n" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>

### Custom playback via API

If you have a custom player, you must get subtitles or captions from the API response or the HLS manifest (.m3u8 file.) Use this <a href="https://api.gcore.com/docs/streaming#tag/Subtitles/operation/get_api_videos_video_id_subtitles" target="_blank">API method</a> to get the list of subtitles for the video. 

### Native playback with HLS

Captions are integrated into the HLS manifest. This means they can be automatically played on many native and custom players.

Make sure there are cues in the WebVTT format.

Example of the request:

```
curl 'https://demo-public.gvideo.io/videos/2675_QtN3sYHVPy3KF2n/master.m3u8'
```

Example of the response:

```
#EXTM3U

#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs0",NAME="English",LANGUAGE="en",AUTOSELECT=YES,DEFAULT=YES,URI="index-f5.m3u8"
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs0",NAME="Español",LANGUAGE="es",AUTOSELECT=NO,DEFAULT=NO,URI="index-f6.m3u8"
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs0",NAME="Français",LANGUAGE="fr",AUTOSELECT=NO,DEFAULT=NO,URI="index-f7.m3u8"
#EXT-X-MEDIA:TYPE=SUBTITLES,GROUP-ID="subs0",NAME="Deutsch",LANGUAGE="de",AUTOSELECT=NO,DEFAULT=NO,URI="index-f8.m3u8"

#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=1928000,RESOLUTION=1720x720,FRAME-RATE=24.000,CODECS="avc1.640020,mp4a.40.2",VIDEO-RANGE=SDR,SUBTITLES="subs0"
index-svod720n-v1-a1.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=928000,RESOLUTION=1144x480,FRAME-RATE=24.000,CODECS="avc1.4d401f,mp4a.40.2",VIDEO-RANGE=SDR,SUBTITLES="subs0"
index-svod480n-v1-a1.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=514000,RESOLUTION=860x360,FRAME-RATE=24.000,CODECS="avc1.42c01e,mp4a.40.2",VIDEO-RANGE=SDR,SUBTITLES="subs0"
index-svod360n-v1-a1.m3u8
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=264000,RESOLUTION=572x240,FRAME-RATE=24.000,CODECS="avc1.42c015,mp4a.40.2",VIDEO-RANGE=SDR,SUBTITLES="subs0"
index-svod240n-v1-a1.m3u8
```

### Examples of different players’ playback interfaces

Example of iOS player playback:
<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/subtitles-and-closed-captions-for-vod/captions-30.png" alt="Example of iOS player playback">

Example of Android Exoplayer playback:
<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/subtitles-and-closed-captions-for-vod/captions-40.png" alt="Example of Android Exoplayer playback">

Example of Android Exoplayer playback:
<img src="https://assets.gcore.pro/docs/streaming-platform/video-hosting/subtitles-and-closed-captions-for-vod/captions-50.png" alt="Example of Android Exoplayer playback">