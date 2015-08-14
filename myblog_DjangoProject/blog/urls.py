# coding: utf-8
from django.conf.urls import include, url, patterns

urlpatterns = patterns('',

                       url(r'^1/', 'blog.views.homepage'),

                       )
