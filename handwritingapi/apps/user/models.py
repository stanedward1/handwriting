from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    telephone = models.CharField(max_length=11)
    icon = models.ImageField(upload_to='icon', default='icon/default.png')
    address = models.TextField(max_length=2048, verbose_name="收货地址", null=True, blank=True)
