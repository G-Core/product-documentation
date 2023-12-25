---
title: embed-real-time-video-into-your-app-with-iframe
displayName: Embed with iframe
published: true
order: 60
toc:
   --1--Overview: "overview-of-how-the-real-time-video-module-is-embedded-into-apps"
   --1--Embedding: "how-to-embed-a-real-time-video-module-into-your-app"
   --2--For beginners: "for-beginners"
   --2--For pro: "for-developers-advanced-customization"
pageTitle: A Detailed Guide on how to Embed the Real-Time Video via Iframe | Gcore
pageDescription: Instructions on how to integrate video call module into your application for beginners and advanced users. 
---
# How to embed Real-Time Video into your app with iframe

## Overview of how the Real-Time Video module is embedded into apps

<a href="https://gcore.com/streaming-platform/realtime" target="_blank">Real-Time Video</a> is an embeddable customizable Gcore Video Streaming Platform module. Using the <a href="https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe" target="_blank">iframe HTML element</a>, you should embed the video calls module into your apps. For example:  

```
<iframe src="https://meet.gcore.com/call/serv2testroom" allow="camera; microphone; fullscreen; display-capture; autoplay; screen-wake-lock"></iframe>
```

- In the <span style="color:#FF5913">src</span> attribute, the <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial#create-room-url" target="_blank">URL with your video room ID</a> should be specified
- In the <span style="color:#FF5913">allow</span> attribute, the necessary <a href="https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Permissions-Policy#specifications" target="_blank">permission policies</a> (e.g., for the camera, microphone, fullscreen, etc.) should be set.

This is how the module is displayed after implementing iframe in websites:

<img src="https://assets.gcore.pro/docs/streaming-platform/real-time-video/embed-real-time-video-into-your-app-with-iframe/iframe-example.gif" alt="Example of Real-Time Video implementing" width="80%">

We have described the process of embedding the module in various types of OS in the following materials:

- <a href="https://gcore.com/blog/add-video-call-feature-to-ios-app/" target="_blank">How to add a video call feature to your iOS app in 15 minutes</a> 
- <a href="https://gcore.com/blog/how-to-launch-rtc-for-ios-and-android/" target="_blank">How to launch real-time communications for iOS/Android</a> 
- <a href="https://github.com/G-Core/reactnative-demo-video-calls" target="_blank">Embed into ReacNative app</a> (GitHub code)
- <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial" target="_blank">Real-Time Video API tutorial</a> 

## How to embed a Real-Time Video module into your app

### For beginners

1\. Generate a room URL for your video call according to the <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial#create-room-url" target="_blank">Create room URL guide</a>. For example, we generated the URL ```https://meet.gcore.com/call/serv2testroom```.

2\.  Add additional attributes from the table for managing security and Real-Time Video module features, if necessary, to your URL. For example, if we want to invite to our call a user with the Interpreter role, we should add the <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial#rolerole" target="_blank">following attribute</a> to the URL from the first step:

```
https://meet.gcore.com/call/serv2testroom?role=interpreter
```

> **Note**: Additional attributes are necessarily separated from the URL by “?” and each other by the characters “&.”

3\. Create an iframe HTML code. Don’t forget to add permissions policy attributes, e.g., ```allow="camera; microphone; fullscreen; display-capture; autoplay; screen-wake-lock"```. You can use the “disallow” policy.  

For example, with the parameters above, the code of our iframe will be: 

```
<iframe src="https://meet.gcore.com/call/serv2testroom?role=interpreter" allow="camera; microphone; fullscreen; display-capture; autoplay; screen-wake-lock"></iframe>
```

Where: 

- ```https://meet.gcore.com/call/serv2testroom``` is a room URL
- ```?``` is a delimiter character for adding optional attributes
- ```role=interpreter``` is an additional attribute
- ```camera; microphone; fullscreen; display-capture; autoplay; screen-wake-lock``` are permission policies

4\. Add the iframe to the code of your web app. 

That’s it! It will be displayed in your app as the following module: 

<iframe src="https://meet.gcore.com/call/serv2testroom?role=interpreter" allow="camera; microphone; fullscreen; display-capture; autoplay; screen-wake-lock" height="600px" width="100%"></iframe>

