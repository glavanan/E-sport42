# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0005_tournament_max_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='max_player',
        ),
    ]
