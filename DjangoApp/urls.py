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
    # Examples:
    url(r'^$', home, name='home'),
    url(r'^contact$', contact, name='contact'),
    url(r'^about', about, name='about'),
    # url(r'^login/$', login, {
    #         'template_name': 'app/login.html',
    #         'authentication_form': BootstrapAuthenticationForm,
    #         'extra_context':
    #         {
    #             'title':'Log in',
    #             'year':datetime.now().year,
    #         }
    #     },
    #     name='login'),
    # url(r'^logout$', logout, {  'next_page': '/'  },        name='logout'),
    url(r'^app/', include('app.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

