# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path, include
from app import views
from django.views.decorators.csrf import csrf_exempt
 
urlpatterns = [

        # The home page
        path('', views.index, name='home'),
        
        path('user/', views.userPage, name='user-page'),

        path('chartdata/', views.ChartData.as_view(), name='chartdata'),

        path('newapp/', views.newapp, name='newapp'),
       
        re_path(r'^profile/add/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.OrderItemCreate.as_view(),
                name='profile-add'), 
        
        re_path(r'^orderupdate/(?:(?P<pk>\d+)/)/?(?:(?P<action>\d+)/)?', views.OrderItemUpdate.as_view(),
                name='order-update'),

        re_path(r'^apps/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.AppView.as_view(),
                name='apps'),

        re_path(r'^orders/(?:(?P<pk>\d+)/)?(?:(?P<action>\w+)/)?', views.OrderView.as_view(),
                name='orders'),    

        # Matches any html file
        re_path(r'^.*\.*', views.pages, name='pages'),

]
