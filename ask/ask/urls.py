from django.conf.urls import patterns, include, url
from django.http import Http404
from django.contrib import admin

from qa.views import test

admin.autodiscover()

urlpatterns = patterns('',
    url(r'/', Http404, name='main'),
    url(r'^login/', Http404, name='login'),
    url(r'^signup/', Http404, name='signup'),
    url(r'^question/(?P<id>[\d]+)$/', test, name='test'),
    url(r'^ask/', Http404, name='ask'),
    url(r'^popular/', Http404, name='popular'),
    url(r'^new/', Http404, name='new'),
    url(r'^admin/', include(admin.site.urls)),
)
