from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from . import models
from . import serializer

class PayView(object):
    queryset = models.OrderInfo.objects.all()
    serializer_class = serializer.OrderSerializer