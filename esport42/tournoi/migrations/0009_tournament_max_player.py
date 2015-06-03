# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0008_remove_tournament_max_player'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='max_player',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
