# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-19 08:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
