---
title: fix-the-camera-or-microphone-if-they-do-not-work
displayName: Camera and microphone
published: true
order: 10
toc:
   --1--Ensure that Real-Time Video supports your browser: "ensure-that-real-time-video-supports-your-browser"
   --1--Check permissions and settings in the browser: "check-your-browser-permissions-and-settings"
   --2--Google Chrome: "for-chrome"
   --2--Firefox: "for-firefox"
   --2--Opera: "for-opera"
   --2--Safari: "for-safari"
   --1--Clear cache and cookies: "clear-cache-and-cookies"
   --1--Check the installed browser extensions: "check-the-installed-browser-extensions"
   --1--Inspect the firewall settings: "шnspect-the-firewall-settings"
   --1--Check the camera and microphone in your OS: "check-the-camera-and-microphone-settings-in-your-os"
   --2--macOS: "macos"
   --2--Windows: "windows"
pageTitle: Camera and Microphone Issues | Gcore
pageDescription: A troubleshooting guide on how to solve camera and microphone issues.
---
# Fix the camera or microphone if they do not work

If no one can hear or see you in a video call, and the camera or microphone icons are crossed out, and clicking on them does not change anything, please follow the instructions below consistently.

## Ensure that Real-Time Video supports your browser

Our video call service supports the following browser versions:

| OS      | Browser version                          |
|---------|------------------------------------------|
| Windows | Chrome 70+ Edge 79+ Firefox 70+Opera 60+ |
| MacOS   | Chrome 70+Safari 12+Firefox 70+Opera 60+ |
| Android | Chrome 70+                               |
| iOS     | Safari iOS 13+                           |

Check the version of your browser using the appropriate instructions for your device, and update the browser if the version is lower than the values from the table: <a href="https://google.com/chrome/update" target="_blank">Chrome (Windows)</a>, <a href="https://support.microsoft.com/en-us/microsoft-edge/find-out-which-version-of-microsoft-edge-you-have-c726bee8-c42e-e472-e954-4cf5123497eb" target="_blank">Edge</a>, <a href="https://support.mozilla.org/en-US/kb/find-what-version-firefox-you-are-using" target="_blank">Firefox</a>, <a href="https://help.opera.com/en/latest/browser-window" target="_blank">Opera</a>, <a href="https://support.apple.com/en-am/HT201541" target="_blank">Safari (Mac)</a>, <a href="https://support.google.com/chrome/answer/95414?co=GENIE.Platform%3DiOS&oco=1" target="_blank">Chrome (Android)</a>, or <a href="https://support.apple.com/en-am/HT204204" target="_blank">Safari (iOS)</a>.

## Check your browser permissions and settings

Your camera and microphone may have been disabled in the browser settings. To check this, follow the instructions below for your browser:

### For Chrome

Click on the padlock icon in the browser's address bar to check browser permissions. If **Camera** or **Microphone** switchers are disabled, enable them as follows:

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13080497186449.png" alt="Camera or Microphone switchers are disabled" width="50%">

To check the camera and microphone settings in Chrome: 

1\. Open the browser Settings, select the "Privacy and Security" tab, and go to the **Site settings**.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13080561876625.png" alt="Privacy and Security">

2\. Check the Microphone and Camera permissions and make sure that ```meet.gcore.com``` is in the "Allowed to use your microphone" section.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13080685472401.png" alt="Allowed to use your microphone" width="80%">

### For Firefox

To check your browser permissions, click on the icons on the left side of the browser's address bar, as shown in the screenshot. If the "Use the camera" or "Use the microphone" field is temporarily blocked, click the **×** next to this value and reload the page.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13080971968273.png" alt="the icons on the left side of the browser's address bar" width="50%">

To access Firefox's camera and microphone settings, go to the browser Settings and select the "Privacy & Security" section. In the **Permissions** block, open the "Camera" and "Microphone" settings and ensure that ```meet.gcore.com``` is not on the block list.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13081090317969.png" alt="browser Settings" width="80%">

### For Opera

Click on the padlock icon in the browser's address bar to check browser permissions. If the window that appears indicates that access to the camera and microphone is disabled, enable the switchers and reload the page.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13081119381265.png" alt="padlock icon in the browser's address bar " width="50%">

