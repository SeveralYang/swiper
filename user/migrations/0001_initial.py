# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2023-11-06 02:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=32)),
                ('min_distance', models.IntegerField(default=1)),
                ('max_distance', models.IntegerField(default=10)),
                ('max_data_age', models.IntegerField(default=18)),
                ('min_data_age', models.IntegerField(default=40)),
                ('sex', models.CharField(choices=[('M', '男'), ('F', '女')], default='M', max_length=8)),
                ('virbation', models.BooleanField(default=True)),
                ('friend_only', models.BooleanField(default=False)),
                ('auto_play', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(max_length=32, unique=True)),
                ('phone_number', models.CharField(max_length=16, unique=True)),
                ('sex', models.CharField(choices=[('M', '男'), ('F', '女')], max_length=8)),
                ('birth_year', models.IntegerField(default=2000)),
                ('birth_month', models.IntegerField(default=1)),
                ('birth_day', models.IntegerField(default=1)),
                ('avatar', models.CharField(max_length=256)),
                ('location', models.CharField(max_length=32)),
            ],
        ),
    ]
