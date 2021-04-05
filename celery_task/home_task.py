# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 15:24
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : home_task.py
# @Software: PyCharm
from .celery import app


@app.task
def banner_update():
    from home import models
    from django.conf import settings
    from home import serializer
    from django.core.cache import cache
    queryset_banner = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('display_order')[
                      :settings.BANNER_COUNTER]
    serializer_banner = serializer.BannerModelSerializer(instance=queryset_banner, many=True)
    print(serializer_banner.data)
    for banner in serializer_banner.data:
        banner['img'] = 'http://127.0.0.1:8000' + banner['img']
    cache.set('banner_list', serializer_banner.data)
    return True
