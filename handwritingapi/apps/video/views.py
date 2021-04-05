from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from . import models
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from . import models
from . import serializer

class VideoCategoryView(GenericViewSet,ListModelMixin):
    queryset = models.VideoCategory.objects.filter(is_delete = False,is_show=True).order_by('orders')
    serializer_class = serializer.VideoCategorySerializer

class VideoView(GenericViewSet,ListModelMixin):
    queryset = models.VideoCategory.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.VideoModelSerializer