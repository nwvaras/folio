# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 06:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='voter',
            name='lastName',
            field=models.CharField(default='god', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='voter',
            name='fullName',
            field=models.CharField(max_length=100),
        ),
    ]
