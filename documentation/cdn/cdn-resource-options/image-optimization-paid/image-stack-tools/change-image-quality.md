---
title: change-image-quality
displayName: Change quality
published: true
order: 20
toc:
   --1--About Quality: "about-the-quality-feature"
   --1--Enable: "enable-quality"
   --1--Use: "use-quality"
   --2--in the control panel: "use-quality-in-the-control-panel"
   --2--via query parameters: "use-quality-via-query-parameters"
   --1--Check HTTP headers: "check-http-headers"
---
  
  
  
  
  

About the Quality feature
-------------------------

**What is it?** Quality is a feature included in the Image Stack option. The feature helps to reduce the quality of the images in conjunction with other features such as compression. Quality cannot be performed on its own and must be done as part of another feature. This means that you can’t just downgrade the quality of the picture without also changing its format to WebP or AVIF, or applying other features such as Crop or Resize.

Below is a photo to which we have applied the Quality feature. The appearance of the photo has not changed much, even though the last picture’s quality is half that of the original.

|<img src="https://support.gcore.com/hc/article_attachments/11030503003793" alt="" width="135" height="192">  |<img src="https://support.gcore.com/hc/article_attachments/11030503010449" alt="" width="135" height="192">|    <img src="https://support.gcore.com/hc/article_attachments/11030503150481" alt="" width="135" height="192">       |     <img src="https://support.gcore.com/hc/article_attachments/11030503151121" alt="" width="135" height="192">               |
|-------------------------------------------------------------------------------------------------------------|--------------|-----------|--------------------|
| High (90%)                                                                                                  | Medium (80%) | Low (65%) | Custom value (50%) |


The final appearance of the image depends on its granularity and color scheme. So, if the image has a monolithic figure standing out against a contrasting background (e.g., a brown bird on a green background), the changes in quality will be more noticeable. If the image is detailed and non-contrasted, the changes will be less obvious.

**How it works.** To change image quality, you need to set the required option in the control panel or add the appropriate query string to the image URL in your website source. The configuration is described in the Use Quality section. When a user requests an image from the site, the CDN will change the image quality and deliver the modified image to the user.

For example: An origin server hosts a JPG image with its original quality, but you set the quality to Low (65%). When the image gets to the CDN cache, our CDN automatically reduces its quality. The origin still has the high-resolution image, but end users receive its low-resolution version.

Enable Quality
--------------

Quality is included in the paid Image Stack option. This option helps optimize images, such as by converting them to WebP or AVIF formats, cropping them, or changing their quality and size. To use Quality, you need to activate Image stack according to the “Enable and configure Image stack” guide.

Use Quality
-----------

There are two ways to use the Quality feature: in the control panel and by query strings. If you want to reduce the quality of all images, use the first method. If you want to reduce the quality of individual images you’ve added in query strings, use the second one.

### Use Quality in the control panel

1. Go to the **Rules** section in the settings of the CDN resource you want to apply Quality to and open the **Image optimization** rule.

<img src="https://support.gcore.com/hc/article_attachments/11774830851473" alt="mceclip0.png">

2. Select one of the built-in presets: High (95%), Medium (80%), Low (65%), or set a Custom Value. By default, after enabling the Image Stack option, the quality will be High (95%).

You can also toggle on **Enable lossless for PNG** to avoid quality reduction for images with the PNG extension. If this function is enabled, the quality configurations are applied only for JPG images.

**Note:** You cannot set the quality to more than 100%.

<img src="https://support.gcore.com/hc/article_attachments/11030503278097" alt="" width="536" height="654">

3. Click **Save changes** at the top right corner of the page.

The setup is complete. After that, images are delivered to end users at the quality you have set.

### Use Quality via query parameters

1. Open the website source code.

2. Find strings with the URLs of the images whose quality you want to change.

3. Add the query strings to the URLs of the images as follows:

image.jpg?quality=value1&tool2=value2…

where:

*   _value1_ is a number between 0 and 100
*   _tool2=value2_ represents query parameters for any other Image Stack function such as [Compression](https://gcore.com/support/articles/4417800051729/), [Resize](https://gcore.com/support/articles/7120882595985/), or [Crop](https://gcore.com/support/articles/7777427871761/)

For example, to reduce the quality to 76%, convert it to AVIF format, and crop the area 200×200 px from the center, you should use the following query string:

image.jpg?quality=76&fmt=avif&crop=200,200

5. Save the changes in the website source code. Images on the website will now be shown to the end user with the quality that you set.

Let’s see how the photo of Charly, our business analyst’s pet, will change when we set different quality values.

| Before                                                                                                                                                                                             | After                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Link: img.jpg<br/>Size: 813 KB<br/>Quality: 100%<br/>The original image before WebP compression:<br/><img src="https://support.gcore.com/hc/article_attachments/11030480618769" alt="" width="222" height="393"> | Link: img.jpg?quality=95&amp;fmt=webp<br/>Size: 97.4 KB<br/>Quality: 95%<br/>The image with the default quality:<br/><img src="https://support.gcore.com/hc/article_attachments/11030480610193" alt="" width="216" height="382"> |
| Link: img.jpg?quality=50&amp;fmt=avif\nSize: 48 KB<br/>Quality: 50%<br/>                                                                                                                                 | Link: img.jpg?quality=10&amp;crop=300,600<br/>Size: 18.5 KB<br/>Quality: 10%<br/><img src="https://support.gcore.com/hc/article_attachments/11030480735505" alt="" width="188" height="376">                                                                                                                                    |

Check HTTP headers
------------------

After converting, an image does not change its URL or extension. So you can use the HTTP header value of the image to check if the changes have been applied.

The X-Img-Operations header reflects all the conversions performed. If the value includes “convert”, the image quality has changed.

<img src="https://support.gcore.com/hc/article_attachments/11030503623825" alt="" width="360" height="367">

If the HTTP header contains no convert value and CDN returns the image with original quality, check the Img-Skip-Reason HTTP header. This will explain the reason why the operation could not be done. For example, “converted image bigger than origin value” appears when the value that you set is higher than the original one. You can also try to use Quality within other features.

<img src="https://support.gcore.com/hc/article_attachments/11030503627153" alt="" width="553" height="386">
