# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 20:42
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : urls.py
# @Software: PyCharm
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from video import views

router = SimpleRouter()
router.register('categories', views.VideoCategoryView, basename='categories')
router.register('video', views.VideoView, basename='video')
# router.register('culturevideo', views.CultureVideoView, basename='video')
router.register('videochapter', views.VideoChapterView, basename='videochapter')
router.register('search',views.VideoSearchView,basename='search')

urlpatterns = [
    path('', include(router.urls)),
]
