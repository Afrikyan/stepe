from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import Http404

from ask.qa.views import test

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include("qa.urls")),
    url(r'^admin/', include(admin.site.urls)),
)
