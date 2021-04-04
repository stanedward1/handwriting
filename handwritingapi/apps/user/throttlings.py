# -*- coding: utf-8 -*-
# @Time    : 2021/4/4 16:02
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : throttlings.py
# @Software: PyCharm
from rest_framework.throttling import SimpleRateThrottle


class SMSThrotting(SimpleRateThrottle):
    scope = 'sms'
    def get_cache_key(self, request, view):
        telephone = request.query_params.get('telephone')
        return self.cache_format%{'scope':self.scope,'ident':telephone}
