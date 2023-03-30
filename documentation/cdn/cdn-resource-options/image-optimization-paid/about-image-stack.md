---
title: about-image-stack
displayName: Image stack overview
published: true
order: 10
toc:
   --1--What is Image Stack?: "what-is-image-stack"
   --1--How it works: "how-image-stack-works"
   --1--When images cannot be processed: "when-images-cannot-be-processed"
   --1--Rewrite doesn’t work: "the-rewrite-option-does-not-work-when-image-stack-is-enabled"
---
  
  

What is Image Stack?
--------------------

Image Stack is a paid option for optimizing images in JPG and PNG formats (mime-type: image/jpeg, image/png) on the fly. The original images remain unchanged but their versions in the CDN cache change according to your requirements.

The Image Stack option includes the following features:

*   [Quality](https://www.gcore.com/support/articles/9612768329489/) allows you to set the quality level for your images by lowering it to the specified value. The file size of images also decreases, so users will get them faster.
*   [Compression](https://www.gcore.com/support/articles/4417800051729/) converts images to WebP and AVIF formats providing up to 55% file size savings at a given quality level.
*   [Resize](https://www.gcore.com/support/articles/7120882595985/) allows you to reduce the height, width, and scale of your original image.
*   [Crop](https://www.gcore.com/support/articles/7777427871761/) allows you to cut off the excessive image area beyond the established parameters.

<img src="https://support.gcore.com/hc/article_attachments/11085759102353" alt="" width="555" height="621">

How Image Stack can change your image:

|   | Original image                                                                                 | Compression                                  | Quality  |
|---|------------------------------------------------------------------------------------------------|----------------------------------------|---|
|   | <img src="https://support.gcore.com/hc/article_attachments/11758218361745" alt="original.jpg"> |              <img src="https://support.gcore.com/hc/article_attachments/11758218290321" alt="compression.jpg">                         |  <img src="https://support.gcore.com/hc/article_attachments/11758218279441" alt="quality.jpg"> |
|   | Format: jpg<br/>Quality: 100%<br/>Size: 3.55 MB<br/>W×H: 553×743 px                            | Format: avif<br/>Quality: 95%<br/>Size: 476 KB | Quality: 10%<br/>Format: avif<br/>Size: 8 KB  |


|   | Resize          | Crop                                   |   |
|---|-----------------|----------------------------------------|---|
|   |             <img src="https://support.gcore.com/hc/article_attachments/11758218201233" alt="resize.jpg" width="172" height="258">    |  <img src="https://support.gcore.com/hc/article_attachments/11758218206481" alt="crop.jpg" width="183" height="229">                                      |   |
|   | W×H: 333×500 px | W×H: 400×500 pxSegment from the center |   |


Segment from the center

 

How Image Stack works
---------------------

If you use Image Stack requests for images that will be proxied through our Processing Server, it takes an original image from your Origin Server and converts the image to WebP or applies others features. After that, a new version of the image will be saved in the Caching Server and sent to end users.

<img src="https://support.gcore.com/hc/article_attachments/11756318311697" alt="image-stack.webp">

After converting, an image does not change its URL or extension. Only the following processing details will be added to image HTTP headers:

*   **X-Img-Operations**: operations performed
*   **X-Img-Origin-Download-Time**: time to download an image from an origin in milliseconds
*   **X-Img-Origin-Size**: original image size in bytes
*   **X-Img-Processing-Time**: time taken to convert in milliseconds
*   **X-Img-Saved-Bytes**: how many bytes the image size is reduced by after processing
*   **X-Img-Server**: the server that has converted the image
*   **Img-Skip-Reason**: the reason why an operation wasn’t performed

The image transformation operations are performed in this order:

*   Resizing
*   Cropping
*   Compression to WebP and AVIF with changing quality

**Note:** The quality feature cannot be performed separately from the others. If you want to change the image quality, activate one more feature.

When images cannot be processed
-------------------------------

If an image cannot be processed, an end user will receive the original image downloaded into the CDN cache from the Origin Server. We will serve original images in the following cases:

*   **The original image quality is lower than the target quality.** For instance, if the original quality is 45 and the target is 80, the image size after processing will increase rather than decrease.
*   **Gzip compression is applied to the original images.** If the image is already compressed by Gzip (contains the HTTP header _Content-Encoding: gzip_), Image Stack cannot unzip the original image.
*   **The end-user browser doesn’t support the target format (WebP, AVIF).** If HTTP headers don’t contain the values _image/webp_ or _image/avif_, it means that the browser does not support WebP or AVIF formats.
*   **The image has a format that Image Stack doesn’t support.** If you want to convert files with extensions other than JPG and PNG (e. g., GIF), Image Stack will not be able to process them.

Use the _Img-Skip-Reason_ HTTP header to find out why the image was not converted:

<img src="https://support.gcore.com/hc/article_attachments/11085759743505" alt="" width="428" height="484">

The Rewrite option does not work when Image Stack is enabled
------------------------------------------------------------

Some browsers (e.g., Google Chrome) add the Accept header with the value _image/webp_ or _image/avif_ not only to images, but also to static content like PHP and JS scripts.

All requests with the Accept header are redirected to the Image Processing Server. Usually, when the server cannot convert the file (e.g., when it’s a PHP file), it returns the content from the origin.

Difficulties appear if the [Rewrite](https://www.gcore.com/support/articles/115005353949/) option is enabled for your resource. It redirects the requests to the origin. The origin responds with the 3xx code, but the Image Processing Server cannot return the 3xx response code.

If the PHP or JS files are requested, the Image Processing Server will turn to the origin. But it responds only with the 3xx code. The Processing Server will try to follow the redirect until it receives a different response code. This will cause the file to be inaccessible.

To avoid this issue, we recommend enabling the Image Stack option in the Rules section by following the steps in our [“Enable and configure Image Stack”](https://www.gcore.com/support/articles/11085768264593/#h_01GK96NTDDBNKKC7WS40PK3QZT) guide. This way, you clearly indicate that the option will only work for files with mime type image/jpeg or image/png.

You can enable Image Stack for the entire resource in the resource settings only if the origin consists of static image assets.
