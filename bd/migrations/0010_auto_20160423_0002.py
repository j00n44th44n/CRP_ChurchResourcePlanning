# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-23 04:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bd', '0009_auto_20160422_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='gender',
            field=models.CharField(choices=[('femmale', 'Femenino'), ('male', 'Masculino')], max_length=32, verbose_name='G\xe9nero'),
        ),
    ]
