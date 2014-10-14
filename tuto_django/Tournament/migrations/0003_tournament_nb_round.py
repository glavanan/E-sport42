# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Tournament', '0002_match_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='nb_round',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
