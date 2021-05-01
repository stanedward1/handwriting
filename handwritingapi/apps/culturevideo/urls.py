# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 20:42
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from culturevideo import views

router = SimpleRouter()
router.register('culturevideocategories', views.CultureVideoCategoryView, basename='categories')
router.register('culturevideo', views.VideoView, basename='video')
router.register('culturevideochapter', views.VideoChapterView, basename='videochapter')
router.register('culturevideosearch',views.VideoSearchView,basename='search')

urlpatterns = [
    path('', include(router.urls)),
]
