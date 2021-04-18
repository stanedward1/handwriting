from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from rest_framework.viewsets import GenericViewSet, ViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from utils.logger import logger
from . import models, serializer

# 支付接口
from .models import ShoppingCart
from .paginations import PageNumberPagination
from .serializer import ShopCartSerializer


class PayViewSet(GenericViewSet, CreateModelMixin):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = models.Order.objects.all()
    serializer_class = serializer.OrderSerializer
    pagination_class = PageNumberPagination

    filter_backends = [DjangoFilterBackend, OrderingFilter]

    filter_fields = ['category']

    # 重写create方法，返回pay_url，pay_url是在serializer对象中，所以要知道serializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.context['pay_url'])

class SuccessViewSet(ViewSet):
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]

    # 支付宝同步回调给前台，在同步通知给后台处理
    def get(self, request, *args, **kwargs):
        out_trade_no = request.query_params.get('out_trade_no')
        order = models.Order.objects.filter(out_trade_no=out_trade_no).first()
        if order.order_status==1:
            return Response(True)
        else:
            return Response(False)


    # 支付宝异步回调处理
    def post(self, request, *args, **kwargs):
        try:
            result_data = request.data.dict()
            out_trade_no = result_data.get('out_trade_no')
            signature = result_data.pop('sign')
            from libs import iPay
            result = iPay.alipay.verify(result_data, signature)
            if result and result_data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
                # 完成订单修改：订单状态、流水号、支付时间
                models.Order.objects.filter(out_trade_no=out_trade_no).update(order_status=1)
                # 完成日志记录
                logger.warning('%s订单支付成功' % out_trade_no)
                return Response('success')
            else:
                logger.error('%s订单支付失败' % out_trade_no)
        except:
            pass
        return Response('failed')

class ShoppingCartViewSet(viewsets.ModelViewSet):
    """
    购物车功能
    list
        获取购物车详情
    create
        假如购物车
    delete
        删除购物车记录
    """
    authentication_classes = [JSONWebTokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ShopCartSerializer
    queryset = ShoppingCart.objects.all()