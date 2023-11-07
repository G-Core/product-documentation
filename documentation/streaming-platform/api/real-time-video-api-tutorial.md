---
title: real-time-video-api-tutorial
displayName: Real-Time Video API tutorial
published: true
order: 20
toc:
   --1--Get started: "get-started"
   --1--Codeless integration: "codeless-integration"
   --2--Create Room URL: "create-room-url"
   --2--Embed Room on Site: "embed-room-on-a-site"
   --1--Mobile app integration: "mobile-app-integration"
   --2--Embedding in Android app: "embedding-in-android-app"
   --2--Embedding in iOS app: "embedding-in-ios-app"
   --2--Embedding in React Native app: "embedding-in-react-native-app"
   --1--Video call customization: "video-call-customization"
   --2--Calls or webinars: "calls-or-webinars"
   --3--Video call rooms: "video-call-rooms"
   --3--Webinar rooms: "webinar-rooms"
   --2--Allowed domain names: "allowed-domain-names"
   --2--Advanced: "advanced-url-attributes-for-rich-customization"
   --2--Attribute details: "attribute-details"
   --3--&accessToken=<token>: "accesstokentoken"
   --3--&autoplayWithoutAudioTrack=<true|false>: "autoplaywithoutaudiotracktruefalse"
   --3--&canRecord=<true|false>: "canrecordtruefalse"
   --3--&controlsDisabled=<true|false>: "controlsdisabledtruefalse"
   --3--&disableChat=<true|false>: "disablechattruefalse"
   --3--&handEnabled=<true|false>: "handenabledtruefalse"
   --3--&hideIndicators=<true|false>: "hideindicatorstruefalse"
   --3--&displayName=<name>: "displaynamename"
   --3--&itisparticipant=<true|false>: "itisparticipanttruefalse"
   --3--&lang=<code>: "langcode"
   --3--&maxBroadcasters=<num>: "maxbroadcastersnum"
   --3--&maxWatchers=<num>: "maxwatchersnum"
   --3--&minimizeTiles=<true|false>: "minimizetilestruefalse"
   --3--&nameScreenDisabled=<true|false>: "namescreendisabledtruefalse"
   --3--&peerId=<id>: "peeridid"
   --3--&role=<role>: "rolerole"
   --3--&roomId=<id>: "roomidid"
   --3--&sortPeers=<true|false>: "sortpeerstruefalse"
   --3--&startWithFS=<true|false>: "startwithfstruefalse"
   --3--&token=<jwt>: "tokenjwt"
   --3--&tokenLifetime=<milliseconds>: "tokenlifetimemilliseconds"
   --3--&video=<url>: "videourl"
   --3--&waitingRoom=<true|false>: "waitingroomtruefalse"
   --2--Debug and Dev URL attributes only: "debug-and-dev-url-attributes-only"
   --3--&accessUrl=<url>: "accessurlurl"
   --3--&apiEvent=<url>: "apieventurl"
   --3--&authEvent=<header>: "autheventheader"
   --3--&authorizationAccess=<header>: "authorizationaccessheader"
   --2--Moderator: "moderator"
   --2--Recording: "recording"
   --3--What can be recorded: "what-can-be-recorded"
   --3--Auto-recording: "auto-recording"
   --3--Where to find recorded video: "where-to-find-recorded-videos"
   --3--Set up: "how-to-set-up-our-recording-feature"
   --2--Language Interpretation (beta): "language-interpretation-beta"
   --1--Client API: "client-api"
   --2--Iframe integration: "iframe-integration"
   --3--Example of iframe Integration: "example-of-iframe-integration"
   --3--Interaction with iframe: "interaction-with-iframe"
   --3--Public methods of Real-Time Video iframe: "public-methods-of-real-time-video-iframe"
   --3--Events from an iframe: "events-from-an-iframe"
   --1--Server API: "server-api"
   --2--Server endpoints: "server-endpoints"
   --3--Video Conferencing Endpoints: "video-conferencing-endpoints"
   --3--Common Response Codes: "common-response-codes"
   --3--List of Servers: "list-of-servers"
   --3--Example of a video server performance check: "example-of-video-server-performance-check"
   --2--Webhooks: "webhooks"
   --3--Webhook joinPeer: "webhook-joinpeer"
   --3--Webhook closePeer: "webhook-closepeer"
   --2--Special API of Streaming Platform: "special-api-of-streaming-platform"
   --3--Statistics: "statistics"
   --3--Getting Recorded Video: "getting-recorded-video"
   --3--Rate Limits: "rate-limits"
   --1--Security: "security"
   --2--Validating Client API Requests: "validating-client-api-requests"
   --3--What is a JWT: "what-is-a-jwt"
   --3--Limitations when using JWT: "limitations-when-using-jwt"
   --3--JWT Header: "jwt-header"
   --3--JWT Body: "jwt-body"
   --3--JWT Signature: "jwt-signature"
   --2--Validating server API Requests: "validating-server-api-requests"
   --3--Validating using Authorization Header: "validation-with-authorization-header"
   --3--Bearer Authentication: "bearer-authentication"
   --2--Authentication of participants and Access Limitation: "authentication-of-participants-and-access-limitation"
   --1--Troubleshooting: "troubleshooting"
   --2--JWT Digital Signature Algorithm: "jwt-digital-signature-algorithm"
   --2--RSA Public & Secret Key generation: "rsa-public--secret-key-generation"
pageTitle: Mastering Real-Time Video API | Gcore
pageDescription: A comprehensive guide on how to embed real-time calling module into applications.
---
# Real-Time Video API tutorial

It is an easy-to-use video meeting tool.

A video conference room can be inserted in two ways:

1. **Codeless** — just copy a URL, paste iframe on your page and join a call.
2. **API-based** — for fine-tuning and integration with your platforms or enterprise internal systems.

Embed video meetings into an application or website with iframe or Server API/Client API allowing your team to build faster and release more often.

## Get started

Create a meeting in a browser:

1\. Open <a href="https://meet.gcore.com/new" target="_blank">https://meet.gcore.com/new</a>.

2\. Click the **Create conference** button.

3\. A Room URL will be created automatically.

4\. Click the **Join** button.

5\. Send the URL to other attendees to join your video call.

Example: ```https://meet.gcore.com/call/?roomId=serv2testroom```

**Embed a video call room in your website or app via iFrame**. The iframe’s src attribute is specified as the URL.

Example:

```
<iframe allow="camera; microphone; fullscreen; display-capture" src="https://meet.gcore.com/call/?roomId=serv2testroom"></iframe>
```

**Customize a video call room with URL attributes**. 

Example: ```https://meet.gcore.com/call/?roomId=serv2testroom&displayName=JohnSnow```

## Codeless integration

### Create Room URL

1\. Generate a video room ID. Use an alphanumeric character set. For example: *bokxlj33*.

2\. Add a server location to the beginning of the set. For example, insert "serv2" for a server in the USA: *serv2bokxlj33*.

