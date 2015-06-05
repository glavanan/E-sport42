# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0015_auto_20150605_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(unique=True, max_length=5),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='tag',
            field=models.CharField(unique=True, max_length=5),
            preserve_default=True,
        ),
    ]
