# -*- coding: utf-8 -*-
# @Time    : 2021/4/4 13:14
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : send.py
# @Software: PyCharm
import random


def get_code():
    code = ''
    for i in range(4):
        code += str(random.randint(0, 9))
    return code


from qcloudsms_py import SmsSingleSender
from . import settings
from utils.logger import logger

sender = SmsSingleSender(settings.APP_ID, settings.APP_KEY)


def send_code(mobile, code, exp):
    try:
        result = sender.send_with_param(
            86,
            mobile,
            settings.TEMPLATE_ID,
            (code, exp),
            sign=settings.SIGN,
            extend="", ext=""
        )
        if result and result.get('result') == 0:
            return True
        logger.error('短信发送失败：%s' % result.get('errmsg'))
    except Exception as e:
        logger.critical('短信发送异常：%s' % e)
    return False
