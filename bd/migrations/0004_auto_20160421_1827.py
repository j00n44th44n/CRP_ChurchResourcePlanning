# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-21 22:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0003_auto_20160417_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='cell',
        ),
        migrations.AddField(
            model_name='member',
            name='cell',
            field=models.ManyToManyField(blank=True, null=True, to='bd.Cell', verbose_name='celula'),
        ),
    ]
