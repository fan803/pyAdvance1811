from django.db import models
from goods.models import Goods
from django.contrib.auth.models import User
# Create your models here.

class ShopCart(models.Model):
    # 购物编号：
    id = models.AutoField(primary_key=True)
    # 购买商品：
    goods = models.ForeignKey(Goods, verbose_name="购买商品")
    # 购买数量：
    count = models.IntegerField(verbose_name="购买数量")
    # 添加时间：
    addTime = models.DateTimeField(auto_now_add=True, verbose_name="添加购物车时间")
    # 小计金额：
    allTotal = models.FloatField()
    # 所属用户：
    user = models.ForeignKey(User)
