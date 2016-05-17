from django.conf.urls import patterns, include, url
from django.contrib import admin

from qa.views import test

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', test, name='main'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/(?P<id>[\d]+)$/', test, name='test'),
    url(r'^ask/', test, name='ask'),
    url(r'^popular/', test, name='popular'),
    url(r'^new/', test, name='new'),
)
