from django.db import models
from django.contrib.auth.models import  User
# Create your models here.


# 用户类型：Users
class UserInfo(models.Model):
    # 用户编号
    id = models.AutoField(primary_key=True)
    # 用户昵称
    nickname = models.CharField(max_length=255, unique=True,verbose_name="用户昵称")
    # 用户年龄
    age = models.IntegerField(default=18,verbose_name="用户年龄")
    # 用户性别
    gender = models.CharField(max_length=10,default='男',verbose_name="用户性别")
    # 用户头像
    header = models.ImageField(upload_to="static/images/headers",default="static/images/headers/defaul.png",verbose_name="用户头像")
    # 联系方式
    phone = models.CharField(max_length=50,default='120',verbose_name="联系方式")
    #外键关联
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class Address(models.Model):
    # 地址编号
    id = models.AutoField(primary_key=True)
    # 地址所属用户
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="地址所属用户")
    # 收货人姓名
    recv_name = models.CharField(max_length=100,verbose_name="收货人姓名")
    # 收货人联系方式
    recv_phone = models.CharField(max_length=20,verbose_name="收货人联系方式")
    #收货人省区
    provice = models.CharField(max_length=100,verbose_name="收货人省区")
    #详细描述
    desc = models.CharField(max_length=100,verbose_name="详细描述")
    # 是否默认地址
    is_default = models.BooleanField(default=False,verbose_name="是否默认地址")
    # False非默认]