### For developers (advanced customization)

1\. Build an HTML page with iframes, buttons, and other interface elements. This page will be bound to the methods necessary to control the Real-Time Video module. In the expandable block below, you can acquaint yourself with the example of implementing the Real-Time Video module into HTML. 

<expandable-element title="Example of an HTML code">

We have prepared a demo page using a simple HTML sample to demonstrate elements. We used: 

- **Room ID** field inserted using ```<input>``` tag with ID ```<id="id-room">```. Users should enter an ID in the field. When they click the “Generate ID” button, the content entered in the field will be pasted as a part of the src attribute after ```src="https://meet.gcore.com/call/$id-room"```. Also, autogeneration of ID with substitution of value from an array using ```getRandomInt``` function is added to the field. Values are changed every 2 seconds. When clicking “Generate ID,” a random value is substituted into the src attribute.

- **iframe** tag with ```src``` attribute and enabling access policy to enable camera, microphone, fullscreen mode, autoplay, hide buttons from iframe field (as we will put them separately), and participant's name. For example:

```
<iframe src="https://meet.gcore.com/call/serv2test2room?controlsDisabled=true&displayName=<name>" allow="camera; microphone; fullscreen; display-capture; autoplay; screen-wake-lock" id="myIframe"></iframe>
```

- **Buttons** control the participant's camera, microphone, and buttons responsible for sharing the screen and showing/hiding buttons inside the iframe. Real-Time Video API methods will be applied to them. 
- **A field and a button** to change the participant's name specified in the iframe.
- **Buttons** that toggle between the mobile version and the desktop version of iframe.

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Demo</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
    <script src="https://kit.fontawesome.com/155a070cb6.js" crossorigin="anonymous"></script>
    <script type="module" src="main.js"></script>
    <link rel="stylesheet" href="style.css">
    <link rel="icon" type="image/x-icon" href="assets/gcore-icon.svg">  
</head>
<body>
    <header class="head">
        <div class="container">
            <h1>Demo of integration Video Conference API in your project</h1>
        </div>
    </header>
    <main class="main">
        <div class="container">
            <div class="wrapper">
                <section class="step-one">
                    <h2>Step 1</h2>
                    <label for="id-room">Input a server location and any ID of a room:</label>
                    <input type="text" id="enterID" value="" name="id-room" placeholder=" serv1test">
                    <button type="button" id="stopButton">Generate ID</button>
                </section>
                <section class="step-two">
                    <h2>Step 2</h2>
                    <p> Copy the folowing iFrame of the room and paste to your code:</p>
                    <div class="iframe-code-block">
                        <span class="green">&lt;iframe&nbsp;</span><span class="blue"> src=</span>"https://meet.gcore.com/call/<span id="urlroom"></span>&controlsDisabled=true&displayName=<name>"<span class="blue">&nbsp;allow=</span>"camera; microphone; fullscreen; display-capture; autoplay; screen-wake-lock" id="myIframe"<span class="green">&gt;&lt;/iframe&gt;</span>
                    </div>
                </section>
                <section class="step-three">
                    <h2 class="header">Step 3</h2>
                    <p>Push the button to start a call</p>
                    <button id="get_id">Start call</button>
                </section>
                <section class="step-four">
                    <h2>Step 4</h2>
                    <p>Invite participants. To do this copy the link below and send it to your guests.</p>
                    <div class="invite-link">
                        <input class="link" type="text" size="60" value="">
                        <button id="invite-button">
                            <i class="fa-regular fa-copy"></i>
                        </button>
                    </div>
                </section>
                <section class="step-five">
                    <h2>Step 5</h2>
                    <p>Press <strong>Join</strong> in the iFrame and manage the call with buttons on the right</p>
                    <div class="iframe-block">
                        <div class="iframe">
                            <div class="iframe-wrapper">
                                <h2 class="iframe__notification">IFrame not initialized</h2>
                                <iframe class="iframe__content hidden" src="https://meet.gcore.com/new/call" allow="camera; microphone; fullscreen; display-capture; autoplay; screen-wake-lock" id="myIframe"></iframe>
                            </div>
                            <div class="adaptive">
                                <button type="button" id="desktop"><i class="fa-solid fa-display"></i></button>
                                <button type="button" id="mobile"><i class="fa-solid fa-mobile-screen-button"></i></button>            
                            </div>
                        </div>
                        <div class="button-group">
                            <div class="camera">
                                <button class="button button_room" id="camera_btn">
                                    <i class="fa-solid fa-video"></i>
                                </button>
                                <p class="cam-caption">Disable camera</p>
                            </div>
                            <div class="micro">
                                <button class="button button_room" id="microphone_btn">
                                    <i class="fa-solid fa-microphone"></i>
                                </button>
                                <p class="mic-caption">Disable microphone</p>
                            </div>
                            <div class="screen">
                                <button class="button button_room" id="share_screen_btn">
                                    <i class="fa-solid fa-display"></i>
                                </button>
                                <p class="screen-caption">Share screen</p>
                            </div>
                            <div class="indicators">
                                <button class="button button_room" id="hide_indicators_btn">
                                    <i class="fa-solid fa-eye"></i></button>
                                <p class="indicator-caption">Hide indicators</p>
                            </div>
                            <div class="change-name">        
                                <input type="text" id="name1" placeholder="John Snow">
                                <button class="button_changename with-tooltip" id="change_name_btn">Change name</button>
                            </div>
                        </div>
                    </div>            
                </section>
            </div>
        </div>
    </main>
