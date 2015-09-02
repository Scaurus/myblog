# coding: utf-8
from django.conf.urls import include, url, patterns

urlpatterns = patterns('',

                       url(r'^1/', 'blog.views.homepage'),
                       url(r'^2/', 'blog.views.homepage2'),
                       url(r'^3/', 'blog.views.homepage3'),
                       url(r'^articles/all/$', 'blog.views.articles'),
                       url(r'^articles/get/(?P<article_id>\d+)/$', 'blog.views.this_article'),
                       url(r'^articles/addlike/(?P<article_id>\d+)/$', 'blog.views.addlike'),
                       url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'blog.views.addcomment'),
                       url(r'^page/(\d+)/$', 'blog.views.articles'),
                       url(r'^articles/get/(?P<article_id>\d+)/comments/(?P<comments_page_number>\d+)/$',
                           'blog.views.this_article'),
                       url(r'^$', 'blog.views.articles'),
                       )
