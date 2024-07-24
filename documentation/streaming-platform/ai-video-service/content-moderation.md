---
title: content-moderation
displayName: Content moderation
published: true
order: 20
toc:
   --1--How it works: "how-it-works"
   --1--Use cases: "use-cases"
pageTitle: Guide to Gcore's AI video content moderation | Gcore
pageDescription: Learn how to use Gcore's AI tasks for moderating video content to ensure it's suitable for your audience.
---
# Content moderation

Gcore AI content moderation is a powerful solution for analyzing and filtering video content. It detects inappropriate materials and ensures that delivered videos are safe and suitable for your users.  

You can also use content moderation to detect specific sports activities for better personalization or copyright protection.  

Content types we detect in videos and images: 

* Not safe for work (NSFW) materials 
* Hard nudity 
* Soft nudity 
* Child Sexual Abuse Material (CSAM) 
* Sport activities  
* Weapons 

## How it works 

We run multiple AI models on our infrastructure to conduct real-time analysis of sensitive and restricted content types. After the video is processed, the original file is deleted from AI’s local storage. 

The content is detected by analyzing keyframes (iFrames) in a video. For example, if a keyframe is set every 2 seconds, the analyzis will occur at these intervals. Currently, we don’t detect objects between these timestamps. However, we’re working on a version to analyze more frames. 

You can also process static images, where the duration of one picture is counted as 1 second. 

## Billing

Check out Gcore <a href="https://gcore.com/pricing/streaming-platform" target="_blank">pricing page</a> for detailed information about AI content moderation costs.

## Use cases 

Video streaming & TV broadcasting:  

* Ensure delivery of age-appropriate content and compliance with platform policies 
* Identify illegal or potentially violent content in real-time 

Broadcasting of sports events: 

* Identify and tag specific sports and key moments in video content 
* Create personalized content recommendations based on viewers' preferences 

Video on demand (VOD) platforms: 

* Block uploading of illegal materials 
* Streamline content review process and enhance its accuracy 

## Assessing the probability of inappropriate content 

There's no one-size-fits-all criterion or nudity score that can definitively determine whether a video is inappropriate. Different video hosting services cater to specific audiences such as adults, children, educational groups, etc. For instance, an acceptable nudity percentage for a site dedicated to sex education would be higher than for a hosting site that uploads entertainment videos intended for children. 

You can set a probability threshold to determine when a video is inappropriate for your specific use case. One method is to run videos for one day and analyze the resulting probability coefficient.
