---
title: integrate-cdn-resource-with-django-cms
displayName: Django CMS
published: true
order: 70
toc:
---
Before you take any steps please back up your files and database. The plugin works only with default CMS pattern. If you manually changed CMS patterns, the plugin might not help you.

First, [create a CDN Resource](https://support.gcore.com/hc/en-us/articles/213969429-How-to-set-up-a-CDN-service) within your G-CORE control panel.

Configure your urls.py file to point the static files to the appropriate static folder (i.e same directory as your media folder)

Before:

\# This is only needed when using runserver.   
if settings.DEBUG:   
urlpatterns = patterns('',   
url(r'^media/(?P<path>.\*)$', 'django.views.static.serve', # NOQA   
{'document\_root': settings.MEDIA\_ROOT, 'show\_indexes': True}),   
) + staticfiles\_urlpatterns() + urlpatterns # NOQA   
#urlpatterns = static(settings.STATIC\_URL, document\_root=settings.STATIC\_ROOT)       

After:

\# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = patterns('',
        url(r'^static/(?P<path>.\*)$', 'django.views.static.serve', # NOQA
            {'document\_root': settings.STATIC\_ROOT, 'show\_indexes': True}),
        ) + urlpatterns # NOQA
    urlpatterns = patterns('',
        url(r'^media/(?P<path>.\*)$', 'django.views.static.serve', # NOQA
            {'document\_root': settings.MEDIA\_ROOT, 'show\_indexes': True}),
        ) + staticfiles\_urlpatterns() + urlpatterns # NOQA
    #urlpatterns = static(settings.STATIC\_URL, document\_root=settings.STATIC\_ROOT)  
         

Modify the settings.py file to point your Django application to the CDN.

Find:

STATIC\_URL and MEDIA\_URL variables and modify them to reflect your CDN url or Zonealias similar to:   
STATIC\_URL = 'http://cname/static/' MEDIA\_URL = 'http://cname/media/'

Replace CNAME with the CNAME that you specified in the G-CORE [control panel](https://control.gcdn.co/).

Ensure that your CNAME record has been [configured](https://support.gcore.com/hc/en-us/articles/213969769-%D0%A1NAME) in a proper way before using it for integration      

Now any files within the static or media folders should be delivered via the CDN. However, there are still some static files that Django uses to run the CMS. In order to complete the integration, these files should be removed to your STATIC\_ROOT folder, defined in the settings.py file. In order to copy these static files, first, ensure you are running in a virtual environment from the Django root directory

$ source env/bin/activate

Once this is complete, navigate to your app directory, where the manage.py file is stored, and run the following command:

$ python manage.py collectstatic

Any external static files will now be pulled into your STATIC\_ROOT folder which will subsequently be delivered via the CDN.  
  
Use the STATIC\_URL within your template files in order to reference your files from the static folder, for example:

<link rel="stylesheet" type="text/css" href="<strong>{{ STATIC\_URL }}</strong>test.css">

Integration has been completed! We highly recommend you to check the HTML code of your web page to ensure that URLs have been rewritten properly from your original ones to CNAME from the control panel.

To do that press F12 or open Developers Tools in your browser, choose the Network tab and refresh the page. All static files should have your CNAME in URLs.