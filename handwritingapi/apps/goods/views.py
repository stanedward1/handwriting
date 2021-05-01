from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from goods import filters, models, serializer
from goods.paginations import PageNumberPagination
from goods.serializer import GoodsSerializer, CategorySerializer
from rest_framework.filters import OrderingFilter, SearchFilter


class GoodsListViewSet(GenericViewSet, ListModelMixin,RetrieveModelMixin):
    """
    商品列表页，搜索，过滤，排序！！！
    """
    queryset = models.Goods.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = GoodsSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ofdering_fields = ['id', 'name']
    filter_fields = ['name', 'desc']


class CategoryViewset(GenericViewSet, ListModelMixin):
    """
    List:
        商品分类列表数据
    """
    queryset = models.GoodsCategory.objects.order_by('id')
    serializer_class = serializer.CategorySerializer
    fields="__all__"


class GoodsSearchView(GenericViewSet, ListModelMixin):
    """
    搜索接口
    """
    queryset = models.Goods.objects.filter(is_delete=False, is_show=True)
    serializer_class = serializer.GoodsSerializer
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ['name']
