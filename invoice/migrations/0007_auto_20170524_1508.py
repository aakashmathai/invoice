# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-24 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0006_auto_20170524_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='address',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='phone',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='pincode',
            field=models.CharField(max_length=6),
        ),
    ]
