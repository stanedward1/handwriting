# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 9:46
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : exceptions.py
# @Software: PyCharm
from rest_framework.response import Response


class APIResponse(Response):
    def __init__(self, code=1, msg='成功', result=None, status=None, headers=None, content_type=None, **kwargs):
        dic = {
            'code': code,
            'msg': msg
        }
        if result:
            dic['result'] = result
        dic.update(kwargs)

        # 对象来调用对象的绑定方法，会自动传值
        super().__init__(data=dic, status=status, headers=headers, content_type=content_type)
