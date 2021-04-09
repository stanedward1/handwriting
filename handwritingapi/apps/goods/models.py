from django.db import models
from utils.models import BaseModel


class Goods(BaseModel):
    name = models.CharField(max_length=30, verbose_name="商品名")
    category = models.ForeignKey("GoodsCategory",on_delete=models.SET_NULL,db_constraint=False,null=True,blank=True,verbose_name="商品类别")
    goods_img = models.ImageField(upload_to="goods", max_length=255, verbose_name="商品图片", blank=True, null=True)
    desc = models.TextField(verbose_name="商品描述", help_text="商品描述")
    goods_sn = models.CharField(max_length=50, default="", verbose_name="商品唯一货号"),
    click_num = models.IntegerField(default=0, verbose_name="点击数")
    sold_num = models.IntegerField(default=0, verbose_name="商品销售量")
    fav_num = models.IntegerField(default=0, verbose_name="收藏数")
    goods_num = models.IntegerField(default=0, verbose_name="库存数")
    goods_price = models.FloatField(default=0, verbose_name="商品价格")
    ship_free = models.BooleanField(default=True, verbose_name="是否包邮")

    class Meta:
        db_table = "goods_goods"
        verbose_name = "商品信息"
        verbose_name_plural = "商品信息"

    def __str__(self):
        return self.name


class GoodsCategory(BaseModel):
    # 商品类别,比如是书籍，字帖，还是笔，练习本
    name = models.CharField(default="", max_length=30, verbose_name="类别名")
    desc = models.TextField(default="", verbose_name="类别描述", help_text="类别描述")

    class Meta:
        db_table: "goods_category"
        verbose_name = "商品类别"
        verbose_name_plural = "商品类别"

    def __str__(self):
        return self.name
