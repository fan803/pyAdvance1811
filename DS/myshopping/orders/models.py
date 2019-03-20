from django.db import models
from django.contrib.auth.models import User


#订单
class Oder(models.Model):
    # 订单编号：
    id = models.AutoField(primary_key=True)
    #所属用户
    user = models.ForeignKey(User,on_delete=models.CASCADE, verbose_name="订单所属用户")
    # 下单时间：
    create_time = models.DateTimeField(auto_now_add=True)
    # 收货人：
    recv_name = models.CharField(max_length=100,verbose_name="收货人")
    # 收货地址：recv_address 非外键
    recv_address = models.CharField(max_length=100, verbose_name="收货地址")
    # 联系方式：
    recv_phone = models.CharField(max_length=100, verbose_name="联系方式")
    # 备注信息：
    remark = models.CharField(max_length=255,verbose_name="备注信息")
    # 总计金额：
    all_price = models.FloatField(verbose_name="总计金额")

#订单单项
class OderItem(models.Model):
    #
    id = models.AutoField(primary_key=True)
    #商品编号
    goods_id = models.IntegerField(verbose_name="商品编号")
    #购买商品图片
    goods_img = models.CharField(max_length=100,verbose_name="商品图片")
    #购买商品名称
    goods_name = models.CharField(max_length=100,verbose_name="商品名称")
    #购买商品单价
    goods_price = models.FloatField(verbose_name="商品单价")
    #购买商品数量
    goods_count = models.FloatField(verbose_name="商品数量")
    # 成交价格
    goods_price_all = models.FloatField(verbose_name="商品总价")
    # 所属订单
    oder = models.ForeignKey(Oder,on_delete=models.CASCADE,verbose_name="所属订单")










