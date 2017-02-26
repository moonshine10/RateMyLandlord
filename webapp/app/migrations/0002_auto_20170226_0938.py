# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-02-26 09:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landlord',
            name='landlord_email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='landlord',
            name='link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='landlord',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='landlord',
            name='score',
            field=models.FloatField(default=0.0),
        ),
    ]