from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from . import models
from . import serializer
from .paginations import PageNumberPagination


class VideoCategoryView(GenericViewSet, ListModelMixin):
    """
    视频分类信息
    """
    queryset = models.VideoCategory.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.VideoCategorySerializer
    fields = '__all__'


class VideoView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    """
    list----所有视频信息

    read----根据id获取视频信息
    """
    queryset = models.Video.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.VideoModelSerializer
    pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['id', 'updated_time', 'students']

    filter_fields = ['video_category', 'students']

# class CultureVideoView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
#     """
#     list----所有视频信息
#
#     read----根据id获取视频信息
#     """
#     queryset = models.CultureVideo.objects.filter(is_delete=False, is_show=True).order_by('orders')
#     serializer_class = serializer.CultureVideoModelSerializer
#     pagination_class = PageNumberPagination
#
#     filter_backends = [DjangoFilterBackend, OrderingFilter]
#     ordering_fields = ['id', 'updated_time', 'students']
#
#     filter_fields = ['video_category', 'students']


class VideoChapterView(GenericViewSet, ListModelMixin):
    """
    视频的章节信息
    """
    queryset = models.VideoChapter.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializer.VideoChapterSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['video']


class VideoSearchView(GenericViewSet, ListModelMixin):
    """
    视频的搜索功能
    """
    queryset = models.Video.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializer.VideoModelSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']
