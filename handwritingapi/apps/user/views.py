from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin

from rest_framework.viewsets import ViewSet, GenericViewSet

from libs import tencent_sms
from . import serializer, models
from handwritingapi.utils.response import APIResponse
from rest_framework.decorators import action
from .throttlings import SMSThrotting


class LoginView(ViewSet):
    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        ser = serializer.UserSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user'].username
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg=ser.errors)

    @action(methods=['GET'], detail=False)
    def check_telephone(self, request, *args, **kwargs):
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
        import re
        from handwritingapi.libs.tencent_sms import send_code
        from django.core.cache import cache
        telephone = request.query_params.get('telephone')
        if not re.match('^1[3-9][0-9]{9}', telephone):
            return APIResponse(code=0, msg='手机号码不合法哦')
        code = tencent_sms.get_code()
        result = send_code(telephone, code, 5)
        cache.set(telephone, code, 600)
        if result:
            return APIResponse(code=1, msg='验证码发送成功')
        else:
            return APIResponse(code=0, msg='验证码发送失败')


class RegisterView(GenericViewSet, CreateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.UserRegisterSerializer
