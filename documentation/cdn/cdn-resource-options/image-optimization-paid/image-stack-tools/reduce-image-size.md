---
title: reduce-image-size
displayName: Resize
published: true
order: 40
toc:
   --1--About Resize: "about-the-resize-feature"
   --1--Enable: "enable-resize"
   --1--Use: "use-resize"
   --1--Check HTTP headers: "check-http-headers"
---
  
  
  

About the Resize feature
------------------------

**What is it?** Resize is a feature that reduces the height and width of an original JPG or PNG before it is delivered over the CDN. You set the height, width, and reduction method (compression or cropping) for each image.

**Example.** An origin server hosts an 1100×1500 px image, but you set the following Resize parameters: _height=200, width=150._ As soon as the image gets to the CDN cache, it is automatically reduced in size. As a result, the origin still has the 1100×1500 image, but end users receive the 200×150 reduced version:

| <img src="https://support.gcore.com/hc/article_attachments/11031151427473" alt="" width="286" height="381">               |<img src="https://support.gcore.com/hc/article_attachments/11031138460049" alt="" width="150" height="200">               |
|----------------|---------------|
| Original image | Resized image |


**How it works.** To set a new height and width for an image, you add the necessary query string to the image URL on your website source. These query strings are described in the [Use Resize](#use-resize) section. When a user requests a website page, the CDN will deliver it with reduced images.

Enable Resize
-------------

Resize is included in the paid Image Stack option. This option helps optimize images, such as by converting them to WebP or AVIF format, cropping them, or changing their quality and size. To use Resize, you need to activate Image Stack according to the [“Enable and configure Image Stack”](https://www.gcore.com/support/articles/11085768264593/#h_01GK96NTDDBNKKC7WS40PK3QZT) guide.

Use Resize
----------

1. Open the website source code.

2. Find the strings with the URLs of the images that you want to reduce using Resize.

3. Add the query strings to the URLs of the images.

A query parameter should be set as follows:

image.jpg?parameter=value

Two or more parameters should be set as follows:

image.jpg?parameter#1=value&parameter#2=value&…

where _image.jpg_ is the URL of an image on the website.

| Query parameter, how it works                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | Example                                                                                                                                                                                           |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \nWidth\nWidth compresses an image while preserving the aspect ratio of the original image. This parameter is used to set the target width of the new image in pixels. The height will be automatically adjusted to maintain the original aspect ratio.\nExample. An origin server hosts a 900×600 image (W×H). You set the target width: width=300. The width must be reduced by three. The height will also be reduced by three, and you will get a 300×200 image. \n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \nBefore: image.jpg\n\n500×333\nAfter: image.jpg?width=300\n\n300×200\n    <img src="https://support.gcore.com/hc/article_attachments/11031151470993" alt="image3.png" width="499" height="333">  |
| \nHeight\nHeight compresses an image while preserving the aspect ratio of the original image. This parameter is used to specify the target height of the new image in pixels. The width will be automatically adjusted to maintain the original aspect ratio.\nExample. An origin server hosts a 900×600 image (W×H). You set the target height: height=300. The height must be reduced by two. The width will also be reduced by two, and you will get a 450×300 image.\n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | \nBefore: image.jpg\n\n500×333\nAfter: image.jpg?height=300\n\n450×300\n    <img src="https://support.gcore.com/hc/article_attachments/11031151622929" alt="image4.png" width="300" height="200"> |
| \nFit\nFit controls how the image will be reduced: cropped from sides, compressed keeping the original aspect ratio, or compressed ignoring the original aspect ratio.\nTo use fit, specify both the width and height of a future image and then add the fit parameter as follows: image.jpg?width=300&amp;height=100&amp;fit=…\nIf you specify only width and height, without the fit parameter, the default value fit=fit will be applied.\nThere are four possible values for fit:\n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | \nBefore: image.jpg\n\n500×333\n    <img src="https://support.gcore.com/hc/article_attachments/11031151470993" alt="image3.png" width="499" height="333">                                         |
| \n1. fit=fit\nThe image will be as wide and high as you have specified. The excess pixels will be cut off evenly from all four sides.\nExample. an original image is 1000×500 pixels, and you specify: width=800, height=100, fit=fit. To fit the final image for 800×100, the system will cut off 100 pixels from the top and bottom and 200 pixels from the left and right sides.\n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       | \nAfter: width=200&amp;height=100&amp;fit=fit or image.jpg?width=200&amp;height=100\n\n200×100\n <img src="https://support.gcore.com/hc/article_attachments/11031151666193" alt="image5.png" width="450" height="300">|
| \n2. fit=bounds\nThe image will be compressed proportionally. Resize will select the greater dimension between the width and height and will use it to resize, ignoring the second dimension value.\nSimply put, the size of the greater dimension will be as you have specified, and the size of a smaller one will be adjusted to maintain the aspect ratio of the original image.\nExample. An origin server hosts an image that is 1000×500 pixels. You specify: width=500, height=300, fit=bounds. How Resize will work:\nIt will compare the width and height values and select the largest. In this case, the width value is greater (500 pixels). The height value will be ignored.\nIt will calculate the aspect ratio of the original image. In this case, it is 1000×500, which means the height is half as much as the width.\nIt will compress the image considering the following: the width is 500, and the height should be half as much. Meaning, the height needs to be 250. Resize will compress the image to 500×250.\n | \nAfter: image.jpg?width=200&amp; height=100&amp;fit=bounds\n\n200×133\n <img src="https://support.gcore.com/hc/article_attachments/11031151470993" alt="image3.png" width="499" height="333">                                                                                                                         |
| \n3. fit=cover\nThe image will be compressed proportionally. Resize will select the smaller dimension between the width and height and will use it to resize, ignoring the second dimension value.\nSimply put, the size of a smaller dimension will be as you have specified, and the size of a greater one will be adjusted to maintain the aspect ratio of the original image.\nExample. An origin server hosts an image that is 1000×500 pixels. You specify: width=500, height=300, fit=bounds. How Resize will work:\nIt will compare the width and height values and select the smaller one. In this case, the height is smaller (300 pixels). The width parameter will be ignored.\nIt will calculate the aspect ratio of the original image. In this case, it is 1000×500, which means the width is twice as much as the height.\nIt will compress the image considering the following: the height is 300, and the width should be twice as much. Meaning, the width needs to be 600. The image will be compressed to 300×600.\n   | \nAfter: image.jpg?width=200&amp; height=100&amp;fit=cover\n\n150×100\n   <img src="https://support.gcore.com/hc/article_attachments/11031151470993" alt="image3.png" width="499" height="333">                                                                                                                        |
| \n4. fit=force\nThe final image will be as wide and high as you have specified in the parameters. The image will be compressed in width and height, and the aspect ratio of the original image will be ignored.\n                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | \nAfter: image.jpg?width=200&amp; height=50&amp;fit=force\n\n200х50\n <img src="https://support.gcore.com/hc/article_attachments/11031138745617" alt="image6.png" width="200" height="100">                                                                                                                            |


2. fit=bounds

The image will be compressed proportionally. Resize will select the greater dimension between the width and height and will use it to resize, ignoring the second dimension value.

Simply put, the size of the greater dimension will be as you have specified, and the size of a smaller one will be adjusted to maintain the aspect ratio of the original image.

Example. An origin server hosts an image that is 1000×500 pixels. You specify: _width=500_, _height=300_, _fit=bounds_. How Resize will work:

It will compare the width and height values and select the largest. In this case, the width value is greater (500 pixels). The height value will be ignored.

It will calculate the aspect ratio of the original image. In this case, it is 1000×500, which means the height is half as much as the width.

It will compress the image considering the following: the width is 500, and the height should be half as much. Meaning, the height needs to be 250. Resize will compress the image to 500×250.

After: image.jpg?width=200& height=100&fit=bounds

<img src="https://support.gcore.com/hc/article_attachments/11031151744913" alt="image7.png" width="200" height="133">

200×133

3. fit=cover

The image will be compressed proportionally. Resize will select the smaller dimension between the width and height and will use it to resize, ignoring the second dimension value.

Simply put, the size of a smaller dimension will be as you have specified, and the size of a greater one will be adjusted to maintain the aspect ratio of the original image.

Example. An origin server hosts an image that is 1000×500 pixels. You specify: _width=500_, _height=300_, _fit=bounds_. How Resize will work:

It will compare the width and height values and select the smaller one. In this case, the height is smaller (300 pixels). The width parameter will be ignored.

It will calculate the aspect ratio of the original image. In this case, it is 1000×500, which means the width is twice as much as the height.

It will compress the image considering the following: the height is 300, and the width should be twice as much. Meaning, the width needs to be 600. The image will be compressed to 300×600.

After: image.jpg?width=200& height=100&fit=cover

<img src="https://support.gcore.com/hc/article_attachments/11031151765649" alt="image8.png" width="150" height="100">

150×100

4. fit=force

The final image will be as wide and high as you have specified in the parameters. The image will be compressed in width and height, and the aspect ratio of the original image will be ignored.

After: image.jpg?width=200& height=50&fit=force

<img src="https://support.gcore.com/hc/article_attachments/11031138871697" alt="image9.png" width="200" height="50">

200х50

4. Save the changes in the website source code.

Images on the website will now be shown to the end-user with the dimensions that you set.

Check HTTP headers
------------------

You can use the HTTP header value of the image to check if the changes have been applied. The _X-Img-Operations_ header reflects all the conversions performed. If the value includes _“resize”_, the image size has changed.

<img src="https://support.gcore.com/hc/article_attachments/11031152077329" alt="image10.png" width="355" height="536">

If the HTTP header contains no _resize_ value and CDN returns origin image, check the _Img-skip-reason_ HTTP header. This will explain the reason why the operation could not be done.
