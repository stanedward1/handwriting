from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from . import models, serializer
from django.conf import settings

class BannerView(GenericViewSet, ListModelMixin):
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('display_order')[:settings.BANNER_COUNTER]
    serializer_class = serializer.BannerModelSerializer
