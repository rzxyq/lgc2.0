# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-24 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newstudent', '0005_auto_20160124_0306'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstudent',
            name='heard',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newstudent',
            name='participated',
            field=models.CharField(default=False, max_length=20),
            preserve_default=False,
        ),
    ]
