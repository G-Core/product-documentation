---
title: crop-images
displayName: Crop
published: true
order: 30
toc:
   --1--About Crop: "about-the-crop-feature"
   --1--Enable Crop: "enable-the-crop-feature"
   --1--Use Crop: "use-crop"
   --1--Crop parameters: "crop-parameters"
   --1--Crop an image by changing its aspect ratio: "crop-an-image-by-customizing-its-aspect-ratio"
   --1--Crop an image at its center: "crop-an-image-at-its-center"
   --1--Crop a section at a specific location: "crop-a-section-of-an-original-image-from-a-specific-location"
   --2--using two offsets measured in pixels: "specify-a-location-with-two-offsets-measured-in-pixels"
   --2--using two coordinates measured as a percentage of the original image: "specify-a-location-using-two-coordinates-measured-as-a-percentage-of-the-original-image"
   --2--using a ratio of unwanted areas: "specify-a-location-using-the-ratio-of-unwanted-areas"
   --2--using one offset and one coordinate: "specify-a-location-using-one-offset-measured-in-pixels-and-one-coordinate-measured-as-a-percentage-of-the-original-image"
   --1--Check HTTP headers: "check-http-headers"
---
  
  
  
  
  
  
  
  
  
  
  

About the Crop feature
----------------------

**What is it?** Crop is a feature that crops an original JPG or PNG image before it is delivered over the CDN. You specify cropping parameters in the settings (a target area and its location).

Example. an origin server hosts a 750×1150 px image, but with Crop, you set 500×400 as the dimensions of a new image to be cropped at its center. When the CDN delivers the image, it gets automatically cropped—the tool cuts off everything except for the 500x400 area at the center. The origin still has the 750×1150 image, but end users get the 500×400 cropped version.

| <img src="https://support.gcore.com/hc/article_attachments/11029483026961" alt="image1.png" width="264" height="395">               |<img src="https://support.gcore.com/hc/article_attachments/11029483001489" alt="image2.png" width="286" height="229">               |
|----------------|---------------|
| Original image | Cropped image |

