# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 20:42
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from user import views

router = SimpleRouter()
router.register('', views.LoginView, basename='login')
router.register('', views.SendSmSView, basename='send')
router.register('register', views.RegisterView, basename='register')
router.register('user', views.UserView, basename='user')

urlpatterns = [
    path('', include(router.urls)),
]
