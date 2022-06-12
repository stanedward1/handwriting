# -*- coding: utf-8 -*-
# @Time    : 2021/4/5 15:25
# @Author  : Longbiu
# @Email   : longbiu@foxmail.com
# @File    : celery_task.py
# @Software: PyCharm
from celery import Celery

# 加载django的环境
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "handwritingapi.settings.dev")
django.setup()

broker = 'redis://127.0.0.1:6379/1'
backend = 'redis://127.0.0.1:6379/2'

app = Celery(__name__, broker=broker, backend=backend,include=['celery_task.home_task',])

# 时区
app.conf.timezone = 'Asia/Shanghai'
# 是否使用UTC
app.conf.enable_utc = False

# 任务的定时配置
from datetime import timedelta

app.conf.beat_schedule = {
    'low-task': {
        'task': 'celery_task.home_task.banner_update',
        'schedule': timedelta(seconds=30),
        # 'schedule': crontab(hour=8, day_of_week=1),  # 每周一早八点
        # 'args': (300, 150),
    }
}