# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-22 10:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0006_auto_20170422_1225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='game_name',
            field=models.CharField(db_tablespace=None, max_length=255),
        ),
    ]