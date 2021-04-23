from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from . import models, serializer
from django.conf import settings
from django.core.cache import cache
from rest_framework.response import Response


class BannerView(GenericViewSet, ListModelMixin):
    """
    显示轮播图的接口
    """
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('orders')[
               :settings.BANNER_COUNTER]
    serializer_class = serializer.BannerModelSerializer

    def list(self, request, *args, **kwargs):
        banner_list = cache.get('banner_list')
        if not banner_list:
            print('数据进入database')
            response = super().list(request, *args, **kwargs)
            cache.set('banner_list', response.data, 60 * 60 * 24)
            return response
        return Response(data=banner_list)
