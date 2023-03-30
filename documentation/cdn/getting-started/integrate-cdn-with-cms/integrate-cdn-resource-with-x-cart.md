---
title: integrate-cdn-resource-with-x-cart
displayName: X-Cart
published: true
order: 230
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Type in your CNAME that you specified in the G-CORE [control panel](https://control.gcdn.co/). Assume that you are using _cdn.example.com as CNAME for content delivery._ Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration.  
  
X-Cart 4.4.x and later - fixed path to skin2

Open _smarty.php_ _file_ located in the root directory of X-Cart.

Replace the following lines

> $smarty->assign('ImagesDir', $xcart\_web\_dir . $smarty\_skin\_dir . '/images');
> $smarty->assign('SkinDir',  $xcart\_web\_dir . $smarty\_skin\_dir);

With the following lines

> if ($\_SERVER\['HTTPS'\] != 'on')
> {
>     $smarty->assign("SkinDir","http://**_cdn.example.com_**/skin/ideal\_comfort");
>     $smarty->assign("ImagesDir","http://**_cdn.example.com_**/skin/ideal\_comfort/images");
> }
> else
> {
>     $smarty->assign("SkinDir","https://**_cdn.example.com_**/skin/ideal\_comfort");
>     $smarty->assign("ImagesDir","https://**_cdn.example.com_**/skin/ideal\_comfort/images");
> }

X-Cart 4.4.x and later - dynamic path to skin

Open _smarty.php_ file located in the root directory of X-Cart.

Replace the following lines

> $smarty->assign('ImagesDir', $xcart\_web\_dir . $smarty\_skin\_dir . '/images');
> $smarty->assign('SkinDir', $xcart\_web\_dir . $smarty\_skin\_dir);

With the following lines

> if ($\_SERVER\['HTTPS'\] != 'on')
> {
>     $smarty->assign('ImagesDir', "http://**_cdn.example.com_**" . $smarty\_skin\_dir . '/images');
>     $smarty->assign('SkinDir', "http://**_cdn.example.com_**" . $smarty\_skin\_dir);
> }
> else
> {
>     $smarty->assign('ImagesDir', "https://**_cdn.example.com_**" . $smarty\_skin\_dir . '/images');
>     $smarty->assign('SkinDir', "https://**_cdn.example.com_**" . $smarty\_skin\_dir);
> }

  
Open  _/include/templater/plugins/function.load\_defer\_code.php_ file.

Replace the following line

> $cacheWebFile = $var\_dirs\_web\['cache'\] . '/' . $label . '.' . $md5Suffix . '.' . $type;

With the following lines

> if ($\_SERVER\['HTTPS'\] != 'on') 
> { 
>     $cacheWebFile = "http://**_cdn.example.com_**/var/cache" . '/' . $label . '.' . $md5Suffix . '.' . $type; 
> } 
> else 
> { 
>     $cacheWebFile = "https://**_cdn.example.com_**/var/cache" . '/' . $label . '.' . $md5Suffix . '.' . $type;  
> }

  
Open  _/include/func/func.files.php_.

Find (do not replace) the following line

> global $config, $sql\_tbl, $xcart\_dir, $current\_location;

And add (do not replace) the following lines

> if ($HTTPS) 
>     $current\_location = 'https://**_cdn.example.com_**'; 
> else 
>     $current\_location = 'http://**_cdn.example.com_**';

  
Open  _/include/templater/plugins/function.get\_category\_image\_url.php_.

Replace the following line

> return func\_convert\_amp(func\_get\_image\_url($category\['categoryid'\], 'C', $category\['image\_path'\]));

With the following line

> return return str\_replace("domain.com ","**_cdn.example.com_**",func\_convert\_amp(func\_get\_image\_url($category\['categoryid'\], 'C', $category\['image\_path'\])));

  
Open  _/skin/common\_files/modules/Banner\_System/banner\_rotator.tpl_ file

Replace the following line

> src="{$content.image\_path|amp}"

With the following line.

> src="{$content.image\_path|amp|replace:'domain.com':'**_cdn.example.com_**'}"

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.