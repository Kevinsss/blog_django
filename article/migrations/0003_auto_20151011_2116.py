# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151011_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='date_time',
            field=models.DateField(verbose_name='创建时间', auto_now_add=True),
        ),
    ]
