from django.db.models import Q
from django_filters import rest_framework as filters
from .models import Goods


class GoodsFilter(filters.FilterSet):
    """
    商品的过滤类
    """
    pricemin = filters.NumberFilter(field_name="goods_price", lookup_expr='gte')
    pricemax = filters.NumberFilter(field_name="goods_price", lookup_expr='lte')
    name = filters.CharFilter(field_name='name')


    class Meta:
        model = Goods
        fields = ['pricemin', 'pricemax','name']

