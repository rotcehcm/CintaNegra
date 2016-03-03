# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-27 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0012_auto_20160226_0504'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='kid',
            name='full_name',
        ),
        migrations.AddField(
            model_name='kid',
            name='slug',
            field=models.SlugField(blank=True, max_length=152, unique=True),
        ),
    ]