3\. Specify */call/* as a method for your video call room.

4\. Insert the Room ID into the final URL. The result should be as follows: ```https://meet.gcore.com/call/?roomId=serv2bokxlj33```

You can create a URL, save it, send it, or write it in your notes. The URL is reusable. The URL will be accessible all the time – before an event, during an event, and even 1 year later after an event.

The Room is created on a server when the first participant enters it.

The Room is automatically destroyed without saving information when the last participant leaves.

### Embed Room on a Site

Embedding a meeting into a service or app requires using an iframe with the src attribute specified as the URL. Read the "Allowed domain names" section to learn how to configure your website’s domain so that browsers don’t block the iframe.

Settings of iframe must have the special permissions required for video calling:

allow="camera;microphone;fullscreen;display-capture;autoplay;screen-wake-lock"

HTTP Feature-Policy header provides a mechanism to allow: 

- camera – <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy/camera" target="_blank">permission to use a cam inside iframe</a>.  
- microphone – <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy/microphone" target="_blank">permission to use a mic inside iframe</a>. 
- fullscreen – <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy/fullscreen" target="_blank">permission to open iframe’s UI in the fullscreen mode</a>. 
- display-capture – <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy/display-capture" target="_blank">permission to use the screen sharing feature inside iframe</a>. 
- autoplay – <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy/autoplay" target="_blank">permission to start the video autoplay inside iframe after page load</a>. 
- screen-wake-lock – <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Feature-Policy/screen-wake-lock" target="_blank">permission that allows devices not to dim or turn off the screen during a call</a>. 

Example:

```
<iframe src="https://meet.gcore.com/call/?roomId=serv2bokxlj33"    
allow="camera; microphone; fullscreen; display-capture; autoplay; screen-wake-lock"></iframe>

```

## Mobile app integration

### Embedding in Android app

Embedding in Android can be done in two ways:  

1.  **Android Native SDK** – please look at <a href="https://github.com/G-Core/android-demo-video-calls" target="_blank">SDK and open-source demo app</a>.
2.  **WebView**. 

It’s better to use the native Android SDK. One-to-one calls and/or with many participants for real-time communication within your own app. 

There are two modules: 

1. SDK — a  native library of video calls to be implemented into apps. The library is responsible for all internal processes: get cam/mic data, make video streams, send, and receive data to/from a video server.
2. DEMO —  a native demo application with open-source code. The app shows cases and scenarios of SDK usage in real app. You can compile the code and run it.   

WebView requires the use of the <a href="https://developer.android.com/reference/android/webkit/WebView" target="_blank">WebView</a> class. To allow a video call room access the camera, you need to do two things: 

1.  Override the  WebChromeClient.onPermissionRequest  method to avoid the default implementation. You can just return true. 
2.  Add the  ```&nameScreenDisabled=true``` parameter  to the Room URL and call "Join" Client API method. 

### Embedding in iOS app

Embedding in iOS can be done in two ways:  

1.  **iOS Native SDK** – please look at <a href="https://github.com/G-Core/ios-demo-video-calls" target="_blank">SDK and open-source demo app</a>. 
2.  **WebView**. 

It’s better to use the native iOS SDK. One-to-one calls and/or with many participants for real-time communication within your own app. 

There are two modules: 

1.  SDK —  a native library of video calls to be implemented into apps. The library is responsible for all internal processes: get cam/mic data, make video streams, send, and receive data to/from a video server.  
2.  DEMO —  a native demo application with open-source code. The app shows cases and scenarios of SDK usage in real app. You can compile the code and run it.   

<a href="https://developer.apple.com/documentation/webkit/wkwebview" target="_blank">WKWebView</a> supports embedding pages that use WebRTC from iOS 14.5 onwards.  

To support older iOS versions, we recommend using one of the following options: 

- For iOS 14.3 and 14.4, use <a href="https://developer.apple.com/documentation/safariservices/sfsafariviewcontroller" target="_blank">SFSafariViewController</a> to open a web page containing an iframe with its src specified as a video call room URL. 
- Redirect to mobile Safari for iOS versions lower than 14.3. 

To use Video Calls with Cordova (Phonegap) please use the plugin for <a href="https://github.com/topics/safari-view-controller" target="_blank">SafariViewController</a>.

### Embedding in React Native app 

Embedding in React Native iOS/Android can be done via wrapper:  

React Native Wrapper – please look at <a href="https://github.com/G-Core/reactnative-demo-video-calls" target="_blank">SDK and open-source demo app</a>.

There are four modules: 

1.  iOS Wrapper – React Native demo app with open-source code. 
2.  Android Wrapper – React Native demo app with open-source code. 
3.  SDK – native library of video calls to be implemented into apps. The library is responsible for all internal processes: get cam/mic data, make video streams, send, and receive data to/from the video server.  
4.  DEMO – demo app with open-source code. The app shows cases and scenarios of SDK usage in the real app. You can compile the code and run it. 

## Video Call Customization 

### Calls or Webinars

#### Video call rooms 

A video conferencing room is a room where all invited participants are active and have their cameras and microphones on. One video call room can hold up from 1 to 100 participants or more. 

A method to create video conferencing rooms is ```/call/```. 

Example: ```https://meet.gcore.com/call/?roomId=```

#### Webinar rooms 

A webinar room is a room  where participants are divided into two groups: speakers and viewers. Speakers  are active participants with cameras and microphones. Speakers' video is shown on the screen of the webinar room, participants can watch and hear them. Viewers can only watch the speakers without interaction. They have neither camera, nor microphone on. One webinar room can hold up between 1 and 20 speakers and between 0 and 2000 viewers.  
A method to create video conferencing rooms is ```/webinar/```.  

Moreover, please see <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial#itisparticipant-true-false" target="_blank">&itisparticipant attribute</a>. 

Example: ```https://meet.gcore.com/webinar/?roomId=```

### Allowed domain names

Video calls are accessible from two types of domains:

1.  *companyname.gvideo.co* – example of a client's special domain in our "gvideo.co" zone. 
2.  *video.domain.com* – example of an external client's domain.

By default, we provide a third-level tech domain in the  "gvideo.co"  zone. If you prefer to use your own domain, please contact us.

### Advanced URL Attributes for rich customization

Conferencing is customized by optional URL parameters for each iframe instance. It’s possible for each participant in a meeting to have different parameter combinations. 

| &amp;accessToken=&lt;token&gt;                    | Set a one-time access token                                                                       | JWT, URL  |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------|---------------|
| &amp;accessUrl=&lt;url&gt;                        | Set your server-based authorization method for access token verification                          | JWT, URL  |
| &amp;apiEvent=&lt;url&gt;                         | Set webhooks server-based method for receiving server events                                      | JWT, URL  |
| &amp;authEvent=&lt;header&gt;                     | Set specific webhooks HTTP request header for receiving server events                             | JWT, URL  |
| &amp;authorizationAccess=&lt;header&gt;           | Set specific HTTP request header for access token verification                                    | JWT, URL  |
| &amp;autoplayWithoutAudioTrack=&lt;true|false&gt; | Set a flag "Don’t ask mic permission" on iOS devices for webinar viewer                           | URL       |
| &amp;canRecord=&lt;true|false&gt;                 | Allow the recording function for a moderator                                                       | JWT only |
| &amp;controlsDisabled=&lt;true|false&gt;          | Hide main UI controls and buttons                                                                 | URL       |
| &amp;disableChat=&lt;true|false&gt;               | Disable text chat                                                                                 | URL       |
| &amp;displayName=&lt;name&gt;                     | Set display name of participant                                                                   | JWT, URL  |
| &amp;handEnabled=&lt;true|false&gt;               | Activate the "Raising Hand" feature                                                               | JWT, URL  |
| &amp;hideIndicators=&lt;true|false&gt;            | Hide icons in a participant's tile (mic, cam, name, etc.)                                         | URL       |
| &amp;itisparticipant=&lt;true|false&gt;           | Set a role of a viewer or a participant in webinars                                               | JWT, URL  |
| &amp;lang=&lt;code&gt;                            | Set the interface language explicitly                                                             | URL       |
| &amp;maxBroadcasters=&lt;num&gt;                  | Set the maximum number of participants with camera/audio devices                                  | JWT,URL   |
| &amp;maxWatchers=&lt;num&gt;                      | Set the maximum number of viewers without camera/audio devices                                    | JWT, URL  |
| &amp;minimizeTiles=&lt;true|false&gt;             | Increase the number of participants displayed on a single screen without scrolling to the maximum | URL       |
| &amp;nameScreenDisabled=&lt;true|false&gt;        | Skip welcome page with a cam/mic selection and a name input                                       | URL       |
| &amp;peerId=&lt;id&gt;                            | ID of a participant from your internal system                                                     | JWT, URL  |
| &amp;roomId=&lt;id&gt;                            | Room ID                                                                                           | URL       |
| &amp;role=&lt;role&gt;                            | Set a privilege role for a participant                                                            | JWT only  |
| &amp;sortPeers=&lt;true|false&gt;                 | Move participants with cameras up to the visible area                                             | URL       |
| &amp;startWithFS=&lt;true|false&gt;               | Start meeting in the full screen mode                                                             | URL       |
| &amp;token=&lt;jwt&gt;                            | Set a JWT token                                                                                   | JWT, URL  |
| &amp;video=&lt;url&gt;                            | Display an external HTML player with external video broadcasting for joint viewing                | JWT, URL  |
| &amp;waitingRoom=&lt;true|false&gt;               | Activate waiting room                                                                             | JWT only  |

```
Examples:

1. https://meet.gcore.com/call/?roomId=serv2testroom&displayName=JohnSnow
  
2. https://meet.gcore.com/call/?roomId=serv2testroom&displayName=JohnSnow&disableChat=true
  
3. https://meet.gcore.com/call/?roomId=serv2testroom&displayName=JohnSnow&disableChat=true&lang=en

```  

### Attribute details

#### &amp;accessToken=&lt;token&gt;

It is a security access token generated on your side. If this parameter is specified, then, whenever a user enters a room, our server will additionally ask your authorization server whether the user with the peerID and accessToken parameters is allowed to connect. For more details, refer to the server-side authorization method. 

Type: String. default = not set.

Example: ```&accessToken=802380f4-dd70-4d60-9738-fb5ae8709ae7```

#### &amp;autoplayWithoutAudioTrack=&lt;true|false&gt;

It is used only for iOS devices and only for webinars.  

The iOS Safari Browser policy requires microphone permission to use audio with WebRTC. So, the browser requests a passive viewer (with no cam/mic buttons) in a webinar room to allow access to the mic. This parameter ensures the browser will not ask for access to a microphone, but will play audio using the simple "play" method. 

Type: Boolean, default = false.

Example: ```&autoplayWithoutAudioTrack=true```

#### &amp;canRecord=&lt;true|false&gt;

This allows to record and save everything what happens in a room to the Cloud. Not everyone needs a recording for security reasons, legal restrictions, or storage usage. Recording feature can be activated with this attribute. If the feature is on, a moderator can turn on the recording using the UI button.

Type: Boolean, default = false.

Example: ```&canRecord=true```

#### &amp;controlsDisabled=&lt;true|false&gt;

It is used to hide general controls and buttons from the screen. In this case, you should use ClientAPI methods to manage actions and allow users to turn on/off their cams/mics.

Type: Boolean, default = false.

Example: ```&controlsDisabled=true```

#### &amp;disableChat=&lt;true|false&gt;

This is designed to disable the chat function. If you add the parameter, the "Chat" button will be un-clickable and chatting will be unavailable for participants. It is useful when you prefer to use our own chat.

Type=Boolean, default value = false.

Example: ```&disbleChat=true```

#### &amp;handEnabled=&lt;true|false&gt; 

This parameter helps to activate the "Raise Hand" feature in a room. Participants will be able to click the "Raise hand" button, and the raised hand icon will appear. The icon is displayed in participant’s tile and in the list of participants in the moderator’s panel.  

Type=Boolean, default value = false. 

Example: ```&handEnabled=true``` 

#### &amp;hideIndicators=&lt;true|false&gt;

It is used to make icons inside a tile of a participant invisible. With this parameter, you can hide a participant name and the following icons: cam on/off, mic on/off, absence, raised hand, and pin button.

Type=Boolean, default value = false.

Example: ```&hideIndicators=true```

#### &amp;displayName=&lt;name&gt;

This allows to display a name of a participant.

A participant’s name may be known before they join the meeting. It is possible to pass their name from your internal system, so the user doesn't have to enter it on the welcome page.

If you specify the name in the attribute, the user will not be able to change it through UI.

Type: String, default value = not set.

Example: ```&displayName=JohnSnow```

#### &amp;itisparticipant=&lt;true|false&gt;

This parameter determines roles in a webinar room where there are participants and viewers. All attendees are viewers only by default.

Participants join a room as regular users and can turn on their camera and microphone. Participants also have a standard rectangle icon of a participant. Viewers can observe what is happening in a room, can see and hear, but they do not have a dedicated participant rectangle icon and cannot turn on their camera or microphone.

**Note**: It is used for webinar rooms only.

Type = Boolean, default value = false.

Example: ```&itisparticipant=true```

#### &amp;lang=&lt;code&gt;

This helps to set the UI language of a meeting to match your product or service. In general, the UI language depends on language settings of a participant's browser. A user sets the language in their browser settings, and then its value is transmitted by the browser in the "Accept-Language" header of an HTTP request <a href="https://w3.org/International/questions/qa-lang-priorities" target="_blank">info</a>.  

Select one of these: 

- English = en
- French = fr 
- German = de 
- Luxembourgian = lb 

Therefore, in most cases, you do not need to specify this parameter explicitly. If the UI of a video room  is translated and available for user’s language, then UI will be automatically switched to it. If a language is unavailable, the default English version will be shown. 

But sometimes you need to explicitly set a language based on your internal/enterprise settings, use this parameter. 

Type: String, default = not set.

Example: ```&lang=en```

#### &amp;maxBroadcasters=&lt;num&gt; 

This sets the number of concurrent active attendees in a room at one time. This is the maximum value of users/attendees with turned on cams/mics.  

If another user starts to speak (be active, turn on the cam/mic), but the number of active attendees exceeds the specified value, then this user will receive a system error that they cannot turn it on: "The limit of maximum active attendees is exceeded". 

If no value is specified in the URL, any participant can turn on cam/mic. Please be aware that the number of active users is directly proportional to the load on media servers. With an overwhelming number of active attendees, a server may become overloaded, and newly connected users may see a connection error. 

The maxBroadcasters and maxWatchers parameters should be specified for each participant in the URL. Please refer to &maxWatchers parameter. 

Type: Numeric, default = 0. 

Example: ```&maxBroadcasters=10```

#### &amp;maxWatchers=&lt;num&gt; 

This sets the number of concurrent attendees in a room at one time. This is the maximum value of users/viewers that can be in a room and be represented by their own "participant" rectangle. Participants can turn on their cam/mic at any time.   

The maxBroadcasters and maxWatchers parameters should be specified for each participant in the URL. Please refer to *&maxWatchers* parameter. 

Type: Numeric, default = 0. 

Example: ```&maxWatchers=50``` 

#### &amp;minimizeTiles=&lt;true|false&gt;

This helps to squeeze the participants' tiles so that as many participants as possible can fit into one view without scrolling. This parameter allows increasing the number of simultaneously displayed tiles of participants on a screen to the maximum.

Type: Boolean, default = false.

Example: ```&minimizeTiles=true```

#### &amp;nameScreenDisabled=&lt;true|false&gt;

This helps to skip the welcome page with the name input field and cam/mic selection. You can skip the cam/mic selection elements when you already know the user's devices, or you need to connect the user immediately.

In that case, you should specify a user’s name in the attribute and use ClientAPI for "Join" method. Please refer to the "Join" method.

Type: Boolean, default = false.

Example: ```&nameScreenDisabled=true```

#### &amp;peerId=&lt;id&gt;

This is an identifier of a participant in case you want to set it explicitly. It is used for synchronization with your database or enterprise services.

You can select any value you prefer: number, GUID or even email.

**Please, note:** Only one session is possible with one unique identifier. If another participant with the same peerID connects, a new session will be created for the recent participant, while the session of the first one will be terminated. This is also the case when a link is opened in a different browser: a new session will be created with the recent browser, while previous connection will be terminated.

Example:

* User1 opens a link with &peerID=5 and then User2 opens the same link with &peerID=5. The second user will log in, but the server connection with the first user will be closed and the User1 will not be able to participate. Thus, you need to use two different peerID's.
* A User opens a link with &peerID=5 on a desktop computer and then opens the same link on a mobile device. They will log in on the mobile device, but the server connection with the desktop computer will be closed.

The peerID is used for:

* ClientAPI methods when you want to apply a method for a specific user.
* Download statistics on the attendance of a video call room and the duration of the users' presence on a call.

Type = String, default value = set by the video server with a random GUID value.

Example: ```&peerId=802380f4-dd70-4d60-9738-fb5ae8709ae7```

#### &amp;role=&lt;role&gt;

This parameter sets a privileged role for a participant.

Values:

* [not set] — regular participant.
* moderator —  super-user who can manage participants and video call settings.
* interpreter —  (beta) special role for interpreters from one language to another. A special audio channel is dedicated for them. Be aware that users of this role cannot turn on their cameras. 

By default, all attendees are regular participants. They can manage their own cams and mics. But a moderator can manage participants, turn off their cams/mics, allow entering, etc. You can assign the "moderator" role to a host, and all other attendees will be regular participants. For more details, please refer to the Moderator feature.

Type: String, default = not set.

Example: ```&role=moderator```

#### roomId=&lt;id&gt;

A room ID is set by you according to your rules. You don't need to call any special methods that might restrict you in naming rooms. 

An identifier consists of two parts: «server ID» + «room ID». A server ID is a "servN". Please see the List of servers. A room ID is any alphanumeric character set. If a server is not specified, you will be connected to a default one. If a server is specified explicitly, you will be connected to it.

Please note that &roomId determines the room number, but the prefixes */call/* or */webinar/* are interface modifiers. Thus, the methods */call/?roomId=testroom* and */webinar/?roomId=testroom* lead to the same room with a different interface. 

