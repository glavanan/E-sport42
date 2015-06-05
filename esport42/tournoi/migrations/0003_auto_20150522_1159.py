# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0002_auto_20150522_0948'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournament',
            name='bg_image',
        ),
        migrations.RemoveField(
            model_name='tournament',
            name='max_player',
        ),
    ]
