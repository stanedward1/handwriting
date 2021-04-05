# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 20:42
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

# router = SimpleRouter()
# router.register('banner', views.BannerView, 'banner')

urlpatterns = [
    # path('', include(router.urls))
]
