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


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ['name', 'signature']


class VideoModelSerializer(serializers.ModelSerializer):
    organization = OrganizationSerializer()

    class Meta:
        model = models.Video
        fields = ['id', 'name', 'video_img', 'students','attachment_path', 'brief',
                  'sections', 'video_section', 'organization']
