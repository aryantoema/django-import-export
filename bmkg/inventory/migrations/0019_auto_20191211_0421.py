# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-11 04:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0018_auto_20191210_1455'),
    ]

    operations = [
        migrations.AlterField(
            model_name='angin',
            name='tanggal',
            field=models.DateField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='kelembaban',
            name='tanggal',
            field=models.DateField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='radiasi',
            name='tanggal',
            field=models.DateField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='suhu',
            name='tanggal',
            field=models.DateField(blank=True, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tekanan',
            name='tanggal',
            field=models.DateField(blank=True, primary_key=True, serialize=False),
        ),
    ]
