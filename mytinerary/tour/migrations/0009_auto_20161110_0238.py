# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-10 02:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0008_auto_20161110_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='picture_url',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='poi',
            name='summary',
            field=models.CharField(max_length=500),
        ),
    ]
