"""
Definition of urls for DjangoGirl.
"""

from datetime import datetime
from django.conf.urls import patterns, url
from app.forms import BootstrapAuthenticationForm
#import blog
# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
from django.contrib.auth.views import login
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'blog.views.home', name='home'),
    #url(r'^contact$', 'app.views.contact', name='contact'),
    #url(r'^about', 'app.views.about', name='about'),
    #url(r'^login/$',
    #    'django.contrib.auth.views.login',
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title':'Log in',
    #            'year':datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    'django.contrib.auth.views.logout',
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'',include('blog.urls')),   
     url(r'^admin/', include(admin.site.urls)),
     url(r'^account/login/$','django.contrib.auth.views.login',name="login_url"),
     url(r'^map/$','blog.views.map',name="map"),
     
     url(r'^static/map/(?P<mapfile>[^\\]*\.(\w+))$','blog.views.mapkml'),
     
)
