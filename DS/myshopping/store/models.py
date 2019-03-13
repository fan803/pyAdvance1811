from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Store(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,unique=True,verbose_name="店铺名称")
    cover = models.ImageField(upload_to='static/images/store',default='static/images/store/defaul.png',verbose_name="店铺头像")
    intro = models.TextField(verbose_name="店铺描述")
    opentime = models.DateField(auto_now_add=True,verbose_name="开店时间")
    status = models.IntegerField(default=0,verbose_name="店铺状态")    #0正常营业 1 暂停营业  2 永久删除
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="店铺所属")















