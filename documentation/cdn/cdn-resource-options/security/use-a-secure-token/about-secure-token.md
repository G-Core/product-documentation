---
title: about-secure-token
displayName: Overview
published: true
order: 10
toc:
   --1--What is Secure Token?: "what-is-secure-token"
   --1--What it is used for: "what-secure-token-is-used-for"
   --1--Parameters: "secure-token-parameters"
   --1--How it works: "how-secure-token-works"
   --2--What secures a link: "what-secures-a-link"
   --2--How a secured URL looks: "how-a-secured-url-looks"
   --2--How content is requested via a secured link: "how-content-is-requested-via-a-secured-link"
   --1--Configure: "configure-secure-token"
pageTitle: Understanding Secure Token in Gcore CDN | Gcore
pageDescription: A detailed guide on Secure Token in Gcore CDN—how it protects content, its uses, parameters, operational mechanism, and how to configure it.
---
# About Secure Token

## What is Secure Token?

Secure Token is a feature of the <a href="https://gcore.com/cdn" target="_blank">Gcore CDN</a> that protects your files from unwanted downloading. It helps to make a link to your content temporary or restrict the access to the content by an IP address. If a fraud uses an expired URL or sends a request from not a whitelisted IP, no files will be downloaded. 

## What Secure Token is used for

Secure Token is used to protect content from stealing or from using it longer than allowed. We illustrate the use of this feature with four examples. 

**Company private content**. You have sensitive data and want it to be available only from your company office. You set up the feature, so links to this data can be open only from an office IP address.  

**Paid content**. Your users buy temporary access to content — for instance, one month’s access to an online course. You set up the feature, so a link to this content “lives” only one month after the purchase. 

**Temporary access to files set up by users**. Your users want to share temporary links to their files — for instance, to allow 24-hour access to a folder. You set up the feature, so your users can generate temporary links to files for sharing. 

**Broadcasting**. You want to protect live broadcasts from frauds, who steal direct links to your broadcasts and place them on their sites. You set up the feature, so users get a link with a very short lifespan — for instance, two seconds. Thus, your users enjoy a video without any issues and frauds cannot steal the content: a link expires while they are copy-pasting it. 

## Secure Token parameters

You can restrict the access to your content based on an IP address, but it is optional. If you like, you can make the content accessible from all IP addresses. 

You set a link lifespan. If it expires while the content is downloading, the CDN won’t stop sending the files until they are complete. Therefore, even users with a slow internet speed can receive your files without worrying about download abortion. For example, if a link expiration time is 18:40, and a user requests the content at 18:39, they will receive the full file, even if the download takes several hours. But if they open the link at 18:40 or later, no files will be sent. 

## How Secure Token works 

### What secures a link 

URLs are secured by a special character set — it is added to every link. This set is a code that stores a directive on how long a link can be available and what IP address may access the content. The code is known as a secure token. When a user follows the link our <a href="https://gcore.com/cdn" target="_blank">CDN</a> processes this request and decrypts a secure token. It doesn’t send content if a link is expired, or an IP address is not whitelisted. 

Secure tokens are created and added to links by your site. To configure the site is easy — you just need to add a necessary script. You can use our script templates. For PHP, generate secure tokens using <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token#generate-links-with-a-secure-token-in-php" target="_blank">this template</a>; for Python, use <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token#generate-links-with-a-secure-token-in-python" target="_blank">this one</a>; for OpenSSL, use <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token#generate-a-secure-token-in-openssl" target="_blank">this one</a>. The script will create secure tokens and add them to URLs. 

### How a secured URL looks 

Here is how a link with a secure token looks:  
  
<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/use-a-secure-token/about-secure-token/Frame_2.png" alt="How a secured URL looks " width="80%">

### How content is requested via a secured link 

1\. When enabling Secure Token in the <a href="https://gcore.com/cdn" target="_blank">CDN</a> resource options, you specify a key (any character set).

2\. You add a script for secured URLs generation to your site. In the script, you specify four variables: a link lifespan, a whitelisted IP, a path to your file, and the key from Step 1.

3\. Using the key, the script encodes other variables turning them into a string such as ```DMF1ucDxtHCxwYQ```.

4\. The script adds the ```DMF1ucDxtHCxwYQ``` string to a URL of a file as follows: ```http://cdn.example.com/photo.jpeg?md5=DMF1ucDxtHCxwYQ&expires=2147483647```. This is the link a user sees.

5\. The user tries to request content using this secured URL.

6\. Our <a href="https://gcore.com/cdn" target="_blank">CDN</a> processes the request. It knows the key used by the script to encrypt variables, and therefore it can decrypt ```DMF1ucDxtHCxwYQ```. The CDN sees three variables: the link expiration time, the whitelisted IP and the path to your file.

7\. If a link is not yet expired, the request comes from a whitelisted IP address, and a file's path is correct, the <a href="https://gcore.com/cdn" target="_blank">CDN</a> sends the content. If something doesn’t match, the CDN returns an error.

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/use-a-secure-token/about-secure-token/mceclip0.png" alt="How content is requested via a secured link " width="80%">

## Configure Secure Token 

For Secure Token operation, your site must generate secured URLs and give them to users, and our <a href="https://gcore.com/cdn" target="_blank">CDN</a> needs a key to decrypt such links. How to configure a website and the <a href="https://gcore.com/cdn" target="_blank">CDN</a>, we describe in the article <a href="https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token" target="_blank">Configure and use Secure Token</a>.