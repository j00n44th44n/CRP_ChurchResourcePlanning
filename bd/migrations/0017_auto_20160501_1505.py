# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-05-01 19:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0016_auto_20160501_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='score',
        ),
        migrations.AddField(
            model_name='member_praises',
            name='score',
            field=models.FileField(null=True, upload_to='Partituras', verbose_name='partitura'),
        ),
    ]
