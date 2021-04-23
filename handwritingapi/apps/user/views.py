import self as self
from django.shortcuts import render
from rest_framework import viewsets, mixins
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated

from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from libs import tencent_sms
from . import serializer, models
from handwritingapi.utils.response import APIResponse
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializer import UserSerializer
from .throttlings import SMSThrotting


class LoginView(ViewSet):
    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        """
        登陆的接口
        """
        ser = serializer.UserSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg=ser.errors)

    @action(methods=['GET'], detail=False)
    def check_telephone(self, request, *args, **kwargs):
        """
        检查电话号码是否符合规范，是否存在
        """
        import re
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}', telephone):
            return APIResponse(code=0, msg='手机号码不合法哦')
        try:
            user = models.User.objects.get(telephone=telephone)
            return APIResponse(code=1)
        except:
            return APIResponse(code=0, msg="手机号不存在")

    @action(methods=['POST'], detail=False)
    def code_login(self, request, *args, **kwargs):
        """
        验证码
        """
        ser = serializer.LoginCodeSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg=ser.errors)


class SendSmSView(ViewSet):
    throttle_classes = [SMSThrotting]

    @action(methods=['GET'], detail=False)
    def send(self, request, *args, **kwargs):
        """
        发送验证码
        """
        import re
        from handwritingapi.libs.tencent_sms import send_code
        from django.core.cache import cache
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}', telephone):
            return APIResponse(code=0, msg='手机号码不合法哦')
        code = tencent_sms.get_code()
        code = 1234
        result = send_code(telephone, code, 5)
        cache.set(telephone, code, 600)
        if result:
            return APIResponse(code=1, msg='验证码发送成功')
        else:
            return APIResponse(code=0, msg='验证码发送失败')


class RegisterView(GenericViewSet, CreateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        """
        注册
        """
        response = super().create(request, *args, **kwargs)
        username = response.data.get('username')
        return APIResponse(code=1, msg='注册成功', username=username)


class UserView(viewsets.ModelViewSet, mixins.RetrieveModelMixin,mixins.UpdateModelMixin):
    """
    list----打印当前用户登陆下的个人信息

    create----此接口禁用

    read----与list的区别就是json数据格式不同

    update----根据id对个人信息进行更新

    partial_update----自动生成的批量更新，但是因为对用户的权限进行了限制，此接口不起作用

    delete----此接口可以用来做用户删除自己的账户
    """
    authentication_classes = [JSONWebTokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = User.objects.filter()
    # serializer_class = serializer.UserRegisterSerializer

    def get_serializer_class(self):
        return serializer.UserSerializer

    def get_queryset(self):
        # print("打印当前用户：")
        # user = User.objects.filter(username=self.request.user)
        print(self.request.user)
        user = self.request.user
        if user.is_authenticated:
            return User.objects.filter(username=self.request.user)
        else:
            raise Exception('I am said to be authenticated, but I really am not.')
