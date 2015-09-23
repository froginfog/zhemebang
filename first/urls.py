# -*- coding:utf-8 -*-
"""first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^media/pics/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_URL+'pics'}),
    url(r'^$', 'website.views.index'),
    url(r'^single/(?P<url>\w+)/$', 'website.views.single'),
    url(r'^news/(?P<nc>\d+)$', 'website.views.news_list'),
    url(r'^news_show/(?P<nid>\d+)$', 'website.views.news_show'),
    url(r'^products/(?P<pc>\d*)$', 'website.views.products_list'),
    url(r'^products_show/(?P<pid>\d+)$', 'website.views.products_show'),
    url(r'^message/$', 'website.views.message_show'),
    url(r'^save/$', 'website.views.save')
]
