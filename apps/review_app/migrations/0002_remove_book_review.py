# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-18 01:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('review_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='review',
        ),
    ]
