# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20150403_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='phase',
            name='tournament',
        ),
        migrations.DeleteModel(
            name='Phase',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='members',
        ),
        migrations.RemoveField(
            model_name='teams',
            name='tournoi',
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
        migrations.DeleteModel(
            name='Tournament',
        ),
    ]