</body>
</html>
```

</expandable-element>

2\. Install the <a href="https://www.npmjs.com/package/@gcorevideo/videocalls-iframe-adapter" target="_blank">npm package</a> to integrate the viewcall module into your application. 

```
npm i @gcorevideo/videocalls-iframe-adapter
```

3\. In the JS file (instead can be used Vue, React, Angular, or another component), import ```MeetIframeBridge``` from the *npm* package;

```
import MeetIframeBridge from "@gcorevideo/videocalls-iframe-adapter"
```

4\. Initialize a ```MeetIframeBridge``` for the iframe (request via the ID). The following part of the code performs this action:  

```
    let bridge;
    $('#get_id').on("click", async function() {
        $('#myIframe').attr('src', `https://meet.gcore.com/call/${value}?displayName=John&itisparticipant=true&nameScreenDisabled=true&controlsDisabled=true`);
        bridge = new MeetIframeBridge({
            element: $("#myIframe")[0],
            roomId: $('#enterID').val()
        }) 
    })
```

5\. Control video calls embedded in an iframe through your shell interface using <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial#public-methods-of-real-time-video-iframe" target="_blank">API methods from the documentation</a>. The general schema is:

```
bridge.method({ name: methodName, data: methodData { } }) 
```

Where ```data: methodData { }``` is optional and is only used in certain methods.

For example, to join the call, use:

```
bridge.method({
            name: "join",
            data: {constraints: {video: true, audio: true }},
            callback: function(e) {
                alert(1);
                return true;
            }
        });
