# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-18 05:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCM', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
