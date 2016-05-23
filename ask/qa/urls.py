from django.conf.urls import patterns, include, url
from django.contrib import admin

from qa.views import test, question_list, question_detail, popular, question_ask,\
    question_answer, user_signup, user_login,user_logout

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', question_list, name='main'),
    url(r'^login/', user_login, name='login'),
    url(r'^signup/', user_signup, name='signup'),
    url(r'^question/(?P<id>\d+)/', question_detail, name='question_detail'),
    url(r'^ask/', question_ask, name='question_ask'),
    url(r'^popular/', popular, name='popular'),
    url(r'^new/', test, name='new'),
    url(r'^answer/', question_answer, name='question_answer'),
    url(r'^logout/', user_logout, name='logout'),
)
