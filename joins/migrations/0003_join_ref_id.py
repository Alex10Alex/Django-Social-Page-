# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-27 19:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0002_auto_20160327_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='join',
            name='ref_id',
            field=models.CharField(default=b'ABC', max_length=120),
        ),
    ]
