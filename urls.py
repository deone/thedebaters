from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin

import os

admin.autodiscover()

urlpatterns = patterns('',
    (r"^$", include("accesscard.urls")),
    (r"^register$", include("ziphon.urls")), # direct to ziphon in the mean time, we'll direct to accesscard when its ready.
    (r"^admin/(.*)", admin.site.root),
)

if settings.DEBUG:
    urlpatterns += patterns('',
	    (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
		    {'document_root': os.path.join(os.path.dirname(__file__), 'site_media')}),
    )
