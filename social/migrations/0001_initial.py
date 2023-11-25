# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2023-11-25 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid1', models.IntegerField()),
                ('uid2', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Swiped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='滑动者uid')),
                ('sid', models.IntegerField(verbose_name='被滑动者uid')),
                ('status', models.CharField(choices=[('crazy', '超级喜欢'), ('like', '喜欢'), ('dislike', '不喜欢')], max_length=8)),
                ('time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
