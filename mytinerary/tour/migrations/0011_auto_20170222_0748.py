# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-02-22 07:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour', '0010_auto_20161112_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poi',
            name='latitude',
            field=models.DecimalField(decimal_places=17, max_digits=30),
        ),
        migrations.AlterField(
            model_name='poi',
            name='longitude',
            field=models.DecimalField(decimal_places=17, max_digits=30),
        ),
    ]
