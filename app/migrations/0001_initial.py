# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-02 08:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('breed', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('character', models.CharField(max_length=100)),
                ('data_of_birth', models.CharField(max_length=100)),
                ('condition', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('photo', models.FileField(upload_to='')),
            ],
        ),
    ]
