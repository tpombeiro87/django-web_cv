from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponseRedirect


urlpatterns = [
    url(r'^$', lambda x: HttpResponseRedirect('/web-cv/view.html')),
    url(r'^admin/',     include(admin.site.urls)),
    url(r'^web-cv/',    include('cv.urls', namespace="cv")),
]
