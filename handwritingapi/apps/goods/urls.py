# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 20:42
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from goods import views

router = SimpleRouter()
router.register('goods', views.GoodsListViewSet, basename='goods')
router.register('categories', views.CategoryViewset, basename='categories')
router.register('search', views.GoodsSearchView, basename='search')

urlpatterns = [
    path('', include(router.urls)),
]
