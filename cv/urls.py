from django.conf.urls import url
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

import views

urlpatterns = [
    url(r'^view.html?$',    views.index),
    url(r'^favicon.ico$', RedirectView.as_view(url=staticfiles_storage.url('3rdparty/orbit-v1.0/favicon.ico'), permanent=False), name="favicon")
]
