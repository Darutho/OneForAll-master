# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-28 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('journey_id', models.BigIntegerField(default=0, unique=True)),
                ('PNR', models.BigIntegerField()),
                ('train_no', models.BigIntegerField()),
                ('date', models.DateTimeField()),
                ('price', models.BigIntegerField()),
                ('train_name', models.CharField(max_length=200)),
                ('location_from', models.CharField(max_length=200)),
                ('location_to', models.CharField(max_length=200)),
            ],
        ),
    ]