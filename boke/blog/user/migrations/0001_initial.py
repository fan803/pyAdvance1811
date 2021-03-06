# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-08 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='类型id')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('concent', tinymce.models.HTMLField(verbose_name='文章内容')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='用户编号')),
                ('account', models.IntegerField(verbose_name='用户Id')),
                ('name', models.CharField(max_length=20, verbose_name='用户姓名')),
                ('age', models.CharField(max_length=200, verbose_name='用户年龄')),
                ('gender', models.CharField(max_length=50, verbose_name='用户性别')),
                ('phone', models.CharField(max_length=50, verbose_name='联系方式')),
                ('addr', models.CharField(max_length=255, verbose_name='用户地址')),
            ],
        ),
        migrations.AddField(
            model_name='articletype',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.Users', verbose_name='作者'),
        ),
    ]
