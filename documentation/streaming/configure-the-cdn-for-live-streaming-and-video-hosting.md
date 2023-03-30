---
title: configure-the-cdn-for-live-streaming-and-video-hosting
displayName: Configure CDN
published: true
order: 40
toc:
   --1--How a video is distributed: "how-our-streaming-platform--distributes-videos"
   --1--Distribute a video from *.gvideo.io: "distribute-videos-from--gvideo-io"
   --1--Distribute a video from your own subdomain: "distribute-a-video-from-your-own-subdomain"
---
   
  
 

How our "Streaming Platform" distributes videos
-----------------------------------------------

The "Streaming Platform" delivers content over our [CDN](https://gcore.com/cdn/): CDN servers pull your video from storage and forward it to end-users at high speed. The CDN sends content to your viewers from CDN resource subdomain name.

Distribute videos from \*.gvideo.io 
------------------------------------

As soon as you [create a live stream](https://gcore.com/support/articles/5307972492945/) or [upload a video](https://gcore.com/support/articles/5485665300369/), we automatically generate a CDN resource with a domain name _\*.gvideo.io_. All videos will be sent from that domain. You don't need to configure anything.

Distribute a video from your own subdomain 
-------------------------------------------

If you want to use your own domain rather than _\*.gvideo.io_, create a CDN resource with the required subdomain name and configure it. 

1.  (Skip the step if you already have a CDN resource). In the "CDN settings" section, click "Create a CDN resource".  
      
    <img src="https://support.gcore.com/hc/article_attachments/5499305980177/1.jpg" alt="1.jpg">
2.  (Skip the step if you have already created a CDN resource). If you only want to change a subdomain name _name_.gvideo.io, select "gvideo.io zone".    
       
    If you want to change the entire domain name, select "Custom Value", enter a subdomain name such as _cdn.yourdomain.com_ and click «Create». Then you have to perform two actions outside Gcore control panel. First, go to your domain registrar's personal account and add a CNAME record pointing to our CDN for this subdomain — so, viewers will receive content from our CDN but on behalf of your subdomain. You can add a CNAME record using the instruction: "[Create a domain name for content delivery through a CDN](https://gcore.com/support/articles/213969769/)". Then you need to add an SSL certificate to your subdomain; you can get a free Let's Encrypt SSL certificate using the instruction: "[Add an SSL certificate to transfer content over HTTPS](https://gcore.com/support/articles/213970109/#h_06869840-3861-4117-8743-b92f968308b7)".  
      
    <img src="https://support.gcore.com/hc/article_attachments/5543783671185/mceclip0.png" alt="mceclip0.png" width="416" height="247">
3.  Click the "Connect CDN resource" button next to the desired resource. So, you integrate the resource with the "Streaming Platform", and we will automatically configure it: we will add the caching rules suitable for video delivery. Please note that if a resource was previously used to distribute static content, it would first be unlinked from a previous origin and then be linked to the "Streaming Platform". Resource rules will also be reconfigured.    
       
    Do not change CDN resource settings without assistance because this may disrupt the video delivery. If you need to change the settings, contact our technical support [support@gcore.com](mailto:support@gcore.com) or chat — we will help you.  
      
    <img src="https://support.gcore.com/hc/article_attachments/5499355015953/3.jpg" alt="3.jpg" width="428" height="524">
4.  Set a default CDN resource — all videos will be distributed over it in the future. You can use the same resource or different resources to distribute videos on demand and live streams. Select the resource and click "Save".  
      
    <img src="https://support.gcore.com/hc/article_attachments/5499350771985/4.png" alt="4.png" width="503" height="267">