# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 14:22
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : middle.py
# @Software: PyCharm
from django.utils.deprecation import MiddlewareMixin


class MyMiddle(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        if request.method == "OPTIONS":
            response["Access-Control-Allow-Origin"] = 'Content-Type'

        return response
