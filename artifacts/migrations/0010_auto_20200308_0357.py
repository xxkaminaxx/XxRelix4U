# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-08 03:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0009_auto_20200228_0534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artifact',
            name='description',
            field=models.TextField(max_length=105),
        ),
    ]