Type: String. Default = required field to be specified explicitly.

Example:

```
&roomId=1111   
&roomId=bokxlj33   
&roomId=serv21111   
&roomId=serv2bokxlj33   
&roomId=serv2f53c1aa5-1492-4964-b4fe-f83b5b545e8d
``` 

#### &amp;sortPeers=&lt;true|false&gt;

It is used to arrange tiles of participants so that those who have cameras on will be displayed on the top.  

By default, the participants' tiles are ordered based on the time they connected. This order does not change during a meeting. For example, if first users connect without video, and then the last participant turns on the camera, they may be placed under the scrolling (visible area) of the screen and no one will see them. 

Using this parameter allows you to show active participants with video. However, enabling this option increases load on participants' CPUs. 

Type=Boolean, default value = false.

Example: ```&sortPeers=true```

#### &amp;startWithFS=&lt;true|false&gt;

It helps to start a meeting room in the Full Screen mode. Please see the "Full Screen mode" in our Knowledge Base.

Type: Boolean, default = false.

Example: ```&startWithFS=true```

#### &amp;token=&lt;jwt&gt;

The JSON Web Tokens is an open, standard method for representing claims securely between two parties: <a href="https://jwt.io" target="_blank">https://jwt.io/</a>

The JWT allows you:

* To specify attributes inside a token, rather than URL attributes.
* Sign a token with a secret key and be sure that all parameters in it are specified by you, and cannot be changed by someone else.

