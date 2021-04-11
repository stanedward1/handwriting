# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 1:30
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : serializer.py
# @Software: PyCharm
from rest_framework import serializers

from goods.models import Goods
from trade import models


class OrderSerializer(serializers.ModelSerializer):
    goods = serializers.PrimaryKeyRelatedField(queryset=Goods.objects.all(),write_only=True,many=True)
    class Meta:
        model = models.OrderInfo
        fields = '__all__'

        # 生成订单号

    def _get_out_trade_no(self):
        import uuid
        code = '%s' % uuid.uuid4()
        return code.replace('-', '')

        # 获取支付人

    def _get_user(self):
        return self.context.get('request').user

        # 入库(两个表)的信息准备

    def _before_create(self, attrs, user, out_trade_no):
        attrs['user'] = user
        attrs['out_trade_no'] = out_trade_no

    def validate(self, attrs):
        # 1）订单总价校验
        total_amount = self._check_total_amount(attrs)
        # 2）生成订单号
        out_trade_no = self._get_out_trade_no()
        # 3）支付用户：request.user
        user = self._get_user()
        # 4）支付链接生成
        self._get_pay_url(out_trade_no, total_amount, attrs.get('subject'))
        # 5）入库(两个表)的信息准备
        self._before_create(attrs, user, out_trade_no)

        # 代表该校验方法通过，进入入库操作
        return attrs

        # 重写入库方法的目的：完成订单与订单详情两个表入库操作

    def create(self, validated_data):
        courses = validated_data.pop('courses')
        # 订单表入库，不需要courses
        order = models.Order.objects.create(**validated_data)

        # 订单详情表入库：只需要订单对象，课程对象(courses要拆成一个个course)
        for course in courses:
            models.OrderDetail.objects.create(order=order, course=course, price=course.price, real_price=course.price)

        # 先循环制造数据列表[{}, ..., {}]，用群增完成入库 bulk_create()，效率高

        return order

