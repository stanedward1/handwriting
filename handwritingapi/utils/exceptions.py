# -*- coding: utf-8 -*-
# @Time    : 2021/4/2 9:46
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : exceptions.py
# @Software: PyCharm

from rest_framework.views import exception_handler
from .response import APIResponse
from .logger import logger


def common_exception_handler(exc, context):
    # log格式：ERROR exceptions 14 view is TestView, and error is 'age'
    logger.error('view is %s, and error is %s'%(context['view'].__class__.__name__,str(exc)))
    ret = exception_handler(exc, context)  # 是Response对象，它内部有个data
    # drf处理不了的，跑到这里来
    if not ret:
        # 可以在这写更具体的捕获异常
        if isinstance(exc, KeyError):
            return APIResponse(code=0, msg='key error')
        return APIResponse(code=0, msg='error', result=str(exc))
    else:
        return APIResponse(code=0, msg='error', result=ret.data)
