---
title: audio-quality-is-reduced-when-using-bluetooth-headsets-in-video-call-apps
displayName: Bad audio while Bluetooth mic
published: true
order: 30
toc:
   --1--Overview: "overview"
   --1--Audio profiles: "what-are-bluetooths-audio-profiles"
   --1--Cause: "how-do-bluetooth-audio-profiles-cause-a-decrease-in-sound-quality"
   --1--Recommendations: "recommendations-for-solving-the-problem"
pageTitle:  Bluetooth Headsets—Quality Drop | Gcore
pageDescription: Bluetooth audio profiles impact sound quality in calls.
---
# Audio quality is reduced when using Bluetooth headsets in video call apps

## Overview

If you listen to high-quality audio content such as music with Bluetooth headphones and then open an application that uses the Bluetooth headphones’ microphone, e.g., Zoom or Microsoft Team, and so on, the audio quality may be reduced, or some unconventional popping sounds may appear. The problem is that high-quality audio has been changed to low-quality audio. This problem isn’t connected to the concrete application—it occurs because of Bluetooth technology in general and its audio profiles’ limitations.

## What are Bluetooth’s audio profiles? 

A Bluetooth audio profile is a set of standards that define how Bluetooth devices exchange audio data. Bluetooth supports several different audio profiles designed for different types of audio applications. The most common Bluetooth audio profiles are:

- **Advanced Audio Distribution Profile (A2DP)**. This profile is intended for high-quality stereo playback.
- **Headset Profile (HSP)/Hands-Free Profile (HFP)**. This profile is meant for calls. It allows phone calls to be controlled wirelessly using the headset’s own microphone and speaker.

More available audio profiles are listed in the <a href="https://www.bluetooth.com/specifications/specs/" target="_blank">official specification base</a>.

## How do Bluetooth audio profiles cause a decrease in sound quality?

The limitations of Bluetooth’s audio profiles cause the problem with audio quality degradation. Bluetooth headsets can only use one audio profile at a time.

So, when you open a video call application with a Bluetooth headset, the A2DP profile (high sound quality but no microphone capability) is replaced by the HSP/HFP profile (headphones and microphone capability but low sound quality). So, the high-quality audio is changed to low-quality.

## Recommendations for solving the problem 

1\. Switch to wired headphone use.

2\. Change the audio input source from the Bluetooth headset microphone to, for example, the built-in microphone of a laptop or smartphone. The A2DP audio profile will be activated, and the sound quality will be recovered.