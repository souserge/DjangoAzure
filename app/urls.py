"""
Definition of urls for DjangoApp.
"""
from datetime import datetime
from django.conf.urls import include, url
from django.contrib.auth.views import *
from . import views

urlpatterns = [
    url(r'^test', views.test, name='test'),
    url(r'^jsson/$', views.jsson, name='t'),
    url(r'^get_pets', views.get_pets, name='get_pets'),
]
