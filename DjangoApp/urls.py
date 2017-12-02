"""
Definition of urls for DjangoApp.
"""

from datetime import datetime
from django.conf.urls import include, url
from app.forms import BootstrapAuthenticationForm
from app.views import *
from app.models import *
from django.contrib.auth.views import *
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^bot/', include('app.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

