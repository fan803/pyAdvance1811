from django.db import models
# import store
from store.models import Store

# Create your models here.

# 商品类型：GoodsType
class GoodsType(models.Model):
    # 类型主键：id
    id = models.AutoField(primary_key=True)
    # 类型名称：name
    name = models.CharField(max_length=255,unique=True,verbose_name="商品类名称")
    # 图片：cover
    cover = models.ImageField(upload_to='static/images/goods',default='static/images/goods/defaul.png',verbose_name="商品类型名称")
    # 类型描述：gt_desc   =  intro
    intro = models.TextField(verbose_name="商品类别描述")
    # 父级类型：
    parent = models.ForeignKey('self',null=True,blank=True,verbose_name="父级类型",on_delete=models.CASCADE)



#商品信息：Goods
class Goods(models.Model):
    # 商品编号：
    id = models.AutoField(primary_key=True)
    # 商品名称：
    name = models.CharField(max_length=255,verbose_name='商品名称')
    # 商品单价：
    # price = models.DecimalField(max_length=8,decimal_places=2)
    price = models.FloatField(verbose_name="商品单价")
    # 商品库存：
    stock = models.IntegerField()
    # 销售数量：count
    count = models.IntegerField()
    # 上架时间  add_time  =  creatTime
    creatTime = models.DateTimeField(auto_now_add=True)
    # 商品介绍：desc  = intro
    intro = models.TextField()
    # 所属店铺：goods_store
    store = models.ForeignKey(Store,on_delete=models.CASCADE,verbose_name="商品所属商店")
    # 商品类型：goods_detail_type
    goodstype = models.ForeignKey(GoodsType,on_delete=models.CASCADE,verbose_name="商品类型")



# 商品图片：GoodsImage
class GoodsImage(models.Model):
    # 图片编号：id
    id = models.AutoField(primary_key=True)
    # 图片路径：path
    path = models.ImageField(upload_to='static/images/goods',default='static/images/goods/defaul.png',verbose_name="商品图片")
    # 默认展示：status [True默认展示的商品图片]
    status = models.BooleanField(default=False,verbose_name="是否默认显示该图片")
    intro = models.TextField(verbose_name="商品图片描述")
    # 所属商品：goods
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE,verbose_name="所属商品")






