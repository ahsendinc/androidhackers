# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-25 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170424_0659'),
    ]

    operations = [
                migrations.AlterField(
            model_name='batterylevel',
            name='value',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='batterytemperature',
            name='value',
            field=models.IntegerField(),
        ),
    ]