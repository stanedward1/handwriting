# -*- coding: utf-8 -*-
# @Time    : 2021/4/6 15:43
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : paginations.py
# @Software: PyCharm
from rest_framework.pagination import PageNumberPagination as DRFPageNumberPagination


class PageNumberPagination(DRFPageNumberPagination):
    page_size = 1
    page_query_param = 'page'
    max_page_size = 10
    page_size_query_param = 'organization'
