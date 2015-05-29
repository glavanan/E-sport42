# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0002_auto_20150526_1652'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='game_name',
            field=models.CharField(default='LoL', max_length=40),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='teams',
            name='name',
            field=models.CharField(unique=True, max_length=50),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='teams',
            name='tag',
            field=models.CharField(unique=True, max_length=5),
            preserve_default=True,
        ),
    ]
