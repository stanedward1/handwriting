# -*- coding: utf-8 -*-
# @Time    : 2021/4/12 20:45
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : test.py
# @Software: PyCharm
from libs.iPay import alipay

subject = u"测试订单".encode("utf8")
# 如果你是 Python 3的用户，使用默认的字符串即可
subject = "测试订单"

# 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
order_string = alipay.api_alipay_trade_page_pay(
    out_trade_no="20161112",
    total_amount=0.01,
    subject=subject,
    return_url="https://example.com",
    notify_url="https://example.com/notify" # 可选, 不填则使用默认notify url
)