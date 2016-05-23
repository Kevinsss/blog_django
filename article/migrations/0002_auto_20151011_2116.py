# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章', 'ordering': ['-date_time']},
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(verbose_name='类别', max_length=50, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='content',
            field=models.TextField(verbose_name='内容', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateTimeField(verbose_name='创建时间', auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(verbose_name='标题', max_length=100),
        ),
    ]