Please see "Security" for details.

Type=String, default value = not set.

Example: 

```
&token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoibW9kZXJhdG9yIiwic3RhcnRUaW1lIjoiMjAyMS0wNi0yMVQwMDowMDowMC4wWiJ9.Atj-TPL_GSLyuI565pI6X6GFjopXf62C6y4OgeeEk9KEb1cosDmo2sytpBv44PRuMRwgDg8AcqlMMgA0kcdJrBZ7AAywjb6RZVXlian6-6XQ0zx7OhYyDo2-mVxCO9dgYroXfz2Fw8lyNuqFl0AKEfFMPKaYf46u5kjwWmSyhh7bLbL969Eu3zWMk3sYLpWxULyndhkXrLqOVspK08Mla-AbxGJ94pZXJCKHK5UslhrGJ6RProN5nL4NaXOCKRX0ffKnklxiyn9MgKf0cc6Za0GCpjg-d3y6-UOVd0AXW8TWR-RllTgXaTUMMSLyWzHPsv-e2O-GsA0WJnBJEg
```

#### &amp;tokenLifetime=&lt;milliseconds&gt;

The parameter limits the lifetime of a token. The lifetime is counted in milliseconds from the first connection. After the specified period has expired, a participant cannot reconnect to the room with the token.

Type=Number, default value = not set.

Example: ```&tokenLifetime=60000```

#### &amp;video=&lt;url&gt;

This is a super feature for joint viewing of online broadcasts directly in a video call room. No, you do not need to "share screen" with others and lose both video and audio quality and overload one of the participant's PC. You just need to insert a code of the YouTube player, our player, or any other HTML player, and it will appear for all participants in the room. Besides, the player saves all its standard functions: adaptive bitrate, counting unique viewers, displaying ads, Google Analytics counter, etc. Please refer to .

Type=String, default value = not set.

Example: ```https://meet.gcore.com/call/?roomId=serv2testroom&displayName=John%20Snow&video=https%3A%2F%2Fwww.youtube.com%2Fembed%2FXBPjVzSoepo```

#### &amp;waitingRoom=&lt;true|false&gt;

The waiting room function allows a moderator to manually determine which user is allowed to enter a video call room and who is not.

After enabling the feature, each participant will see the "Please wait for confirmation" message.

Type: Boolean, default = false.

Example: ```&waitingRoom=true```

### Debug and Dev URL attributes only

A set of debug attributes can be used by developers to create and test a video call room.

These parameters are used for debugging only.

#### &amp;accessUrl=&lt;url&gt;

A URL of REST method to check accessToken. Please see "Authentication of participants" for details. 

Make sure you use ```https://``` instead of ```http://```. 

Please do not use this attribute publicly. For public use, a URL must be registered on our server or in your account. 

Type=String, default value = not set.

Example: ```&accessUrl= https://your.domain.com/api/gcore/auth```

#### &amp;apiEvent=&lt;url&gt;

A URL to get webhooks/events from a video calls server. Please see "Webhooks" for details.

Make sure you use ```https://``` instead of ```http://```.

Please do not use this attribute publicly. For public use, URL must be registered on our server or in your account.

Type=String, default value = not set.

Example: ```&apiEvent=https://your.domain.com/api/gcore/webhook```

#### &amp;authEvent=&lt;header&gt;

This is for extra header request parameters and credentials for server-side webhooks/events. Use it for enabling Basic or Bearer authentication, etc.

Please do not use this attribute publicly. For public use, a URL must be registered on our server or in your account.

Type=String, default value = not set.

Example: ```&authorizationAccess=Basic%20Z2NvcmVfbWVldDo4dFpvOTZLSkhWRXFBanFBQlpZQg%3D%3D```

#### &amp;authorizationAccess=&lt;header&gt;

This is for extra header request parameters and credentials for server-side check of authorization.

Use it for enabling Basic or Bearer authentication, etc.

Please do not use this attribute publicly. For public use, URL must be registered on our server or in your account.

Type=String, default value = not set.

Example: ```&authorizationAccess=Basic%20Z2NvcmVfbWVldDo4dFpvOTZLSkhWRXFBanFBQlpZQg%3D%3D```

### Moderator 

By default, all attendees are regular participants. They can manage their own cams and mics. But a moderator can manage participants, turn off their cams/mics, allow entering etc. 

A moderator can do the following:  

1\. Operate the "Waiting room" function:  

- Activate and deactivate a waiting room.
- Confirm and reject a participant's entry    

2\. Operate cameras and microphones of participants: 

- Allow or disallow cameras and microphones.
- Ask participants to turn on cameras and microphones.

3\. Operate the sharing screen feature:

- Allow or disallow the screen sharing.
- Ask to turn on the screen sharing.

4\. Operate raised hands: 

- Remove a participant's hand.

5\. Operate the list of participants: 

- Kick the user out of the room. 

To use the moderator role, you need to follow these steps: 

1.  Get a Secret Key for JWT. See the "Security" section.  
2.  Generate a link for regular participants with &roomId=XXX parameter. 
3.  Generate a JWT token and add additional attribute &role=moderator to it.  
4.  Generate a link for moderators. Concatenate the JWT token from Step 3 to the general link from Step 2. 

Example:

Link for a regular user:

```
https://meet.gcore.com/call/?roomId=serv0_test1
```

Link for a moderator:

```
https://meet.gcore.com/call/?roomId=serv0_test1&token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoibW9kZXJhdG9yIiwid2FpdGluZ1Jvb20iOnRydWUsImhhbmRFbmFibGVkIjp0cnVlfQ.DO_JHMDfK2mi5rycIepLVxDVs0qcQAXAhHvI7hcOIjw
```

Where JWT is:

- HEADER: (ALGORITHM & TOKEN TYPE)
- { "alg": "HS256", "typ": "JWT" }
- PAYLOAD: (DATA)
- { "role": "moderator", "waitingRoom": true, "handEnabled": true, "roomId": "serv0_test1" }

### Recording

#### What can be recorded 

Recording is a video recording of the entire interface of a meeting room, as it is seen by regular viewers. A video includes:  

- attendees,  
- screen sharing, 
- original audio of speakers.  

Recording is a complex process that is carried out by our professional Streaming Platform. The video is recorded on a cloud server and is also stored in the Cloud of the Streaming Platform.   

When a meeting is over and a video is recorded, it is automatically converted and becomes available for viewing in the video player. You can download the video, copy the player code for viewing on a web site, or get HLS video stream and insert manifest.m3u8 into your mobile app. 

Recording can be started by moderator only. 

To record, you need to follow these steps: 

1\.  Generate a JWT token with additional attribute role=moderator inside it. 
2\.  Add attribute ```canRecord=_true``` into the JWT. 
3\.  Open a room with the link.  
4\.  Open the "Moderator" panel inside a room.  
5\.  Press the "Record" button.  
6\.  Press the "Stop" button. 

A JWT example: 

PAYLOAD: (DATA) 

```
{ "role": "moderator", "canRecord": true, "roomId": "serv0_test1" } 
```

#### Auto-recording 

By default, a moderator can manually record meetings.  

If you want to record all meeting rooms automatically, you can enable the "Auto Recording" feature for your account.  

- Recording starts automatically for every new room in ±60 seconds after the first user logs in. 
- Recording goes on for as long as there is at least one user in the room. 
- Recording stops automatically after ±60 seconds after last user logs out. Thus, if by chance all users leave the room and return without a timeout, then the recording will continue. 

Please note that, if one of the users forgets to close a browser tab, they still will be present in the room. And if they are present in the room, recording will continue. 

Ask your manager or support team to enable the Auto recording feature. 

#### Where to find recorded videos

Recording of room is made by our Streaming Platform. Video files are stored in the media storage. 

Steps to find a video: 

1.  Open your personal dashboard via link: ```https://streaming.gcore.com/```.  
2.  Select the "Video hosting" tab. 
3.  Select videos with the "Recording" title with the exact roomId and the exact time.  
4.  Open the video.  
5.  Copy the video player code, link of the player, or download the video on the "export" tab. 

Also, you can use Special API of the Streaming Platform. Please see the "Getting Recorded Video" section. 

#### How to set up our recording feature 

As you know, recording of a room is made by our Streaming Platform, and video files are stored in the media storage. 

Steps: 

