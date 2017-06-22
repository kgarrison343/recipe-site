# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-22 01:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_remove_step_step_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='on_the_menu',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='recipe',
            name='recipe_url',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date published'),
        ),
    ]