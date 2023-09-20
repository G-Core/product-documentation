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
pageTitle: Configuring Secure Token | Gcore
pageDescription:  A detailed guide on configuring Secure Token with the PHP, Python, and OpenSSL scripts.
---
# Configure and use Secure Token
  
## Configure Secure Token

Do the first three steps in your control panel in the "Secure token" tab. 

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token/mceclip4.png" alt="Configure Secure Token" width="80%">

1\. Enable the "Secure token" option in the resource settings. 

2\. Enter a key that contains between 6 and 32 characters. 

3\. If you want your content to be accessible from any IP address, leave the "Add a client's IP to the token" unchecked. If you want to make your content available only from one IP, check the checkbox (you will specify the whitelisted IP address later at Step 4). 

4\. Do this step on your origin server. Insert a script on your website which generates secure links. The generated links should look like as below:

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token/mceclip3.png" alt="generated links" width="80%">

Where:

- ```http://cdn.example.com/photo.jpeg``` is the path to the file,
- ```DMF1ucDxtHCxwYQ``` is the output of the "MD5(String)" hash function, where *String* is the parameter obtained by merging elements: ```<link expiry time><file path><whitelisted IP address><key from Step 2>```,
- ```2147483647``` is the time in the UNIX timestamp format until which the link is considered valid. 

We have prepared script templates for PHP, Python, and OpenSSL — just copy one of them from the "[Scripts for link generation](https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token#scripts-for-link-generation)" section below. The script will start creating secure links to the content. 

5\. Do this step on your origin server. Arrange the content on your website to allow access to the protected files only over a secured link — that is, rule out the delivery of the required content over a link without a secure token. 

Moreover, make sure our CDN can access the content on your origin server regardless of whether a key is present or not.  

## Scripts for link generation 

### Generate links with a secure token in PHP 

Below is the script for creating temporary links with the IP-based access restriction. The files will be accessible only from a whitelisted IP address and only until the link expires. 

```
<?php
$secret = 'secret_key';
$ip = '1.2.3.4';
$path = '/live/133529_2/chunklist.m3u8';
$expires = time() + 10000;
$link = "$expires$path$ip $secret";
$md5 = md5($link, true);
$md5 = base64_encode($md5);
$md5 = strtr($md5, '+/', '-_');
$md5 = str_replace('=', '', $md5);
$url = "http://cdn.site.com{$path}?md5={$md5}&expires={$expires}";
 echo $url;
 echo "\n";
```

Below is the script for creating temporary links without any IP-based access restriction. The files will be accessible from any IP address, but only until the link expires. 

```
<?php
$secret = 'secret_key';
$path = '/live/133529_2/chunklist.m3u8';
$expires = time() + 10000;
$link = "$expires$path $secret";
$md5 = md5($link, true);
$md5 = base64_encode($md5);
$md5 = strtr($md5, '+/', '-_');
$md5 = str_replace('=', '', $md5);
$url = "http://cdn.site.com{$path}?md5={$md5}&expires={$expires}";
 echo $url;
 echo "\n"
 ```

In these scripts:

- *$secret* is the secret key, 
- *$path* is the path to the file, 
- *$ip* is the IP address that is allowed to access the content, 
- *$expires* is the link expiry time (in seconds), 
- *$url* is the address of the file. 

### Generate links with a secure token in Python 

The script for creating temporary links with the IP-based access restriction. The files will be accessible only from a whitelisted IP address and only until the link expires. 

```
import base64
from hashlib import md5
from time import timesecret = 'secret_key'  
path = "/images/1.jpg"  
ip = '1.2.3.4' 
# TTL of URL (in sec)
ttl = 100000
expires = int(time()) + ttl#Token generation
token_hash = md5(f"{expires}{path}{ip} {secret}".encode()).digest()
token = base64.b64encode(token_hash).decode().replace("\n", "").replace("+", "-").replace("/", "_").replace("=", "")
secured_url = f"http://cdn.site.com{path}?md5={token}&expires={expires}"# File's URL
print(secured_url) 
```

Below is the script for creating temporary links without any IP-based access restriction. The files will be accessible from any IP address, but only until the link expires. 

```
import base64
from hashlib import md5
from time import timesecret = 'secret_key'  
path = "/images/1.jpg"  
# TTL of URL (in sec)
ttl = 100000
expires = int(time()) + ttl#Token generation
token_hash = md5(f"{expires}{path} {secret}".encode()).digest()
token = base64.b64encode(token_hash).decode().replace("\n", "").replace("+", "-").replace("/", "_").replace("=", "")
secured_url = f"http://cdn.site.com{path}?md5={token}&expires={expires}"# File's URL
print(secured_url) 
```

In these scripts: 

- *secret* is the secret key, 
- *path* is the path to the file, 
- *ip* is the IP address that is allowed to access the content, 
- *expires* is the link expiry time (in seconds), 
- *secured_url* is the link to the file. 

### Generate a secure token in OpenSSL 

The script for creating a secure token that limits the link lifespan and allows access only to a whitelisted IP:

```
echo -n '2147483647/images/1.jpg1.2.3.4 secret_key' | openssl md5 -binary | openssl base64 | tr +/ -_ | tr -d =
'2147483647/images/1.jpg1.2.3.4 secret_key' = '{expires}{path}{ip} {secret_key}'
```

The script for creating a secure token that only limits the link lifespan:

```
echo -n '2147483647/images/1.jpg secret_key' | openssl md5 -binary | openssl base64 | tr +/ -_ | tr -d =
'2147483647/images/1.jpg secret_key' = '{expires}{path} {secret_key}'
```

In these scripts:

- *2147483647/images/1.jpg* is the path to the file, 
- *1.2.3.4* is the IP address that is allowed to access the content, 
- *secret_key* is a secret key you specified at Step 2 of the [Configure Secure Token](https://gcore.com/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token#configure-secure-token) instruction.

The scripts above can only generate a secure token. You need to create a separate script that will add a secure token and expiry time to links. The script is supposed to create a link as shown below:

<img src="https://assets.gcore.pro/docs/cdn/cdn-resource-options/security/use-a-secure-token/configure-and-use-secure-token/mceclip3.png" alt="created a link" width="80%">

Where:

- *http://cdn.example.com/photo.jpeg* is the path to the file,
- *DMF1ucDxtHCxwYQ* is a secure token,
- *2147483647* is the time in the UNIX timestamp format until which the link is considered valid.