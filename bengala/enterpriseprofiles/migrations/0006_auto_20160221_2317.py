# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-21 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseprofiles', '0005_auto_20160221_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='enterprise',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='relations', to='enterpriseprofiles.Enterpriseprofile'),
        ),
    ]
