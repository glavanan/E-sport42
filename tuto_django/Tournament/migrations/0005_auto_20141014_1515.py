# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament', '0004_tournament_string_matchs'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournament',
            name='string_matchs',
            field=models.CharField(max_length=2048),
        ),
    ]
