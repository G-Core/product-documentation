---
title: customize-appearance-of-the-built-in-player 
displayName: Players
published: true
order: 10
toc:
   --1--Configure player in the Customer Portal: "configure-custom-player-in-the-customer-portal"
   --1--Customize player behavior via query string: "customize-player-behavior-using-query-string"
pageTitle: Guide to Customizing Players Features | Gcore
pageDescription: A step-by-step guide on configuring custom players with your branding and additional features.
---
# Customize appearance of the built-in player 
  
Player is a free feature that allows customizing the default player.

Let’s compare the default and custom player. To show you the customization options:

- We set new interface colors.
- Add a logo (dog icon in the bottom-right corner).
- Add the button to select the playback speed.
- Enable the "mute" option by default.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/customize-appearance-of-the-built-in-player/mceclip0.png" alt="customization options" width="80%">

## Configure custom player in the Customer Portal

1\. Go to the <a href="https://streaming.gcore.com/players/list" target="">Players</a> tab and click **Create a player**.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/customize-appearance-of-the-built-in-player/create-player.png" alt="Players tab" width="80%">

2\. Enter the name of your player (it will be displayed in the Gcore Customer Portal) and click **Create**.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/customize-appearance-of-the-built-in-player/mceclip2.png" alt="Enter the name of your player" width="50%">

The configuration page opens. Complete the remaining steps in it.

<img src="https://assets.gcore.pro/docs/streaming-platform/extra-features/customize-appearance-of-the-built-in-player/mceclip3.png" alt="The configuration page" width="80%">

3\.  Set the custom player as the default one for VOD or/and Live stream if you want to use this player for all videos/streams. You can also choose a custom player for a specific video or stream.

4\.  Enable necessary video behavior options:

- **Autoplay**. If the option is active, a video starts playing automatically when a user opens the website page with it. This option should be enabled if you want to playback <a href="https://gcore.com/docs/streaming-platform/video-hosting/create-an-illusion-of-a-live-broadcast-with-uploaded-videos" target="_blank">Live imitation</a> automatically.

- **Mute**. If the option is active, video plays with the sound off.

<alert-element type="info" title="Info">

If both Autoplay and Mute options are active, only one option will work. It depends on an end user's browser policy (<a href="https://developer.mozilla.org/en-US/docs/Web/Media/Autoplay_guide" target="_blank">Mozilla</a>, <a href="https://developer.chrome.com/blog/autoplay" target="_blank">Chrome</a>).

</alert-element>

5\.  Enable necessary player control options:

- **Disable skin**. If the option is active, the player control elements are hidden. 
- **Save user settings.** If the option is active, users watch the video with the same quality and sound settings they have had previously. It works until the browser cache gets cleared.
- **Share video.** If the option is active, a sharing button appears in the upper-right corner of the video for the users to post it to social networks.
- **Playback speed control.** If the option is active, users can slow down and speed up VOD playback. 
- **Pause when clicking on player.** If the option is active, video stops by clicking at any point on the player's screen.

6\.  Select colors for different elements of your player:

- Background color for the bottom panel of the player.
- Foreground color for the elements on the bottom panel.
- Text color for timeline.
- Hover color for those elements on the bottom panel that the cursor is hovering over.

7\.  To collect data on your viewers' actions in the player, activate the Enables Google Analytics option and specify your Google Analytics ID.

8\.  Add a logo that will be displayed on the screen.

9\.  Select the logo position. 

10\.  Save changes.

## Customize player behavior using query string

You can make real-time adjustments to the player's functionality by adding the following parameters to the player's URL: 

* `?no_low_latency`
* `?t=(format)`
* `?sub_lang=(language)`

### ?no_low_latency 

Use this parameter to ensure that the player uses non-low-latency streams HLS MPEG T instead of MPEG-DASH CMAF or LL-HLS CMAF. This parameter takes no arguments. 

Example: `https://player.gvideo.co/broadcasts/2675_21606?no_low_latency`

### ?t=(format) 

Set time to rewind from the beginning of play. It only applies to video on demand (VOD). 

This parameter takes two arguments:  

<table>
<thead>
<tr>
<th>Argument</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left"><code>t = (integer)</code></td>
<td style="text-align: left">Number of seconds to start playing from.</td>
<td style="text-align: left">t=15<br><br>
<code>https://player.gvideo.co/videos/2675_zH5vyOfkNqoxzei?t=15</code>
</td>
</tr>
<tr>
<td style="text-align: left"><code>t = [(integer)h][(integer)m][(integer)s]</code></td>
<td style="text-align: left">Set start time point in HMS format, where h = hours, m = minutes, s = seconds.</td>
<td style="text-align: left">t=1h30m, 34m, 2m30s<br><br>
<code>https://player.gvideo.co/videos/2675_zH5vyOfkNqoxzei?t=1m2s</code>
</tr>
</tbody>
</table>

### ?sub_lang=(language) 

Display subtitles in a specific language. This parameter takes the following argument: 

<table>
<thead>
<tr>
<th>Argument</th>
<th>Description</th>
<th>Example</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left"><code>sub_lang = (ISO language code, 2 letters)</code></td>
<td style="text-align: left">Use two letters that correspond to the <a href="https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes" target="_blank">ISO 639 language codes</a>.</td>
<td style="text-align: left">sub_lang=de <br><br>
<code>https://player.gvideo.co/videos/2675_QtN3sYHVPy3KF2n?&sub_lang=de</code>
</td>
</tr>
</tbody>
</table>