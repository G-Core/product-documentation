---
title: configure-image-compression-to-webp-and-avif
displayName: Convert to WebP or AVIF
published: true
order: 10
toc:
   --1--About Compression: "about-the-compression-feature"
   --1--Enable: "enable-compression"
   --1--Configure: "use-compression"
   --2--in the Control panel: "use-compression-in-the-control-panel"
   --2--via query parameters: "use-compression-via-query-parameters"
   --1--Check HTTP headers: "check-http-headers"
pageTitle: Guide to converting image format to WebP and AVIF using CDN | Gcore
pageDescription: A guide on changing image format using the Compression feature of the Image stack option.
---
# Сonfigure image compression to WebP and AVIF
  
## About the Compression feature

**What is it?** Compression is a feature that allows you to automatically convert of JPG and PNG images into WebP and AVIF format when delivering over the CDN.

WebP and AVIF are modern optimized image formats with advanced compression algorithms. They help reduce image weight with no significant visible loss of quality.

Below is a painting by Wassily Kandinsky in PNG, JPG, WebP, and AVIF formats. Sharpness and color rendering are the same, but the WebP and AVIF file sizes are smaller.

| <img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif/11028965206801.png" alt="PNG example"> | <img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif/11028965205905.png" alt="JPG example"> | <img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif/11028965337873.png" alt="WebP example"> | <img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif/11028965357457.png" alt="AVIF example"> |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PNG (1860 KB)                                                                                                                                                                                  | JPG (169 KB)                                                                                                                                                                                   | WebP (136 KB)                                                                                                                                                                                   | AVIF (113 KB)                                                                                                                                                                                   |


WebP and AVIF images give you a smaller web page and shorter load time. The more images a website hosts, the greater the difference in download time will be.

**How it works.** To convert an image to WebP or AVIF, you need to set the desired option in the control panel or add the necessary query string to the image URL in your website source. The configuration is described in the Use Compression section. When a user requests an image from the site, the CDN will change the image format (not extension) and deliver the modified image to the user.

## Enable Compression

Compression is included in the paid Image Stack option. This option helps optimize images, such as by converting them to WebP or AVIF formats, cropping them, or changing their quality and size. To use Compression, you need to activate the image stack according to the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/enable-image-stack" target="_blank">Enable Image Stack</a>" guide.

## Use Compression

There are two ways to use the compression feature: in the Control panel and by query strings. If you want to apply WebP and AVIF compression to all images, use the first method. If you want to apply the compression to individual images for those you’ve added the necessary query strings, use the second one.

### Use Compression in the Control panel

1\. Go to the "Rules" section in the settings of that CDN resource you want to compress and open the **Image optimization** rule.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif/11774756992785.png" alt="Rules" width="80%">

2\. Click **Enable WebP compression** and/or **Enable AVIF compression**. If you enable both options, the format will be chosen depending on which format (WebP or AVIF) the end-user’s browser supports. If the browser supports both, the image will be converted to the AVIF format.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif/11028965476113.png" alt="Enable WebP compression" width="60%">

3\. Click **Save changes** at the right top corner of the page.

The setup is complete. Now images will be delivered to end-users in WebP or AVIF format.

### Use Compression via query parameters

1\. Open the website source code.

2\. Find strings with the URLs of the images whose quality you want to change.

3\. Add the query strings to the URLs of the images as follows:

<code-block>
image.jpg?fmt=<span style="color:#FF5913">value</span>
</code-block>

where ```value``` is:

- <span style="color:#FF5913">webp</span> (if you want to convert images into the WebP format)
- <span style="color:#FF5913">avif</span> (if you want to convert images into the AVIF format)
- <span style="color:#FF5913">avif,webp</span> (if you want to convert into both)

For example: ```image.jpg?fmt=avif,webp```.

4\. Save the changes in the website source code. Images on the website will now be shown to the end-user in the format you set.

## Check HTTP headers

After converting, an image does not change its URL or extension. So you can use the HTTP header value of the image to check if the changes have been applied.

The *X-Img-Operations* header reflects all the conversions performed. If the value includes "convert", the image size has changed.

The *Content-Type* header shows the compression format. If the value is image/webp or image/avif, the image is in a new format.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif/11028965537425.png" alt="Check HTTP headers" width="50%">

If the HTTP header contains no convert value and CDN returns the image with original quality, check the _Img-Skip-Reason_ HTTP header. This will explain the reason why the operation could not be done. For example, “converted image bigger than origin value” appears when the value that was set is higher than the original one. In this case, lower the quality according to the "<a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/change-image-quality" target="_blank">Change image quality</a>" guide.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif/11028973043857.png" alt="Check HTTP headers" width="50%">