# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 23:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20170606_0106'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='step',
            name='step_num',
        ),
    ]