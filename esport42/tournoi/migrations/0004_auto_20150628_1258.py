# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tournoi', '0003_auto_20150616_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='phase',
            name='end',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phase',
            name='filled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='phase',
            name='order',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
