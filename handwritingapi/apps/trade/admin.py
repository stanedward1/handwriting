from django.contrib import admin
from trade import models

admin.site.register(models.ShoppingCart)
admin.site.register(models.Order)
admin.site.register(models.OrderDetail)

