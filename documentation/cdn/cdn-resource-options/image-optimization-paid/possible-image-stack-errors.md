---
title: possible-image-stack-errors
displayName: Troubleshooting
published: true
order: 40
toc:
   --1--Overview: "troubleshooting-overview"
   --1--Check image: "how-to-check-an-images-details-for-troubleshooting"
   --1--Image not available: "common-errors-that-result-in-a-broken-image"
   --1--Image available but not processed: "common-errors-that-deliver-an-image-in-its-original-state"
   --1--Compression and Quality errors: "compression-and-quality-operation-errors"
   --1--Resize errors: "resize-operation-errors"
   --1--Crop errors: "crop-operation-errors"
pageTitle:  Image Stack Troubleshooting | Gcore
pageDescription: Learn to resolve common issues and errors with Image Stack processing.
---
# Possible Image Stack errors

## Troubleshooting overview

Normally, a successfully converted image is returned with code 200, the converted content in the body, and the following set of headers in the response:

- X-Img-Server
- headers from origin
- X-IMG-Saved-Bytes
- X-IMG-Origin-Download-Time
- X-IMG-Processing-Time
- "Content-Type":"{image/webp or image/avif}"
- Content-Length
- X-GCDN-Origin-Size

However, you may encounter problems when using <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/about-image-stack" target="_blank">Image Stack</a>. For example, an image might be delivered to your web page in its original state without Image Stack processing, or an image may not be displayed on the page at all.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/possible-image-stack-errors/image3733.png" alt="Troubleshooting overview" width="80%">

This article describes all possible errors that may occur when working with Image Stack, and explains how to fix them.

## How to check an image’s details for troubleshooting

The developer tools allow you to check your processed image’s status code, response headers, and body outputs. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/image-optimization-paid/possible-image-stack-errors/image1.png" alt="How to check an image’s details for troubleshooting">

1\. Go to the page where you used Image Stack and open the developer tools (Ctrl+Shift+I for Chrome)

2\. Navigate to the Network section on the top side

3\. In the page elements list on the left of the page, click the image you want to examine

4\. Use the headers section to view information about the selected image

Below, you will find a list of errors. You can identify the error you faced by comparing the status code, response headers, and body outputs provided for each case. 

## Common errors that result in a broken image

<table>
<thead>
  <tr>
    <th><b>Error</b></th>
    <th><b>Details</b></th>
    <th><b>Causes</b></th>
    <th><b>Solutions</b></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Incorrect image request method</td>
    <td><b>Status</b>: 405<br><b>Response Headers</b>: X-GCDN-Img-Server<br><b>Body</b>: "error": "method not found"</td>
    <td>The used request method is not GET<br></td>
    <td>Use the GET request method</td>
  </tr>
  <tr>
    <td>Incorrect format for conversion in headers or query</td>
    <td><b>Status</b>: 400<br><b>Response Headers</b>: X-Img-Server<br><b>Body</b>: "error": "only webp format supported"</td>
    <td>An unsupported format has been chosen for conversion<br></td>
    <td>Set WebP as the format for conversion<br></td>
  </tr>
  <tr>
    <td>Image Stack internal error</td>
    <td><b>Status</b>: 500<br><b>Response Headers</b>: X-Img-Server<br><b>Body</b>: "error": "&lt;err&gt;"</td>
    <td>Internal Image Stack error<br></td>
    <td>Contact our technical support team at <a href="mailto:support@gcore.com">support@gcore.com</a></td>
  </tr>
  <tr>
    <td>Origin timeout</td>
    <td><b>Status</b>: 504<br><b>Response Headers</b>: X-Img-Server<br><b>Body</b>: "error": "request to origin timeout: &lt;err&gt;"</td>
    <td>The origin did not respond<br></td>
    <td>Fix the outages of your origin</td>
  </tr>
  <tr>
    <td>Too many requests to the origin</td>
    <td><b>Status</b>: 504<br><b>Response Headers</b>: X-Img-Server<br><b>Body</b>: "error": "too many requests"</td>
    <td>Your origin is receiving too many requests <br></td>
    <td>Reduce the number of requests to your origin; you can do so with our paid <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/enable-and-configure-origin-shielding" target="_blank">Origin shielding</a> option<br></td>
  </tr>
  <tr>
</table>

## Common errors that deliver an image in its original state

**Note**: The request’s body will be proxied from your origin. The response headers will include X-Img-Server and headers from the origin. The status code of the response will be 200 OK.
  
