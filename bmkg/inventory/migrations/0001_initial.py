# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-30 09:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kelembaban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField()),
                ('jam0', models.IntegerField()),
                ('jam1', models.IntegerField()),
                ('jam2', models.IntegerField()),
                ('jam3', models.IntegerField()),
                ('jam4', models.IntegerField()),
                ('jam5', models.IntegerField()),
                ('jam6', models.IntegerField()),
                ('jam7', models.IntegerField()),
                ('jam8', models.IntegerField()),
                ('jam9', models.IntegerField()),
                ('jam10', models.IntegerField()),
                ('jam11', models.IntegerField()),
                ('jam12', models.IntegerField()),
                ('jam13', models.IntegerField()),
                ('jam14', models.IntegerField()),
                ('jam15', models.IntegerField()),
                ('jam16', models.IntegerField()),
                ('jam17', models.IntegerField()),
                ('jam18', models.IntegerField()),
                ('jam19', models.IntegerField()),
                ('jam20', models.IntegerField()),
                ('jam21', models.IntegerField()),
                ('jam22', models.IntegerField()),
                ('jam23', models.IntegerField()),
                ('rata', models.IntegerField()),
                ('maksimum', models.IntegerField()),
                ('minimum', models.IntegerField()),
                ('publish', models.DateField(auto_now=True)),
            ],
        ),
    ]
