# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-05 23:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogSitesi', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gonderi',
            old_name='baslik',
            new_name='turler',
        ),
        migrations.RemoveField(
            model_name='gonderi',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='gonderi',
            name='y_tarihi',
        ),
        migrations.RemoveField(
            model_name='gonderi',
            name='yazar',
        ),
    ]