<table>
<thead>
  <tr>
    <th><b>Error</b></th>
    <th><b>Details</b></th>
    <th><b>Causes</b></th>
    <th><b>Solutions</b></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Unsupported content type from the origin for the converter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"detected content type &lt;content type&gt; is not supported"</td>
    <td>The image format is not supported<br></td>
    <td>Change the image format to JPG or PNG</td>
  </tr>
  <tr>
    <td>Quality difference skips for jpeg</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"{webp/avif} will be bigger, than origin: OriginQ: &lt;origin quality&gt;, DesiredQ: &lt;desired jpeg quality&gt;"</td>
    <td>Compression occurred incorrectly; the quality of the processed image is greater than or equal to the original image</td>
    <td>Ensure that the original image isn’t already optimized; possible ways to solve the problem are described in the <a href="https://developers.google.com/speed/webp/faq#can_a_webp_image_grow_larger_than_its_source_image" target="_blank">official WebP guide</a></td>
  </tr>
  <tr>
    <td>Invalid response code from the origin</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"not valid response code from the origin; response code — {response code from client’s origin}"</td>
    <td>Your origin responded to the Image Stack with a non-200 response code, and Image Stack could not receive the image<br></td>
    <td>Ensure your origin responds to the Image Stack with a 200 status code</td>
  </tr>
</table>

## Compression and Quality operation errors

**Note**: The request's body will be proxied from your origin. The response headers will include X-Img-Server and headers from the origin. The status code of the response will be 200 OK.

<table>
<thead>
  <tr>
    <th><b>Error</b></th>
    <th><b>Details</b></th>
    <th><b>Causes</b></th>
    <th><b>Solutions</b></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Rate limit exceeded</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"compression: rate limit is exceeded"</td>
    <td>The rate limit for conversions to WebP and AVIF formats has been exceeded<br></td>
    <td>Wait for the limit to renew, or request a limit increase by contacting <a href="mailto:support@gcore.com">support@gcore.com</a></td>
  </tr>
  <tr>
    <td>Bad quality parameter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"compression: bad quality parameter"</td>
    <td>The quality parameter is invalid; we can't convert the quality value to a number</td>
    <td>Please ensure you set a value in the range 0–100; learn more in our <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/change-image-quality#use-quality-via-query-parameters" target="_blank">quality guide</a></td>
  </tr>
  <tr>
    <td>Unsupported format of the fmt value</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"compression: unsupported format of the fmt query parameter"</td>
    <td>You were trying to convert an image into an unsupported format<br></td>
    <td>Set WebP or AFIV as the fmt value according to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/configure-image-compression-to-webp-and-avif#use-compression-via-query-parameters" target="_blank">guide</a></td>
  </tr>
  <tr>
    <td>The WebP or AVIF format is not supported by the user client</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"compression: webp/avif format is not supported by the client"</td>
    <td>The WebP or AVIF format is not supported by the browser where the webpage is loaded</td>
    <td>Choose a browser that supports the required format</td>
  </tr>
  <tr>
    <td>The output image size is bigger or equal to the original image size</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"compression: output image size is bigger than/equal to the original image size"</td>
    <td>The output image size is too big</td>
    <td>Set the output image size to be smaller than the original image</td>
  </tr>
  <tr>
    <td>Conversation to WebP or AVIF internal error</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"compression: {image/webp or image/avif} conversation internal error"</td>
    <td>Internal conversion error</td>
    <td>Contact our technical support team at <a href="mailto:support@gcore.com">support@gcore.com</a><br></td>
  </tr>
  </table>

## Resize operation errors

**Note**: The request’s body will be proxied from your origin. The response headers will include X-Img-Server and headers from the origin. The status code of the response will be 200 OK.
  
<table>
<thead>
  <tr>
    <th><b>Error</b></th>
    <th><b>Details</b></th>
    <th><b>Causes</b></th>
    <th><b>Solutions</b></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Bad “width” parameter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"resizing: bad width parameter"</td>
    <td>The width parameter is invalid. We cannot parse the value to a number<br></td>
    <td>Please ensure you set a positive number; learn more in our <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/reduce-image-size" target="_blank">resize guide</a></td>
  </tr>
  <tr>
    <td>Bad “height” parameter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"resizing: bad height parameter"</td>
    <td>The height parameter is invalid. We can’t parse value to a number<br></td>
    <td>Please ensure you set a positive number; learn more in our <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/reduce-image-size" target="_blank">resize guide</a></td>
  </tr>
  <tr>
    <td>The output image width or height parameter is larger than the original image size</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"resizing: destination image width or height parameter is more than the original image size"</td>
    <td>You were attempting to convert the original image to a larger size <br></td>
    <td>Convert the original image into a smaller size</td>
  </tr>
  <tr>
    <td>Resizing internal error</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"resizing: internal error"</td>
    <td>Internal Image Stack error</td>
    <td>Contact our technical support team at <a href="mailto:support@gcore.com">support@gcore.com</a></td>
  </tr>
</table>

## Crop operation errors

**Note**: The request’s body will be proxied from your origin. The response headers will include X-Img-Server and headers from the origin. The status code of the response will be 200 OK.