1. Generate a permanent token in your personal account via the <a href="https://accounts.gcore.com/profile/api-tokens" target="_blank">link</a>.  
2. Use parameters: 
  - Name = "Video conference recording" or any title you prefer; 
  - Role = Administrator; 
  - Expiration = Never expire. 
3. Copy the token from the result page 
4. Send us the copied token 
5. Add the ```&canRecord``` advanced attribute to the URL for a moderator, or ask us to set the Auto Recording feature.

Example of a permanent token: 

```
1030$0b219f0239c7a418c499a9b0f4d93f0b081700000c346ad254694b15d09981d7cf6b24e41a243df6e9e23d5483820d98921d64c0cb06e9981c842ab31fd0e4db 
```

### Language Interpretation (beta)

In normal use, each user hears the original audio of a speaker. The interpretation feature allows users to hear the interpreter’s speech, that they can understand, in simultaneous translation mode. 

If a moderator wants to include interpreters in their meetings or webinars, they now can enable Language Interpretation. With it, a host can designate an unlimited number (over 20) of participants as interpreters during a video session.  

When a meeting or webinar starts, a host can turn on the interpretation feature which will provide interpreters with their own audio channels for the language they translate to. Attendees can then select the channel and listen to the audio translated in the language they need. They can also mute the original audio so not to hear it at a lower volume together with their chosen language.    

In case of meetings with interpretation, only the original audio of a meeting or webinar is recorded, not the translated speech.  

The languages below are available by default. If you need more, just please let us know: 

- Chinese, zh 
- Dutch, nl 
- English, en 
- French, fr 
- German, de 
- Luxembourgian, lb 
- Portuguese, pt
- Spanish, es 
- Swedish, sv 
- Ukrainian, uk  

There can be more than one interpreter for one language. If several interpreters use the same link, all of them can speak in the corresponding channel. They can speak both simultaneously or/and consecutively. For consecutive interpretation, they just need to mute the microphones. 

For regular attendees, new language automatically appears when an interpreter is connected. 

If an interpreter disconnects from a room for whatever reason, regular users can select the language for 30 seconds. If none of the interpreters reconnects, the language will become unavailable for select, and listeners of that language will be switched to the original audio.   

A JWT example is: 

- PAYLOAD: (DATA) 
- ```{ "role": "interpreter", "featureInterpreters": true, "intLang": "de", "roomId": "serv0_test1" }``` 

<img src="https://assets.gcore.pro/docs/streaming-platform/api/real-time-video-api-tutorial/11649788899601.png" alt="example">

## Client API

### Iframe Integration

#### Example of iFrame integration

```
<iframe allow="camera; microphone; display-capture" style="height: 100%; width: 100%;" src="https://meet.gcore.com/webinar/?roomId=qwesfder4w4&displayName=Tom&accessToken=sda3-q23aed-aerae&peerId=123123-321as-waaew-ads&apiEvent=https://example.com/api/meet&accessUrl=https://example.com/api/accessCheck/&itisparticipant=true&nameScreenDisabled=true&startWithFS=true&controlsDisabled=true"></iframe>
```

Please see Embed a <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial#embed-room-on-a-site">Room on Site</a> and <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial#attribute-details">Attributes details</a>.

#### Interaction with iFrame

There is a special library for interacting with iframe, which should be loaded separately.

```
<script type="text/javascript" charset="utf-8" src="https://<yourdomain.gvideo.co>/meetBridgeApi.js"></script> 
```

Example:

```
<script type="text/javascript" charset="utf-8" src="https://meet.gcore.com/meetBridgeApi.js"></script> 
```

JavaScript's method for initialization:

```
meetIframeBridge = new MeetIframeBridge.default({ element: $iframe.get(0), roomId: "serv1m6oci9e8" });
```

Where:

- `element` is a DOM object of iFrame.
- `roomId`is an ID of the room.

**Note**: Before initializing a class, you need to wait for an iframe element to be loaded.

#### Public methods of Real-Time Video iframe

Client API methods allow you to control a video room, perform actions with hidden main controls, react to what is happening in a room.

Example of method:

**Initializing**:

```
var meetIframeBridge;  
$('#meetframe').on("load", function() { 
            meetIframeBridge = new MeetIframeBridge.default({ element: $("#meetframe")[0], roomId: "serv1m6oci9e8" });       
});
```

**Joining**:

```
meetIframeBridge.method({ name: "join", data: {constraints: {video: false, audio: false }}, callback: (e) => { alert(1); return true; } });
```

**Volume adjusting**:

```
meetIframeBridge.method({ name: "setVolume", data: 100, callback: (e) => { alert(1); return true; } });
```

**Name changing**:

```
meetIframeBridge.method({ name: "changeDisplayName", data: "Tom", callback: (e) => { // return value } });
```

**Getting screenshot of a user’s video**:

```
meetIframeBridge.method({ name: "getScreenshotByPeerId", data: "id", callback: (e) => { // "e" parameter will have screenshotted data } });
```

