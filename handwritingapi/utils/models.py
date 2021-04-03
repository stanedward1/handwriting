# -*- coding: utf-8 -*-
# @Time    : 2021/4/3 13:12
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : models.py
# @Software: PyCharm

from django.db import models


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后更新时间')
    is_delete = models.BooleanField(default=False, verbose_name='是否删除')
    is_show = models.BooleanField(default=True, verbose_name='是否展示')
    display_order = models.IntegerField()

    class Meta:
        abstract = True
