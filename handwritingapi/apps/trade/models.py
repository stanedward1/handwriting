from django.db import models

from goods.models import Goods
from user.models import User


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=u"用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name=u"商品")
    nums = models.IntegerField(default=0, verbose_name="购买数量")

    class Meta:
        verbose_name = '购物车'
        verbose_name_plural = verbose_name
        unique_together = ("user", "goods")

    def __str__(self):
        return "%s(%d)".format(self.goods.name, self.nums)


class Order(models.Model):
    """订单模型"""
    status_choices = (
        (0, '未支付'),
        (1, '已支付'),
        (2, '已取消'),
        (3, '超时取消'),
    )
    pay_choices = (
        (1, '支付宝'),
        (2, '微信支付'),
    )
    subject = models.CharField(max_length=150, verbose_name="订单标题")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="订单总价", default=0)
    out_trade_no = models.CharField(max_length=64, verbose_name="订单号", unique=True,null=True)
    trade_no = models.CharField(max_length=64, null=True, verbose_name="流水号")
    order_status = models.SmallIntegerField(choices=status_choices, default=0, verbose_name="订单状态")
    pay_type = models.SmallIntegerField(choices=pay_choices, default=1, verbose_name="支付方式")
    pay_time = models.DateTimeField(null=True, verbose_name="支付时间")
    user = models.ForeignKey(User, related_name='order_user', on_delete=models.DO_NOTHING, db_constraint=False, verbose_name="下单用户")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        db_table = "order_order"
        verbose_name = "订单记录"
        verbose_name_plural = "订单记录"

    def __str__(self):
        return "%s - ￥%s" % (self.subject, self.total_amount)

    @property
    def goods(self):
        data_list = []
        for item in self.goods.all():
            data_list.append({
                "id": item.id,
                "name": item.name,
                "goods_price": item.goods_price,
            })
        return data_list


class OrderDetail(models.Model):
    """订单详情"""
    order = models.ForeignKey(Order, related_name='order_courses', on_delete=models.CASCADE, db_constraint=False, verbose_name="订单")
    goods = models.ForeignKey(Goods, related_name='goods_orders', on_delete=models.CASCADE, db_constraint=False, verbose_name="课程")

    class Meta:
        db_table = "order_detail"
        verbose_name = "订单详情"
        verbose_name_plural = "订单详情"

    def __str__(self):
        try:
            return "%s的订单：%s" % (self.goods.name, self.order.out_trade_no)
        except:
            return super().__str__()