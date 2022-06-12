# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 1:30
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers

from culturevideo import models


class CultureVideoCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CultureVideoCategory
        fields = ['name']


class CultureVideoOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Organization
        fields = ['name', 'signature', 'image']


class CultureVideoModelSerializer(serializers.ModelSerializer):
    organization = CultureVideoOrganizationSerializer()

    class Meta:
        model = models.Video
        fields = ['id', 'name', 'video_img', 'students', 'attachment_path', 'brief',
                  'sections', 'video_section', 'organization', 'updated_time']

class CultureVideoSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CultureVideoSection
        fields = ['name', 'orders', 'duration', 'pub_date', 'section_link', 'section_type_name']


class CultureVideoChapterSerializer(serializers.ModelSerializer):
    videosections = CultureVideoSectionSerializer(many=True)

    class Meta:
        model = models.CultureVideoChapter
        fields = ['name', 'chapter', 'summary', 'pub_date', 'videosections']
