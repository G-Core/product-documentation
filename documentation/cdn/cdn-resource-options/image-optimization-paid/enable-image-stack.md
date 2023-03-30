---
title: enable-image-stack
displayName: Enable Image stack
published: true
order: 20
toc:

---

## Enable and configure Image Stack


1. Send us a request to activate the option via [support@gcore.com](mailto:support@gcore.com) or the chat window in the bottom-right corner of [our website](https://gcore.com/). Please specify your ID in the request so we can identify your account. You can find it on the main page of your [control panel](https://accounts.gcore.com/reports/dashboard).

<img src="https://support.gcore.com/hc/article_attachments/11774056177297" alt="mceclip1.png">

Message template: _“Good afternoon! Please enable the Image Stack option for the account with ID \[your ID\]”._

We will notify you when we configure the option. After that, you will be able to enable Image Stack for your CDN resources.

**Note:** You can enable the Image Stack option in two ways: in the Resource settings and the Rule section. We recommend sticking to the second one (rule creation) because the first one (common settings) can lead to the [“Rewrite doesn’t work”](#the-rewrite-option-does-not-work-when-image-stack-is-enabled) issue.

We have outlined how to enable the option through rule creation below.

2. Open the settings of the required CDN resource and go to **Rules**. Click **“Create rule”** and select the image optimization template.

<img src="https://support.gcore.com/hc/article_attachments/11774126764817" alt="mceclip0.png">

On the next page, you will be able to create a rule for image optimization. You only need to configure the Image Stack section.

<img src="https://support.gcore.com/hc/article_attachments/11085759569041" alt="" width="500" height="740">

3. Enable the Image Stack option and set parameters:

<img src="https://support.gcore.com/hc/article_attachments/11085790662801" alt="" width="500" height="599">

**Image quality.** Specify in what quality the images will be delivered to your users. Four values are available:

*   High: 95%
*   Medium: 80%
*   Low: 65%
*   Custom value: any value from 0% to 100%

The quality of individual images is set by adding the necessary query strings. Note, that the quality feature is connected to the compression feature and can’t be set separately. For example:

https://image.example.ru/image.jpg?fmt=avif&quality=50

More information can be found in the “[Quality. Change image quality](https://www.gcore.com/support/articles/9612768329489/)” guide.

**Compression.** Enable WebP and/or AVIF compression. If you have enabled both and the end users’ browser supports both formats, images will be converted to AVIF by default.

The compression for individual images is set by adding the necessary query strings. For example:

https://image.example.ru/image.jpg?fmt=webp

https://image.example.ru/image.jpg?fmt=avif

More information can be found in the “[Compression. Convert images into WebP and AVIF](https://www.gcore.com/support/articles/4417800051729/)” guide.

**Image Stack overview.** The resize and crop features can only be configured by the query parameters. Because each image is unique and has different characteristics (size and crop area), it is not possible to create standard settings for them.

More information can be found in the “[Crop. Crop images](https://www.gcore.com/support/articles/7777427871761/)” and “[Resize. Reduce image size](https://www.gcore.com/support/articles/7120882595985/)” guides.

4. Click **Create rule** to save changes.

The setup is complete. Changes will take effect within about 5–10 minutes. After that, your images will be served to end users optimized with the configurations that you set in step 3.

Please note that when you add a rule with the Image Stack option enabled, the resource cache will be automatically cleared. CDN servers will start requesting your origin for content. To avoid overload, we recommend turning on the option when your users are least active, or first enabling the [Origin Shielding](https://www.gcore.com/support/articles/214080309/) option.