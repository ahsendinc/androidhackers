# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-18 04:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenericData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pubdate', models.DateTimeField(auto_now_add=True)),
                ('jsondata', models.CharField(max_length=500)),
            ],
        ),
    ]
