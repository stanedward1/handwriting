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
    queryset = models.VideoCategory.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.VideoCategorySerializer


class VideoView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = models.Video.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.VideoModelSerializer
    pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['id', 'updated_time', 'students']

    filter_fields = ['video_category', 'students']


class VideoChapterView(GenericViewSet, ListModelMixin):
    queryset = models.VideoChapter.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializer.VideoChapterSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['video']


class VideoSearchView(GenericViewSet, ListModelMixin):
    queryset = models.Video.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializer.VideoModelSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']
