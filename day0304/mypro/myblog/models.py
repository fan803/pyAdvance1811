from django.db import models
from tinymce.models import HTMLField
# Create your models here.

class Usermanager(models.Manager):
    def createUser(self, name, age):
       au = self.create(name=name, age=age)
       return au


class Users(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(10)
    # um = Usermanager()
    avater = models.CharField(max_length=255,default="static/myblog/img/dl_01.png")
    # password = models.

'''
    @classmethod
    def create(cls,name,age):
        au = cls(name = name,age =age)
        return au
'''
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255 ,verbose_name="标题")
    concent = HTMLField(verbose_name="内容")
    author = models.ForeignKey(Users)