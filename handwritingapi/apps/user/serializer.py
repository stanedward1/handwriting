# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 20:45
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : serializer.py
# @Software: PyCharm
import token
from rest_framework import serializers

from user import models
from rest_framework.exceptions import ValidationError
import re
from django.core.cache import cache
from rest_framework_jwt.serializers import jwt_payload_handler, jwt_encode_handler


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['username', 'password', 'id', 'icon']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        user = self._get_user(attrs)
        # 签发token
        token = self._get_token(user)
        # 放入上下文，可在view层取出
        self.context['token'] = token
        self.context['user'] = user
        return attrs

    def _get_user(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        import re
        if re.match('^1[3-9][0-9]{9}$', username):
            user = models.User.objects.filter(telephone=username).first()
        elif re.match('^.+@.+$', username):
            user = models.User.objects.filter(email=username).first()
        else:
            user = models.User.objects.filter(username=username).first()
        if user:
            ret = user.check_password(password)
            if ret:
                return user
            else:
                raise ValidationError('密码错误')
        else:
            raise ValidationError('用户不存在')

    def _get_token(self, user):
        payload = jwt_payload_handler(user)  # 通过user对象获得payload
        token = jwt_encode_handler(payload)  # 通过payload获得token
        return token


class LoginCodeSerializer(serializers.ModelSerializer):
    code = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['telephone', 'code']

    def validate(self, attrs):
        user = self._get_user(attrs)
        token = self._get_token(user)
        self.context['token'] = token
        self.context['user'] = user
        return attrs

    def _get_user(self, attrs):
        telephone = attrs.get('telephone')
        code = attrs.get('code')
        # 取出code
        cache_code = cache.get(telephone, code)
        if code == cache_code:
            # 验证码通过验证！
            if re.match('^1[3-9][0-9]{9}$', telephone):
                user = models.User.objects.filter(telephone=telephone).first()
                # 用户存在，签发token
                if user:
                    cache.set(telephone, code)
                    return user
                else:
                    raise ValidationError('此用户不存在')
            else:
                raise ValidationError('手机号不合法')
        else:
            raise ValidationError('验证码错误')

    def _get_token(self, user):
        payload = jwt_payload_handler(user)  # 通过user对象获得payload
        token = jwt_encode_handler(payload)  # 通过payload获得token
        return token


class UserRegisterSerializer(serializers.ModelSerializer):
    code = serializers.CharField(max_length=4, min_length=4, write_only=True)

    class Meta:
        model = models.User
        fields = ['telephone', 'code', 'password']
        extra_kwargs = {
            'password': {'max_length': 18, 'min_length': 8}
        }

    def validate(self, attrs):
        telephone = attrs.get('telephone')
        code = attrs.get('code')
        # 取出code
        cache_code = cache.get(telephone, code)
        if code == cache_code:
            # 验证码通过验证！
            if re.match('^1[3-9][0-9]{9}$', telephone):
                attrs['username'] = telephone
                attrs.pop('code')
                return attrs
            else:
                raise ValidationError('手机号不合法')
        else:
            raise ValidationError('验证码错误')

    # 多了个字段，所以重写create方法
    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user
