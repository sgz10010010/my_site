#!/user/bin/env python
# _*_ coding:utf-8 _*_

from django.urls import path
from .views import login, success_login, logout, register


urlpatterns = [
	path('login/', login, name='login'),
	path('register/', register, name='register'),
	path('logout/', logout, name='logout'),
	path('success_login/', success_login, name='success_login')
]