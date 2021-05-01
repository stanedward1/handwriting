# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 13:23
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers

from home import models


class BannerModelSerializer(serializers.ModelSerializer):
    "首页的轮播图"
    class Meta:
        model = models.Banner
        fields = ['name', 'link', 'img']
