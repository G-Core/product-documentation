---
title: integrate-cdn-resource-with-x-cart
displayName: X-Cart
published: true
order: 230
toc:
pageTitle: Integrate CDN with X-Cart Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with X-Cart CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with X-Cart

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

Type in your CNAME that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>. Assume that you are using *cdn.example.com* as CNAME for content delivery. Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration.  
  
**X-Cart 4.4.x and later - fixed path to skin2**

Open *smarty.php* file located in the root directory of X-Cart.

Replace the following lines

```
$smarty->assign('ImagesDir', $xcart_web_dir . $smarty_skin_dir . '/images');
$smarty->assign('SkinDir',  $xcart_web_dir . $smarty_skin_dir);
```

With the following lines

```
if ($_SERVER['HTTPS'] != 'on')
{
    $smarty->assign("SkinDir","http://cdn.example.com/skin/ideal_comfort");
    $smarty->assign("ImagesDir","http://cdn.example.com/skin/ideal_comfort/images");
}
else
{
    $smarty->assign("SkinDir","https://cdn.example.com/skin/ideal_comfort");
    $smarty->assign("ImagesDir","https://cdn.example.com/skin/ideal_comfort/images");
}
```

**X-Cart 4.4.x and later - dynamic path to skin**

Open *smarty.php* file located in the root directory of X-Cart.

Replace the following lines

```
$smarty->assign('ImagesDir', $xcart_web_dir . $smarty_skin_dir . '/images');
$smarty->assign('SkinDir', $xcart_web_dir . $smarty_skin_dir);
```

With the following lines

```
if ($_SERVER['HTTPS'] != 'on')
{
    $smarty->assign('ImagesDir', "http://cdn.example.com" . $smarty_skin_dir . '/images');
    $smarty->assign('SkinDir', "http://cdn.example.com" . $smarty_skin_dir);
}
else
{
    $smarty->assign('ImagesDir', "https://cdn.example.com" . $smarty_skin_dir . '/images');
    $smarty->assign('SkinDir', "https://cdn.example.com" . $smarty_skin_dir);
}
```
 
Open ```/include/templater/plugins/function.load_defer_code.php``` file.

Replace the following line

```
$cacheWebFile = $var_dirs_web['cache'] . '/' . $label . '.' . $md5Suffix . '.' . $type;
```

With the following lines

```
if ($_SERVER['HTTPS'] != 'on') 
{ 
    $cacheWebFile = "http://cdn.example.com/var/cache" . '/' . $label . '.' . $md5Suffix . '.' . $type; 
} 
else 
{ 
    $cacheWebFile = "https://cdn.example.com/var/cache" . '/' . $label . '.' . $md5Suffix . '.' . $type;  
}
```
  
Open  */include/func/func.files.php*.

Find (do not replace) the following line

```
global $config, $sql_tbl, $xcart_dir, $current_location;
```

And add (do not replace) the following lines

```
if ($HTTPS) 
    $current_location = 'https://cdn.example.com'; 
else 
    $current_location = 'http://cdn.example.com';
```
  
Open  */include/templater/plugins/function.get_category_image_url.php*.

Replace the following line

```
return func_convert_amp(func_get_image_url($category['categoryid'], 'C', $category['image_path']));
```

With the following line

```
return return str_replace("domain.com ","cdn.example.com",func_convert_amp(func_get_image_url($category['categoryid'], 'C', $category['image_path'])));
```
  
Open  */skin/common_files/modules/Banner_System/banner_rotator.tpl* file

Replace the following line

```
src="{$content.image_path|amp}"
```

With the following line.

```
src="{$content.image_path|amp|replace:'domain.com':'cdn.example.com'}"
```

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.