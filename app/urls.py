"""
Definition of urls for DjangoApp.
"""
from datetime import datetime
from django.conf.urls import include, url
from django.conf import settings
from django.views.static import serve
from django.contrib.auth.views import *
from . import views

urlpatterns = [
    url(r'^test', views.test, name='test'),
    url(r'^jsson/$', views.jsson, name='t'),
    url(r'^get_pets', views.get_pets, name='get_pets'),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    ]