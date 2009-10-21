from django.conf.urls.defaults import *

import views

urlpatterns = patterns("",
    url(r"^$", views.login, name="access_login"),
)
