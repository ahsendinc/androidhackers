# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-23 08:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_batteryhealth_batterylevel_batterystatus_batterytemperature_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='battery_health',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.BatteryHealth'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='battery_level',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.BatteryLevel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='battery_status',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.BatteryStatus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='battery_temperature',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app.BatteryTemperature'),
            preserve_default=False,
        ),
    ]
