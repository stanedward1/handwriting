from django.contrib import admin
from user import models

admin.site.register(models.User)


class Meta:
    verbose_name = "用户"
    verbose_name_plural = "用户"


# 修改网页title和站点header。
admin.site.site_title = "间架笔画后台管理平台"
admin.site.site_header = "间架笔画后台管理平台"
