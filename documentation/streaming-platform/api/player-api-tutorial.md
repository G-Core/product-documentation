---
title: player-api-tutorial
displayName: Player API tutorial
published: true
order: 30
toc:
   --1--Player Initialization via iFrame: "player-initialization-via-iframe"
   --1--Events: "events"
   --1--Calling player methods: "calling-player-methods"
   --1--API testing tool: "api-testing-tool"
pageTitle: Player API. Initialization, Events, Methods | Gcore
pageDescription: A detailed guide on using Player API to manage player settings, collect data, and handle various events.
---
# Player API tutorial

The API allows you to manage the player settings using JavaScript and collect data about its use for further analysis.

## Player Initialization via iFrame

Copy the iFrame code from the VOD/broadcast settings in your account:

- For videos: the All videos section, Settings, Export, Code
- For live streaming: the Live streaming section, Settings, Links for the export

Add the ```id='gplayer'``` parameter to the iFrame and paste it into the site code.

Example of the iFrame code from the control panel with the id= 'gplayer' parameter:

```
<iframe width="640" height="360" src="https://12345.gvideo.io/video/dSmuIp-tNRtwACT" allow="autoplay" allowfullscreen frameborder="0" id="gplayer"></iframe>
```

Parameters:

- **width** - the width of the player,
- **height** - the height of the player,
- **src** - content URL (link to VOD or live stream),
- **allowfullscreen** - if the parameter is added to the iframe, a button for switching to full-screen mode is added to the controls of the player,
- **frameborder** - border of the player. The default value is "0" (the border shouldn't be visible),
- **id** - the player ID. Required for further initialization of the player when calling API methods.

After the iframe add the following code to initialize the player:

```
<script type="text/javascript" charset="utf-8" src="https://vplatform.gcdn.co/_players/latest/gplayerAPI.min.js"></script>

<script>  
  window.onload = function() {  
    let gplayerAPI = new GcorePlayer.gplayerAPI(document.getElementById('gplayer'));   
  }  
</script>
```

The onload event on window is triggered when the entire page, including the iframe, is loaded. Then there is an indication of the player to which the API call will be applied.

Example of the full player initialization code and iframe for HTML page:

```
<!DOCTYPE html>  
<html>  
<head>  
 <title>TITLE</title>  
</head>  
<body>  
 <iframe width="640" height="360" src="https://12345.gvideo.io/video/dSmuIp-tNRtwACT" allowfullscreen frameborder="0" id='gplayer'></iframe>  
 <script type="text/javascript" charset="utf-8" src="https://vplatform.gcdn.co/_players/latest/gplayerAPI.min.js"></script>  
 <script>  
 window.onload = function() {  
 let gplayerAPI = new GcorePlayer.gplayerAPI(document.getElementById('gplayer'));  
}  
 </script>  
 </script>  
</body>  
</html>
```

## Events

| Event        | Returns                          | Description                                               |
|--------------|----------------------------------|-----------------------------------------------------------|
| ready        |                                  | Fired when playback is ready                              |
| play         |                                  | Fired when player starts to play                          |
| pause        |                                  | Fired when player is paused                               |
| seek         | the current time in seconds      | Fired when player seeks the video                         |
| resize       | the object with the current size | Fired when player is resized                              |
| fullscreen   | true/false                       | Fired when the player is switched to the full screen mode |
| timeupdate   | data progress object             | Fired when the time is updated on player                  |
| volumeupdate | current volume level             | Fired when player's volume is updates                     |
| error        | error                            | Fired when player receives an error                       |
| ended        |                                  | Fired when player ends the video                          |
| stop         |                                  | Fired when player stops                                   |


## Calling player methods

You can start calling methods once you receive the ready event:

```
gplayerAPI.on('ready', () => {  
console.log('[Event]', 'ready')  
gplayerAPI.method({name: 'play'})  
})
```

Available methods:

| Method name    | Data type | Description                                                                                                                        |
|----------------|-----------|------------------------------------------------------------------------------------------------------------------------------------|
| getCurrentTime | Number    |  The current time in seconds                                                                                                       |
| getDuration    | Number    |  The duration time in seconds                                                                                                      |
| getVolume      | Number    |  Volume. Value from 0 (sound off, mute) to 100 (maximum volume)                                                                    |
| isDvrEnabled   | Boolean   |  Shows DVR service status:true - DVR is enabled,false - DVR is disabled                                                |
| isPlaying      | Boolean   |  Checks if the player is playing:true - the current source is playing,false - playback is off/stopped/not started      |
| mute           |           |  Turns off the sound                                                                                                               |
| unmute         |           |  Turns on the sound                                                                                                                |
| pause          |           |  Pauses playback                                                                                                                   |
| play           |           |  Starts playback                                                                                                                   |
| resize         | Object    |  Modifies the canvas of the player                                                                                                 |
| seek           | Number    |  Rewinds playback (seconds). For example, player.seek (120) rewinds the video and starts at 2 minutes                        |
| seekPercentage | Number    |  Rewinds playback (percent). For example, player.seek (50) rewinds the video and starts playing from the middle of the video |
| setVolume      | Number    |  Sets the volume for the current video                                                                                             |
| stop           |           |  Stops playback of the current video                                                                                               |


Method call pattern:

```
gplayerAPI.method({name: 'isPlaying', params: {}, callback: (res) => {  
 console.log(res)  
}})
```

- name - the name of the function,
- params - the parameters of the function,
- callback - the callback function.

Examples:

```
<script>  
 window.onload = function() {  
 let gplayerAPI = new GcorePlayer.gplayerAPI(document.getElementById('gplayer'));  
 let flag = true;  
 gplayerAPI.on('ready', () => {  
 console.log('\[Event\]', 'ready')  
 gplayerAPI.method({name: 'play'})  
 })  
  
gplayerAPI.on('play', () => {  
 if(flag) {  
 gplayerAPI.method({name: 'pause'})  
 flag = false;  
 }  
 console.log('[Event]', 'play')  
 })  
  
gplayerAPI.on('pause', () => {  
 console.log('[Event]', 'pause')  
 })  
  
gplayerAPI.on('volumeupdate', () => {  
 console.log('[Event]', 'volumeupdate')  
 })  
  
gplayerAPI.on('timeupdate', () => {  
 console.log('[Event]', 'timeupdate')  
 })  
  
gplayerAPI.on('stop', () => {  
 console.log('[Event]', 'stop')  
 })  
  
gplayerAPI.on('seek', () => {  
 console.log('[Event]', 'seek')  
 })  
  
gplayerAPI.on('resize', () => {  
 console.log('[Event]', 'resize')  
 })  
  
gplayerAPI.on('fullscreen', () => {  
 console.log('[Event]', 'fullscreen')  
 })  
  
gplayerAPI.on('error', () => {  
 console.log('[Event]', 'error')  
 })  
  
gplayerAPI.on('ended', () => {  
 console.log('[Event]', 'ended')  
 }) }  
</script>
```