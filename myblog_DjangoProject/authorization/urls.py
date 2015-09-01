# coding: utf-8
from django.conf.urls import include, url, patterns

urlpatterns = patterns('',

                       url(r'^login/$', 'authorization.views.login'),
                       url(r'^logout/$', 'authorization.views.logout'),
                       url(r'^register/$', 'authorization.views.register'),

                       )
