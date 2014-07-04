#coding:utf-8
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moon.views.home', name='home'),
    # url(r'^moon/', include('moon.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^$', 'views.main'),
    url(r'^first$', 'views.first'),
    url(r'^stat/(?P<action>[0-9a-zA-Z]+)', 'views.stat'),
    url(r'^error/(?P<action>[0-9a-zA-Z]+)', 'views.error'),
    url(r'^session$', 'views.session'),
    url(r'^robots$', 'views.robots'),

    url(r'^c$', 'views.company_info'),



)
