# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='match',
            name='score_t1',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='match',
            name='score_t2',
            field=models.IntegerField(default=0, blank=True),
            preserve_default=True,
        ),
    ]
