# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PCM', '0004_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_options',
            name='skip_blank',
            field=models.BooleanField(default=True),
        ),
    ]
