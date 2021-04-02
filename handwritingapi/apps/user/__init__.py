import os
from django.apps import AppConfig

default_app_config = 'user.UserConfig'


def get_current_app_name(__file__):
    return os.path.split(os.path.dirname(__file__))[-1]


class UserConfig(AppConfig):
    name = 'user'
    verbose_name = "用户"
