# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 20:42
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from trade import views

router = SimpleRouter()
router.register('pay', views.PayViewSet, basename='pay')
router.register('shopcarts',views.ShoppingCartViewSet,basename='shopcarts'),

urlpatterns = [
    path('', include(router.urls)),

    path('success/', views.SuccessViewSet.as_view({'get': 'get', 'post': 'post'}))
]
