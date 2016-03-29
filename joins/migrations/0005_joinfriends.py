# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-28 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('joins', '0004_auto_20160327_2005'),
    ]

    operations = [
        migrations.CreateModel(
            name='JoinFriends',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Sharer', to='joins.Join')),
                ('emailall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='emailall', to='joins.Join')),
                ('friends', models.ManyToManyField(blank=True, null=True, related_name='Friend', to='joins.Join')),
            ],
        ),
    ]
