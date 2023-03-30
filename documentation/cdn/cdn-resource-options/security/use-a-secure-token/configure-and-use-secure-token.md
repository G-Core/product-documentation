---
title: configure-and-use-secure-token
displayName: Configure and use
published: true
order: 20
toc:
   --1--Configure: "configure-secure-token"
   --1--Scripts for link generation: "scripts-for-link-generation"
   --2--PHP: "generate-links-with-a-secure-token-in-php"
   --2--Python: "generate-links-with-a-secure-token-in-python"
   --2--OpenSSL: "generate-a-secure-token-in-openssl"
---
  
  
     
     
   

Configure Secure Token
----------------------

Do the first three steps in your control panel in the "Secure token" tab. 

<img src="https://support.gcore.com/hc/article_attachments/6420558625553/mceclip4.png" alt="mceclip4.png">

1\. Enable the "Secure token" option in the resource settings. 

2\. Enter a key that contains between 6 and 32 characters. 

3\. If you want your content to be accessible from any IP address, leave the "Add a client's IP to the token" unchecked. If you want to make your content available only from one IP, check the checkbox (you will specify the whitelisted IP address later at Step 4). 

4\. Do this step on your origin server. Insert a script on your website which generates secure links. The generated links should look like as below:

<img src="https://support.gcore.com/hc/article_attachments/6420152091281/mceclip3.png" alt="mceclip3.png">

Where:

*   **http://cdn.example.com/photo.jpeg** is the path to the file,
*   **DMF1ucDxtHCxwYQ** is the output of the _MD5(String)_ hash function, where _String_ is the parameter obtained by merging elements: _<link expiry time><file path><whitelisted IP address> <key from Step 2>_,
*   **2147483647** is the time in the UNIX timestamp format until which the link is considered valid. 

We have prepared script templates for PHP, Python, and OpenSSL — just copy one of them from the "[Scripts for link generation](#scripts-for-link-generation)" section below. The script will start creating secure links to the content. 

5\. Do this step on your origin server. Arrange the content on your website to allow access to the protected files only over a secured link — that is, rule out the delivery of the required content over a link without a secure token. 

Moreover, make sure our CDN can access the content on your origin server regardless of whether a key is present or not.  

Scripts for link generation 
----------------------------

### Generate links with a secure token in PHP 

Below is the script for creating temporary links with the IP-based access restriction. The files will be accessible only from a whitelisted IP address and only until the link expires. 

<?php  
$secret = 'secret\_key';  
$ip = '1.2.3.4';  
$path = '/live/133529\_2/chunklist.m3u8';  
$expires = time() + 10000;  
$link = "$expires$path$ip $secret";  
$md5 = md5($link, true);  
$md5 = base64\_encode($md5);  
$md5 = strtr($md5, '+/', '-\_');  
$md5 = str\_replace('=', '', $md5);  
$url = "http://cdn.site.com{$path}?md5={$md5}&expires={$expires}";  
 echo $url;  
 echo "\\n";

Below is the script for creating temporary links without any IP-based access restriction. The files will be accessible from any IP address, but only until the link expires. 

<?php  
$secret = 'secret\_key';  
$path = '/live/133529\_2/chunklist.m3u8';  
$expires = time() + 10000;  
$link = "$expires$path $secret";  
$md5 = md5($link, true);  
$md5 = base64\_encode($md5);  
$md5 = strtr($md5, '+/', '-\_');  
$md5 = str\_replace('=', '', $md5);  
$url = "http://cdn.site.com{$path}?md5={$md5}&expires={$expires}";  
 echo $url;  
 echo "\\n"

In these scripts:

*   _$secret_ is the secret key, 
*   _$path_ is the path to the file, 
*   _$ip_ is the IP address that is allowed to access the content, 
*   _$expires_ is the link expiry time (in seconds), 
*   _$url_ is the address of the file. 

### Generate links with a secure token in Python 

The script for creating temporary links with the IP-based access restriction. The files will be accessible only from a whitelisted IP address and only until the link expires. 

import base64  
from hashlib import md5  
from time import time  
secret = 'secret\_key'  \\\\The URL signature key  
path = "/images/1.jpg" \\\\ The file path or file directory   
ip = '1.2.3.4' \\\\ The IPs that allow to access  
expires = int(time()) + 100000  
\# TTL of URL (in sec)  
#Token generation  
token = base64.encodestring(  
md5(  
"%s%s%s %s" % (expires, path, ip, secret)  
).digest()  
).replace("\\n", "").replace("+", "-").replace("/", "\_").replace("=", "")  
secured\_url = "http://cdn.site.com%s?md5=%s&expires=%s" % (path, token, expires)  
# File's URL  
print secured\_url

Below is the script for creating temporary links without any IP-based access restriction. The files will be accessible from any IP address, but only until the link expires. 

import base64  
from hashlib import md5  
from time import time  
secret = 'secret\_key'   
path = "/images/1.jpg"   
expires = int(time()) + 100000  
token = base64.encodestring(  
 md5(  
 "%s%s %s" % (expires, path, secret)  
 ).digest()  
 ).replace("\\n", "").replace("+", "-").replace("/", "\_").replace("=", "")  
secured\_url = "http://cdn.site.com%s?md5=%s&expires=%s" % (path, token, expires)   
print secured\_url

In these scripts: 

*   _secret_ is the secret key, 
*   _path_ is the path to the file, 
*   _ip_ is the IP address that is allowed to access the content, 
*   _expires_ is the link expiry time (in seconds), 
*   _secured\_url_ is the link to the file. 

### Generate a secure token in OpenSSL 

The script for creating a secure token that limits the link lifespan and allows access only to a whitelisted IP:

echo -n '2147483647/images/1.jpg1.2.3.4 secret\_key' | openssl md5 -binary | openssl base64 | tr +/ -\_ | tr -d =  
'2147483647/images/1.jpg1.2.3.4 secret\_key' = '{expires}{path}{ip} {secret\_key}'

The script for creating a secure token that only limits the link lifespan:

echo -n '2147483647/images/1.jpg secret\_key' | openssl md5 -binary | openssl base64 | tr +/ -\_ | tr -d =  
'2147483647/images/1.jpg secret\_key' = '{expires}{path} {secret\_key}'

In these scripts:

*   _2147483647/images/1.jpg_ is the path to the file, 
*   _1.2.3.4_ is the IP address that is allowed to access the content, 
*   _secret\_key_ is a secret key you specified at Step 2 of the [Configure Secure Token](#configure-secure-token) instruction.

The scripts above can only generate a secure token. You need to create a separate script that will add a secure token and expiry time to links. The script is supposed to create a link as shown below:

<img src="https://support.gcore.com/hc/article_attachments/6420152091281/mceclip3.png" alt="mceclip3.png">

Where:

*   **http://cdn.example.com/photo.jpeg** is the path to the file,
*   **DMF1ucDxtHCxwYQ** is a secure token,
*   **2147483647** is the time in the UNIX timestamp format until which the link is considered valid.