**How it works.** To use Crop, you need to add the [necessary query strings](#crop-parameters) to image URLs on your website source. Then, when a user requests a webpage, the CDN returns it with cropped images.

Enable the Crop feature
-----------------------

Crop is included in the paid Image Stack option. This option helps optimize images, such as by converting them to WebP or AVIF format, cropping them, or changing their quality and size. To use Crop, you need to activate Image Stack according to the [Enable and configure Image Stack](https://www.gcore.com/support/articles/11085768264593/#h_01GK96NTDDBNKKC7WS40PK3QZT) guide.

Use Crop
--------

1. Open the website source code.

2. Find the strings with the URLs of the images you want to crop.

3. Add the query strings to the URLs of the images as follows:

image.jpg?parameter=values

where _image.jpg_ is the image URL on the website. Learn more about all available parameters in the [Crop parameters](#crop-parameters) section.

4. Save the changes in the website source code.

The setup is finished! Now, when a user goes to the webpage, it will open with cropped pictures.

Crop parameters
---------------

With Crop, you can cut out a section of an original image. This is the section that your users will receive. You add a query string with a target area and its location. There are three configuration options. Each of them is described below.

Crop an image by customizing its aspect ratio
---------------------------------------------

**Parameter:** _?crop=16:9_

where:

*   16 = the ratio of the target width to its height
*   9 = the ratio of the target height to its width

**How it works.** The tool crops an image evenly to fit for the specified aspect ratio.

**Example.** An origin server hosts a 400×300 image. Its aspect ratio is 4:3. To illustrate this, we’ve place a grid on the picture.

<img src="https://support.gcore.com/hc/article_attachments/11029474366609" alt="image3.png" width="441" height="349">

You set a new aspect ratio (4:5) by adding the query parameter to the image URL:

img.jpg?crop=4:5

The tool selects a section with this aspect ratio at the center of the original image.

<img src="https://support.gcore.com/hc/article_attachments/11029474389521" alt="image4.png" width="466" height="355">

Then it cuts off the unwanted parts. Your users will see the image as follows:

<img src="https://support.gcore.com/hc/article_attachments/11029483306129" alt="image5.png" width="184" height="306">

How the tool defines what to crop:

It compares the values in the aspect ratio (4 and 5, in this example) and chooses the greater one (5). This is how it figures out which side of the original image does not need to be cropped. The value 5 corresponds to the height, so the height would remain the same: 300 px.

It calculates the width to fit for the aspect ratio. It then multiplies the original height by the ratio of 4:5, that is, 300 by 4:5. This is how the target width (240 px) is determined.

It then places a 240×300 area at the center of the original image and crops it.

Crop an image at its center
---------------------------

**Parameter:** _?crop=300,200_

where:

*   300 = the target width
*   200 = the target height

**How it works.** The tool keeps the target area at the center and cuts off the unwanted parts.

**Example.** An origin server hosts a 400×300 image. You only want to keep a 200×100 section at the center. To do this, you add the desired parameter to the image URL:

img.jpg?crop=200,100

<img src="https://support.gcore.com/hc/article_attachments/11029483307409" alt="image6.png" width="534" height="367">

The tool crops a 200×100 area from the center. This is the section that users will receive when downloading the webpage.

<img src="https://support.gcore.com/hc/article_attachments/11029483406225" alt="image7.png" width="200" height="100">

Crop a section of an original image from a specific location
------------------------------------------------------------

To cut out a section from a specific location, first add the target width and height parameters _(?crop=(width),(height))_ and then the location of the section. The location can be specified in four ways. We describe them below.

### Specify a location with two offsets measured in pixels

**Parameter:** _?crop=300,200,x100,y50_

where:

*   300 = the target width
*   200 = the target height
*   100 = the number of pixels to offset from the original left side
*   50 = the number of pixels to offset from the original top

**How it works.** The tool positions the target area so that its upper-left corner is at the specified coordinate. Then it cuts out the section.

**Example.** An origin server hosts a 400×300 image; you want to cut out only a 200×100 section with the dog’s muzzle.

<img src="https://support.gcore.com/hc/article_attachments/11029474628113" alt="image8.png" width="520" height="363">

To crop an image, you add the query parameter to the URL:

img.jpg?crop=200,100,x107,y30

Before being delivered to an end user, the image goes through the following conversions:

1. As you set in the query parameter, the target area is 200×100 (_crop=200,100_), so the tool selects this area in the picture.

<img src="https://support.gcore.com/hc/article_attachments/11029474783121" alt="image9.png" width="520" height="363">

2. You also indicate the coordinates of the starting point for cropping: 107 px from the left side and 30 pixels from the top (_x107,y30_). The tool drags the target area so that its upper-left corner is at this point.

<img src="https://support.gcore.com/hc/article_attachments/11029474833169" alt="image10.png" width="520" height="363">

3. The tool cuts out the section. The cropped image looks as follows:

<img src="https://support.gcore.com/hc/article_attachments/11029474904721" alt="image11.png" width="200" height="99">

### Specify a location using two coordinates measured as a percentage of the original image

**Parameter:** _?crop=300,200,x25p,y10p_

where:

*   300 = the target width
*   200 = the target height
*   25 = the percent of the original width to offset from the left side
*   10 = the percent of the original height to offset from the top

**How it works.** The tool positions the target area so that its upper-left corner is at the specified coordinate. Then it cuts out the section.

**Example.** An origin server hosts a 400×300 image; you want to cut out only a 200×100 section with the dog’s muzzle.

<img src="https://support.gcore.com/hc/article_attachments/11029483676177" alt="image12.png" width="520" height="360">

To crop an image, you add the query parameter to the URL:

img.jpg?crop=200,100,x25p,y10p

Before being delivered to an end user, the image goes through the following conversions:

1. As you set in the query parameter, the target area is 200×100 (_?crop=**200,100**,x25p,y10p_), so the tool selects this area in the picture.

<img src="https://support.gcore.com/hc/article_attachments/11029475042705" alt="image13.png" width="520" height="362">

2. You also indicate the starting point for cropping (_?crop=200,100,**x25p,y10p**_): offset 25% of the original width from the left side and 10% of the original height from the top (_x25p,y10p_). The tool drags the target area so that its upper-left corner is at this point.

<img src="https://support.gcore.com/hc/article_attachments/11029475091729" alt="image14.png" width="601" height="364">

3. Then it cuts out the section. The cropped image looks as follows:

<img src="https://support.gcore.com/hc/article_attachments/11029474904721" alt="image11.png" width="200" height="99">

### Specify a location using the ratio of unwanted areas

**Parameter:** _?crop=300,200,offset-x20,offset-y40_

where:

*   300 = the target height
*   200 = the target width
*   20 = the percent of the unwanted width that should be cropped from the left side
*   20 = the percent of the unwanted height that should be cropped from the top

**How it works.** The tool positions the target area so that the specified percentage of unwanted area remains on the left and on the top. Then it crops the image.

**Example.** An origin server hosts a 400×300 image; you want to cut out only a 100×100 section with the dog’s paws.

<img src="https://support.gcore.com/hc/article_attachments/11029483884945" alt="image15.png" width="520" height="362">

To crop the image, you add the query parameter to the URL:

img.jpg?crop=100,100,offset-x50,offset-y81

Before being delivered to an end user, the image goes through the following conversions:

1. You specify the target area: 100×100 (_crop=**100,100**,offset-x50,offset-y81_). The tool selects the target area in the picture.

<img src="https://support.gcore.com/hc/article_attachments/11029475244561" alt="image16.png" width="520" height="362">

2. The tool drags the target area to the right until 50% of the unwanted width remains on the left _(crop=100,100,**offset-x50**,offset-y81)_. Accordingly, 50% of the unwanted area remains on the right.

<img src="https://support.gcore.com/hc/article_attachments/11029484044049" alt="image17.png" width="520" height="362">

3. It moves the target area down until 81% of the unwanted height remains on the top _(crop=100,100,offset-x50,**offset-y81**)_. Accordingly, 19% of the unwanted height remains at the bottom.

<img src="https://support.gcore.com/hc/article_attachments/11029475395345" alt="image18.png" width="576" height="363">

4. The tool cut outs the target area. The cropped image looks as follows:

<img src="https://support.gcore.com/hc/article_attachments/11029475474321" alt="image19.png" width="100" height="99">

### Specify a location using one offset measured in pixels and one coordinate measured as a percentage of the original image

You can combine the previous options to crop an original image from a specific place. For example, you can set the horizontal coordinate in pixels and the percentage of unwanted vertical area.

Examples of combined query parameters:

*   _?crop=width,height,x_(x-axis value)_,offset-y_(percentage of unwanted area to be cropped from the top)
*   _?crop=width,height,offset-x_(percentage of unwanted area to be cropped from the left)_,y_(y-axis value)
*   _?crop=width,height,x_(percentage of unwanted area on the x axis)_,offset-y_(percentage of unwanted area to be cropped from the top)

The tool will crop an image as described above.

Check HTTP headers
------------------

You can use the HTTP header value of the image to check if the changes have been applied. The X-Img-Operations header reflects all the conversions performed. If the value includes “crop”, the image has been cropped.

<img src="https://support.gcore.com/hc/article_attachments/11029475507985" alt="image20.png" width="440" height="381">

If the header contains no “crop” value and the CDN returns the original uncropped image, check the _img-skip-reason_ header. This explains why the conversion has failed.

<img src="https://support.gcore.com/hc/article_attachments/11029475548049" alt="image21.png" width="397" height="298">
