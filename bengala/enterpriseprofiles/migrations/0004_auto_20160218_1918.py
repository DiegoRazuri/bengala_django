# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 19:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseprofiles', '0003_auto_20160218_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='phone',
            field=models.PositiveIntegerField(),
        ),
    ]