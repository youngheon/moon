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
    url(r'^company$', 'views.company'),
    url(r'^company/salary$', 'views.company_salary'),
    url(r'^company/profile$', 'views.company_profile'),

    #rpc
    url(r'^rpc/company/getList$', 'views.rpc'),
    url(r'^rpc/company/salary/getList$', 'views.rpc'),
    url(r'^rpc/visit/getList$', 'views.rpc'),
    url(r'^rpc/like/getList$', 'views.rpc'),
    url(r'^rpc/tag/getList$', 'views.rpc'),
    url(r'^rpc/cmtary/scoreStat$', 'views.rpc'),
    url(r'^rpc/cmtary/getList$', 'views.rpc'),
    url(r'^rpc/opn/cloud$', 'views.rpc'),



)
