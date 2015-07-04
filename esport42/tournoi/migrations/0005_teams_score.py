# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0004_auto_20150628_1258'),
    ]

    operations = [
        migrations.AddField(
            model_name='teams',
            name='score',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