<table class="tg">
<thead>
  <tr>
    <th  >Method name</th>
    <th  >Parameters</th>
    <th  >Description</th>
    <th class="tg-9r46"></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td  >join</td>
    <td   >"constraints" = object<br> <br>Setup new devices:<br>data: {constraints: { video: { deviceId: 'id', label: 'label', groupId: 'groupId', kind: 'video'}, audio: { deviceId: 'deviceId', label: 'label', groupId: 'groupId', kind: 'audio'}}}<br> <br>If you want to use devices by default:<br>data: {constraints: {video: true, audio: true }}<br> </td>
    <td   >The Join method receives a stream from these devices (usually used with the <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial#nameScreenDisabled=true|false">nameScreenDisabled</a> parameter)</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >enableMic</td>
    <td class="tg-6tt1"> </td>
    <td   >Unmute a microphone</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >disableMic</td>
    <td class="tg-6tt1"> </td>
    <td   >Mute a microphone</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >enableWebcam</td>
    <td class="tg-6tt1"> </td>
    <td   >Turn on a camera</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >disableWebcam</td>
    <td class="tg-6tt1"> </td>
    <td   >Turn off a camera</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >enableShare</td>
    <td class="tg-6tt1"> </td>
    <td   >Enable the screen sharing</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >disableShare</td>
    <td class="tg-6tt1"> </td>
    <td   >Disable the screen sharing</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >changeDisplayName</td>
    <td   >"name"<br>data: string</td>
    <td   >Change a name</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >setVolume</td>
    <td   >"volume"<br>data: number</td>
    <td   >Set a volume level (0 - 100)</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >getScreenshotByPeerId</td>
    <td   >"peerId"<br>data: string</td>
    <td   >Get a screenshot of a user with an id equal to peerId, the screenshot is given in base64</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >setControlsVisible</td>
    <td   >"visible"<br>data: bool</td>
    <td   >Show and hide controls</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >isCameraEnabled</td>
    <td class="tg-6tt1"> </td>
    <td   >The user's camera is enabled</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >isMicroEnabled</td>
    <td class="tg-6tt1"> </td>
    <td   >The user's microphone is enabled</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >isShareEnabled</td>
    <td class="tg-6tt1"> </td>
    <td   >The user's sharing is enabled</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >changeDevice</td>
    <td   >"constraints" = object<br>data: {constraints: { audio: { deviceId: 'deviceId', label: 'label', groupId: 'groupId', kind: 'audio'}}}<br> <br>or<br> <br>data: {constraints: { video: { deviceId: 'id', label: 'label', groupId: 'groupId', kind: 'video'}}}</td>
    <td   >Change a device on the fly. Specify 1 (one) device per method call.</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >playAudio</td>
    <td class="tg-6tt1"> </td>
    <td   >Start audio that failed to play (usually used together with autoplayWithoutAudioTrack)</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >muteAudio</td>
    <td class="tg-6tt1"> </td>
    <td   >Mute incoming audio</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >unmuteAudio</td>
    <td class="tg-6tt1"> </td>
    <td   >Unmute incoming audio</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >setBitrate</td>
    <td   >"bitrateValue"<br>data: number</td>
    <td   >Set the maximum video bitrate in a room</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >isFullscreenEnabled</td>
    <td class="tg-6tt1"> </td>
    <td   >The fullscreen is enabled</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >enableFullscreen</td>
    <td class="tg-6tt1"> </td>
    <td   >Enable the fullscreen</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >disableFullscreen</td>
    <td class="tg-6tt1"> </td>
    <td   >Disable the fullscreen</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >enablePin</td>
    <td   >"peerId"<br>data: string</td>
    <td   >Enable the PIN for a specified user</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >disablePin</td>
    <td class="tg-6tt1"> </td>
    <td   >Disable the PIN </td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >setLocale</td>
    <td   >"locale"<br>data: string</td>
    <td   >Dynamic language changes, available languages: en, ru</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >disabledTrackByModerator</td>
    <td   >"peerId", "kind = (audio || video)"<br>data: {userPeerId: 'peerId', kind: 'audio'}</td>
    <td   >Turn off video or audio from another user in a moderator mode. Only a moderator can disable video and audio</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >disableAllMics</td>
    <td   > </td>
    <td   >Mute mics of all participants. It can be used only by a moderator</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td   >disableAllCameras</td>
    <td   > </td>
    <td   >Turn off cams of all participants. It can be used only by a moderator</td>
    <td class="tg-twlz"></td>
  </tr>
  <tr>
    <td  >setHideIndicators</td>
    <td  >"hide"<br>data: bool</td>
    <td  >Show and hide indicators of other users (icons for microphones, cameras, username, pin button)</td>
    <td class="tg-0lax"></td>
  </tr>
</tbody>
</table>



#### Events from an iframe

Events on the client side allow you to react quickly to actions in a video room.

Example of event subscription:

```
meetIframeBridge.on('switchOnCamera', (e) => { your code here });
```




| Event name          | Data                 | Description                                                                                     |
|-------------------------|---------------------------|-----------------------------------------------------------------------------------------------------|
| join                | peerId, displayName   | A user is added to the room.                                                                    |
|    ready              |                      | Iframe is fully loaded and ready to go.                                                        |
| readyToJoin        |                     | The Room is ready to "join".                                                                  |
| switchOnCamera      | peerId, displayName   | Camera is on                                                                                   |
| switchOffCamera     | peerId, displayName   | Camera is off                                                                                   |
| nerrorGetCamera      | peerId, displayName   | Camera connection error                                                                         |
| switchOnMic         | peerId, displayName   | Microphone is on                                                                                |
| switchOffMic        | peerId, displayName   | Microphone off                                                                                  |
| errorGetMic         | peerId, displayName   | Microphone connection error                                                                     |
| switchOnShare       | peerId, displayName   | Screen sharing enabled                                                                          |
| switchOffShare      | peerId, displayName   | Screen sharing is off                                                                           |
| errorGetShare       | peerId, displayName   | Screen sharing error                                                                            |
| newPeer             | peerId, displayName   | New user connected                                                                              |
| peerClosed          | peerId, displayName   | The user left the room                                                                          |
| connectionFailed    |                           | Connection to the server failed                                                                 |
| disconnected        |                           | Connection to the server was closed (example: the server is unavailable)                        |
| connectionClosed    |                           | The user has closed the connection to the server                                                |
| connectionError     | peerId, error message | An error message appeared on a client's side or on a server's side                              |
| playingAudioPrevent |                           | Audio doesn't play unless clicking (used together with the autoplayWithoutAudioTrack parameter) |
| switchOnPin         | peerId                | The PIN function is on                                                                          |
| switchOffPin        |                           | The PIN function is off                                                                         |
| errorGetPin         | peerId                | The PIN feature error                                                                           |


## Server API

### Server Endpoints

#### Video Conferencing Endpoints

Please see REST API specification. Below is a brief list of endpoints.

To access Server API methods, you need to be authenticated. Please see "Server API Authentication" below.

<table class="tg">
<thead>
  <tr>
    <th  >Method name</th>
    <th  >Parameters</th>
    <th  >Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td  >/rooms/:roomId/closePeer</td>
    <td   >peerId, <br>body:{peerId: id}</td>
    <td   >Remove a user from a room, POST</td>
  </tr>
  <tr>
    <td   >/rooms/:roomId/closeRoom</td>
    <td class="tg-6tt1"> </td>
    <td   > Delete a room, GET</td>
  </tr>
  <tr>
    <td   >/rooms/:roomId/durationOfBroadcast</td>
    <td class="tg-6tt1"> </td>
    <td   >View how long the room existed, GET</td>
  </tr>
  <tr>
    <td class="tg-6tt1">/rooms/:roomId/exists</td>
    <td class="tg-6tt1"> </td>
    <td   >Check if the specified room exists, GET</td>
  </tr>
  <tr>
    <td   >/rooms/:roomId/existingPeer<br>(depricated)</td>
    <td   >peerId,<br>body:{peerId: id}</td>
    <td   >Check does the user exist in the room, POST<br> <br>Please, use new method instead – /rooms/:roomId/existingPeer/:peerId</td>
  </tr>
  <tr>
    <td   >/rooms/:roomId/existingPeer/:peerId</td>
    <td class="tg-6tt1"> </td>
    <td   >Check does the user exist in the room, GET</td>
  </tr>
  <tr>
    <td   >/rooms/:roomId/numberPeers</td>
    <td class="tg-6tt1"> </td>
    <td   >View the number of participants in the room, GET</td>
  </tr>
  <tr>
    <td   >chat/clear-rooms</td>
    <td class="tg-6tt1">body: { hostname: string, rooms: [{roomId: id, type: "call"|"webinar"}]}</td>
    <td   >Clear chat history in specific rooms, POST<br> <br>Where:<br>"hostname" – domain name<br>"type" – type of room, unnecessary attribute, where "call" is default value</td>
  </tr>
  <tr>
    <td   >/rooms/:roomId/recording/start</td>
    <td class="tg-6tt1"> </td>
    <td   >Start recording for a specific room, POST</td>
  </tr>
  <tr>
    <td   >/rooms/:roomId/recording/stop</td>
    <td class="tg-6tt1"> </td>
    <td   >Stop recording for a specific room, POST</td>
  </tr>
  <tr>
    <td   >/rooms/:roomId/recording</td>
    <td class="tg-6tt1"> </td>
    <td   >Check video recording status, GET</td>
  </tr>
</tbody>
</table>


Example #1:

```
curl -L -X GET 'https://webrtc3.gvideo.co/rooms/serv1l8bsg8zw/durationOfBroadcast' -H 'Authorization: Bearer eyJ0eXAiOiJKV'
```

Example #2:

```
curl -X POST 'https://webrtc3.gvideo.co/rooms/serv0dxrpxoqr/recording/start' -H 'Authorization: Bearer eyJ0eXAiOiJKV'
```

Example #3:

Request:   

```
curl -L -X POST 'https://webrtc3.gvideo.co/chat/clear-rooms' \  
-H 'Authorization: Bearer eyJ0eXAiOiJKV' \  
-H 'Content-Type: application/json' \  
--data-raw '{  
   "hostname": "102748.gvideo.co",  
   "rooms": [  
    {  
      "roomId": "serv0d17nfe1s"  
    }  
  ]  
}'
```

Response: ```200 OK {"deleted":["serv0d17nfe1s"]}``` 

#### Common Response Codes

There is a list of common response codes of REST API methods:

| Code | Response Label        | Description                               |
|------|-----------------------|-------------------------------------------|
| 200  | OK                    | OK                                        |
| 400  | Bad Request           | Token, roomId, peerId not found           |
| 401  | Unauthorized          | Invalid token                             |
| 403  | Forbidden             | Access denied, contact your administrator |
| 404  | Not found             | Invalid room ID                           |
| 500  | Internal Server Error | Server connection error                   |


#### List of servers

We have a lot of servers worldwide. Some of them are for public usage.

A server can be derived from a room ID. For example: &roomId = serv1qweqwe.

| Server | Country    | Server URL                      | Description                                                    |
|------------|----------------|-------------------------------------|--------------------------------------------------------------------|
| serv0  | Luxembourg | ```https://webrtc3.gvideo.co:443```   | DEFAULT server, unless states otherwise (like &amp;roomId=BMW) |
| serv1  | Australia  | ```https://webrtc4.gvideo.co:443```   |                                                                |
| serv2  | USA        | ```https://webrtc5.gvideo.co:443```   |                                                                |
| serv3  | Singapore  | ```https://webrtc6.gvideo.co:443``` |                                                              |


**Note**: There is an offset in a server’s URL. This is a temporary but necessary solution that will be changed soon. We will inform you additionally.

For debug purposes, you can call a server endpoint directly. But for public use, we apply strong restrictions and increase the level of security. Please tell us if you want to allow server-calls for specific servers and security parameters. In this case, all other calls will be rejected.

#### Example of  video server performance check 

A call method such as:

```
https://webrtc3.gvideo.co/rooms/serv0l8bsg8zw1/durationOfBroadcast
```

For a non-existent room, the answer will be 400 error. If it is a 500 error or a timeout error, the server is unavailable.

### Webhooks

Webhooks are user-defined callbacks triggered by meeting events. Webhooks are pushed to the URL specified in the apiEvent attribute:

| Event name | Parameters                  | Description        |
|------------|-----------------------------|--------------------|
| joinPeer   | roomId, peerId, displayName | New user connected |
| closePeer  | roomId, peerId, displayName | User disconnected  |


#### Webhook joinPeer

This is a method of notifying that a participant has joined a room. This method is used for extra authentication on your side.

```
POST /joinPeer
```

Attributes:

- roomId
- peerId
- displayName

Example: 

```
{"event":"connected","roomId":"44fde071","peerId":"de9b6927","displayName":"user16"}
```

Example:

```
https://meet.gcore.com/call/?roomId=44fde071&displayName=user16&accessToken=caa630bb&peerId=de9b6927&apiEvent=https://dev.com/api/events&accessUrl=https://dev.com/api/accesscheck
```

#### Webhook closePeer

This is a method of notifying that the connection between a server and a participant’s browser has been closed. In most cases, this means that the participant has left the room intentionally or due to a connection issue.

```
POST /closePeer
```

Attributes:

- roomId
- peerId
- displayName

Example:

```
{"event":"disconnected","roomId":"44fde071","peerId":"de9b6927","displayName":"user16"}
```

### Special API of Streaming Platform

Video conferencing tool manages data in real time. Thus, Server API and Client API of video conferencing are designed to control the behavior of users and video rooms in real time.

Statistics on usage and video recordings are stored in the Streaming Platform. Thus, please use

Video Platform’s REST API for those methods: <a href="https://api.gcore.com/docs/streaming" target="_blank">https://api.gcore.com/docs/streaming</a>.

To access Video Platform API, you need to be authenticated. Please see "Authentication of Participants and Access Limitation" above.

#### Statistics

Video conferencing tool sends statistics data every 30 seconds to the Video Platform servers. This means that the usage statistics can always be multiply by 30 seconds. 

1. General data about a room:

This is a summary about a room.

```
GET /streaming/statistics/peers/summary
```

Attributes:

- room_id
- from – start period of selecting data
- to – finish period of selecting data

Output codes: 

- 200 – OK, json object with the data. 
- 400 – Bad Request, in case of incorrect input attribute values. 
- 403 – Unauthorized access.   
- 404 – Not found, in case there is no data for a room or room is not found in statistics. 
- 500 – Internal error. 

Output values:

- participants – total sum of unique participants in a room.
- start_time – UNIX time in seconds when the first participant entered, ex = 1624276920.
- end_time – UNIX time in seconds when the last participant left, ex = 1624358940
- duration – number of seconds when the room was «active», calculated as difference from the end_time parameter value and the start_time parameter value. Ex = 90660

**Note**: The result is aggregated data for all sessions of the specified room between «from» period until «to» period. Thus, if you use the same room ID each day, then use separate periods.

Example:

```https://meet.gcore.com/call/?roomId=serv2test1``` used for 60 minutes each day on Monday Jun 21 and on Tuesday Jun 22.

- /summary?from=2021-06-21T00:00:00.0Z&to=2021-06-21T23:59:59.99Z&room_id=serv1test1 – will return 60 minutes (60 mins on Jun 21).
- /summary?from=2021-06-21T00:00:00.0Z&to=2021-06-22T23:59:59.99Z&room_id=serv1test1 – will return 120 minutes (60 mins on Jun 21 + 60 mins on Jun 22).

Example of usage:

```
https://api.gcore.com/streaming/statistics/peers/summary/?from=2021-06-21T00:00:00.0Z&to=2021-06-22T23:59:59.99Z&room_id=serv2test2a
```

Example of return data:

```
{   
    "data": {   
        "participants": 3,   
        "start_time": 1624268280,   
        "end_time": 1624358940,   
        "duration": 90660   
    },   
    "errors": []  
}
```

2. Detailed data per participant:

This is data for each participant’s sessions in a room.

If an event lasted 60 minutes, and the user attended it for the first 5 minutes, then left the room, and joined again for the last 5 minutes, the statistics will reflect two sessions, each lasted for five minutes: 5 min + 5 min = 10 minutes (that is, = 600 seconds, instead of 3600 seconds of the total duration).

```
GET /streaming/statistics/peers/
```

Attributes:

- room_id
- from
- to

Output codes:

- 200 – OK, json object with the data.
- 400 – Bad Request, in case of incorrect input attribute values.
- 403 – Unauthorized access.
- 404 – Not found, in case there is no data for room or room is not found in statistics.
- 500 – Internal error.

Output values:

- array of participant sessions
- person_id – peerId data (your value, if it was specified in URL attributes, or unique GUID made automatically if it was omitted)
- join_time – UNIX time in seconds of the participant's join time, ex = 1624268280
- leave_time – UNIX time in seconds of the participant's leave time, ex = 1624269300
- duration – number of seconds of the session, ex = 1260

Example of usage:

```
https://api.gcore.com/streaming/statistics/peers/summary?from=2021-06-21T00:00:00.0Z&to=2021-06-22T23:59:59.99Z&room_id=serv2test2a
```

Example of return data:

```
{   
    "data": [   
        {   
            "person_id": "peer2",   
            "join_time": 1624268640,   
            "leave_time": 1624269300,   
            "duration": 660   
        },   
        {   
            "person_id": "peer1",   
            "join_time": 1624270800,   
            "leave_time": 1624274520,   
            "duration": 3720   
        },   
        {   
            "person_id": "peer1",   
            "join_time": 1624270380,   
            "leave_time": 1624270740,   
            "duration": 360   
        }   
    ],   
    "errors": []   
} 
```

#### Getting Recorded Video 

Recordings of room meetings are stored in the media storage of the Streaming Platform.

You need to search the video and then get by id.

1. Search a video

```
GET /streaming/videos/search
```

**Attributes**: q – Search query. The search performed among all video names. Specify roomId as a search query.

**Output values**: Array of available videos for specified ID.

If a session lasted more than 4 hours, the recording will be divided into several videos for 4 hours each. In this case, you need to get all videos separately.

Please see more details in <a href="https://api.gcore.com/docs/streaming#operation/get_api_videos_id" target="_blank">documentation</a>. 

2. Get video metadata 

```
GET https://api.gcore.com/streaming/videos/{video_id}
```

Please see more details in <a href="https://api.gcore.com/docs/streaming#operation/get_api_videos_id" target="_blank">documentation</a>.  

**Output values**: Metadata of the video. Use fields "hls_url" for .m3u8 stream in external players or "origin_host"+"origin_resource" for getting an original MP4 file.  

Example of output data:  

```
{   
  "hls_url": "https://id10835.gcore.com/videos/10835_UaX2pjxen2guUw3/master.m3u8",   
  "origin_host": "s-ed1.cloud.gcore.lu",   
  "origin_resource": "9208-mediaplatform10835/videos/UaX2pjxen2guUw3.mp4",   
}

```

Please see more details in <a href="https://api.gcore.com/docs/streaming#operation/get_api_videos_id" target="_blank">documentation</a>.  

Example of usage: 

Step 1: ```https://api.gcore.com/streaming/videos/search?q=serv1test2a```

Step 2: ```https://api.gcore.com/streaming/videos/117800```

#### Rate Limits

There is a general limit of four requests per second. If you exceed the rate limit, you will receive a message.

## Security

Calling API should be done through an endpoint on your server. This will help to avoid exposing secret keys to users and to keep them safe.

### Validating Client API Requests

#### What is a JWT 

To access Client API, we use  JSON Web Tokens (JWT), which is an open, industry standard  RFC 7519  method for representing claims securely between two parties.

For more information what JWT is and how to use it please visit <a href="https://jwt.io/introduction" target="_blank">https://jwt.io/introduction</a>

JWT allows you to accurately determine the validity of the video room settings and unambiguously determine the belonging of the token to your account. 

To use the JWT, you need a Public & Secret Key. A new key is generated by you. Send us your public part of the key via support or personal manager. Please see "RSA Public & Secret Key generation" section below for details.

#### Limitations when using JWT

You can activate the option to use the JWT in your account. If you activate it, you will have to send a JWT &token=xxx in every request. Without a token, the "Access denied" message will appear.

If you activate the JWT option, you will not be able to use the &accessToken=xxx attribute.

#### JWT Header

The header typically consists of two parts: the type of the token and the signing algorithm being used.

Signing algorithms are:

- RS256 – asymmetric key,
- HS256 – symmetric key.

```
HEADER:ALGORITHM & TOKEN TYPE   
{  
"typ": "JWT",  
"alg": "RS256"  
}
```

```
HEADER:ALGORITHM & TOKEN TYPE   
{  
"typ": "JWT",  
"alg": "HS256"  
}
```

#### JWT Body

The body of a JWT contains important data that should be signed and verified. The data in a JWT has a higher priority over the values of the same parameters specified in the URL attributes. This means that if an attribute value is specified both in a JWT and in the URL attribute set, the value from the JWT will be used.

Please refer to the table of attributes above to see the parameters that can be set in a JWT.

Priority of data from a JWT and URL:

- Parameters with the "JWT" label can be specified inside a token or as an attribute in the URL. If an attribute value is specified in a token, the value in the URL is ignored. If an attribute is not specified in a token, the attribute value will be taken from the URL.
- Parameters with the "URL" label can only be specified as an attribute in the URL.

The list of extra attributes for a JWT: 

- startTime – planned start time of an event in a video room. Please see "Webhook joinPeer method". Date/time is in UTC time zone only, represented as number (milliseconds since Unix epoch), formatted as ISO 8601.
- iat – (optional) Issued At. The "iat" claim identifies the time at which the JWT was issued. This claim can be used to determine the age of a JWT. Date/time is in UTC time zone only, representedas number (milliseconds since Unix epoch), formatted as ISO 8601.

The list of attributes is expanding, tell us what attributes (from general list of URL attributes) you need inside a token.

```
PAYLOAD:DATA  
{  
"roomId": "abcd1234",  
"role": "moderator",  
"startTime": "2022-06-21T00:00:00.0Z",  
"iat": 1516239022  
}

```

Example:

```
https://meet.gcore.com/call/?roomId=YOUR_ROOM_ID&token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJyb2xlIjoibW9kZXJhdG9yIiwic3RhcnRUaW1lIjoiMjAyMS0wNi0yMVQwMDowMDowMC4wWiJ9.Atj-TPL_GSLyuI565pI6X_6GFjopXf62C6y4OgeeEk9KEb_1cosDmo2sytpBv44PRuMRwgDg8AcqlMMgA0kcdJrBZ7AAywjb6RZVXlian6-6XQ0zx7OhYyDo2-mVxCO9dgYroXfz2Fw8lyNuqFl0AKEfFMPKaYf46u5kjwWmSyhh7bLbL969Eu3zW_Mk3sYLpW_xULyndhkXrLqOVspK08Mla-AbxGJ94pZXJCKHK5UslhrGJ6RProN5nL4NaXOCKRX0ffKnklxiyn9MgKf0cc6Za0GCpjg-d3y6-UOVd0AXW8TWR-RllTgXaTUMMSLyWzHPsv-e2O-GsA0WJnBJEg

```

#### JWT Signature

Use your key to sign the token with the algorithm specified in the header.

The signature is used to verify the data wasn't changed along the way, and, in the case of tokens signed with a private key, it can also verify that the sender of the JWT is who it says it is.

We highly recommend using RS256 asymmetric type of algorithm. See section "RSA Public & Secret Key generation" to generate public/private keys.

### Validating Server API Requests

#### Validation with Authorization Header

To access Server API and Streaming Platform API, we use an API token in the Authorization header. The API token is a unique key that all users and applications should add to requests to interact with our services.

Please authenticate via <a href="https://api.gcore.com/docs/streaming#section/Authentication" target="_blank">API</a>.

Choose one of the methods described below: Bearer authentication or Permanent API tokens.

#### Bearer Authentication

The token will be provided upon <a href="https://api.gcore.com/docs/account#tag/Account/paths/~1auth~1jwt~1login/post" target="_blank">Login</a> request with login and password from your personal account. 

In the response, you will get two tokens: access and refresh. 

To manage Server API services, add your access token after Bearer in the authorization header like this:  

```
Authorization: Bearer eyJ0eXAiOiJKV 

```

Use the  <a href="https://api.gcore.com/docs/account#tag/Account/paths/~1auth~1jwt~1refresh/post" target="_blank">Refresh</a> request to refresh your access token. 

Steps as an example: 

1.  You authorize in your backend using your username and password: https://api.gcore.com/docs/account#tag/Account/paths/~1auth~1jwt~1login/post 
2.  You get two token values: "access" and "refresh".  
3.  The "access" token is a token that is active for several hours (24 hours, but we recommend updating every 4 hours). 
4.  You pass the auth headers into each endpoint: 'Authorization': Bearer ${token} '. 
5.  If the token is correct, everything is fine. 
6.  If not, then a 401 error will be returned. 

Example: 

```
curl -L -X GET 'https://webrtc3.gvideo.co/rooms/serv1l8bsg8zw/durationOfBroadcast' -H 'Authorization: Bearer eyJ0eXAiOiJKV'
```

### Authentication of Participants and Access Limitation

We allow integration with your user control systems. It could be an external CMS, LMS or any security server. You can verify every user who enters a room.

Our server calls the method specified in &accessUrl attribute. Your server should return code as below. Based on the code, the system allows access to the room or doesn't.

If the access to the specified method is protected via Basic authorization, you need to register a required header in the attribute ```&authorizationAccess=<header>```.

These debugging attributes can be used in the URL. But for public use, you need to inform us to register methods on the server.

Example:

```
https://meet.gcore.com/call/?roomId=44fde071&displayName=user16&accessToken=caa630bb&peerId=de9b6927&apiEvent=https://dev.com/api/events&accessUrl=https://dev.com/api/accesscheck

```

POST

Input values:

- accessToken – unique security identifier from ```&accessToken``` attribute
- roomId – ID of the room from &roomId attribute
- peerId – ID of the participant from &peerId attribute

Example:

```{"accessToken":"caa630bb","roomId":"44fde071","peerId":"de9b6927"}```

Output codes we require from you:

| Code | Response Label        | Description                                                                                                                                                                                                                                                         |
|------|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 200  | OK                    | A participant is allowed to join the room.                                                                                                                                                                                                                          |
| 400  | Bad Request           | Token, roomId, peerId not found.                                                                                                                                                                                                                                    |
| 401  | Unauthorized          | A participant is not allowed to join the room, access declined.                                                                                                                                                                                                     |
| 403  | Forbidden             | Invalid token.                                                                                                                                                                                                                                                      |
| 404  | Not found             | Invalid room ID.                                                                                                                                                                                                                                                    |
| 409  | Conflict              | Another connection with an existing peerId was found. In this case, a new connection is established. The previous connection is terminated, and its users get the message: "Someone joined into the room with your ID".                                           |
| 423  | Locked                | Access is closed temporarily or permanently for locked rooms after you close it or limit the maximum number of participants. It is to display a human readable message about the reason and contact info for a moderator, instead of the "Access denied" message. |
| 425  | Too Early             | Access is closed temporarily for those events that have not yet started. We display a human readable message "The event has not started yet. Start % d%." Start time is taken from a JWT.                                                                         |
| 500  | Internal Server Error | Server connection error.                                                                                                                                                                                                                                            |


More examples:

- How to prevent unregistered users from joining – send 401 Locked for requests with empty peerId.
- How to close a room after the event is over – send 423 Locked for all requests after the event is over.
- How to limit the maximum number of participants – send 423 Locked for all requests after the maximum is reached, resend 200 OK for a room with decreasing number of participants when someone leaves.

## Troubleshooting

### JWT Digital Signature Algorithm

We use RS256 or HS256 algorithm for signing and generating hash. RS256 refers to the SHA256 hash function (<a href="https://tools.ietf.org/html/rfc7518#page-8" target="_blank">RFC</a> states). 

| "alg" Param Value   | Digital Signature Algorithm     |
|---------------------|---------------------------------|
| RS256               | RSASSA-PKCS1-v1_5 using SHA-256 |
|  HS256              |  HMAC using SHA-256             |

Please use <a href="https://jwt.io" target="_blank">https://jwt.io/</a> to verify your JWT tokens.

**RS256**

RS256 refers to the SHA256 hash function. (<a href="https://tools.ietf.org/html/rfc7518#page-8" target="_blank">RFC</a> states).

RSA key of size 2048 bits or larger must be used with this algorithm.

The RSASSA-PKCS1-v1_5 SHA-256 digital signature is generated as follows: generate a digital signature of the JWS Signing Input using RSASSA-PKCS1-v1_5-SIGN and the SHA-256 hash function with the desired private key. This is the JWS Signature value.

Please see "RSA Public & Secret Key generation" section below for details.

**HS256** 

A key of the same size as the hash output (for instance, 256 bits for "HS256") or larger MUST be used with this algorithm. 

### RSA Public & Secret Key generation

Keys can be generated by any RSA keygen tool. If you don’t know what to do, we recommend using the OpenSSL tool.

To perform the following actions for Windows or Linux, check and/or install <a href="https://en.wikipedia.org/wiki/OpenSSL" target="_blank">OpenSSL</a> on your system.

Commands to generate secret key and export public key:

```
openssl genrsa -out key_name.key 2048
```

```
openssl rsa -in key_name.key -pubout -outform PEM -out key_name.key.pub
```

File key_name.key.pub will contain public part of the key. File key_name.key will contain the private part of the key.

**Note**: The number "2048" in the above command indicates the size of the private key. You can choose one between 2048 and 4096 (these numbers represent bits). The larger sizes offer greater security, but this is offset by a penalty in CPU performance. We recommend the best practice size of 2048. It seems like 2048 bits is enough for the foreseeable future (2030 horizon).