```

In the expandable block below, you can acquaint yourself with the example of the JS file. 

<expandable-element title="Example of a JS code">

Below is the content of the JS code written in jQuery, with explanations in the comments. 

```
import MeetIframeBridge from "@gcorevideo/videocalls-iframe-adapter";
$(window).on('load', function() {
    let array = [
        "a0bd5a67b08c",
        "9a8dc19e55a5",
        "5c357ec79a8e",
        "96c922570b80",
        "24f98cbd873d",
        "04d81b10857d"
    ];
   
    function getRandomInt(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min) + min);
    }


    /* Auto-renew input value every two seconds randomly */
    let intervalMilliSeconds = 2000;
    let intervalId = setInterval(function() {
        let randomInt = getRandomInt(0, array.length);
        let roomId = array[randomInt];
        $('#enterID').val(roomId);
    }, intervalMilliSeconds);


    /* Stop auto-renew by clicking the button and set the result value for iFrame */
    let value;
    $('#stopButton').on('click', function() {
        clearInterval(intervalId);
        value = $('#enterID').val();
        $('#urlroom').text(value);
        $('.link').attr('value', `https://meet.gcore.com/call/${value}`).css("color", "white")


        let linkToCopy = $('.link').val();
        $('#invite-button').on('click', function() {
            navigator.clipboard.writeText(linkToCopy).then(
                function() {
                    console.log('successfully copied')
                },
                function() {
                    console.log('Your browser does not support Clipboard API')
                }
            )
        })  
    })
   
    /* Stop auto-renew by any keypress in input */
    $('#enterID').keyup(function() {
        clearInterval(intervalId)
        value = $(this).val();
        $('#urlroom').text(value);
    })


    /* initializaton of bridgeAPI */
    let bridge;
    $('#get_id').on("click", async function() {
        $('#myIframe').attr('src', `https://meet.gcore.com/call/${value}?displayName=John&itisparticipant=true&nameScreenDisabled=true&controlsDisabled=true`);
        bridge = new MeetIframeBridge({
            element: $("#myIframe")[0],
            roomId: $('#enterID').val()
        }),
        $(".iframe__notification").addClass("hidden")
        $(".iframe__content").removeClass("hidden")
        let clickCam;
        $('#camera_btn').on('click', function() {
            clickCam = !clickCam;
            if (clickCam) {
                bridge.method({
                    name: "disableWebcam"
                })
                $('.camera button').css("background-color", "#f40828ed").html(`<i class="fa-solid fa-video-slash"></i>`);
                $('.cam-caption').html(`<p class="cam-caption">Enable camera</p>`)
            } else {
                bridge.method({
                    name: "enableWebcam"
                })
                $('.camera button').css("background-color", "#17cf45").html(`<i class="fa-solid fa-video" title="Turn off Camera">`);
                $('.cam-caption').html(`<p class="cam-caption">Disable camera</p>`)
            }
        })   
        let clickMic;
        $('#microphone_btn').on('click', function() {
            clickMic = !clickMic;
            if (clickMic) {
                bridge.method({
                    name: "disableMic"
                })
                $('.micro button').css("background-color", "#f40828ed").html(`<i class="fa-solid fa-microphone-slash"></i>`);
                $('.mic-caption').html(`<p class="mic-caption">Enable microphone</p>`)
            } else {
                bridge.method({
                    name: "enableMic"
                })
                $('.micro button').css("background-color", "#17cf45").html(`<i class="fa-solid fa-microphone"></i>`)
                $('.mic-caption').html(`<p class="mic-caption">Disable microphone</p>`)
            }
        });
        let clickShare;
        $('#share_screen_btn').on("click", function() {
            clickShare = !clickShare
            if (clickShare) {
                bridge.method({
                    name: "enableShare"
                })
                $('.screen-caption').html(`<p class="screen-caption">Stop screen sharing</p>`)             
            } else {
                bridge.method({
                    name: "disableShare"
                })
                $('.screen-caption').html(`<p class="screen-caption">Share screen</p>`)
            }
        })
        let hideIndicator
        $('#hide_indicators_btn').on('click', function() {
            hideIndicator = !hideIndicator;
            if (hideIndicator) {
                bridge.method({
                    name: "setHideIndicators",
                    data: true,
                })
                $('.indicators button').css("background-color", "#f40828ed").html(`<i class="fa-solid fa-eye-slash"></i>`);
                $('.indicator-caption').html(`<p class="mic-caption">Show indicators</p>`)
            } else {
                bridge.method({
                    name: "setHideIndicators",
                    data: false,
                })
                $('.indicators button').css("background-color", "#17cf45").html(`<i class="fa-solid fa-eye"></i>`);
                $('.indicator-caption').html(`<p class="mic-caption">Hide indicators</p>`)
            }
        });                
        $('#change_name_btn').on("click", function() {
            let name = $('#name1').val();
            bridge.method({
                name: "changeDisplayName",
                data: name,
                callback: (e) => {
                    return
                }
            });
        });
    }) 
    $('#desktop').on('click', function() {
        $(".iframe-wrapper").removeClass("iframe-wrapper_mobile")
    })
    /* This function does not change userAgent. Only the size of the iFrame changes */
    $('#mobile').on('click', function() {
        $(".iframe-wrapper").addClass("iframe-wrapper_mobile")
    })
})
```
</expandable-element>

That’s it! It will be displayed in your app as the following module: 

<iframe src="https://demo-files.gvideo.io/vcapi-iframe-demo/index.html"  width="100%" height="800px"></iframe>