To check the camera and microphone settings in Opera:

1\. Go to the browser Settings, select the "Privacy & security" section, and navigate to **Site settings**.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13081222474513.png" alt="Settings" width="80%">

2\. In the "Permissions" section, open the **Camera** and **Microphone** settings and ensure that ```meet.gcore.com``` is not on the block list.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13080991315601.png" alt="Permissions section" width="80%">

### For Safari

To set browser permissions, reload the page with Real-Time Video opened and click **Allow** in the pop-up.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13081307372817.png" alt="Safari">

To check the camera and microphone settings in Safari, open the application settings, select "Camera" or "Microphone," and ensure that ```meet.gcore.com``` is not on the block list.

## Clear cache and cookies

If you're experiencing difficulties with video and audio delivery, it could be due to an outdated cookie file that's allowing other applications to use the camera and microphone instead of Real-Time Video.

We recommend clearing the cache and cookies for the entire browser and restarting your computer using the appropriate instructions for your browser: <a href="https://support.google.com/accounts/answer/32050?co=GENIE.Platform=Desktop&hl=en" target="_blank">Chrome</a>, <a href="https://support.microsoft.com/en-us/microsoft-edge/delete-cookies-in-microsoft-edge-63947406-40ac-c3b8-57b9-2a946a29ae09#:~:text=Select%20Settings%20%3E%20Privacy%2C%20search%2C,and%20then%20select%20Clear%20now." target="_blank">Edge</a>, <a href="https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox" target="_blank">Firefox</a>, <a href="https://opera.com/ru/use-cases/clean-browser-and-remove-trackers#:~:text=and%20site%20data-,Press%20Ctrl%2BShift%2BDel%20to%20open%20your%20Clear%20browsing%20data,Security%20and%20click%20Site%20settings." target="_blank">Opera</a>, <a href="https://support.apple.com/en-am/guide/safari/sfri11471/mac" target="_blank">Safari (Mac)</a>, or <a href="https://support.apple.com/en-us/HT201265" target="_blank">Safari (iOS)</a>.

## Check the installed browser extensions

Third-party extensions installed in your browser could also be causing problems with the camera and microphone on some websites. To ensure that extensions aren't blocking Real-Time Video's access to the camera and microphone, open ```meet.gcore.com``` in incognito or private browser mode. This will allow you to run the website without any extensions impacting it. If the website works correctly in this mode, issues with the camera or microphone were likely caused by one of the installed extensions.

Please note that there is no quick way to determine which extension is causing the issue. To solve the problem, it is recommended that you disable each installed extension one by one to determine which one is causing the trouble. Once you've identified the problematic extension, you can disable it each time you use Real-Time Video.

## Inspect the firewall settings

If you're experiencing firewall restrictions, it's possible that some browsers won't be able to connect through strict networks or firewalls (such as when you're calling through a corporate network). In this case, it's best to use a different browser to solve the issue.

## Check the camera and microphone settings in your OS

Your browser may have been mistakenly blocked from accessing the camera or microphone. To check and allow your browser to access these devices, follow these steps:

### MacOS

1\. Open **System Preferences** and go to the "Security & Privacy" section. 

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13081820659857.png" alt="System Preferences" width="80%">

2\. Select "Camera" or "Microphone" from the list of options, then go to the **Privacy** section and check the boxes next to your browser to allow access.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13081892456593.png" alt="Privacy section" width="80%">

Finally, restart the browser for the changes to take effect.

### Windows

If you're using Windows 11, you can set the default microphone at the system level or check the microphone or camera access.

To set up the default microphone, go to the "System" settings and select the **Sound** section. In the Input settings section, choose the desired input device.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13081899519505.png" alt="Sound section">

To check and configure access to your microphone and camera, go to the "Privacy & Security" settings and select the **Camera** or **Microphone** sections. Ensure that your browser has permission to use the camera or microphone.

<img src="https://assets.gcore.pro/docs/streaming-platform/troubleshooting/real-time-video-issues/fix-the-camera-or-microphone-if-they-do-not-work/13081924169617.png" alt=" Camera or Microphone sections">
