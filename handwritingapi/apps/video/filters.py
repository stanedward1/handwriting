# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 22:43
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : filters.py
# @Software: PyCharm
from rest_framework.filters import BaseFilterBackend


class MyFilter(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        # 写过滤规则
        return queryset[:1]
