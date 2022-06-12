# -*- coding: utf-8 -*-
# @Time    : 2021/4/23 1:23
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : gunicorn.py
# @Software: PyCharm
import multiprocessing

bind = "0.0.0.0:8000"   #绑定的ip与端口
workers = 1                #进程数