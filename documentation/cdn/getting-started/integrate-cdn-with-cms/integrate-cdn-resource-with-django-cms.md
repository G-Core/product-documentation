---
title: integrate-cdn-resource-with-django-cms
displayName: Django CMS
published: true
order: 70
toc:
pageTitle: Integrate CDN with Django CMS Guide | Gcore
pageDescription: A comprehensive guide on integrating CDN resources with Django CMS to enhance your site's speed and user experience.
---
# Integrate CDN resource with Django CMS

Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

First, <a href="https://gcore.com/docs/cdn/getting-started/create-a-cdn-resource/create-a-cdn-resource-for-only-static-files" target="_blank">create a CDN resource</a> within your Gcore control panel.

Configure your urls.py file to point the static files to the appropriate static folder (i.e same directory as your media folder)

Before:

```
# This is only needed when using runserver.   
if settings.DEBUG:   
urlpatterns = patterns('',   
url(r'^media/(?P<path>.*)$', 'django.views.static.serve', # NOQA   
{'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),   
) + staticfiles_urlpatterns() + urlpatterns # NOQA   
#urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)       
```

After:

```
# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', # NOQA
            {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        ) + urlpatterns # NOQA
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        ) + staticfiles_urlpatterns() + urlpatterns # NOQA
    #urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  
```

Modify the ```settings.py``` file to point your Django application to the CDN.

Find:

```
STATIC_URL and MEDIA_URL variables and modify them to reflect your CDN url or Zonealias similar to:   
STATIC_URL = 'http://cname/static/' MEDIA_URL = 'http://cname/media/'
```

Replace CNAME with the CNAME that you specified in the Gcore <a href="https://accounts.gcore.com/reports/dashboard" target="_blank">Control panel</a>.

Ensure that your <a href="https://gcore.com/docs/cdn/cdn-resource-options/general/create-and-set-a-custom-domain-for-the-content-delivery-via-cdn" target="_blank">CNAME record has been configured</a> in a proper way before using it for integration      

Now any files within the static or media folders should be delivered via the CDN. However, there are still some static files that Django uses to run the CMS. In order to complete the integration, these files should be removed to your ```STATIC_ROOT``` folder, defined in the settings.py file. In order to copy these static files, first, ensure you are running in a virtual environment from the Django root directory

```
$ source env/bin/activate
```

Once this is complete, navigate to your app directory, where the manage.py file is stored, and run the following command:

```
$ python manage.py collectstatic
```

Any external static files will now be pulled into your ```STATIC_ROOT``` folder which will subsequently be delivered via the CDN.  
  
Use the ```STATIC_URL``` within your template files in order to reference your files from the static folder, for example:

```
<link rel="stylesheet" type="text/css" href="<strong>{{ STATIC_URL }}</strong>test.css">
```

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press **F12** or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.