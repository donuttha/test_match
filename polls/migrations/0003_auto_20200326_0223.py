# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2020-03-26 02:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_hscore_tablerender_tempcount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tablerender',
            name='score',
        ),
        migrations.AddField(
            model_name='tablerender',
            name='table',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
