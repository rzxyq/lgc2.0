# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-24 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newstudent', '0003_auto_20160122_0955'),
    ]

    operations = [
        migrations.AddField(
            model_name='newstudent',
            name='partnering',
            field=models.TextField(null=True),
        ),
    ]
