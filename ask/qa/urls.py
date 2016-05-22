from django.conf.urls import patterns, include, url
from django.contrib import admin

from qa.views import test, question_list, question_detail, popular

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', question_list, name='main'),
    url(r'^login/', test, name='login'),
    url(r'^signup/', test, name='signup'),
    url(r'^question/(?P<id>\d+)/', question_detail, name='question_detail'),
    url(r'^ask/', test, name='ask'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', test, name='new'),
)
