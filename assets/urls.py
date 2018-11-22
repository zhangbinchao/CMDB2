#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django.urls import path,include
from assets import views

app_name = 'assets'

urlpatterns = [
	path('dashboard/', views.dashboard, name='dashboard'),
	path('index/', views.index, name='index'),
	path('detail/(?P<asset_id>[0-9]+)/$', views.detail, name="detail"),
	path('login/', views.login,name="login"),
	path('add/', views.add, name="add"),
	path('edit/(?P<asset_id>[0-9]+)/$', views.edit, name="edit"),
	path('del/(?P<asset_id>[0-9]+)/$', views.del_equipment, name="del_equipment"),
]