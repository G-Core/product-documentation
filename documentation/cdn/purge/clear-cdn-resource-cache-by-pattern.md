---
title: clear-cdn-resource-cache-by-pattern
displayName: By pattern
published: true
order: 20
toc:
   --1--Why purge the cache?: "why-purge-the-cache"
   --1--Purge in the control panel: "purge-in-the-control-panel"
   --2--Purge all: "purge-all"
   --2--Purge by pattern: "purge-by-pattern"
---

Why purge the cache?  

-----------------------

You need to clear the cache of CDN servers when you have renewed all content (or part of the content), or when data is not displayed correctly.

There are 2 ways to clear the cache:

*   Via API. Read more about it in the [API documentation](https://apidocs.gcore.com/cdn#tag/Tools/paths/~1cdn~1resources~1%7Bid%7D~1purge/post).
*   In the control panel. Follow the instructions below.

Purge in the control panel
--------------------------

1\. Open the [list of your CDN resources](https://cdn.gcore.com/resources/list) and go to the **Purge** section. 

<img src="https://support.gcore.com/hc/article_attachments/10601454058641" alt="mceclip0.png">

A new page opens. Do the remaining steps in it. 

<img src="https://support.gcore.com/hc/article_attachments/10601672787729" alt="mceclip1.png">

2.  Select the CDN resource from the drop-down list. The cache will be purged only for the selected resource.

3\. Select the purge method that you would like to use:

*   **Purge all** is the option for a complete purge**.** Read about it in the [section below](#purge-all). 
*   **Purge by pattern** is the option for a selective purge. Fill in the field according to the [instructions below](#purge-by-pattern). 

4\. Press the **Purge** button. 

Purge calls limitations**:**

*   You can make 1 purge request per minute.
*   One purge request is limited to 10 patterns.

A request for a purge will be formed within one minute. Then it will be sent to the CDN servers. Purging time depends on the number of files/paths and usually does not take longer than 15 minutes.

### Purge All

When you purge all files from the cache, CDN servers will pull them from the origin. It may cause a significant load on your server. If you have a large amount of content, we recommend using our [API](https://apidocs.gcore.com/cdn#tag/Tools/paths/~1cdn~1resources~1%7Bid%7D~1purge/post).

### Purge by pattern

In the input line, specify the path to the file you want to purge or a path pattern without a domain name.  Use the **\*** operator, which replaces any number of symbols in your path (you can use several \* operators in one request). A path must start with the **/** or the **\*** symbols.  Each path must be on a separate line.

If you don’t specify a query string, files with all the possible query strings will be purged from the cache according to the path pattern.

Several types of patterns are available:

| Type and explanation                                                                                                                                                                                                                                                                                                         | Purge target                  | Purge pattern            |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|--------------------------|
| 1. Purge the selected fileSpecify a file path without a domain name. As a result, all files at cdn.site/static/image.jpg will be purged,     including files with query string .jpg?VERSION. If you want to purge only a selected file with a query string, specify it in the file path: /static/image.jpg?VERSION | cdn.site/static/image.jpg | /static/image.jpg  |
| 2. Purge the group of files from one folderInput pattern without a domain name and * operator: /statiс/*                                                                                                                                                                                                               | cdn.site/static               | /statiс/*                |
| 3. Purge the group of files with a certain type Input the * operator and the file name extension .jpgAs a result, all the jpg files will be purged, including files with the query string .jpg?VERSION                                                                                                               | cdn.site/*.jpg                | *.jpg                    |
| 4. Purge the group of files having a common folder in the pathInput path pattern without a domain name and use the * operator twice                                                                                                                                                                                    | cdn.site/*/static/*           | */static/*               |
| 5. Purge the group of files with a certain type having a common folder in the pathInput path pattern with the * operator                                                                                                                                                                                               | cdn.site/*/static/*.jpg       | */static/*.jpg           |
