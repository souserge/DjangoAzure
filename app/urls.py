"""
Definition of urls for DjangoApp.
"""
from datetime import datetime
from django.conf.urls import include, url
from django.contrib.auth.views import *
from . import views

urlpatterns = [
    url(r'^test/$', views.test, name='test'),
]