<table>
<thead>
  <tr>
    <th><b>Error</b></th>
    <th><b>Details</b></th>
    <th><b>Causes</b></th>
    <th><b>Solutions</b></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Bad “width-ratio” or “height-ratio” parameter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: bad width-ratio or height-ratio parameter"</td>
    <td>The count of ratio parameters is two or fewer<br></td>
    <td>You must specify two values (numbers) with the “:” delimiter according to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/crop-images#crop-an-image-by-customizing-its-aspect-ratio" target="_blank">guide</a></td>
  </tr>
  <tr>
    <td>Bad “height ratio” parameter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: bad height ratio parameter"</td>
    <td>We can’t parse height value to an integer or value less than 0<br></td>
    <td>Set the “height ratio” as a positive number according to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/crop-images#crop-an-image-by-customizing-its-aspect-ratio" target="_blank">guide</a></td>
  </tr>
  <tr>
    <td>Bad “width ratio” parameter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: bad width ratio parameter"</td>
    <td>We can’t parse width value to an integer or value less than 0<br></td>
    <td>Set the “width ratio” as a positive number according to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/crop-images#crop-an-image-by-customizing-its-aspect-ratio" target="_blank">guide</a></td>
  </tr>
  <tr>
    <td>x or y parameter is not specified</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: x or y parameter is not specified"</td>
    <td>The x or y parameters specifying the number of pixels to offset do not contain values<br></td>
    <td>Specify the x and y values according to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/crop-images#crop-an-image-at-its-center" target="_blank">guide</a> </td>
  </tr>
  <tr>
    <td>Bad x or/and y percentage parameter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: bad x/y percentage parameter"</td>
    <td>The x or y parameters cannot be parsed to an integer or have a value less than 0<br></td>
    <td>Set the percentage between 0 and 100 [0, 100]</td>
  </tr>
  <tr>
    <td>Bad x or y pixel parameter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: bad x/y pixels parameter"</td>
    <td>The x or y pixel parameters cannot be parsed to an integer or have a value less than 0<br></td>
    <td>Set x or y as a positive number according to the <a href="https://gcore.com/docs/cdn/cdn-resource-options/image-optimization-paid/image-stack-tools/crop-images#specify-a-location-with-two-offsets-measured-in-pixels" target="_blank">guide</a></td>
  </tr>
  <tr>
    <td>x and y pixels number parameter and percentage x and y parameter cannot be specified simultaneously</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: x/y pixel and percentage values cannot be specified simultaneously"</td>
    <td>You have specified the x and y values twice: once by the number of pixels and once by the percentage x and y correlation<br></td>
    <td>Choose only one method to specify the x and y values</td>
  </tr>
  <tr>
    <td>Bad offset value for the x or y parameter</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: bad offset-x/y parameter"</td>
    <td>The value of offset for x or y is empty <br></td>
    <td>Specify x and y values for offset; it should be larger than 0</td>
  </tr>
  <tr>
    <td>“width”, “height” and “width-ratio”:”height-ratio” values cannot be specified simultaneously</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: width={value},height={value} and width-ratio={value}:height-ratio={value} values cannot be specified simultaneously"</td>
    <td>Pixels size parameters and aspect ratio are specified simultaneously<br></td>
    <td>Choose only one method to specify the “width” and “height” or “width-ration” and “height-ratio”</td>
  </tr>
  <tr>
    <td>x and y percentage parameter cannot be more than 100</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: x/y percentage parameter cannot be more than 100"</td>
    <td>The x or y parameter is more than 100%<br><br></td>
    <td>Set the x and y parameters between 0 and 100 [0, 100]</td>
  </tr>
  <tr>
    <td>“offset x”, “offset-y” parameters cannot be more than 100</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: offset-x/y parameter cannot be more than 100"</td>
    <td>The "offset-x“ or “offset-y” parameters are more than 100<br></td>
    <td>Specify the “offest-x” and “offset-y” parameters as less than 100</td>
  </tr>
  <tr>
    <td>Output “height” and “width” are bigger than the original image size</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: output height and width cannot be bigger than the original image size"</td>
    <td>The “height” and “width” parameters are more than the width and height of the original image</td>
    <td>Set the height and width parameters to be less than the original image</td>
  </tr>
  <tr>
    <td>Output x or y pixel value is bigger than the original image value</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: output x/y pixel value cannot be more than the original image pixels"</td>
    <td>The x or y pixel size of the output image is larger than the original image <br></td>
    <td>Ensure the x and y pixel size of the output image is smaller than the original image</td>
  </tr>
  <tr>
    <td>Output x or y percentage value cannot be more than the original image size </td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"cropping: output x/y percentage value cannot be more than the original image size"</td>
    <td>The correlation between the x and y percentage sizes of the output image is larger than the original image<br></td>
    <td>Set the output image x and y percentage sizes to be less than the original image</td>
  </tr>
  <tr>
    <td>Crop operation internal error</td>
    <td><b>Response Header</b>: "IMG-SKIP-REASON":"resizing: fit operation internal error"</td>
    <td>The crop operation failed due to internal reasons<br></td>
    <td>Contact our technical support team at <a href="mailto:support@gcore.com">support@gcore.com</a></td>
  </tr>
</tbody>
</table>