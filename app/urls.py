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
    url(r'^get_pets', views.get_pets, name='get_pets'),
    url(r'^add_pets', views.add_pets, name='add_pets'),
]


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT}),
    ]