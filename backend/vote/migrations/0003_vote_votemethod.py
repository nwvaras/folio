# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-13 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20170713_0651'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='voteMethod',
            field=models.CharField(default='tui', max_length=20),
            preserve_default=False,
        ),
    ]