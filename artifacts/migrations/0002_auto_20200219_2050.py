# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-02-19 20:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artifacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Artifact',
        ),
    ]