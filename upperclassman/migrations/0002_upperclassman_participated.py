# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-24 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upperclassman', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='upperclassman',
            name='participated',
            field=models.TextField(default='No'),
            preserve_default=False,
        ),
    ]
