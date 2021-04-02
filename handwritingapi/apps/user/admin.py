from django.contrib import admin
from user import models

admin.site.register(models.User)


class Meta:
    verbose_name = "用户"
    verbose_name_plural = "用户"
