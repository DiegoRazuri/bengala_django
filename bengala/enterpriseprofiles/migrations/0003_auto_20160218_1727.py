# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-18 17:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterpriseprofiles', '0002_auto_20160217_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='bannerImage',
            field=models.ImageField(blank=True, default='Equipo.jpg', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='descriptor',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='email',
            field=models.EmailField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='offer',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='profileImage',
            field=models.ImageField(blank=True, default='Equipo.jpg', upload_to=b''),
        ),
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='us',
            field=models.CharField(blank=True, max_length=600),
        ),
        migrations.AlterField(
            model_name='enterpriseprofile',
            name='web',
            field=models.URLField(blank=True),
        ),
    ]
