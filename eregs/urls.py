"""django_skeleton URL Configuration

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
from django.views.decorators.csrf import csrf_exempt
from eregs_core.views import *

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main),
    url(r'^regulation/(?P<version>[\d]+-[\d]+)/(?P<eff_date>[\d]{4}-[\d]{2}-[\d]{2})/(?P<node>.*)$', regulation),
    url(r'^partial/(?P<version>[\d]+-[\d]+)/(?P<eff_date>[\d]{4}-[\d]{2}-[\d]{2})/(?P<node>.*)$', regulation_partial),
    url(r'^interpretations/(?P<version>[\d]+-[\d]+)/(?P<eff_date>[\d]{4}-[\d]{2}-[\d]{2})/(?P<node>.*)$', interpretations),
    url(r'^api/regulation/(?P<version>[\d]+-[\d]+)/(?P<eff_date>[\d]{4}-[\d]{2}-[\d]{2})/(?P<node>.*)$', regulation_json),
    url(r'^api/meta/(?P<version>[\d]+-[\d]+)/(?P<eff_date>[\d]{4}-[\d]{2}-[\d]{2})$', meta_json),
    url(r'^api/toc/(?P<version>[\d]+-[\d]+)/(?P<eff_date>[\d]{4}-[\d]{2}-[\d]{2})$', toc_json)
]
