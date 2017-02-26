# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-26 09:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Landlord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landlord_name', models.CharField(max_length=100)),
                ('landlord_email', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=20)),
                ('score', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=100)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
            ],
        ),
    ]