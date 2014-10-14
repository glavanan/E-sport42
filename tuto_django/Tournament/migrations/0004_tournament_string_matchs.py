# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament', '0003_tournament_nb_round'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='string_matchs',
            field=models.CharField(default=0, max_length=512),
            preserve_default=False,
        ),
    ]
