# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 1:30
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers

from video import models


class VideoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.VideoCategory
        fields = ['name']

class VideoModelSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Video
        fields = ['id','name','video_img']