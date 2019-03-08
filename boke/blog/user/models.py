from django.db import models
# from tinymce.models import HTMLField


# Create your models here.


class Users(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='用户编号')
    account = models.IntegerField(verbose_name='用户Id')
    name = models.CharField(max_length=20,verbose_name='用户姓名')
    age = models.CharField(max_length=200,verbose_name='用户年龄')
    gender = models.CharField(max_length=50,verbose_name='用户性别')
    phone = models.CharField(max_length=50,verbose_name='联系方式')
    addr = models.CharField(max_length=255,verbose_name='用户地址')


class ArticleType(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='类型id')
    title= models.CharField(max_length=50, verbose_name='文章标题')
    concent = models.TextField(max_length=255, verbose_name='文章内容')
    author = models.ForeignKey(Users,verbose_name='作者')
    # def __str__(self):
    #     #     return self.type


