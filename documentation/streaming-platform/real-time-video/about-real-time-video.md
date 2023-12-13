---
title: about-real-time-video
displayName: Overview Real-Time Video (paid)
published: true
order: 10
toc:
   --1--What it is: "what-is-real-time-video"
   --1--Where you can use it: "use-cases-for-real-time-video-module"
   --1--What features it has: "what-features-does-real-time-video-have"
   --1--How it works: "how-does-real-time-video-work"
   --1--How to use it: "how-to-use-the-real-time-video-module"
pageTitle: Real-Time Video Overview | Gcore
pageDescription: Explanation of how the live call module works and what features it contains.
---
# About Real-Time Video

## What is Real-Time Video?

Real-Time Video is a paid module of the Streaming Platform. It has an API, SDK, and free sample apps for iOS and Android. It also allows easy setup via iFrame on websites. With this module, you can integrate video calls into your apps quickly without needing to perform any complex programming. It's perfect for customers who want a simple, ready-to-use solution.

This is how Real-Time Video works with different platforms:

- <a href="https://meet.gcore.com/new" target="_blank">Web apps</a>
- <a href="https://github.com/G-Core/reactnative-demo-video-calls" target="_blank">ReactNative</a>
- <a href="https://github.com/G-Core/android-demo-video-calls" target="_blank">Android</a>
- <a href="https://github.com/G-Core/ios-demo-video-calls" target="_blank">iOS</a>

<img src="https://assets.gcore.pro/docs/streaming-platform/real-time-video/about-real-time-video/mobile-video-calls-module-10.gif" loading="lazy" width="602" height="350" alt="Real-Time Video">

## Use cases for Real-Time Video module

Our video call feature can be used for diverse purposes and group sizes:

- One-to-one video calls or small groups of 2–4 people, like dating, online shopping, finance, and online medicine.
- Video meetings with 2–300+ people, ideal for small and medium businesses, online education, and online events.
- Webinars with 1–25 speakers and 10M+ viewers, like major online events.

<img loading="lazy" src="https://assets.gcore.pro/docs/streaming-platform/real-time-video/about-real-time-video/one-to-one-call-20.gif" width="242" height="532" alt="Real-Time Video">

## What features does Real-Time Video have?

Here are the Real-Time Video features:

- No time limits on calls
- Your logo and branding
- An easy addition to web and mobile apps via API and SDK
- One-to-one video calls
- Up to 300+ people in a call
- Interpretation for 15+ languages
- Chat, including chat history
- Call recording
- Moderation
- Waiting room
- RTMP and HLS streaming to external streaming services like Youtube and - Twitch
- Broadcast to 10M+ viewers via cheap CDN traffic
- Screen sharing and presentation
- Works on any device and modern browsers, supporting WebRTC protocol

<img loading="lazy" src="https://assets.gcore.pro/docs/streaming-platform/real-time-video/about-real-time-video/web-video-calls-module-30.gif" width="602" height="350" alt="Real-Time Video">

## How does Real-Time Video work?

Real-Time Video uses WebRTC technology for video calls. This technology allows real-time video and audio. Video signals are sent from users’ cameras using SFU (Selective Forwarding Unit). This technology lets a user send their video to a server, and then the server sends this video to all other users.

**Note**: Real-Time Video does not connect users directly. All communication is sent via the server, even if there are only two people in the room.

<img src="https://assets.gcore.pro/docs/streaming-platform/real-time-video/about-real-time-video/web-calls-protocols-40.jpg" alt="How does Real-Time Video work">
<figcaption>This article uses an image taken from the website bloggeek.me</figcaption>

Simulcast streaming technology is used for live broadcasts. This technology helps to deliver video to each user, even if their internet is not stable. With this technology, several video streams of different quality are made on the user’s device. These streams are sent to a server. The server chooses what quality to send to each user, depending on their internet connection and device type.

**Note**: You can find a list of supported operating systems and browsers here. 

All data streams are made safe using the DTLS (Datagram Transport Layer Security) protocol. This prevents anyone from spying on the data or interfering with it. Media streams are encrypted using standard encryption. You can also use SRTP (Secure Real-Time Transport Protocol) for extra security.

<img src="https://assets.gcore.pro/docs/streaming-platform/real-time-video/about-real-time-video/video-calls-gcore-process-50.png" alt="How does Real-Time Video work">

## How to use the Real-Time Video module

You can try out the video call module quickly and easily. To do this, go to the <a href="https://meet.gcore.com/new" target="_blank">Real-Time Video demo page</a> and follow the instructions there. 

If you want to use our solution for video calls, please read the <a href="https://gcore.com/docs/streaming-platform/api/real-time-video-api-tutorial" target="_blank">Real-Time Video API tutorial</a> guide.
